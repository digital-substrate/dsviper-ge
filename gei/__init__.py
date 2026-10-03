# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

"""The gei model, generated over dsviper.

Each DSM namespace is a module holding its structures, enumerations and keys, and its
attachments as `attachments`:
`gei.graph`.
`containers` holds the containers the model's structures use, and `definitions()` is the
model.
The pools, rendered with the Pool feature, are imported by their path:
`import gei.tools`, `import gei.model_graph`, `import gei.model_integrity`, `import gei.model_selection`.

A document is stored in a dsviper database that knows the model, and read and written
through an attachment, given the database or a state:

    db = dsviper.Database.create_in_memory()     # a CommitDatabase keeps every commit
    db.extend_definitions(gei.definitions())
    db.begin_transaction()
    gei.graph.attachments.Concept.attachment.set(db, key, document)
    db.commit()

A generated object is a box around a Viper value: `p.unwrap_value()` gives it, and
`Cls.wrap_value(value)` boxes one. A runtime feature is called on that value: bytes are
`dsviper.Value.encode(p.unwrap_value())`, read back with
`Cls.wrap_value(dsviper.Value.decode(blob, Cls.type(), definitions()))`. A value of the wrong
type raises TypeError; what the runtime refuses raises dsviper.ViperError.
"""

import base64 as _base64
import functools as _functools
import zlib as _zlib

import dsviper as _dsviper

from . import resources
from ._codegen import AnyConceptKey, AnyValue, AttachmentProxy, Key

__all__ = ["AnyConceptKey", "AnyValue", "AttachmentProxy", "Key", "containers", "definitions", "graph"]

@_functools.cache
def definitions() -> _dsviper.DefinitionsConst:
    """The model's definitions, decoded once: what a database is extended with, and what
    decoding a value needs."""
    blob = _dsviper.ValueBlob(_zlib.decompress(_base64.b64decode(resources.B64_DEFINITIONS)))
    return _dsviper.Definitions.decode(blob).const()


from . import containers  # noqa: E402
from . import graph  # noqa: E402
