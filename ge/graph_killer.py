from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import containers, graph

from ge import vertex as model_vertex
from ge import random as model_random


def shoot(attachment_mutating: AttachmentMutating,
          graph_key: graph.GraphKey,
          vertex_count: int) -> None:
    """Create many vertices and then keep only the last one (kills all previous work)."""
    position = graph.Position()
    position.x = 100
    position.y = 100
    color = model_random.make_color()

    for _ in range(vertex_count):
        model_vertex.add(attachment_mutating, graph_key, 42, position, color)

    killer = model_vertex.add(attachment_mutating, graph_key, 42, position, color)

    attachments.Graph.description.set_name(attachment_mutating, graph_key, "They have killed Commit!")

    topology = graph.GraphTopology()
    topology.vertex_keys = containers.Set_of_Graph_VertexKey()
    topology.vertex_keys.add(killer)
    topology.edge_keys = containers.Set_of_Graph_EdgeKey()
    attachments.Graph.topology.set(attachment_mutating, graph_key, topology)
