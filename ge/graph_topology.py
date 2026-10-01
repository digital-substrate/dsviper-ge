from dsviper import AttachmentMutating, AttachmentGetting

from gei.graph import attachments
from gei import containers, graph

from ge import tools


def clear(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> None:
    """Clear all topology, selection, comments, and tags from a graph."""
    attachments.Graph.topology.set(attachment_mutating, graph_key, graph.GraphTopology())
    attachments.Graph.selection.set(attachment_mutating, graph_key, graph.GraphSelection())
    attachments.Graph.comments.set(attachment_mutating, graph_key, containers.XArray_of_string())
    attachments.Graph.tags.set(attachment_mutating, graph_key, containers.Map_of_string_to_string())


def remove(attachment_mutating: AttachmentMutating,
           graph_key: graph.GraphKey,
           vertex_keys: containers.Set_of_Graph_VertexKey,
           edge_keys: containers.Set_of_Graph_EdgeKey) -> None:
    """Remove vertices and edges from the graph, including connected edges."""
    topology_edge_keys = containers.Set_of_Graph_EdgeKey()
    opt = attachments.Graph.topology.get(attachment_mutating, graph_key)
    if opt:
        topology_edge_keys = opt.unwrap().edge_keys

    # Find edges connected to removed vertices
    connected_edge_keys = containers.Set_of_Graph_EdgeKey()
    for vertex_key in vertex_keys:
        for edge_key in topology_edge_keys:
            opt_edge = attachments.Edge.topology.get(attachment_mutating, edge_key)
            if not opt_edge:
                continue
            edge = opt_edge.unwrap()
            if edge.va_key == vertex_key or edge.vb_key == vertex_key:
                connected_edge_keys.add(edge_key)

    attachments.Graph.topology.subtract_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    all_edges_to_remove = tools.union_edge_keys(edge_keys, connected_edge_keys)
    attachments.Graph.topology.subtract_edge_keys(attachment_mutating, graph_key, all_edges_to_remove)


def remove_bugged(attachment_mutating: AttachmentMutating,
                  graph_key: graph.GraphKey,
                  vertex_keys: containers.Set_of_Graph_VertexKey) -> None:
    """Remove vertices without removing connected edges (intentionally buggy)."""
    attachments.Graph.topology.subtract_vertex_keys(attachment_mutating, graph_key, vertex_keys)


def has_edge(attachment_getting: AttachmentGetting,
             graph_key: graph.GraphKey,
             va_key: graph.VertexKey,
             vb_key: graph.VertexKey) -> graph.EdgeKey | None:
    """Check if an edge exists between two vertices, return the edge key if found."""
    opt = attachments.Graph.topology.get(attachment_getting, graph_key)
    if not opt:
        return None

    topology = opt.unwrap()
    for edge_key in topology.edge_keys:
        opt_edge = attachments.Edge.topology.get(attachment_getting, edge_key)
        if not opt_edge:
            continue
        edge = opt_edge.unwrap()

        if ((edge.va_key == va_key and edge.vb_key == vb_key) or
            (edge.va_key == vb_key and edge.vb_key == va_key)):
            return edge_key

    return None


def has_vertices(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> bool:
    """Check if the graph has any vertices."""
    opt = attachments.Graph.topology.get(attachment_getting, graph_key)
    if opt:
        return len(opt.unwrap().vertex_keys) > 0
    return False


def has_edges(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> bool:
    """Check if the graph has any edges."""
    opt = attachments.Graph.topology.get(attachment_getting, graph_key)
    if opt:
        return len(opt.unwrap().edge_keys) > 0
    return False


def has_remaining_edges(attachment_getting: AttachmentGetting, graph_key: graph.GraphKey) -> bool:
    """Check if there are remaining edges that can be added to the graph."""
    vertex_keys = containers.Set_of_Graph_VertexKey()
    edge_keys = containers.Set_of_Graph_EdgeKey()

    opt = attachments.Graph.topology.get(attachment_getting, graph_key)
    if opt:
        topology = opt.unwrap()
        vertex_keys = topology.vertex_keys
        edge_keys = topology.edge_keys

    vertex_count = len(vertex_keys)
    max_edges = vertex_count * (vertex_count - 1) // 2
    return vertex_count > 1 and len(edge_keys) < max_edges
