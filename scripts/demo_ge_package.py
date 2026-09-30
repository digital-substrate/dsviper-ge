from __future__ import annotations
from dsviper import *
from gei import graph
from gei.graph import attachments as A
import random
import traceback

def random_word(size: int):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    l = len(letters) - 1
    result = ""
    for _ in range(size):
        result += letters[random.randint(0, l)]
    return result


def random_comment(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey):
    v = random_word(10)
    A.Graph.comments.insert(attachment_mutating, graph_key, ValueUUId.INVALID, ValueUUId.create(), v)


def random_tag(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey):
    A.Graph.tags.union(attachment_mutating, graph_key, {random_word(3): random_word(5)})


def random_position(min: int, max: int) -> graph.Position:
    return graph.Position(x=random.randint(min, max), y=random.randint(min, max))


def random_color(min: int, max: int) -> graph.Color:
    return graph.Color(red=random.randint(min, max) / 255,
                       green=random.randint(min, max) / 255,
                       blue=random.randint(min, max) / 255)


def create_vertex(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey, value: int, position: graph.Position, color: graph.Color) -> graph.VertexKey:
    va = graph.VertexVisualAttributes(value=value, color=color)
    vr = graph.Vertex2DAttributes(position=position)

    vertex_key = graph.VertexKey.create()
    A.Vertex.visual_attributes.set(attachment_mutating, vertex_key, va)
    A.Vertex.render_2d_attributes.set(attachment_mutating, vertex_key, vr)

    return vertex_key


def add_vertex(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey, value: int, position: graph.Position, color: graph.Color) -> graph.VertexKey:
    vertex_key = create_vertex(attachment_mutating, graph_key, value, position, color)
    A.Graph.topology.union_vertex_keys(attachment_mutating, graph_key, {vertex_key})
    return vertex_key


def random_vertex(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey):
    position = random_position(40, 400)
    color = random_color(40, 100)
    add_vertex(attachment_mutating, graph_key, random.randint(1, 100), position, color)


def create_edge(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey, va_key: graph.VertexKey, vb_key: graph.VertexKey) -> graph.EdgeKey:
    edge_key = graph.EdgeKey.create()
    A.Edge.topology.set(attachment_mutating, edge_key, graph.EdgeTopology(va_key=va_key, vb_key=vb_key))
    A.Graph.topology.union_edge_keys(attachment_mutating, graph_key, {edge_key})
    return edge_key


def has_edge(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey, va_key: graph.VertexKey, vb_key: graph.VertexKey) -> graph.EdgeKey | None:
    topology = A.Graph.topology.get(attachment_mutating, graph_key)
    for edge_key in topology.edge_keys:
        e_topology = A.Edge.topology.get(attachment_mutating, edge_key)
        if e_topology is None:
            continue

        e_va_key = e_topology.va_key
        e_vb_key = e_topology.vb_key
        if (e_va_key == va_key and e_vb_key == vb_key) or (e_va_key == vb_key and e_vb_key == va_key):
            return edge_key

    return None

def random_edge(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey) -> graph.EdgeKey:
    topology = A.Graph.topology.get(attachment_mutating, graph_key)
    vertex_keys = topology.vertex_keys
    edge_keys = topology.edge_keys

    vertex_count = len(vertex_keys)
    max_edge = (vertex_count * (vertex_count - 1)) / 2
    assert len(vertex_keys)
    assert len(edge_keys) < max_edge

    v_keys: list[graph.VertexKey] = list(vertex_keys)

    while True:
        ra = random.randint(0, len(v_keys) - 1)
        rb = random.randint(0, len(v_keys) - 1)
        if ra == rb:
             continue

        va_key = v_keys[ra]
        vb_key = v_keys[rb]
        if not has_edge(attachment_mutating, graph_key, va_key, vb_key):
            return create_edge(attachment_mutating, graph_key, va_key, vb_key)

def random_graph(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey, vertex_count: int, edge_count: int):

    def r_next_value(attachment_getting: AttachmentGetting) -> int:
        value = -1
        for key in A.Vertex.visual_attributes.keys(attachment_getting):
            if v := A.Vertex.visual_attributes.get(attachment_getting, key):
                value = max(value, v.value)
        return value + 1

    def r_vertex(attachment_mutating: AttachmentMutating, graph_key: graph.GraphKey, value) -> graph.VertexKey:
        position = random_position(40, 400)
        color = random_color(40, 100)
        return create_vertex(attachment_mutating, graph_key, value, position, color)

    def r_has_edge(va_key: graph.VertexKey, vb_key: graph.VertexKey, edges: list[graph.EdgeTopology]):
        for edge in edges:
          if (edge.va_key == va_key and edge.vb_key == vb_key) or (edge.va_key == vb_key and edge.vb_key == va_key):
               return True
        return False

    def r_add_edge(attachment_mutating: AttachmentMutating, va_key: graph.VertexKey, vb_key: graph.VertexKey, edges: list[graph.EdgeTopology], edge_keys: set[graph.EdgeKey]):
        edge_key = graph.EdgeKey.create()
        edge = graph.EdgeTopology(va_key=va_key, vb_key=vb_key)
        A.Edge.topology.set(attachment_mutating, edge_key, edge)
        edges.append(edge)
        edge_keys.add(edge_key)

    def r_add_edges(attachment_mutating: AttachmentMutating, edge_count: int, vertex_keys: set[graph.VertexKey]):
        candidate_keys = list(vertex_keys)
        edges: list[graph.EdgeTopology] = list()
        edge_keys: set[graph.EdgeKey] = set()

        max_edge = len(vertex_keys) * (len(vertex_keys) - 1) / 2
        count = min(max_edge, edge_count)

        while len(edge_keys) < count:
            va_key = random.choice(candidate_keys)
            vb_key = random.choice(candidate_keys)
            if va_key == vb_key:
                continue

            if not r_has_edge(va_key, vb_key, edges):
                r_add_edge(attachment_mutating, va_key, vb_key, edges, edge_keys)

        return edge_keys

    value = r_next_value(attachment_mutating)
    vertex_keys: set[graph.VertexKey] = set()
    for _ in range(vertex_count):
        vertex_keys.add(r_vertex(attachment_mutating, graph_key, value))
        value += 1

    edge_keys = r_add_edges(attachment_mutating, edge_count, vertex_keys)
    A.Graph.topology.union_vertex_keys(attachment_mutating, graph_key, vertex_keys)
    A.Graph.topology.union_edge_keys(attachment_mutating, graph_key, edge_keys)

#ctx.reset()
#ctx.dispatch("random_vertex", random_vertex, ge_graph_key()) # eval me two times
#ctx.dispatch("random edge", random_edge, ge_graph_key())
#ctx.dispatch("random tags", random_tag, ge_graph_key())
#ctx.dispatch("random comment", random_comment, ge_graph_key())
#ctx.dispatch("random graph", random_graph, ge_graph_key(), 6, 8)
#ctx.undo()
#ctx.redo()

#for r in range(100):
#    ctx.dispatch("random_vertex", random_vertex, ge_graph_key()) # eval me two times
