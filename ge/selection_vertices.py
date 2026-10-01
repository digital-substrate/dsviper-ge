from dsviper import AttachmentMutating, AttachmentGetting

from gei.graph import attachments
from gei import containers, graph

from ge import tools


def select(attachment_mutating: AttachmentMutating,
           graph_key: graph.GraphKey,
           vertex_key: graph.VertexKey) -> None:
    """Select a single vertex, deselecting all others."""
    selected_vertex_keys = containers.Set_of_Graph_VertexKey()
    selected_edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selection = opt.unwrap()
        selected_vertex_keys = selection.vertex_keys
        selected_edge_keys = selection.edge_keys

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, selected_vertex_keys)

    new_selection = containers.Set_of_Graph_VertexKey()
    new_selection.add(vertex_key)
    attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, new_selection)
    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, selected_edge_keys)


def select_multiple(attachment_mutating: AttachmentMutating,
                    graph_key: graph.GraphKey,
                    vertex_keys: containers.Set_of_Graph_VertexKey) -> None:
    """Select multiple vertices, deselecting all others."""
    selected_vertex_keys = containers.Set_of_Graph_VertexKey()
    selected_edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selection = opt.unwrap()
        selected_vertex_keys = selection.vertex_keys
        selected_edge_keys = selection.edge_keys

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, selected_vertex_keys)
    attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, selected_edge_keys)


def combine(attachment_mutating: AttachmentMutating,
            graph_key: graph.GraphKey,
            vertex_key: graph.VertexKey,
            selected: bool) -> None:
    """Add or remove a vertex from the selection."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    vertex_keys.add(vertex_key)

    if selected:
        attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    else:
        attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, vertex_keys)


def select_all(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Select all vertices in the graph."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        vertex_keys = opt.unwrap().vertex_keys

    attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)


def deselect_all(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Deselect all vertices in the graph."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        vertex_keys = opt.unwrap().vertex_keys

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, vertex_keys)


def invert(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Invert the vertex selection."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        vertex_keys = opt.unwrap().vertex_keys

    selected_vertex_keys = containers.Set_of_Graph_VertexKey()
    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selected_vertex_keys = opt.unwrap().vertex_keys

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    attachments.Graph.selection.union_vertex_keys(
        attachment_mutating, graph_key, tools.difference_vertex_keys(vertex_keys, selected_vertex_keys))


def restore(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Restore selected vertices to the topology."""
    selected_vertex_keys = containers.Set_of_Graph_VertexKey()
    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selected_vertex_keys = opt.unwrap().vertex_keys

    attachments.Graph.topology.union_vertex_keys(attachment_mutating, graph_key, selected_vertex_keys)


def increment_value(attachment_mutating: AttachmentMutating,
                    graph_key: graph.GraphKey,
                    increment: int) -> None:
    """Increment the value of all selected vertices."""
    from ge import random as model_random

    selected_vertex_keys = containers.Set_of_Graph_VertexKey()
    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selected_vertex_keys = opt.unwrap().vertex_keys

    color = model_random.make_color()
    for vertex_key in selected_vertex_keys:
        opt_attr = attachments.Vertex.visual_attributes.get(attachment_mutating, vertex_key)
        if opt_attr:
            attrs = opt_attr.unwrap()
            attachments.Vertex.visual_attributes.set_value(attachment_mutating, vertex_key, attrs.value + increment)
            attachments.Vertex.visual_attributes.set_color(attachment_mutating, vertex_key, color)


def has_selected(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> bool:
    """Check if any vertices are selected."""
    return len(selected(attachment_getting, graph_key)) > 0


def selected(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> containers.Set_of_Graph_VertexKey:
    """Get the set of selected vertices."""
    opt = attachments.Graph.selection.get(attachment_getting, graph_key)
    if opt:
        return opt.unwrap().vertex_keys
    return containers.Set_of_Graph_VertexKey()
