# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

from __future__ import annotations

import enum
import functools
import typing

import dsviper

from .. import definitions
from .._codegen import NOT_GIVEN, AnyConceptKey, AnyValue, Key, NotGiven, Proxy, is_known, register, unwrap, wrap
from .._codegen.container import _unwrap_deep

if typing.TYPE_CHECKING:
    from .. import containers

EDGE: dsviper.ValueUUId = dsviper.ValueUUId.create("4d5c7e70-1262-eac1-f8c1-2eb35df4c5cf")
GRAPH: dsviper.ValueUUId = dsviper.ValueUUId.create("0785ad82-048d-7992-5680-edd838ee5ad6")
VERTEX: dsviper.ValueUUId = dsviper.ValueUUId.create("2f11dc82-c440-640f-b684-210936c58f86")
COLOR: dsviper.ValueUUId = dsviper.ValueUUId.create("469d48ae-0e43-0a83-54e6-76eb6ca48d1b")
EDGE_TOPOLOGY: dsviper.ValueUUId = dsviper.ValueUUId.create("00c3d01c-4814-2585-d21c-05f482f2ca77")
GRAPH_DESCRIPTION: dsviper.ValueUUId = dsviper.ValueUUId.create("26b02bf2-78f3-75ff-9fc9-6be36ee21dc8")
GRAPH_SELECTION: dsviper.ValueUUId = dsviper.ValueUUId.create("6285942c-da2d-82bb-9b4c-8c353ad3dad3")
GRAPH_TOPOLOGY: dsviper.ValueUUId = dsviper.ValueUUId.create("8908c86a-01f0-60ed-f3e9-204a52ccef05")
POSITION: dsviper.ValueUUId = dsviper.ValueUUId.create("576fbb64-0742-db36-422b-5a35ff1fa25f")
RECTANGLE: dsviper.ValueUUId = dsviper.ValueUUId.create("dce3db08-b7f7-946c-f02a-32898c72f40d")
VERTEX_2D_ATTRIBUTES: dsviper.ValueUUId = dsviper.ValueUUId.create("d233a482-09ff-5363-8316-97ae4ba4ab5e")
VERTEX_VISUAL_ATTRIBUTES: dsviper.ValueUUId = dsviper.ValueUUId.create("a530433b-d52c-b261-30aa-aa4b3a623fd8")

