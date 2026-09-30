from __future__ import annotations

import typing

from PySide6.QtCore import QObject, Signal, QPointF
from PySide6.QtGui import QColor

from gei import graph


class TransientNotifier(QObject):
    """Notifier for transient (non-persisted) changes.

    Used for live updates during drag operations, color picker changes, etc.
    """

    # Signals
    vertices_moved = Signal(object, QPointF)  # the moved vertex keys, offset
    vertex_value_changed = Signal(object, int)  # graph.VertexKey, value
    vertex_color_changed = Signal(object, QColor)  # graph.VertexKey, color
    vertex_position_changed = Signal(object, QPointF)  # graph.VertexKey, position

    _instance: TransientNotifier | None = None

    @classmethod
    def instance(cls) -> TransientNotifier:
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        super().__init__()

    def notify_vertices_move(self, keys: typing.Iterable[graph.VertexKey], offset: QPointF):
        """Notify that vertices are being moved."""
        self.vertices_moved.emit(keys, offset)

    def notify_vertex_value(self, key: graph.VertexKey, value: int):
        """Notify that a vertex value changed."""
        self.vertex_value_changed.emit(key, value)

    def notify_vertex_color(self, key: graph.VertexKey, color: QColor):
        """Notify that a vertex color changed."""
        self.vertex_color_changed.emit(key, color)

    def notify_vertex_position(self, key: graph.VertexKey, position: QPointF):
        """Notify that a vertex position changed."""
        self.vertex_position_changed.emit(key, position)
