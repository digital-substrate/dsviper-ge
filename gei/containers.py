# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.2 (MIT), Template Model 2.
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

__all__ = [
    "Optional_of_AnyConceptKey",
    "Optional_of_XArray_of_string",
    "Optional_of_Graph_EdgeKey",
    "Optional_of_Graph_EdgeTopology",
    "Optional_of_Graph_GraphDescription",
    "Optional_of_Graph_GraphKey",
    "Optional_of_Graph_GraphSelection",
    "Optional_of_Graph_GraphTopology",
    "Optional_of_Graph_Vertex2DAttributes",
    "Optional_of_Graph_VertexKey",
    "Optional_of_Graph_VertexVisualAttributes",
    "Optional_of_Map_of_string_to_string",
    "Vector_of_string",
    "Set_of_Graph_EdgeKey",
    "Set_of_Graph_GraphKey",
    "Set_of_Graph_VertexKey",
    "Set_of_string",
    "Map_of_string_to_string",
    "XArray_of_string",
]

def _type_bool() -> dsviper.TypeBool: return dsviper.TypeBool()
def _type_uint8() -> dsviper.TypeUInt8: return dsviper.TypeUInt8()
def _type_uint16() -> dsviper.TypeUInt16: return dsviper.TypeUInt16()
def _type_uint32() -> dsviper.TypeUInt32: return dsviper.TypeUInt32()
def _type_uint64() -> dsviper.TypeUInt64: return dsviper.TypeUInt64()
def _type_int8() -> dsviper.TypeInt8: return dsviper.TypeInt8()
def _type_int16() -> dsviper.TypeInt16: return dsviper.TypeInt16()
def _type_int32() -> dsviper.TypeInt32: return dsviper.TypeInt32()
def _type_int64() -> dsviper.TypeInt64: return dsviper.TypeInt64()
def _type_float() -> dsviper.TypeFloat: return dsviper.TypeFloat()
def _type_double() -> dsviper.TypeDouble: return dsviper.TypeDouble()
def _type_string() -> dsviper.TypeString: return dsviper.TypeString()
def _type_blob() -> dsviper.TypeBlob: return dsviper.TypeBlob()
def _type_blob_id() -> dsviper.TypeBlobId: return dsviper.TypeBlobId()
def _type_commit_id() -> dsviper.TypeCommitId: return dsviper.TypeCommitId()
def _type_uuid() -> dsviper.TypeUUId: return dsviper.TypeUUId()
def _type_any() -> dsviper.TypeAny: return dsviper.TypeAny()
def _type_AnyConceptKey() -> dsviper.TypeKey: return dsviper.TypeKey(dsviper.TypeAnyConcept())
def _type_Graph_EdgeKey() -> dsviper.Type: return dsviper.TypeKey(definitions().check_concept(graph.data.EDGE))
def _type_Graph_GraphKey() -> dsviper.Type: return dsviper.TypeKey(definitions().check_concept(graph.data.GRAPH))
def _type_Graph_VertexKey() -> dsviper.Type: return dsviper.TypeKey(definitions().check_concept(graph.data.VERTEX))
def _type_Graph_Color() -> dsviper.Type: return definitions().check_structure(graph.data.COLOR)
def _type_Graph_EdgeTopology() -> dsviper.Type: return definitions().check_structure(graph.data.EDGE_TOPOLOGY)
def _type_Graph_GraphDescription() -> dsviper.Type: return definitions().check_structure(graph.data.GRAPH_DESCRIPTION)
def _type_Graph_GraphSelection() -> dsviper.Type: return definitions().check_structure(graph.data.GRAPH_SELECTION)
def _type_Graph_GraphTopology() -> dsviper.Type: return definitions().check_structure(graph.data.GRAPH_TOPOLOGY)
def _type_Graph_Position() -> dsviper.Type: return definitions().check_structure(graph.data.POSITION)
def _type_Graph_Rectangle() -> dsviper.Type: return definitions().check_structure(graph.data.RECTANGLE)
def _type_Graph_Vertex2DAttributes() -> dsviper.Type: return definitions().check_structure(graph.data.VERTEX_2D_ATTRIBUTES)
def _type_Graph_VertexVisualAttributes() -> dsviper.Type: return definitions().check_structure(graph.data.VERTEX_VISUAL_ATTRIBUTES)

