# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

from __future__ import annotations

import functools
import typing

import dsviper

from . import definitions
from ._codegen import AnyValue, Declared, Fixed, Mapping, Matrix, Optional, Ordered, SetView, Variant, Vector, declare

if typing.TYPE_CHECKING:
    from . import containers
    from ._codegen import AnyConceptKey

type_bool = lambda: dsviper.TypeBool()
type_uint8 = lambda: dsviper.TypeUInt8()
type_uint16 = lambda: dsviper.TypeUInt16()
type_uint32 = lambda: dsviper.TypeUInt32()
type_uint64 = lambda: dsviper.TypeUInt64()
type_int8 = lambda: dsviper.TypeInt8()
type_int16 = lambda: dsviper.TypeInt16()
type_int32 = lambda: dsviper.TypeInt32()
type_int64 = lambda: dsviper.TypeInt64()
type_float = lambda: dsviper.TypeFloat()
type_double = lambda: dsviper.TypeDouble()
type_string = lambda: dsviper.TypeString()
type_blob = lambda: dsviper.TypeBlob()
type_blob_id = lambda: dsviper.TypeBlobId()
type_commit_id = lambda: dsviper.TypeCommitId()
type_uuid = lambda: dsviper.TypeUUId()
type_any = lambda: dsviper.TypeAny()
type_AnyConceptKey = lambda: dsviper.TypeKey(dsviper.TypeAnyConcept())
def type_Graph_EdgeKey() -> dsviper.Type: return dsviper.TypeKey(definitions().check_concept(graph.data.EDGE))
def type_Graph_GraphKey() -> dsviper.Type: return dsviper.TypeKey(definitions().check_concept(graph.data.GRAPH))
def type_Graph_VertexKey() -> dsviper.Type: return dsviper.TypeKey(definitions().check_concept(graph.data.VERTEX))
def type_Graph_Color() -> dsviper.Type: return definitions().check_structure(graph.data.COLOR)
def type_Graph_EdgeTopology() -> dsviper.Type: return definitions().check_structure(graph.data.EDGE_TOPOLOGY)
def type_Graph_GraphDescription() -> dsviper.Type: return definitions().check_structure(graph.data.GRAPH_DESCRIPTION)
def type_Graph_GraphSelection() -> dsviper.Type: return definitions().check_structure(graph.data.GRAPH_SELECTION)
def type_Graph_GraphTopology() -> dsviper.Type: return definitions().check_structure(graph.data.GRAPH_TOPOLOGY)
def type_Graph_Position() -> dsviper.Type: return definitions().check_structure(graph.data.POSITION)
def type_Graph_Rectangle() -> dsviper.Type: return definitions().check_structure(graph.data.RECTANGLE)
def type_Graph_Vertex2DAttributes() -> dsviper.Type: return definitions().check_structure(graph.data.VERTEX_2D_ATTRIBUTES)
def type_Graph_VertexVisualAttributes() -> dsviper.Type: return definitions().check_structure(graph.data.VERTEX_VISUAL_ATTRIBUTES)

@functools.cache
def type_optional_AnyConceptKey() -> dsviper.Type: return dsviper.TypeOptional(type_AnyConceptKey())
@functools.cache
def type_optional_xarray_string() -> dsviper.Type: return dsviper.TypeOptional(type_xarray_string())
@functools.cache
def type_optional_Graph_EdgeKey() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_EdgeKey())
@functools.cache
def type_optional_Graph_EdgeTopology() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_EdgeTopology())
@functools.cache
def type_optional_Graph_GraphDescription() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_GraphDescription())
@functools.cache
def type_optional_Graph_GraphKey() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_GraphKey())
@functools.cache
def type_optional_Graph_GraphSelection() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_GraphSelection())
@functools.cache
def type_optional_Graph_GraphTopology() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_GraphTopology())
@functools.cache
def type_optional_Graph_Vertex2DAttributes() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_Vertex2DAttributes())
@functools.cache
def type_optional_Graph_VertexKey() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_VertexKey())
@functools.cache
def type_optional_Graph_VertexVisualAttributes() -> dsviper.Type: return dsviper.TypeOptional(type_Graph_VertexVisualAttributes())
@functools.cache
def type_optional_map_string_to_string() -> dsviper.Type: return dsviper.TypeOptional(type_map_string_to_string())
@functools.cache
def type_vector_string() -> dsviper.Type: return dsviper.TypeVector(type_string())
@functools.cache
def type_set_Graph_EdgeKey() -> dsviper.Type: return dsviper.TypeSet(type_Graph_EdgeKey())
@functools.cache
def type_set_Graph_GraphKey() -> dsviper.Type: return dsviper.TypeSet(type_Graph_GraphKey())
@functools.cache
def type_set_Graph_VertexKey() -> dsviper.Type: return dsviper.TypeSet(type_Graph_VertexKey())
@functools.cache
def type_set_string() -> dsviper.Type: return dsviper.TypeSet(type_string())
@functools.cache
def type_map_string_to_string() -> dsviper.Type: return dsviper.TypeMap(type_string(), type_string())
@functools.cache
def type_xarray_string() -> dsviper.Type: return dsviper.TypeXArray(type_string())

