from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from dsviper import AttachmentGetting

from gei.graph import attachments
from gei import graph

if TYPE_CHECKING:
    pass


@dataclass
class SortedEdge:
    """An edge in the sorted graph."""
    edge_key: graph.EdgeKey
    vertex_key: graph.VertexKey


@dataclass
class SortedVertex:
    """A vertex in the sorted graph."""
    vertex_key: graph.VertexKey
    value: int
    edges: list[SortedEdge] = field(default_factory=list)


class GraphSortedByValue:
    """A graph structure sorted by vertex value."""

    def __init__(self):
        self.vertices: dict[graph.VertexKey, SortedVertex] = {}

    def sorted_vertices(self) -> list[SortedVertex]:
        """Get vertices sorted by value."""
        result = list(self.vertices.values())
        result.sort(key=lambda v: (v.value, v.vertex_key.instance_id()))
        return result

    @staticmethod
    def build(getting: AttachmentGetting, graph_key: graph.GraphKey) -> GraphSortedByValue:
        """Build a sorted graph from attachments."""
        result = GraphSortedByValue()

        vertex_keys = set()
        edge_keys = set()

        opt_topology = attachments.Graph.topology.get(getting, graph_key)
        if opt_topology:
            topology = opt_topology
            vertex_keys = set(topology.vertex_keys)
            edge_keys = set(topology.edge_keys)

        # Add vertices from edge topologies (in case they're not in graph topology)
        for edge_key in edge_keys:
            opt_edge_topo = attachments.Edge.topology.get(getting, edge_key)
            if opt_edge_topo:
                edge_topo = opt_edge_topo
                vertex_keys.add(edge_topo.va_key)
                vertex_keys.add(edge_topo.vb_key)

        # Build vertex entries
        for vertex_key in vertex_keys:
            opt_attrs = attachments.Vertex.visual_attributes.get(getting, vertex_key)
            value = -1
            if opt_attrs:
                value = opt_attrs.value
            result.vertices[vertex_key] = SortedVertex(vertex_key, value)

        # Build edge entries
        for edge_key in edge_keys:
            opt_edge_topo = attachments.Edge.topology.get(getting, edge_key)
            if not opt_edge_topo:
                continue

            edge_topo = opt_edge_topo
            va_key = edge_topo.va_key
            vb_key = edge_topo.vb_key

            s_va = result.vertices.get(va_key)
            s_vb = result.vertices.get(vb_key)

            if s_va is None or s_vb is None:
                continue

            # Add edge to the vertex with lower value
            if s_va.value < s_vb.value:
                s_va.edges.append(SortedEdge(edge_key, vb_key))
            else:
                s_vb.edges.append(SortedEdge(edge_key, va_key))

        # Sort edges within each vertex
        for vertex in result.vertices.values():
            vertex.edges.sort(key=lambda e: result.vertices[e.vertex_key].value)

        return result
