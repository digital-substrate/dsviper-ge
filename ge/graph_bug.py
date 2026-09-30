from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import containers, graph

from ge import vertex as model_vertex
from ge import edge as model_edge
from ge import random as model_random


def create_with_missing_vertex(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Create a graph with missing vertices (intentionally buggy for testing)."""
    pos0 = graph.Position()
    pos0.x, pos0.y = 100, 100
    pos1 = graph.Position()
    pos1.x, pos1.y = 200, 100
    pos2 = graph.Position()
    pos2.x, pos2.y = 200, 200
    pos3 = graph.Position()
    pos3.x, pos3.y = 100, 200

    v0 = model_vertex.create(attachment_mutating, 1, pos0, model_random.make_color())
    v1 = model_vertex.create(attachment_mutating, 2, pos1, model_random.make_color())
    v2 = model_vertex.create(attachment_mutating, 3, pos2, model_random.make_color())
    v3 = model_vertex.create(attachment_mutating, 4, pos3, model_random.make_color())

    e0 = model_edge.create(attachment_mutating, v0, v1)
    e1 = model_edge.create(attachment_mutating, v1, v2)
    e2 = model_edge.create(attachment_mutating, v2, v3)
    e3 = model_edge.create(attachment_mutating, v3, v0)

    # Introduce the bug: only include v0 and v1 in topology, but all edges
    topology = graph.GraphTopology()
    topology.vertex_keys = containers.Set_of_Graph_VertexKey()
    topology.vertex_keys.add(v0)
    topology.vertex_keys.add(v1)
    topology.edge_keys = containers.Set_of_Graph_EdgeKey()
    topology.edge_keys.add(e0)
    topology.edge_keys.add(e1)
    topology.edge_keys.add(e2)
    topology.edge_keys.add(e3)

    attachments.Graph.topology.set(attachment_mutating, graph_key, topology)
    attachments.Graph.selection.set(attachment_mutating, graph_key, graph.GraphSelection())


def create_with_missing_vertex_properties(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Create a graph with vertices missing their properties (intentionally buggy)."""
    # Create vertices without properties (just keys)
    v0 = graph.VertexKey.create()
    v1 = graph.VertexKey.create()
    v2 = graph.VertexKey.create()
    v3 = graph.VertexKey.create()

    e0 = model_edge.create(attachment_mutating, v0, v1)
    e1 = model_edge.create(attachment_mutating, v1, v2)
    e2 = model_edge.create(attachment_mutating, v2, v3)
    e3 = model_edge.create(attachment_mutating, v3, v0)

    # Create some valid vertices
    pos4 = graph.Position()
    pos4.x, pos4.y = 100, 100
    pos5 = graph.Position()
    pos5.x, pos5.y = 200, 100
    pos6 = graph.Position()
    pos6.x, pos6.y = 300, 150

    v4 = model_vertex.create(attachment_mutating, 1, pos4, model_random.make_color())
    v5 = model_vertex.create(attachment_mutating, 2, pos5, model_random.make_color())
    v6 = model_vertex.create(attachment_mutating, 3, pos6, model_random.make_color())

    e4 = model_edge.create(attachment_mutating, v4, v5)
    e5 = model_edge.create(attachment_mutating, v5, v6)

    # Mix valid and invalid vertices/edges in topology
    topology = graph.GraphTopology()
    topology.vertex_keys = containers.Set_of_Graph_VertexKey()
    topology.vertex_keys.add(v0)
    topology.vertex_keys.add(v1)
    topology.vertex_keys.add(v4)
    topology.vertex_keys.add(v5)
    topology.edge_keys = containers.Set_of_Graph_EdgeKey()
    topology.edge_keys.add(e0)
    topology.edge_keys.add(e1)
    topology.edge_keys.add(e2)
    topology.edge_keys.add(e3)
    topology.edge_keys.add(e4)
    topology.edge_keys.add(e5)

    attachments.Graph.topology.set(attachment_mutating, graph_key, topology)
    attachments.Graph.selection.set(attachment_mutating, graph_key, graph.GraphSelection())


def create_with_error(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Create a graph and then raise an error (for testing error handling)."""
    pos0 = graph.Position()
    pos0.x, pos0.y = 100, 100
    pos1 = graph.Position()
    pos1.x, pos1.y = 200, 100

    v0 = model_vertex.add(attachment_mutating, graph_key, 1, pos0, model_random.make_color())
    v1 = model_vertex.add(attachment_mutating, graph_key, 2, pos1, model_random.make_color())
    model_edge.add(attachment_mutating, graph_key, v0, v1)

    raise RuntimeError("This is a voluntary crash but without any consequence.")
