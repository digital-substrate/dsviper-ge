# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This application has its own version line, independent from the `dsviper`
runtime version (declared as a dependency in `requirements.txt`).

## [Unreleased]

### Changed
- The typed infrastructure is generated from the Graph Editor model by `generate.py`
  (kibo 2): the package `gei`, with the types in `gei.graph` and one scope per
  attachment in `gei.graph.attachments` (`attachments.Graph.topology.union_vertex_keys`).
  It replaces the copy of the 1.2 generated package that lived under `ge/`, and leaves
  out the model's function pools, which belong to GraphEditor's C++ side.
- The business functions, formerly `model/`, are the package `ge`.
- Written against `gei`: a typed container is a Python one (`set[graph.VertexKey]()`
  rather than `Set_Graph_VertexKey()`), `get` returns the document or `None` with no
  optional to unwrap, and fields and methods are spelled in snake_case.

### Added
- `tests/golden/scenario.py`: the business functions run step by step on an in-memory
  database, and every document they leave behind is compared with a recording made
  from the 1.2 code.

## [1.2.0] - 2026-06-17

First standalone release of the Graph Editor (Qt Widgets).

### Added
- Graph Editor GUI over a Database / CommitDatabase.
- Runs on Python 3.10–3.14; requires dsviper >= 1.2.16.
- Independent version line (`_version.py`), reported via the application
  version and the About dialog, decoupled from the `dsviper` runtime.
