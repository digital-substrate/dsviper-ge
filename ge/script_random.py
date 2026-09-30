from dsviper import AttachmentMutating

from gei import graph

from ge import random as model_random
from ge import selection_random


def random_graph(attachment_mutating: AttachmentMutating,
                 graph_key: graph.GraphKey,
                 vertex_count: int,
                 edge_count: int,
                 rect: graph.Rectangle) -> None:
    """Create a random graph and randomly select some elements."""
    model_random.graph(attachment_mutating, graph_key, vertex_count, edge_count, rect)
    selection_random.mixed(attachment_mutating, graph_key)
