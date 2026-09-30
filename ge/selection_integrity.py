from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import graph

from ge import tools


def restore(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Restore selection to only include vertices and edges that exist in topology."""
    vertex_keys = set[graph.VertexKey]()
    edge_keys = set[graph.EdgeKey]()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology = opt
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    selected_vertex_keys = set[graph.VertexKey]()
    selected_edge_keys = set[graph.EdgeKey]()

    opt = attachments.Graph.selection.get(attachment_mutating, graph_key)
    if opt:
        selection = opt
        selected_vertex_keys = selection.vertex_keys
        selected_edge_keys = selection.edge_keys

    restored_vertex_keys = tools.intersection_vertex_keys(selected_vertex_keys, vertex_keys)
    restored_edge_keys = tools.intersection_edge_keys(selected_edge_keys, edge_keys)

    attachments.Graph.selection.subtract_vertex_keys(attachment_mutating, graph_key, selected_vertex_keys)
    attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, restored_vertex_keys)
    attachments.Graph.selection.subtract_edge_keys(attachment_mutating, graph_key, selected_edge_keys)
    attachments.Graph.selection.union_edge_keys(attachment_mutating, graph_key, restored_edge_keys)
