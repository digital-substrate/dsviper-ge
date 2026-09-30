from dsviper import AttachmentMutating, AttachmentGetting

from gei.graph import attachments
from gei import containers, graph

from ge import tools


def select_all(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Select all vertices and edges in the graph."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology = opt
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    attachments.Graph.selection.union_edge_keys(attachment_mutating, graph_key, edge_keys)


def deselect_all(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Deselect all vertices and edges in the graph."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology = opt
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, edge_keys)


def invert(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Invert the selection of all vertices and edges."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology = opt
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    selected_vertex_keys = containers.Set_of_Graph_VertexKey()
    selected_edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selection = opt
        selected_vertex_keys = selection.vertex_keys
        selected_edge_keys = selection.edge_keys

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, selected_vertex_keys)
    attachments.Graph.selection.union_vertex_keys(
        attachment_mutating, graph_key, tools.difference_vertex_keys(vertex_keys, selected_vertex_keys))
    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, selected_edge_keys)
    attachments.Graph.selection.union_edge_keys(
        attachment_mutating, graph_key, tools.difference_edge_keys(edge_keys, selected_edge_keys))


def set_selection(attachment_mutating: AttachmentMutating,
                  graph_key: graph.GraphKey,
                  vertex_keys: containers.Set_of_Graph_VertexKey,
                  edge_keys: containers.Set_of_Graph_EdgeKey) -> None:
    """Set the selection to specific vertices and edges."""
    selected_vertex_keys = containers.Set_of_Graph_VertexKey()
    selected_edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selection = opt
        selected_vertex_keys = selection.vertex_keys
        selected_edge_keys = selection.edge_keys

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, selected_vertex_keys)
    attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, selected_edge_keys)
    attachments.Graph.selection.union_edge_keys(attachment_mutating, graph_key, edge_keys)


def has_selected(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> bool:
    """Check if any vertices or edges are selected."""
    opt = attachments.Graph.selection.get(attachment_getting, graph_key)
    if opt:
        selection = opt
        return len(selection.vertex_keys) > 0 or len(selection.edge_keys) > 0
    return False
