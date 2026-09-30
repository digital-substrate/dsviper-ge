# Graph Editor (dsviper-ge)

A PySide6 desktop application for graph database visualization and editing, built on dsviper.

## Documentation

Full documentation: https://docs.digitalsubstrate.io/commit-apps/dsviper-ge.html

Part of the [DevKit ecosystem](https://docs.digitalsubstrate.io/).

## Prerequisites

- Python 3.10-3.14

## Installation

```bash
pip install -r requirements.txt
```

This installs `dsviper` (the Viper Python binding, from [PyPI](https://pypi.org/project/dsviper/)) along with `PySide6`.

## Usage

Run the application:

```bash
python3 graph_editor.py
```

Open an existing database:

```bash
python3 graph_editor.py path/to/database.db
```

## Code layout

The application reads and writes the databases of the Graph Editor model — the model
of the AppKit reference application, whose definitions live in
`com.digitalsubstrate.ge`. Two packages sit on top of it:

- `gei/` — the typed infrastructure, generated from the model by `generate.py`:
  the types (`gei.graph.VertexKey`, `gei.graph.Position`) and one scope per
  attachment (`gei.graph.attachments.Graph.topology`). Never edited by hand.
- `ge/` — the business functions of the Graph Editor, written against `gei`.

```python
from gei import graph
from gei.graph import attachments

topology = attachments.Graph.topology.get(attachment_getting, graph_key)   # the document, or None
if topology:
    vertex_keys = topology.vertex_keys

attachments.Graph.selection.union_vertex_keys(attachment_mutating, graph_key, {vertex_key})
attachments.Vertex.visual_attributes.set(attachment_mutating, vertex_key,
                                         graph.VertexVisualAttributes(value=1, color=color))
```

Types, fields and operations are named, so an editor completes them. A container field
is a live view over the value, and accepts Python's own sets, lists and dicts when
written.

## Regenerating gei

`gei/` is committed, so a fresh clone runs without regenerating. Regenerate after the
model changes:

```bash
python3 generate.py
```

It needs, as sibling checkouts:

- `../com.digitalsubstrate.ge` — the model's definitions (`definitions/Ge`, or set
  `GE_DEFINITIONS`);
- `../kibo-template-viper` on `kibo-2-dev` — the kibo 2 template pack (or set
  `KIBO_TEMPLATES`) and the Python runtime copied into `gei/_codegen`
  (`python/runtime`, or set `KIBO_PYTHON_RUNTIME`);
- `../kibo`, built: `target/kibo-2.x.y.jar`, or set `KIBO_JAR`.

Only the `Base` feature is generated: types, attachments and the embedded definitions.
The model's function pools belong to GraphEditor's C++ side and are left out.

Always commit the regenerated files.

## Checking the business functions

`tests/golden/scenario.py` runs the functions of `ge/` step by step on an in-memory
database and compares every document left behind with `tests/golden/golden.json`:

```bash
python3 tests/golden/scenario.py
```

## Building

Generated Qt files (`ui_*.py` and `resources_rc.py`) are committed,
so a fresh clone runs immediately. After editing any `*.ui` or
`resources.qrc`, regenerate with:

```bash
python3 dev/build.py
```

The shared `dsviper_components/` package is sourced from
`dsviper-components`. To pull updates from
that source repository (a maintenance task, not a contributor task):

```bash
python3 dev/sync_dsviper_components.py    # refresh dsviper_components/ from sibling
python3 dev/build.py                       # then regenerate ui_*.py / resources_rc.py
git diff dsviper_components resources_rc.py     # review the bump
```

`PySide6` is pinned in `requirements.txt` to guarantee reproducible
regeneration across contributors.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE).

## Runtime dependency

At runtime, this project depends on the `dsviper` Python package
(distributed on PyPI), which is **proprietary** (license expression
`LicenseRef-DigitalSubstrate-Commercial-1.2`). See
[https://pypi.org/project/dsviper/](https://pypi.org/project/dsviper/)
for the package's licensing posture and contact information.
