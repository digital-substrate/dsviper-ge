from dsviper import AttachmentMutating, AttachmentGetting

from gei.graph import attachments
from gei import containers, graph

from ge import tools


def select(attachment_mutating: AttachmentMutating,
           graph_key: graph.GraphKey,
           edge_key: graph.EdgeKey) -> None:
    """Select a single edge, deselecting all others."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selection = opt
        vertex_keys = selection.vertex_keys
        edge_keys = selection.edge_keys

    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, edge_keys)

    new_selection = containers.Set_of_Graph_EdgeKey()
    new_selection.add(edge_key)
    attachments.Graph.selection.union_edge_keys(attachment_mutating, graph_key, new_selection)
    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, vertex_keys)


def combine(attachment_mutating: AttachmentMutating,
            graph_key: graph.GraphKey,
            edge_key: graph.EdgeKey,
            selected: bool) -> None:
    """Add or remove an edge from the selection."""
    edge_keys = containers.Set_of_Graph_EdgeKey()
    edge_keys.add(edge_key)

    if selected:
        attachments.Graph.selection.union_edge_keys(attachment_mutating, graph_key, edge_keys)
    else:
        attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, edge_keys)


def select_all(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Select all edges in the graph."""
    edge_keys = containers.Set_of_Graph_EdgeKey()
    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        edge_keys = opt.edge_keys

    attachments.Graph.selection.union_edge_keys(attachment_mutating, graph_key, edge_keys)


def deselect_all(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Deselect all edges in the graph."""
    edge_keys = containers.Set_of_Graph_EdgeKey()
    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        edge_keys = opt.edge_keys

    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, edge_keys)


def invert(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Invert the edge selection."""
    edge_keys = containers.Set_of_Graph_EdgeKey()
    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        edge_keys = opt.edge_keys

    selected_edge_keys = containers.Set_of_Graph_EdgeKey()
    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selected_edge_keys = opt.edge_keys

    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, selected_edge_keys)
    attachments.Graph.selection.union_edge_keys(
        attachment_mutating, graph_key, tools.difference_edge_keys(edge_keys, selected_edge_keys))


def selected(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> containers.Set_of_Graph_EdgeKey:
    """Get the set of selected edges."""
    opt = attachments.Graph.selection.get(attachment_getting, graph_key)
    if opt:
        return opt.edge_keys
    return containers.Set_of_Graph_EdgeKey()


def has_selected(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> bool:
    """Check if any edges are selected."""
    return len(selected(attachment_getting, graph_key)) > 0
