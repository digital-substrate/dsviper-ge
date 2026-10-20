# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

"""The Graph attachments in a Commit database: read a state, write by mutations.

A read takes an AttachmentGetting: a CommitState's or a mutable state's attachment_getting().
A write takes an AttachmentMutating, which a CommitMutableState gives (attachment_mutating()):
dsviper.CommitMutableState(dsviper.CommitStateBuilder.initial_state(db)) for the first commit,
CommitStateBuilder.state(db, commit_id) to carry on from the last one. The database needs the
model first: db.extend_definitions(definitions()). Nothing is stored until the state is
committed: db.commit_mutations(label, state), or a CommitStore's dispatch. A Database is the
other usage: graph.database_attachments."""

from __future__ import annotations

import dsviper

from .. import definitions
import typing

from .._codegen import AnyConceptKey, AnyValue, AttachmentBase, Option
from .. import containers
from .. import graph
from . import paths as _graph_paths

class Edge:
    class _Topology(AttachmentBase):
        """An Edge in the graph topology.

The attachment attachment<Edge, EdgeTopology> Graph::topology, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_EdgeKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_EdgeKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.EdgeKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.EdgeKey) -> Option[graph.EdgeTopology]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[graph.EdgeTopology]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.EdgeKey, graph.EdgeTopology]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.EdgeKey, graph.EdgeTopology]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_EdgeKey, containers.Set_of_Graph_EdgeKey, containers.Set_of_Graph_EdgeKey, containers.Set_of_Graph_EdgeKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_EdgeKey, containers.Set_of_Graph_EdgeKey, containers.Set_of_Graph_EdgeKey, containers.Set_of_Graph_EdgeKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.EdgeKey, value: graph.EdgeTopology) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.EdgeKey, value: graph.EdgeTopology, *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def set_va_key(self, state: dsviper.AttachmentMutating, key: graph.EdgeKey, value: graph.VertexKey) -> None:
            """Write value in the field va_key. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.EdgeTopology.va_key, value)

        def set_vb_key(self, state: dsviper.AttachmentMutating, key: graph.EdgeKey, value: graph.VertexKey) -> None:
            """Write value in the field vb_key. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.EdgeTopology.vb_key, value)

    topology = _Topology(dsviper.ValueUUId.create("44178d14-4702-e96c-de66-8ca5108aa560"), definitions)

class Graph:
    class _Comments(AttachmentBase):
        """A collection of comments for a Graph.

The attachment attachment<Graph, xarray<string>> Graph::comments, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_GraphKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_GraphKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> Option[containers.XArray_of_string]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[containers.XArray_of_string]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.GraphKey, containers.XArray_of_string]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.GraphKey, containers.XArray_of_string]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.XArray_of_string | typing.Sequence[str]) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.XArray_of_string | typing.Sequence[str], *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def insert(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, before_position: dsviper.ValueUUId, new_position: dsviper.ValueUUId, value: str) -> None:
            """Insert value at new_position, before before_position. A new_position the xarray holds,
            or held before a removal, keeps its place; a before_position it does not hold leaves it
            unchanged."""
            self._insert_in_xarray(state, key, None, before_position, new_position, value)

        def update(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, position: dsviper.ValueUUId, value: str) -> None:
            """Write value at position."""
            self._update_in_xarray(state, key, None, position, value)

        def remove(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, position: dsviper.ValueUUId) -> None:
            """Remove position."""
            self._remove_in_xarray(state, key, None, position)

    comments = _Comments(dsviper.ValueUUId.create("897b2ffb-45b8-e8e0-36cf-7ce37211e431"), definitions)

    class _Description(AttachmentBase):
        """The descriptive information of a graph.

The attachment attachment<Graph, GraphDescription> Graph::description, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_GraphKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_GraphKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> Option[graph.GraphDescription]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[graph.GraphDescription]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.GraphKey, graph.GraphDescription]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.GraphKey, graph.GraphDescription]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: graph.GraphDescription) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: graph.GraphDescription, *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def set_name(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: str) -> None:
            """Write value in the field name. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.GraphDescription.name, value)

        def set_author(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: str) -> None:
            """Write value in the field author. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.GraphDescription.author, value)

        def set_create_date(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: str) -> None:
            """Write value in the field create_date. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.GraphDescription.create_date, value)

    description = _Description(dsviper.ValueUUId.create("5f4ea545-87cb-4292-b40a-3e5b2e78174e"), definitions)

    class _Selection(AttachmentBase):
        """The selected vertices of a graph.

The attachment attachment<Graph, GraphSelection> Graph::selection, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_GraphKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_GraphKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> Option[graph.GraphSelection]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[graph.GraphSelection]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.GraphKey, graph.GraphSelection]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.GraphKey, graph.GraphSelection]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: graph.GraphSelection) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: graph.GraphSelection, *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def set_vertex_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            """Write value in the field vertex_keys. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.GraphSelection.vertex_keys, value)

        def union_vertex_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            """Add the elements of value to the set."""
            self._union_in_set(state, key, _graph_paths.GraphSelection.vertex_keys, value)

        def subtract_vertex_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            """Remove the elements of value from the set."""
            self._subtract_in_set(state, key, _graph_paths.GraphSelection.vertex_keys, value)

        def set_edge_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            """Write value in the field edge_keys. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.GraphSelection.edge_keys, value)

        def union_edge_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            """Add the elements of value to the set."""
            self._union_in_set(state, key, _graph_paths.GraphSelection.edge_keys, value)

        def subtract_edge_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            """Remove the elements of value from the set."""
            self._subtract_in_set(state, key, _graph_paths.GraphSelection.edge_keys, value)

    selection = _Selection(dsviper.ValueUUId.create("eb6f1b63-68dd-1ecc-6bbc-2853648380c4"), definitions)

    class _Tags(AttachmentBase):
        """A collection of tags for a graph.

