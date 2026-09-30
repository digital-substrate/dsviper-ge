from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import graph


def create(attachment_mutating: AttachmentMutating,
           va_key: graph.VertexKey,
           vb_key: graph.VertexKey) -> graph.EdgeKey:

    edge_key = graph.EdgeKey.create()

    topology = graph.EdgeTopology()
    topology.va_key = va_key
    topology.vb_key = vb_key
    attachments.Edge.topology.set(attachment_mutating, edge_key, topology)

    return edge_key


def add(attachment_mutating: AttachmentMutating,
        graph_key: graph.GraphKey,
        va_key: graph.VertexKey,
        vb_key: graph.VertexKey) -> graph.EdgeKey:

    edge_key = create(attachment_mutating, va_key, vb_key)

    edge_keys = set[graph.EdgeKey]()
    edge_keys.add(edge_key)
    attachments.Graph.topology.union_edge_keys(attachment_mutating, graph_key, edge_keys)

    return edge_key