class EdgeKey(Key):
    """An edge in a graph."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def concept(cls) -> dsviper.TypeConcept:
        return definitions().check_concept(EDGE)

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.Type:
        return dsviper.TypeKey(cls.concept())

    def __init__(self, identifier: dsviper.ValueKey | dsviper.ValueUUId | str | NotGiven = NOT_GIVEN,
                 runtime_id: dsviper.ValueUUId | str | NotGiven = NOT_GIVEN) -> None:
        """No argument gives the invalid key, an instance identifier the key of that instance, an
        instance identifier and a runtime id the key of a concept that is a Edge or descends
        from it. A key of another concept is converted with its to_parent_key() or
        to_any_concept_key(), and back with from_any_concept_key()."""
        if isinstance(identifier, Proxy):
            raise TypeError(f"{identifier!r} is not a Graph::EdgeKey: "
                            "widen it with to_parent_key(), or narrow it with from_any_concept_key()")
        if isinstance(identifier, dsviper.ValueKey):
            if not isinstance(runtime_id, NotGiven):
                raise TypeError("a key carries its runtime id")
            if identifier.type() != self.type():
                raise TypeError(f"this value is not a Graph::EdgeKey: {identifier.detail_type_representation()}")
            super().__init__(identifier)
        elif isinstance(identifier, NotGiven):
            if not isinstance(runtime_id, NotGiven):
                raise TypeError("a runtime id needs an instance identifier")
            super().__init__(dsviper.ValueKey.create(self.concept(), dsviper.ValueUUId.INVALID))
        elif isinstance(identifier, (dsviper.ValueUUId, str)):
            if isinstance(runtime_id, NotGiven):
                super().__init__(dsviper.ValueKey.create(self.concept(), identifier))
                return
            concept = definitions().check_concept(dsviper.ValueUUId(runtime_id))
            key = dsviper.ValueKey.create(concept, identifier)
            if not key.is_member(self.concept()):
                raise TypeError(f"{concept.representation()} is not a Graph::Edge")
            super().__init__(key.to_member_key(self.concept()))
        else:
            raise TypeError(f"{identifier!r} is not an instance identifier")

    @classmethod
    def create(cls) -> EdgeKey:
        return cls(dsviper.ValueUUId.create())

    def instance_id(self) -> dsviper.ValueUUId:
        return self._value.instance_id()

    def runtime_id(self) -> dsviper.ValueUUId:
        return self._value.type_concept().runtime_id()

    def is_valid(self) -> bool:
        return self._value.instance_id().is_valid()

    def to_any_concept_key(self) -> AnyConceptKey:
        return AnyConceptKey(self._value.to_any_concept_key())

    @classmethod
    def from_any_concept_key(cls, key: AnyConceptKey | Proxy[dsviper.ValueKey] | dsviper.ValueKey) -> EdgeKey | None:
        value = key._value if isinstance(key, Proxy) else key
        return cls(value.to_member_key(cls.concept())) if value.is_member(cls.concept()) else None

    def description(self) -> str:
        return f"{self._value.instance_id().encoded()}:Graph::EdgeKey{self._held()}"

    def is_known(self) -> bool:
        return is_known(self._value)

    def __repr__(self) -> str:
        return self.description()



class GraphKey(Key):
    """A graph."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def concept(cls) -> dsviper.TypeConcept:
        return definitions().check_concept(GRAPH)

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.Type:
        return dsviper.TypeKey(cls.concept())

    def __init__(self, identifier: dsviper.ValueKey | dsviper.ValueUUId | str | NotGiven = NOT_GIVEN,
                 runtime_id: dsviper.ValueUUId | str | NotGiven = NOT_GIVEN) -> None:
        """No argument gives the invalid key, an instance identifier the key of that instance, an
        instance identifier and a runtime id the key of a concept that is a Graph or descends
        from it. A key of another concept is converted with its to_parent_key() or
        to_any_concept_key(), and back with from_any_concept_key()."""
        if isinstance(identifier, Proxy):
            raise TypeError(f"{identifier!r} is not a Graph::GraphKey: "
                            "widen it with to_parent_key(), or narrow it with from_any_concept_key()")
        if isinstance(identifier, dsviper.ValueKey):
            if not isinstance(runtime_id, NotGiven):
                raise TypeError("a key carries its runtime id")
            if identifier.type() != self.type():
                raise TypeError(f"this value is not a Graph::GraphKey: {identifier.detail_type_representation()}")
            super().__init__(identifier)
        elif isinstance(identifier, NotGiven):
            if not isinstance(runtime_id, NotGiven):
                raise TypeError("a runtime id needs an instance identifier")
            super().__init__(dsviper.ValueKey.create(self.concept(), dsviper.ValueUUId.INVALID))
        elif isinstance(identifier, (dsviper.ValueUUId, str)):
            if isinstance(runtime_id, NotGiven):
                super().__init__(dsviper.ValueKey.create(self.concept(), identifier))
                return
            concept = definitions().check_concept(dsviper.ValueUUId(runtime_id))
            key = dsviper.ValueKey.create(concept, identifier)
            if not key.is_member(self.concept()):
                raise TypeError(f"{concept.representation()} is not a Graph::Graph")
            super().__init__(key.to_member_key(self.concept()))
        else:
            raise TypeError(f"{identifier!r} is not an instance identifier")

    @classmethod
    def create(cls) -> GraphKey:
        return cls(dsviper.ValueUUId.create())

    def instance_id(self) -> dsviper.ValueUUId:
        return self._value.instance_id()

    def runtime_id(self) -> dsviper.ValueUUId:
        return self._value.type_concept().runtime_id()

    def is_valid(self) -> bool:
        return self._value.instance_id().is_valid()

    def to_any_concept_key(self) -> AnyConceptKey:
        return AnyConceptKey(self._value.to_any_concept_key())

    @classmethod
    def from_any_concept_key(cls, key: AnyConceptKey | Proxy[dsviper.ValueKey] | dsviper.ValueKey) -> GraphKey | None:
        value = key._value if isinstance(key, Proxy) else key
        return cls(value.to_member_key(cls.concept())) if value.is_member(cls.concept()) else None

    def description(self) -> str:
        return f"{self._value.instance_id().encoded()}:Graph::GraphKey{self._held()}"

    def is_known(self) -> bool:
        return is_known(self._value)

    def __repr__(self) -> str:
        return self.description()