The attachment attachment<Graph, map<string, string>> Graph::tags, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_GraphKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_GraphKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> Option[containers.Map_of_string_to_string]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[containers.Map_of_string_to_string]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.GraphKey, containers.Map_of_string_to_string]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.GraphKey, containers.Map_of_string_to_string]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Map_of_string_to_string | dict[str, str]) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Map_of_string_to_string | dict[str, str], *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def union(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Map_of_string_to_string | dict[str, str]) -> None:
            """Add the entries of value to the map, replacing the map keys already there."""
            self._union_in_map(state, key, None, value)

        def subtract(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_string | typing.Iterable[str]) -> None:
            """Remove the entries whose map key is in value."""
            self._subtract_in_map(state, key, None, value)

        def update(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Map_of_string_to_string | dict[str, str]) -> None:
            """Update the entries of the map from those of value. Only map keys already there are
            written; a map key only value carries is ignored: union inserts it."""
            self._update_in_map(state, key, None, value)

    tags = _Tags(dsviper.ValueUUId.create("47424e85-2f1f-a78a-f0fc-efeb69391a37"), definitions)

    class _Topology(AttachmentBase):
        """The topology of a graph.

The attachment attachment<Graph, GraphTopology> Graph::topology, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_GraphKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_GraphKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.GraphKey) -> Option[graph.GraphTopology]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[graph.GraphTopology]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.GraphKey, graph.GraphTopology]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.GraphKey, graph.GraphTopology]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey, containers.Set_of_Graph_GraphKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: graph.GraphTopology) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: graph.GraphTopology, *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def set_vertex_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            """Write value in the field vertex_keys. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.GraphTopology.vertex_keys, value)

        def union_vertex_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            """Add the elements of value to the set."""
            self._union_in_set(state, key, _graph_paths.GraphTopology.vertex_keys, value)

        def subtract_vertex_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_VertexKey) -> None:
            """Remove the elements of value from the set."""
            self._subtract_in_set(state, key, _graph_paths.GraphTopology.vertex_keys, value)

        def set_edge_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            """Write value in the field edge_keys. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.GraphTopology.edge_keys, value)

        def union_edge_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            """Add the elements of value to the set."""
            self._union_in_set(state, key, _graph_paths.GraphTopology.edge_keys, value)

        def subtract_edge_keys(self, state: dsviper.AttachmentMutating, key: graph.GraphKey, value: containers.Set_of_Graph_EdgeKey) -> None:
            """Remove the elements of value from the set."""
            self._subtract_in_set(state, key, _graph_paths.GraphTopology.edge_keys, value)

    topology = _Topology(dsviper.ValueUUId.create("09e8fcfb-e07d-3dd7-49d7-d8944538038b"), definitions)

class Vertex:
    class _Render2DAttributes(AttachmentBase):
        """The render attributes used to render a vertex of a graph in 2D.

