# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

"""The path of every field of Graph's structures, for code that reads or writes a field
through the dynamic API. The field names are in the fields module."""

from __future__ import annotations

import typing

import dsviper

from . import fields

class Color:
    """The field paths of Color."""
    red: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Color.red).const()
    green: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Color.green).const()
    blue: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Color.blue).const()


class EdgeTopology:
    """The field paths of EdgeTopology."""
    va_key: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.EdgeTopology.va_key).const()
    vb_key: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.EdgeTopology.vb_key).const()


class GraphDescription:
    """The field paths of GraphDescription."""
    name: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.GraphDescription.name).const()
    author: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.GraphDescription.author).const()
    create_date: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.GraphDescription.create_date).const()


class GraphSelection:
    """The field paths of GraphSelection."""
    vertex_keys: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.GraphSelection.vertex_keys).const()
    edge_keys: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.GraphSelection.edge_keys).const()


class GraphTopology:
    """The field paths of GraphTopology."""
    vertex_keys: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.GraphTopology.vertex_keys).const()
    edge_keys: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.GraphTopology.edge_keys).const()


class Position:
    """The field paths of Position."""
    x: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Position.x).const()
    y: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Position.y).const()


class Rectangle:
    """The field paths of Rectangle."""
    x: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Rectangle.x).const()
    y: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Rectangle.y).const()
    w: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Rectangle.w).const()
    h: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Rectangle.h).const()


class Vertex2DAttributes:
    """The field paths of Vertex2DAttributes."""
    position: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.Vertex2DAttributes.position).const()


class VertexVisualAttributes:
    """The field paths of VertexVisualAttributes."""
    value: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.VertexVisualAttributes.value).const()
    color: typing.Final[dsviper.PathConst] = dsviper.Path.from_field(fields.VertexVisualAttributes.color).const()
