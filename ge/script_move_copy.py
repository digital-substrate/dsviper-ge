from dsviper import AttachmentMutating

from gei.graph import attachments
from gei import containers, graph

from render.graph import MoveCopyData


def run(attachment_mutating: AttachmentMutating,
        graph_key: graph.GraphKey,
        move_copy_data: MoveCopyData,
        offset: graph.Position) -> None:

    vertex_keys = containers.Set_of_Graph_VertexKey()
    for vertex_key, render_vertex in move_copy_data.vertices.items():
        color = graph.Color()
        color.red = render_vertex.color.redF()
        color.green = render_vertex.color.greenF()
        color.blue = render_vertex.color.blueF()

        visual_attributes = graph.VertexVisualAttributes()
        visual_attributes.value = render_vertex.value
        visual_attributes.color = color
        attachments.Vertex.visual_attributes.set(attachment_mutating, vertex_key, visual_attributes)

        position = graph.Position()
        position.x = render_vertex.position.x() + offset.x
        position.y = render_vertex.position.y() + offset.y
        render_attributes = graph.Vertex2DAttributes()
        render_attributes.position = position
        attachments.Vertex.render_2d_attributes.set(attachment_mutating, vertex_key, render_attributes)

        vertex_keys.add(vertex_key)

    edge_keys = containers.Set_of_Graph_EdgeKey()
    for edge_key, render_edge in move_copy_data.edges.items():
        topology = graph.EdgeTopology()
        topology.va_key = render_edge.va.vertex_key
        topology.vb_key = render_edge.vb.vertex_key
        attachments.Edge.topology.set(attachment_mutating, edge_key, topology)

        edge_keys.add(edge_key)

    attachments.Graph.topology.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    attachments.Graph.topology.union_edge_keys(attachment_mutating, graph_key, edge_keys)
