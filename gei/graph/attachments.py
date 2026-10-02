# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

from __future__ import annotations

import dsviper

from .. import definitions
import typing

from .._codegen import AnyConceptKey, AnyValue, AttachmentProxy
from .. import containers
from .. import graph

class Edge:
    class _Topology(AttachmentProxy[graph.EdgeKey, graph.EdgeTopology, containers.Set_of_Graph_EdgeKey, graph.EdgeTopology]):

        def set_va_key(self, mutating: dsviper.AttachmentMutating, key: graph.EdgeKey, value: graph.VertexKey) -> None:
            self._update(mutating, key, "vaKey", value)

        def set_vb_key(self, mutating: dsviper.AttachmentMutating, key: graph.EdgeKey, value: graph.VertexKey) -> None:
            self._update(mutating, key, "vbKey", value)

    topology = _Topology(
        dsviper.ValueUUId.create("44178d14-4702-e96c-de66-8ca5108aa560"), definitions, graph.EdgeKey, graph.EdgeTopology)

class Graph:
    class _Comments(AttachmentProxy[graph.GraphKey, containers.XArray_of_string, containers.Set_of_Graph_GraphKey, containers.XArray_of_string | typing.Sequence[str]]):

        def insert(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, before_position: dsviper.ValueUUId, new_position: dsviper.ValueUUId, value: str) -> None:
            self._insert_in_xarray(mutating, key, None, before_position, new_position, value)

        def update(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, position: dsviper.ValueUUId, value: str) -> None:
            self._update_in_xarray(mutating, key, None, position, value)

        def remove(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, position: dsviper.ValueUUId) -> None:
            self._remove_in_xarray(mutating, key, None, position)

    comments = _Comments(
        dsviper.ValueUUId.create("897b2ffb-45b8-e8e0-36cf-7ce37211e431"), definitions, graph.GraphKey, None)

    class _Description(AttachmentProxy[graph.GraphKey, graph.GraphDescription, containers.Set_of_Graph_GraphKey, graph.GraphDescription]):

        def set_name(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: str) -> None:
            self._update(mutating, key, "name", value)

        def set_author(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: str) -> None:
            self._update(mutating, key, "author", value)

        def set_create_date(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: str) -> None:
            self._update(mutating, key, "createDate", value)

    description = _Description(
        dsviper.ValueUUId.create("5f4ea545-87cb-4292-b40a-3e5b2e78174e"), definitions, graph.GraphKey, graph.GraphDescription)

    class _Selection(AttachmentProxy[graph.GraphKey, graph.GraphSelection, containers.Set_of_Graph_GraphKey, graph.GraphSelection]):

        def set_vertex_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            self._update(mutating, key, "vertexKeys", value)

        def union_vertex_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            self._union_in_set(mutating, key, "vertexKeys", value)

        def subtract_vertex_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            self._subtract_in_set(mutating, key, "vertexKeys", value)

        def set_edge_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            self._update(mutating, key, "edgeKeys", value)

        def union_edge_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            self._union_in_set(mutating, key, "edgeKeys", value)

        def subtract_edge_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            self._subtract_in_set(mutating, key, "edgeKeys", value)

    selection = _Selection(
        dsviper.ValueUUId.create("eb6f1b63-68dd-1ecc-6bbc-2853648380c4"), definitions, graph.GraphKey, graph.GraphSelection)

    class _Tags(AttachmentProxy[graph.GraphKey, containers.Map_of_string_to_string, containers.Set_of_Graph_GraphKey, containers.Map_of_string_to_string | dict[str, str]]):

        def union(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Map_of_string_to_string) -> None:
            self._union_in_map(mutating, key, None, value)

        def subtract(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_string) -> None:
            self._subtract_in_map(mutating, key, None, value)

        def update(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Map_of_string_to_string) -> None:
            self._update_in_map(mutating, key, None, value)

    tags = _Tags(
        dsviper.ValueUUId.create("47424e85-2f1f-a78a-f0fc-efeb69391a37"), definitions, graph.GraphKey, None)

    class _Topology(AttachmentProxy[graph.GraphKey, graph.GraphTopology, containers.Set_of_Graph_GraphKey, graph.GraphTopology]):

        def set_vertex_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            self._update(mutating, key, "vertexKeys", value)

        def union_vertex_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            self._union_in_set(mutating, key, "vertexKeys", value)

        def subtract_vertex_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            self._subtract_in_set(mutating, key, "vertexKeys", value)

        def set_edge_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            self._update(mutating, key, "edgeKeys", value)

        def union_edge_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            self._union_in_set(mutating, key, "edgeKeys", value)

        def subtract_edge_keys(self, mutating: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            self._subtract_in_set(mutating, key, "edgeKeys", value)

    topology = _Topology(
        dsviper.ValueUUId.create("09e8fcfb-e07d-3dd7-49d7-d8944538038b"), definitions, graph.GraphKey, graph.GraphTopology)

class Vertex:
    class _Render2DAttributes(AttachmentProxy[graph.VertexKey, graph.Vertex2DAttributes, containers.Set_of_Graph_VertexKey, graph.Vertex2DAttributes]):

        def set_position(self, mutating: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.Position) -> None:
            self._update(mutating, key, "position", value)

    render_2d_attributes = _Render2DAttributes(
        dsviper.ValueUUId.create("7e190bc3-1a6b-ccbe-eecc-6a53b70778cb"), definitions, graph.VertexKey, graph.Vertex2DAttributes)

    class _VisualAttributes(AttachmentProxy[graph.VertexKey, graph.VertexVisualAttributes, containers.Set_of_Graph_VertexKey, graph.VertexVisualAttributes]):

        def set_value(self, mutating: dsviper.AttachmentMutating, key: graph.VertexKey, value: int) -> None:
            self._update(mutating, key, "value", value)

        def set_color(self, mutating: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.Color) -> None:
            self._update(mutating, key, "color", value)

    visual_attributes = _VisualAttributes(
        dsviper.ValueUUId.create("e09f1e7a-cd64-00f8-66b8-ea072397400d"), definitions, graph.VertexKey, graph.VertexVisualAttributes)
