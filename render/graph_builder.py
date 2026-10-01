from __future__ import annotations

from dsviper import AttachmentGetting
from PySide6.QtCore import QPointF
from PySide6.QtGui import QColor

from gei.graph import attachments
from gei import graph as gei_graph
from .vertex import RenderVertex
from .edge import RenderEdge
from .graph import RenderGraph


def _q_point_from_position(position: gei_graph.Position) -> QPointF:
    """Convert a gei_graph.Position to a QPointF."""
    return QPointF(position.x, position.y)


def _q_color_from_color(color) -> QColor:
    """Convert a gei_graph.Color to a QColor."""
    return QColor(
        int(color.red * 255),
        int(color.green * 255),
        int(color.blue * 255)
    )


def _render_vertex(getting: AttachmentGetting, is_valid: bool,
                   position: gei_graph.Position, vertex_key: gei_graph.VertexKey) -> RenderVertex:
    """Create a RenderVertex from attachments."""
    opt_attrs = attachments.Vertex.visual_attributes.get(getting, vertex_key)
    if opt_attrs:
        attrs = opt_attrs.unwrap()
        value = attrs.value
        color = _q_color_from_color(attrs.color)
    else:
        value = -1
        color = QColor(255, 255, 255)

    return RenderVertex.make(
        vertex_key, value, _q_point_from_position(position), color, is_valid
    )


def _collect_vertices(getting: AttachmentGetting, graph: RenderGraph):
    """Collect vertices from the graph topology."""
    opt_topology = attachments.Graph.topology.get(getting, graph.graph_key)
    vertex_keys = set()
    if opt_topology:
        vertex_keys = set(opt_topology.unwrap().vertex_keys)

    for vertex_key in vertex_keys:
        opt_attrs = attachments.Vertex.render_2d_attributes.get(getting, vertex_key)
        if opt_attrs:
            attrs = opt_attrs.unwrap()
            r_vertex = _render_vertex(getting, True, attrs.position, vertex_key)
            graph.vertex_map[vertex_key] = r_vertex
            graph.vertex_keys.add(vertex_key)
        else:
            graph.is_valid = False


def _collect_edge_vertex_keys(getting: AttachmentGetting, edge_keys: set[gei_graph.EdgeKey]) -> set[gei_graph.VertexKey]:
    """Collect vertex keys from edge topologies."""
    result = set()
    for edge_key in edge_keys:
        opt_topology = attachments.Edge.topology.get(getting, edge_key)
        if opt_topology:
            topology = opt_topology.unwrap()
            result.add(topology.va_key)
            result.add(topology.vb_key)
    return result


def _collect_edges(getting: AttachmentGetting, graph: RenderGraph):
    """Collect edges from the graph topology."""
    opt_topology = attachments.Graph.topology.get(getting, graph.graph_key)
    edge_keys = set()
    if opt_topology:
        edge_keys = set(opt_topology.unwrap().edge_keys)

    vertex_keys = _collect_edge_vertex_keys(getting, edge_keys)
    for vertex_key in vertex_keys:
        if vertex_key not in graph.vertex_map:
            opt_attrs = attachments.Vertex.render_2d_attributes.get(getting, vertex_key)
            if opt_attrs:
                attrs = opt_attrs.unwrap()
                graph.vertex_map[vertex_key] = _render_vertex(getting, False, attrs.position, vertex_key)
                graph.vertex_keys.add(vertex_key)
        graph.is_valid = False

    for edge_key in edge_keys:
        opt_topology = attachments.Edge.topology.get(getting, edge_key)
        if not opt_topology:
            graph.is_valid = False
            continue

        topology = opt_topology.unwrap()
        va = graph.vertex_map.get(topology.va_key)
        vb = graph.vertex_map.get(topology.vb_key)

        if va is not None and vb is not None:
            graph.edge_map[edge_key] = RenderEdge.make(edge_key, va, vb)
            graph.edge_keys.add(edge_key)


def _collect_selection(getting: AttachmentGetting, graph: RenderGraph):
    """Collect selection from the graph."""
    opt_selection = attachments.Graph.selection.get(getting, graph.graph_key)
    graph.selected_vertex_keys.clear()
    graph.selected_edge_keys.clear()
    if opt_selection:
        selection = opt_selection.unwrap()
        graph.selected_vertex_keys = set(selection.vertex_keys)
        graph.selected_edge_keys = set(selection.edge_keys)


def build(getting: AttachmentGetting, graph_key: gei_graph.GraphKey) -> RenderGraph:
    """Build a RenderGraph from attachments."""
    result = RenderGraph.make(graph_key)
    _collect_vertices(getting, result)
    _collect_edges(getting, result)
    _collect_selection(getting, result)
    result.prepare()
    return result