@functools.cache
def _type_optional_AnyConceptKey() -> dsviper.Type: return dsviper.TypeOptional(_type_AnyConceptKey())
@functools.cache
def _type_optional_xarray_string() -> dsviper.Type: return dsviper.TypeOptional(_type_xarray_string())
@functools.cache
def _type_optional_Graph_EdgeKey() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_EdgeKey())
@functools.cache
def _type_optional_Graph_EdgeTopology() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_EdgeTopology())
@functools.cache
def _type_optional_Graph_GraphDescription() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_GraphDescription())
@functools.cache
def _type_optional_Graph_GraphKey() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_GraphKey())
@functools.cache
def _type_optional_Graph_GraphSelection() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_GraphSelection())
@functools.cache
def _type_optional_Graph_GraphTopology() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_GraphTopology())
@functools.cache
def _type_optional_Graph_Vertex2DAttributes() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_Vertex2DAttributes())
@functools.cache
def _type_optional_Graph_VertexKey() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_VertexKey())
@functools.cache
def _type_optional_Graph_VertexVisualAttributes() -> dsviper.Type: return dsviper.TypeOptional(_type_Graph_VertexVisualAttributes())
@functools.cache
def _type_optional_map_string_to_string() -> dsviper.Type: return dsviper.TypeOptional(_type_map_string_to_string())
@functools.cache
def _type_vector_string() -> dsviper.Type: return dsviper.TypeVector(_type_string())
@functools.cache
def _type_set_Graph_EdgeKey() -> dsviper.Type: return dsviper.TypeSet(_type_Graph_EdgeKey())
@functools.cache
def _type_set_Graph_GraphKey() -> dsviper.Type: return dsviper.TypeSet(_type_Graph_GraphKey())
@functools.cache
def _type_set_Graph_VertexKey() -> dsviper.Type: return dsviper.TypeSet(_type_Graph_VertexKey())
@functools.cache
def _type_set_string() -> dsviper.Type: return dsviper.TypeSet(_type_string())
@functools.cache
def _type_map_string_to_string() -> dsviper.Type: return dsviper.TypeMap(_type_string(), _type_string())
@functools.cache
def _type_xarray_string() -> dsviper.Type: return dsviper.TypeXArray(_type_string())

