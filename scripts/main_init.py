from __future__ import annotations
from dsviper import *
from gei import graph
from ge import random as model_random
from ge import graph_topology, selection_vertices, selection_edges


def ge_render_rect() -> graph.Rectangle:
    """Return the rect of the render canvas."""
    r = graph.Rectangle()
    r.x, r.y = 0, 0
    size = render_model.render_widget().size()
    r.w = size.width()
    r.h = size.height()
    return r

def ge_graph_key() -> graph.GraphKey:
    """Return the key of the graph."""
    return ctx.graph_key

def inspect_selection():
    """Return (key, attachment, path) of the current document selection."""
    return _documents_panel.documents().get_selected_inspection()

print("** GraphEditor: Hello from main_init.py **")
print("")
