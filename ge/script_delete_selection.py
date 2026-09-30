from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import graph

from ge import graph_topology
from ge import selection_edges


def delete_selection(attachment_mutating: AttachmentMutating,
                     graph_key: graph.GraphKey) -> None:
    """Delete selected vertices and edges from the graph."""
    vertex_keys = set[graph.VertexKey]()
    edge_keys = set[graph.EdgeKey]()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selection = opt
        vertex_keys = selection.vertex_keys
        edge_keys = selection.edge_keys

    graph_topology.remove(attachment_mutating, graph_key, vertex_keys, edge_keys)
    selection_edges.deselect_all(attachment_mutating, graph_key)


def delete_selection_bugged(attachment_mutating: AttachmentMutating,
                            graph_key: graph.GraphKey) -> None:
    """Delete selected vertices (bugged version for testing)."""
    vertex_keys = set[graph.VertexKey]()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        vertex_keys = opt.vertex_keys

    graph_topology.remove_bugged(attachment_mutating, graph_key, vertex_keys)
    selection_edges.deselect_all(attachment_mutating, graph_key)