class Optional_of_AnyConceptKey(Declared, Optional["AnyConceptKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_AnyConceptKey | dsviper.ValueOptional | AnyConceptKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_AnyConceptKey()

class Optional_of_XArray_of_string(Declared, Optional["containers.XArray_of_string"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_XArray_of_string | dsviper.ValueOptional | containers.XArray_of_string | typing.Sequence[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_xarray_string()

class Optional_of_Graph_EdgeKey(Declared, Optional["graph.EdgeKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_EdgeKey | dsviper.ValueOptional | graph.EdgeKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_EdgeKey()

class Optional_of_Graph_EdgeTopology(Declared, Optional["graph.EdgeTopology"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_EdgeTopology | dsviper.ValueOptional | graph.EdgeTopology | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_EdgeTopology()

class Optional_of_Graph_GraphDescription(Declared, Optional["graph.GraphDescription"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphDescription | dsviper.ValueOptional | graph.GraphDescription | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_GraphDescription()

class Optional_of_Graph_GraphKey(Declared, Optional["graph.GraphKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphKey | dsviper.ValueOptional | graph.GraphKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_GraphKey()

class Optional_of_Graph_GraphSelection(Declared, Optional["graph.GraphSelection"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphSelection | dsviper.ValueOptional | graph.GraphSelection | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_GraphSelection()

class Optional_of_Graph_GraphTopology(Declared, Optional["graph.GraphTopology"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_GraphTopology | dsviper.ValueOptional | graph.GraphTopology | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_GraphTopology()

class Optional_of_Graph_Vertex2DAttributes(Declared, Optional["graph.Vertex2DAttributes"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_Vertex2DAttributes | dsviper.ValueOptional | graph.Vertex2DAttributes | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_Vertex2DAttributes()

class Optional_of_Graph_VertexKey(Declared, Optional["graph.VertexKey"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_VertexKey | dsviper.ValueOptional | graph.VertexKey | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_VertexKey()

class Optional_of_Graph_VertexVisualAttributes(Declared, Optional["graph.VertexVisualAttributes"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Graph_VertexVisualAttributes | dsviper.ValueOptional | graph.VertexVisualAttributes | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_Graph_VertexVisualAttributes()

class Optional_of_Map_of_string_to_string(Declared, Optional["containers.Map_of_string_to_string"]):
    __slots__ = ()

    def __init__(self, value: Optional_of_Map_of_string_to_string | dsviper.ValueOptional | containers.Map_of_string_to_string | dict[str, str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_optional_map_string_to_string()
class Vector_of_string(Declared, Vector["str"]):
    __slots__ = ()

    def __init__(self, value: Vector_of_string | dsviper.ValueVector | typing.Sequence[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_vector_string()
class Set_of_Graph_EdgeKey(Declared, SetView["graph.EdgeKey"]):
    __slots__ = ()

    def __init__(self, value: Set_of_Graph_EdgeKey | dsviper.ValueSet | typing.Iterable[graph.EdgeKey] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_set_Graph_EdgeKey()

class Set_of_Graph_GraphKey(Declared, SetView["graph.GraphKey"]):
    __slots__ = ()

    def __init__(self, value: Set_of_Graph_GraphKey | dsviper.ValueSet | typing.Iterable[graph.GraphKey] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_set_Graph_GraphKey()

class Set_of_Graph_VertexKey(Declared, SetView["graph.VertexKey"]):
    __slots__ = ()

    def __init__(self, value: Set_of_Graph_VertexKey | dsviper.ValueSet | typing.Iterable[graph.VertexKey] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_set_Graph_VertexKey()

class Set_of_string(Declared, SetView["str"]):
    __slots__ = ()

    def __init__(self, value: Set_of_string | dsviper.ValueSet | typing.Iterable[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_set_string()
class Map_of_string_to_string(Declared, Mapping["str", "str"]):
    __slots__ = ()

    def __init__(self, value: Map_of_string_to_string | dsviper.ValueMap | dict[str, str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_map_string_to_string()
class XArray_of_string(Declared, Ordered["str"]):
    __slots__ = ()

    def __init__(self, value: XArray_of_string | dsviper.ValueXArray | typing.Sequence[str] | None = None) -> None:
        super().__init__(value)

    @classmethod
    def type(cls) -> dsviper.Type:
        return _type_xarray_string()

from . import graph  # noqa: E402

declare(Optional_of_AnyConceptKey, Optional_of_XArray_of_string, Optional_of_Graph_EdgeKey, Optional_of_Graph_EdgeTopology, Optional_of_Graph_GraphDescription, Optional_of_Graph_GraphKey, Optional_of_Graph_GraphSelection, Optional_of_Graph_GraphTopology, Optional_of_Graph_Vertex2DAttributes, Optional_of_Graph_VertexKey, Optional_of_Graph_VertexVisualAttributes, Optional_of_Map_of_string_to_string, Vector_of_string, Set_of_Graph_EdgeKey, Set_of_Graph_GraphKey, Set_of_Graph_VertexKey, Set_of_string, Map_of_string_to_string, XArray_of_string)
