# Generated from gei.dsm.json by kibo-2.0.0.jar. Do not edit by hand.
# Templates: kibo-template-viper 2.0.0 (MIT), Template Model 2.
# Runtime: this file imports `dsviper` >=1.2.29 <1.3.0,
# distributed under LicenseRef-DigitalSubstrate-Commercial-1.2.
# Commercial use requires a Commercial Licence from Digital Substrate.

"""The gei model, generated over dsviper.

Each DSM namespace is a module holding its structures, enumerations and keys:
`gei.graph`. Its attachments are
a submodule per usage, imported by its path: `<unit>.database_attachments` over a
dsviper.Database (the DatabaseAttachments feature), `<unit>.commit_attachments` over a Commit
state (the CommitAttachments feature).
`containers` holds one class per container shape the model uses, in a structure, an
attachment or a pool; another shape is built with the runtime, from Viper values:
`dsviper.Value.create(dsviper.TypeSet(gei.graph.EdgeKey.type()), [k.unwrap_value() for k in keys])`.
`definitions()` is the model.
A pool is a package, its modules imported by their path, `<pool>.embedded` for the
host's embedded Python, `<pool>.remote` for a client of a service:
`gei.tools`, `gei.model_graph`, `gei.model_integrity`, `gei.model_selection`.

A document is stored in a dsviper database that knows the model, and read and written
through an attachment; over a Database:

    import gei.graph.database_attachments
    db = dsviper.Database.create_in_memory()
    db.extend_definitions(gei.definitions())
    db.begin_transaction()
    gei.graph.database_attachments.Edge.topology.set(db, key, document)
    db.commit()

A generated object is a box around a Viper value: `p.unwrap_value()` gives it, and
`Cls.wrap_value(value)` boxes one. A runtime feature is called on that value: bytes are
`dsviper.Value.encode(p.unwrap_value())`, read back with
`Cls.wrap_value(dsviper.Value.decode(blob, Cls.type(), definitions(), encoded=False))`, which
asks for the Viper value rather than natives. wrap_value or a constructor given a Viper value of
another type raises TypeError; the rest is the runtime's to refuse, with dsviper.ViperError:
content that does not fit, native or generated, in a field, a container or an attachment.
"""

import base64 as _base64
import functools as _functools
import zlib as _zlib

import dsviper as _dsviper

from . import resources
from ._codegen import AnyConceptKey, AnyValue, AttachmentBase, Key

__all__ = ["AnyConceptKey", "AnyValue", "AttachmentBase", "Key", "containers", "definitions", "graph"]

@_functools.cache
def definitions() -> _dsviper.DefinitionsConst:
    """The model's definitions, decoded once: what a database is extended with, and what
    decoding a value needs."""
    blob = _dsviper.ValueBlob(_zlib.decompress(_base64.b64decode(resources.B64_DEFINITIONS)))
    return _dsviper.Definitions.decode(blob).const()


from . import containers  # noqa: E402
from . import graph  # noqa: E402
