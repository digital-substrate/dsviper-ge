# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.


from __future__ import annotations

import base64 as _base64
import functools as _functools
import zlib as _zlib

import dsviper as _dsviper

from . import resources
from ._codegen import AnyConceptKey, AnyValue, Key

__all__ = ["AnyConceptKey", "AnyValue", "Key", "containers", "definitions", "graph"]

@_functools.cache
def definitions() -> _dsviper.DefinitionsConst:
    blob = _dsviper.ValueBlob(_zlib.decompress(_base64.b64decode(resources.B64_DEFINITIONS)))
    return _dsviper.Definitions.decode(blob).const()


from . import containers  # noqa: E402
from . import graph  # noqa: E402