class VertexKey(Key):
    """A vertex in a graph."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def concept(cls) -> dsviper.TypeConcept:
        return definitions().check_concept(VERTEX)

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.Type:
        return dsviper.TypeKey(cls.concept())

    def __init__(self, identifier: dsviper.ValueKey | dsviper.ValueUUId | str | NotGiven = NOT_GIVEN,
                 runtime_id: dsviper.ValueUUId | str | NotGiven = NOT_GIVEN) -> None:
        """No argument gives the invalid key, an instance identifier the key of that instance, an
        instance identifier and a runtime id the key of a concept that is a Vertex or descends
        from it. A key of another concept is converted with its to_parent_key() or
        to_any_concept_key(), and back with from_any_concept_key()."""
        if isinstance(identifier, Proxy):
            raise TypeError(f"{identifier!r} is not a Graph::VertexKey: "
                            "widen it with to_parent_key(), or narrow it with from_any_concept_key()")
        if isinstance(identifier, dsviper.ValueKey):
            if not isinstance(runtime_id, NotGiven):
                raise TypeError("a key carries its runtime id")
            if identifier.type() != self.type():
                raise TypeError(f"this value is not a Graph::VertexKey: {identifier.detail_type_representation()}")
            super().__init__(identifier)
        elif isinstance(identifier, NotGiven):
            if not isinstance(runtime_id, NotGiven):
                raise TypeError("a runtime id needs an instance identifier")
            super().__init__(dsviper.ValueKey.create(self.concept(), dsviper.ValueUUId.INVALID))
        elif isinstance(identifier, (dsviper.ValueUUId, str)):
            if isinstance(runtime_id, NotGiven):
                super().__init__(dsviper.ValueKey.create(self.concept(), identifier))
                return
            concept = definitions().check_concept(dsviper.ValueUUId(runtime_id))
            key = dsviper.ValueKey.create(concept, identifier)
            if not key.is_member(self.concept()):
                raise TypeError(f"{concept.representation()} is not a Graph::Vertex")
            super().__init__(key.to_member_key(self.concept()))
        else:
            raise TypeError(f"{identifier!r} is not an instance identifier")

    @classmethod
    def create(cls) -> VertexKey:
        return cls(dsviper.ValueUUId.create())

    def instance_id(self) -> dsviper.ValueUUId:
        return self._value.instance_id()

    def runtime_id(self) -> dsviper.ValueUUId:
        return self._value.type_concept().runtime_id()

    def is_valid(self) -> bool:
        return self._value.instance_id().is_valid()

    def to_any_concept_key(self) -> AnyConceptKey:
        return AnyConceptKey(self._value.to_any_concept_key())

    @classmethod
    def from_any_concept_key(cls, key: AnyConceptKey | Proxy[dsviper.ValueKey] | dsviper.ValueKey) -> VertexKey | None:
        value = key._value if isinstance(key, Proxy) else key
        return cls(value.to_member_key(cls.concept())) if value.is_member(cls.concept()) else None

    def description(self) -> str:
        return f"{self._value.instance_id().encoded()}:Graph::VertexKey{self._held()}"

    def is_known(self) -> bool:
        return is_known(self._value)

    def __repr__(self) -> str:
        return self.description()


class Color(Proxy[dsviper.ValueStructure]):
    """An RGB Color."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(COLOR)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 red: float | NotGiven = NOT_GIVEN,
                 green: float | NotGiven = NOT_GIVEN,
                 blue: float | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::Color")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(red, NotGiven):
            self.red = red
        if not isinstance(green, NotGiven):
            self.green = green
        if not isinstance(blue, NotGiven):
            self.blue = blue

    @property
    def red(self) -> float:
        return typing.cast("float", self._value.at("red"))

    @red.setter
    def red(self, value: float) -> None:
        self._value.set("red", value)

    @property
    def green(self) -> float:
        return typing.cast("float", self._value.at("green"))

    @green.setter
    def green(self, value: float) -> None:
        self._value.set("green", value)

    @property
    def blue(self) -> float:
        return typing.cast("float", self._value.at("blue"))

    @blue.setter
    def blue(self, value: float) -> None:
        self._value.set("blue", value)

    def __repr__(self) -> str:
        return f"Graph::Color(red={self.red}, green={self.green}, blue={self.blue})"


