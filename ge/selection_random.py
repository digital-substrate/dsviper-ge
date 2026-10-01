from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import containers, graph

from ge import random as model_random


def mixed(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Randomly select both vertices and edges."""
    vertices(attachment_mutating, graph_key)
    edges(attachment_mutating, graph_key)


def vertices(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Randomly select approximately 1/4 of the vertices."""
    vertex_keys = containers.Set_of_Graph_VertexKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        vertex_keys = opt.unwrap().vertex_keys

    candidate_keys = list(vertex_keys)
    if not candidate_keys:
        return

    count = len(vertex_keys) // 4
    random_vertex_keys = containers.Set_of_Graph_VertexKey()

    while len(random_vertex_keys) < count:
        candidate = model_random.random_int() % len(candidate_keys)
        random_vertex_keys.add(candidate_keys[candidate])

    attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, random_vertex_keys)


def edges(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Randomly select approximately 1/4 of the edges."""
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        edge_keys = opt.unwrap().edge_keys

    candidate_keys = list(edge_keys)
    if not candidate_keys:
        return

    count = len(edge_keys) // 4
    random_edge_keys = containers.Set_of_Graph_EdgeKey()

    while len(random_edge_keys) < count:
        candidate = model_random.random_int() % len(candidate_keys)
        random_edge_keys.add(candidate_keys[candidate])

    attachments.Graph.topology.union_edge_keys(attachment_mutating, graph_key, random_edge_keys)
