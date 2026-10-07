# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

"""The name of every field of Graph's structures, as constants: code that handles a structure
through the dynamic API completes the name and a type checker checks it, where a string literal
is neither. Their paths are in the paths module."""

from __future__ import annotations

import typing

class Color:
    """The field names of Color."""
    red: typing.Final = "red"
    green: typing.Final = "green"
    blue: typing.Final = "blue"


class EdgeTopology:
    """The field names of EdgeTopology."""
    va_key: typing.Final = "vaKey"
    vb_key: typing.Final = "vbKey"


class GraphDescription:
    """The field names of GraphDescription."""
    name: typing.Final = "name"
    author: typing.Final = "author"
    create_date: typing.Final = "createDate"


class GraphSelection:
    """The field names of GraphSelection."""
    vertex_keys: typing.Final = "vertexKeys"
    edge_keys: typing.Final = "edgeKeys"


class GraphTopology:
    """The field names of GraphTopology."""
    vertex_keys: typing.Final = "vertexKeys"
    edge_keys: typing.Final = "edgeKeys"


class Position:
    """The field names of Position."""
    x: typing.Final = "x"
    y: typing.Final = "y"


class Rectangle:
    """The field names of Rectangle."""
    x: typing.Final = "x"
    y: typing.Final = "y"
    w: typing.Final = "w"
    h: typing.Final = "h"


class Vertex2DAttributes:
    """The field names of Vertex2DAttributes."""
    position: typing.Final = "position"


class VertexVisualAttributes:
    """The field names of VertexVisualAttributes."""
    value: typing.Final = "value"
    color: typing.Final = "color"