class Optional_of_AnyConceptKey(Declared, Optional["AnyConceptKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_AnyConceptKey | AnyConceptKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_AnyConceptKey()

class Optional_of_XArray_of_string(Declared, Optional["containers.XArray_of_string"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_XArray_of_string | containers.XArray_of_string | typing.Sequence[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_xarray_string()

class Optional_of_Graph_EdgeKey(Declared, Optional["graph.EdgeKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_EdgeKey | graph.EdgeKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_EdgeKey()

class Optional_of_Graph_EdgeTopology(Declared, Optional["graph.EdgeTopology"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_EdgeTopology | graph.EdgeTopology | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_EdgeTopology()

class Optional_of_Graph_GraphDescription(Declared, Optional["graph.GraphDescription"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphDescription | graph.GraphDescription | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_GraphDescription()

class Optional_of_Graph_GraphKey(Declared, Optional["graph.GraphKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphKey | graph.GraphKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_GraphKey()

class Optional_of_Graph_GraphSelection(Declared, Optional["graph.GraphSelection"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphSelection | graph.GraphSelection | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_GraphSelection()

class Optional_of_Graph_GraphTopology(Declared, Optional["graph.GraphTopology"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphTopology | graph.GraphTopology | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_GraphTopology()

class Optional_of_Graph_Vertex2DAttributes(Declared, Optional["graph.Vertex2DAttributes"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_Vertex2DAttributes | graph.Vertex2DAttributes | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_Vertex2DAttributes()

class Optional_of_Graph_VertexKey(Declared, Optional["graph.VertexKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_VertexKey | graph.VertexKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_VertexKey()

class Optional_of_Graph_VertexVisualAttributes(Declared, Optional["graph.VertexVisualAttributes"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_VertexVisualAttributes | graph.VertexVisualAttributes | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_Graph_VertexVisualAttributes()

class Optional_of_Map_of_string_to_string(Declared, Optional["containers.Map_of_string_to_string"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Map_of_string_to_string | containers.Map_of_string_to_string | dict[str, str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_optional_map_string_to_string()
class Vector_of_string(Declared, Vector["str"]):
    __slots__ = ()

    def __init__(self, value: Vector_of_string | typing.Sequence[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_vector_string()
class Set_of_Graph_EdgeKey(Declared, SetView["graph.EdgeKey"]):
    __slots__ = ()

    def __init__(self, value: Set_of_Graph_EdgeKey | typing.Iterable[graph.EdgeKey] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_set_Graph_EdgeKey()

class Set_of_Graph_GraphKey(Declared, SetView["graph.GraphKey"]):
    __slots__ = ()

    def __init__(self, value: Set_of_Graph_GraphKey | typing.Iterable[graph.GraphKey] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_set_Graph_GraphKey()

class Set_of_Graph_VertexKey(Declared, SetView["graph.VertexKey"]):
    __slots__ = ()

    def __init__(self, value: Set_of_Graph_VertexKey | typing.Iterable[graph.VertexKey] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_set_Graph_VertexKey()

class Set_of_string(Declared, SetView["str"]):
    __slots__ = ()

    def __init__(self, value: Set_of_string | typing.Iterable[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_set_string()
class Map_of_string_to_string(Declared, Mapping["str", "str"]):
    __slots__ = ()

    def __init__(self, value: Map_of_string_to_string | dict[str, str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_map_string_to_string()
class XArray_of_string(Declared, Ordered["str"]):
    __slots__ = ()

    def __init__(self, value: XArray_of_string | typing.Sequence[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return type_xarray_string()

from . import graph  # noqa: E402

declare(Optional_of_AnyConceptKey, Optional_of_XArray_of_string, Optional_of_Graph_EdgeKey, Optional_of_Graph_EdgeTopology, Optional_of_Graph_GraphDescription, Optional_of_Graph_GraphKey, Optional_of_Graph_GraphSelection, Optional_of_Graph_GraphTopology, Optional_of_Graph_Vertex2DAttributes, Optional_of_Graph_VertexKey, Optional_of_Graph_VertexVisualAttributes, Optional_of_Map_of_string_to_string, Vector_of_string, Set_of_Graph_EdgeKey, Set_of_Graph_GraphKey, Set_of_Graph_VertexKey, Set_of_string, Map_of_string_to_string, XArray_of_string)
