from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import containers, graph

from ge import tools
from ge import random as model_random


def find_valid_vertex_keys(attachment_mutating: AttachmentMutating) -> containers.Set_of_Graph_VertexKey:
    """Find vertices that have both visual and render attributes."""
    visual_keys = attachments.Vertex.visual_attributes.keys(attachment_mutating)
    render_keys = attachments.Vertex.render_2d_attributes.keys(attachment_mutating)
    return tools.intersection_vertex_keys(visual_keys, render_keys)


def _may_delete(vertex_key: graph.VertexKey,
                edge_key: graph.EdgeKey,
                valid_vertex_keys: containers.Set_of_Graph_VertexKey,
                vertex_to_remove_keys: containers.Set_of_Graph_VertexKey,
                edges_to_remove_keys: containers.Set_of_Graph_EdgeKey) -> None:
    """Mark vertex and edge for removal if vertex is invalid."""
    if vertex_key not in valid_vertex_keys:
        vertex_to_remove_keys.add(vertex_key)
        edges_to_remove_keys.add(edge_key)


def restore_by_deleting(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Restore integrity by deleting invalid vertices and edges."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology = opt.unwrap()
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    valid_vertex_keys = find_valid_vertex_keys(attachment_mutating)

    # Remove invalid vertices
    vertex_to_remove_keys = containers.Set_of_Graph_VertexKey()
    for vertex_key in vertex_keys:
        if vertex_key not in valid_vertex_keys:
            vertex_to_remove_keys.add(vertex_key)

    # Remove invalid edges
    edges_to_remove_keys = containers.Set_of_Graph_EdgeKey()
    for edge_key in edge_keys:
        opt_edge = attachments.Edge.topology.get(attachment_mutating, edge_key)
        if not opt_edge:
            edges_to_remove_keys.add(edge_key)
            continue

        edge = opt_edge.unwrap()

        # Missing referenced vertices in graph vertices
        if edge.va_key not in vertex_keys or edge.vb_key not in vertex_keys:
            edges_to_remove_keys.add(edge_key)

        _may_delete(edge.va_key, edge_key, valid_vertex_keys, vertex_to_remove_keys, edges_to_remove_keys)
        _may_delete(edge.vb_key, edge_key, valid_vertex_keys, vertex_to_remove_keys, edges_to_remove_keys)

    attachments.Graph.topology.subtract_edge_keys(attachment_mutating, graph_key, edges_to_remove_keys)
    attachments.Graph.topology.subtract_vertex_keys(attachment_mutating, graph_key, vertex_to_remove_keys)


def _may_restore_edge_vertex(vertex_key: graph.VertexKey,
                             edge_key: graph.EdgeKey,
                             restorable_vertex_keys: containers.Set_of_Graph_VertexKey,
                             vertex_to_restore_keys: containers.Set_of_Graph_VertexKey,
                             vertex_to_remove_keys: containers.Set_of_Graph_VertexKey,
                             edge_to_remove_keys: containers.Set_of_Graph_EdgeKey) -> None:
    """Mark vertex for restore or removal based on restorability."""
    if vertex_key in restorable_vertex_keys:
        vertex_to_restore_keys.add(vertex_key)
    else:
        vertex_to_remove_keys.add(vertex_key)
        edge_to_remove_keys.add(edge_key)


def restore_by_respawning(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Restore integrity by respawning valid vertices and removing invalid ones."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology = opt.unwrap()
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    restorable_vertex_keys = find_valid_vertex_keys(attachment_mutating)

    # Start by removing non-restorable vertices
    vertex_to_remove_keys = tools.difference_vertex_keys(vertex_keys, restorable_vertex_keys)
    vertex_to_restore_keys = containers.Set_of_Graph_VertexKey()
    edge_to_remove_keys = containers.Set_of_Graph_EdgeKey()

    for edge_key in edge_keys:
        opt_edge = attachments.Edge.topology.get(attachment_mutating, edge_key)
        if not opt_edge:
            edge_to_remove_keys.add(edge_key)
            continue

        edge = opt_edge.unwrap()
        _may_restore_edge_vertex(edge.va_key, edge_key, restorable_vertex_keys,
                                 vertex_to_restore_keys, vertex_to_remove_keys, edge_to_remove_keys)
        _may_restore_edge_vertex(edge.vb_key, edge_key, restorable_vertex_keys,
                                 vertex_to_restore_keys, vertex_to_remove_keys, edge_to_remove_keys)

    attachments.Graph.topology.subtract_vertex_keys(attachment_mutating, graph_key, vertex_to_remove_keys)
    attachments.Graph.topology.union_vertex_keys(attachment_mutating, graph_key, vertex_to_restore_keys)
    attachments.Graph.topology.subtract_edge_keys(attachment_mutating, graph_key, edge_to_remove_keys)


class _RespawnState:
    def __init__(self, vertex_value: int):
        self.index = 0
        self.vertex_value = vertex_value
        self.vertex_to_respawn_keys = containers.Set_of_Graph_VertexKey()


def _respawn(attachment_mutating: AttachmentMutating,
             vertex_key: graph.VertexKey,
             vertex_visual_attributes_keys: containers.Set_of_Graph_VertexKey,
             vertex_render_2d_attributes_keys: containers.Set_of_Graph_VertexKey,
             state: _RespawnState) -> None:
    """Respawn a vertex by creating missing attributes."""
    if vertex_key not in vertex_visual_attributes_keys:
        attrs = graph.VertexVisualAttributes()
        attrs.value = state.vertex_value
        attrs.color = model_random.make_color()
        attachments.Vertex.visual_attributes.set(attachment_mutating, vertex_key, attrs)
        state.vertex_value += 1

    if vertex_key not in vertex_render_2d_attributes_keys:
        position = graph.Position()
        position.x = 10.0 + state.index * 30.0
        position.y = 200.0

        render_attrs = graph.Vertex2DAttributes()
        render_attrs.position = position
        attachments.Vertex.render_2d_attributes.set(attachment_mutating, vertex_key, render_attrs)
        state.index += 1

    state.vertex_to_respawn_keys.add(vertex_key)


def restore_by_creating(attachment_mutating: AttachmentMutating,
                        graph_key: graph.GraphKey,
                        value: int) -> None:
    """Restore integrity by creating missing vertex attributes."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology = opt.unwrap()
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    vertex_visual_attributes_keys = attachments.Vertex.visual_attributes.keys(attachment_mutating)
    vertex_render_2d_attributes_keys = attachments.Vertex.render_2d_attributes.keys(attachment_mutating)

    valid_vertex_keys = find_valid_vertex_keys(attachment_mutating)
    edge_to_remove_keys = containers.Set_of_Graph_EdgeKey()

    state = _RespawnState(value)

    for vertex_key in vertex_keys:
        if vertex_key not in valid_vertex_keys:
            _respawn(attachment_mutating, vertex_key, vertex_visual_attributes_keys,
                     vertex_render_2d_attributes_keys, state)

    for edge_key in edge_keys:
        opt_edge = attachments.Edge.topology.get(attachment_mutating, edge_key)
        if not opt_edge:
            edge_to_remove_keys.add(edge_key)
            continue

        edge = opt_edge.unwrap()
        _respawn(attachment_mutating, edge.va_key, vertex_visual_attributes_keys,
                 vertex_render_2d_attributes_keys, state)
        _respawn(attachment_mutating, edge.vb_key, vertex_visual_attributes_keys,
                 vertex_render_2d_attributes_keys, state)

    attachments.Graph.topology.union_vertex_keys(attachment_mutating, graph_key, state.vertex_to_respawn_keys)
    attachments.Graph.topology.subtract_edge_keys(attachment_mutating, graph_key, edge_to_remove_keys)