class EdgeTopology(Proxy[dsviper.ValueStructure]):
    """An edge in the graph topology."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(EDGE_TOPOLOGY)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 va_key: VertexKey | NotGiven = NOT_GIVEN,
                 vb_key: VertexKey | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::EdgeTopology")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(va_key, NotGiven):
            self.va_key = va_key
        if not isinstance(vb_key, NotGiven):
            self.vb_key = vb_key

    @property
    def va_key(self) -> VertexKey:
        return typing.cast("VertexKey", wrap(self._value.at("vaKey", encoded=False)))

    @va_key.setter
    def va_key(self, value: VertexKey) -> None:
        self._value.set("vaKey", unwrap(value))

    @property
    def vb_key(self) -> VertexKey:
        return typing.cast("VertexKey", wrap(self._value.at("vbKey", encoded=False)))

    @vb_key.setter
    def vb_key(self, value: VertexKey) -> None:
        self._value.set("vbKey", unwrap(value))

    def __repr__(self) -> str:
        return f"Graph::EdgeTopology(va_key={self.va_key}, vb_key={self.vb_key})"


class GraphDescription(Proxy[dsviper.ValueStructure]):
    """The descriptive information's."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(GRAPH_DESCRIPTION)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 name: str | NotGiven = NOT_GIVEN,
                 author: str | NotGiven = NOT_GIVEN,
                 create_date: str | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::GraphDescription")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(name, NotGiven):
            self.name = name
        if not isinstance(author, NotGiven):
            self.author = author
        if not isinstance(create_date, NotGiven):
            self.create_date = create_date

    @property
    def name(self) -> str:
        return typing.cast("str", self._value.at("name"))

    @name.setter
    def name(self, value: str) -> None:
        self._value.set("name", value)

    @property
    def author(self) -> str:
        return typing.cast("str", self._value.at("author"))

    @author.setter
    def author(self, value: str) -> None:
        self._value.set("author", value)

    @property
    def create_date(self) -> str:
        return typing.cast("str", self._value.at("createDate"))

    @create_date.setter
    def create_date(self, value: str) -> None:
        self._value.set("createDate", value)

    def __repr__(self) -> str:
        return f"Graph::GraphDescription(name={self.name}, author={self.author}, create_date={self.create_date})"


