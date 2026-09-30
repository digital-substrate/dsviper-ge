from dsviper import AttachmentMutating, AttachmentGetting

from gei.graph import attachments
from gei import graph

from ge import random as model_random


def referenced_keys(attachment_getting: AttachmentGetting,
                    graph_key: graph.GraphKey) -> set[graph.VertexKey]:
    """Get all vertex keys referenced by the graph (including from edges)."""
    vertex_keys = set[graph.VertexKey]()
    edge_keys = set[graph.EdgeKey]()

    opt = attachments.Graph.topology.get(attachment_getting, graph_key)
    if opt:
        topology = opt
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    for edge_key in edge_keys:
        opt_edge = attachments.Edge.topology.get(attachment_getting, edge_key)
        if opt_edge:
            edge_topo = opt_edge
            vertex_keys.add(edge_topo.va_key)
            vertex_keys.add(edge_topo.vb_key)

    return vertex_keys


def increment_value(attachment_mutating: AttachmentMutating,
                    vertex_keys: set[graph.VertexKey],
                    increment: int) -> None:
    """Increment the value of vertices."""
    color = model_random.make_color()
    for vertex_key in vertex_keys:
        opt = attachments.Vertex.visual_attributes.get(attachment_mutating, vertex_key)
        if opt:
            attrs = opt
            attachments.Vertex.visual_attributes.set_value(
                attachment_mutating, vertex_key, attrs.value + increment
            )
            attachments.Vertex.visual_attributes.set_color(
                attachment_mutating, vertex_key, color
            )


def move(attachment_mutating: AttachmentMutating,
         vertex_keys, offset: graph.Position) -> None:
    """Move vertices by an offset."""
    for vertex_key in vertex_keys:
        opt = attachments.Vertex.render_2d_attributes.get(attachment_mutating, vertex_key)
        if opt:
            attrs = opt
            position = graph.Position()
            position.x = attrs.position.x + offset.x
            position.y = attrs.position.y + offset.y
            attachments.Vertex.render_2d_attributes.set_position(
                attachment_mutating, vertex_key, position
            )
