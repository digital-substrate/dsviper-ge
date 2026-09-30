from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import containers, graph


def create(attachment_mutating: AttachmentMutating,
           value: int,
           position: graph.Position,
           color: graph.Color) -> graph.VertexKey:

    vertex_key = graph.VertexKey.create()

    visual_attributes = graph.VertexVisualAttributes()
    visual_attributes.value = value
    visual_attributes.color = color
    attachments.Vertex.visual_attributes.set(attachment_mutating, vertex_key, visual_attributes)

    render_attributes = graph.Vertex2DAttributes()
    render_attributes.position = position
    attachments.Vertex.render_2d_attributes.set(attachment_mutating, vertex_key, render_attributes)

    return vertex_key


def add(attachment_mutating: AttachmentMutating,
        graph_key: graph.GraphKey,
        value: int,
        position: graph.Position,
        color: graph.Color) -> graph.VertexKey:

    vertex_key = create(attachment_mutating, value, position, color)

    vertex_keys = containers.Set_of_Graph_VertexKey()
    vertex_keys.add(vertex_key)
    attachments.Graph.topology.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)

    return vertex_key