class GraphSelection(Proxy[dsviper.ValueStructure]):
    """The selected vertices and edges."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(GRAPH_SELECTION)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 vertex_keys: containers.Set_of_Graph_VertexKey | NotGiven = NOT_GIVEN,
                 edge_keys: containers.Set_of_Graph_EdgeKey | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::GraphSelection")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(vertex_keys, NotGiven):
            self.vertex_keys = vertex_keys
        if not isinstance(edge_keys, NotGiven):
            self.edge_keys = edge_keys

    @property
    def vertex_keys(self) -> containers.Set_of_Graph_VertexKey:
        return typing.cast("containers.Set_of_Graph_VertexKey", wrap(self._value.at("vertexKeys", encoded=False)))

    @vertex_keys.setter
    def vertex_keys(self, value: containers.Set_of_Graph_VertexKey) -> None:
        self._value.set("vertexKeys", unwrap(value))

    @property
    def edge_keys(self) -> containers.Set_of_Graph_EdgeKey:
        return typing.cast("containers.Set_of_Graph_EdgeKey", wrap(self._value.at("edgeKeys", encoded=False)))

    @edge_keys.setter
    def edge_keys(self, value: containers.Set_of_Graph_EdgeKey) -> None:
        self._value.set("edgeKeys", unwrap(value))

    def __repr__(self) -> str:
        return f"Graph::GraphSelection(vertex_keys={self.vertex_keys}, edge_keys={self.edge_keys})"


class GraphTopology(Proxy[dsviper.ValueStructure]):
    """The vertices and edges of the graph topology."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(GRAPH_TOPOLOGY)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 vertex_keys: containers.Set_of_Graph_VertexKey | NotGiven = NOT_GIVEN,
                 edge_keys: containers.Set_of_Graph_EdgeKey | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::GraphTopology")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(vertex_keys, NotGiven):
            self.vertex_keys = vertex_keys
        if not isinstance(edge_keys, NotGiven):
            self.edge_keys = edge_keys

    @property
    def vertex_keys(self) -> containers.Set_of_Graph_VertexKey:
        return typing.cast("containers.Set_of_Graph_VertexKey", wrap(self._value.at("vertexKeys", encoded=False)))

    @vertex_keys.setter
    def vertex_keys(self, value: containers.Set_of_Graph_VertexKey) -> None:
        self._value.set("vertexKeys", unwrap(value))

    @property
    def edge_keys(self) -> containers.Set_of_Graph_EdgeKey:
        return typing.cast("containers.Set_of_Graph_EdgeKey", wrap(self._value.at("edgeKeys", encoded=False)))

    @edge_keys.setter
    def edge_keys(self, value: containers.Set_of_Graph_EdgeKey) -> None:
        self._value.set("edgeKeys", unwrap(value))

    def __repr__(self) -> str:
        return f"Graph::GraphTopology(vertex_keys={self.vertex_keys}, edge_keys={self.edge_keys})"


class Position(Proxy[dsviper.ValueStructure]):
    """A Position."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(POSITION)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 x: float | NotGiven = NOT_GIVEN,
                 y: float | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::Position")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(x, NotGiven):
            self.x = x
        if not isinstance(y, NotGiven):
            self.y = y

    @property
    def x(self) -> float:
        return typing.cast("float", self._value.at("x"))

    @x.setter
    def x(self, value: float) -> None:
        self._value.set("x", value)

    @property
    def y(self) -> float:
        return typing.cast("float", self._value.at("y"))

    @y.setter
    def y(self, value: float) -> None:
        self._value.set("y", value)

    def __repr__(self) -> str:
        return f"Graph::Position(x={self.x}, y={self.y})"


class Rectangle(Proxy[dsviper.ValueStructure]):
    """A Rectangle."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(RECTANGLE)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 x: float | NotGiven = NOT_GIVEN,
                 y: float | NotGiven = NOT_GIVEN,
                 w: float | NotGiven = NOT_GIVEN,
                 h: float | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::Rectangle")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(x, NotGiven):
            self.x = x
        if not isinstance(y, NotGiven):
            self.y = y
        if not isinstance(w, NotGiven):
            self.w = w
        if not isinstance(h, NotGiven):
            self.h = h

    @property
    def x(self) -> float:
        """the x origin."""
        return typing.cast("float", self._value.at("x"))

    @x.setter
    def x(self, value: float) -> None:
        self._value.set("x", value)

    @property
    def y(self) -> float:
        """the y origin."""
        return typing.cast("float", self._value.at("y"))

    @y.setter
    def y(self, value: float) -> None:
        self._value.set("y", value)

    @property
    def w(self) -> float:
        """the width."""
        return typing.cast("float", self._value.at("w"))

    @w.setter
    def w(self, value: float) -> None:
        self._value.set("w", value)

    @property
    def h(self) -> float:
        """the height."""
        return typing.cast("float", self._value.at("h"))

    @h.setter
    def h(self, value: float) -> None:
        self._value.set("h", value)

    def __repr__(self) -> str:
        return f"Graph::Rectangle(x={self.x}, y={self.y}, w={self.w}, h={self.h})"