The attachment attachment<Vertex, Vertex2DAttributes> Graph::render2DAttributes, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_VertexKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_VertexKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.VertexKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.VertexKey) -> Option[graph.Vertex2DAttributes]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[graph.Vertex2DAttributes]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.VertexKey, graph.Vertex2DAttributes]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.VertexKey, graph.Vertex2DAttributes]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.Vertex2DAttributes) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.Vertex2DAttributes, *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def set_position(self, state: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.Position) -> None:
            """Write value in the field position. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.Vertex2DAttributes.position, value)

    render_2d_attributes = _Render2DAttributes(dsviper.ValueUUId.create("7e190bc3-1a6b-ccbe-eecc-6a53b70778cb"), definitions)

    class _VisualAttributes(AttachmentBase):
        """The visual attributes used to render a vertex of a graph.

The attachment attachment<Vertex, VertexVisualAttributes> Graph::visualAttributes, in a Commit database."""

        def keys(self, state: dsviper.AttachmentGetting) -> containers.Set_of_Graph_VertexKey:
            """Return the keys that hold a document in this state. The set is taken now: a later
            mutation does not reach it."""
            return typing.cast("containers.Set_of_Graph_VertexKey", self._keys(state))

        def has(self, state: dsviper.AttachmentGetting, key: graph.VertexKey) -> bool:
            """Return True if a document is stored at key in this state."""
            return self._has(state, key)

        def get(self, state: dsviper.AttachmentGetting, key: graph.VertexKey) -> Option[graph.VertexVisualAttributes]:
            """Return the document in an Option, empty when none is stored: unwrap() opens it,
            is_nil() tells it is empty. It is a copy: changing it changes nothing; write it back
            with set, or mutate a field."""
            return typing.cast("Option[graph.VertexVisualAttributes]", self._get(state, key))

        def enumerate(self, state: dsviper.AttachmentGetting) -> list[tuple[graph.VertexKey, graph.VertexVisualAttributes]]:
            """Return every (key, document) pair of this state. Each document is a copy, as get
            returns it."""
            return typing.cast("list[tuple[graph.VertexKey, graph.VertexVisualAttributes]]", self._enumerate(state))

        def diff_keys(self, current: dsviper.AttachmentGetting, other: dsviper.AttachmentGetting
                      ) -> tuple[containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey]:
            """Return (added, removed, different, same), from current, the reference, to other:
            the keys other holds and current does not, those current holds and other does not,
            those whose documents differ, those whose documents are equal. For what changed since
            the last load, pass the last loaded state first."""
            return typing.cast("tuple[containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey, containers.Set_of_Graph_VertexKey]", self._diff_keys(current, other))

        def set(self, state: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.VertexVisualAttributes) -> None:
            """Set the document: one mutation, stored when the state is committed. The document is
            copied in: changing it afterwards does not reach what was written."""
            self._set_in_state(state, key, value)

        def diff(self, state: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.VertexVisualAttributes, *, recursive: bool = False) -> None:
            """Write only what differs between value and the stored document. recursive computes
            the difference field by field inside a structure, instead of replacing it whole."""
            self._diff(state, key, value, recursive)

        def set_value(self, state: dsviper.AttachmentMutating, key: graph.VertexKey, value: int) -> None:
            """Write value in the field value. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.VertexVisualAttributes.value, value)

        def set_color(self, state: dsviper.AttachmentMutating, key: graph.VertexKey, value: graph.Color) -> None:
            """Write value in the field color. A key that holds no document is left as it
            is, without a word: set the document first."""
            self._update(state, key, _graph_paths.VertexVisualAttributes.color, value)

    visual_attributes = _VisualAttributes(dsviper.ValueUUId.create("e09f1e7a-cd64-00f8-66b8-ea072397400d"), definitions)