class VertexVisualAttributes(Proxy[dsviper.ValueStructure]):
    """The visual attributes of a vertex."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(VERTEX_VISUAL_ATTRIBUTES)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 value: int | NotGiven = NOT_GIVEN,
                 color: Color | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::VertexVisualAttributes")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(value, NotGiven):
            self.value = value
        if not isinstance(color, NotGiven):
            self.color = color

    @property
    def value(self) -> int:
        return typing.cast("int", self._value.at("value"))

    @value.setter
    def value(self, value: int) -> None:
        self._value.set("value", value)

    @property
    def color(self) -> Color:
        return typing.cast("Color", wrap(self._value.at("color", encoded=False)))

    @color.setter
    def color(self, value: Color) -> None:
        self._value.set("color", unwrap(value))

    def __repr__(self) -> str:
        return f"Graph::VertexVisualAttributes(value={self.value}, color={self.color})"


class Vertex2DAttributes(Proxy[dsviper.ValueStructure]):
    """The attributes used to render a topological vertex in 2D."""
    __slots__ = ()

    @classmethod
    @functools.cache
    def type(cls) -> dsviper.TypeStructure:
        return definitions().check_structure(VERTEX_2D_ATTRIBUTES)

    def __init__(self, source: dsviper.ValueStructure | dict[str, typing.Any] | None = None, /, *,
                 position: Position | NotGiven = NOT_GIVEN) -> None:
        """Fields by keyword, in snake_case; or a source: a Viper ValueStructure of this
        type, copied, or a dict keyed by the DSM field names, as the runtime takes it."""
        if source is None:
            source = dsviper.ValueStructure(self.type())
        elif isinstance(source, dict):
            source = dsviper.ValueStructure(self.type(), _unwrap_deep(source))
        elif source.type() != self.type():
            raise TypeError("this value is not a Graph::Vertex2DAttributes")
        else:
            source = dsviper.ValueStructure(self.type(), source)
        super().__init__(source)
        if not isinstance(position, NotGiven):
            self.position = position

    @property
    def position(self) -> Position:
        return typing.cast("Position", wrap(self._value.at("position", encoded=False)))

    @position.setter
    def position(self, value: Position) -> None:
        self._value.set("position", unwrap(value))

    def __repr__(self) -> str:
        return f"Graph::Vertex2DAttributes(position={self.position})"


register({EDGE: EdgeKey, GRAPH: GraphKey, VERTEX: VertexKey, COLOR: Color, EDGE_TOPOLOGY: EdgeTopology, GRAPH_DESCRIPTION: GraphDescription, GRAPH_SELECTION: GraphSelection, GRAPH_TOPOLOGY: GraphTopology, POSITION: Position, RECTANGLE: Rectangle, VERTEX_2D_ATTRIBUTES: Vertex2DAttributes, VERTEX_VISUAL_ATTRIBUTES: VertexVisualAttributes})

__all__ = ["EdgeKey", "GraphKey", "VertexKey", "Color", "EdgeTopology", "GraphDescription", "GraphSelection", "GraphTopology", "Position", "Rectangle", "Vertex2DAttributes", "VertexVisualAttributes", "EDGE", "GRAPH", "VERTEX", "COLOR", "EDGE_TOPOLOGY", "GRAPH_DESCRIPTION", "GRAPH_SELECTION", "GRAPH_TOPOLOGY", "POSITION", "RECTANGLE", "VERTEX_2D_ATTRIBUTES", "VERTEX_VISUAL_ATTRIBUTES"]
