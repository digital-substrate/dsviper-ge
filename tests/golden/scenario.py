#!/usr/bin/env python3
"""A golden test of the model layer: the documents each business function leaves behind.

The scenario calls the functions of the model layer, one step after the other, on an in-memory
database of the Graph Editor model, and records after each step every document of every
attachment -- read through the dynamic API, which does not depend on the generated package -- and
what the reading functions answered. The recording is compared with `golden.json`.

Two things make a run reproducible. `random` is seeded; and every new key or position takes the
next UUID of a counter instead of a random one, because the model draws vertices from lists built
out of sets of keys, and the order of those depends on the UUIDs.

    python3 tests/golden/scenario.py            # compare with golden.json
    python3 tests/golden/scenario.py --record   # write golden.json from this checkout
    python3 tests/golden/scenario.py --root <checkout> [--record]

The same scenario runs on the code written against the 1.2 package (`model`, `ge.data`) and on
the code written against the kibo 2 one (`ge`, `gei`): an adapter absorbs the two spellings, so
that a golden recorded on the first is the proof the second behaves the same.
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
from pathlib import Path

import dsviper

HERE = Path(__file__).resolve().parent
GOLDEN = HERE / 'golden.json'


# -- reproducible UUIDs ---------------------------------------------------------------------------

class _UUIdMeta(type):
    def __instancecheck__(cls, obj):
        return isinstance(obj, _REAL_UUID)

    def __getattr__(cls, name):
        return getattr(_REAL_UUID, name)


_REAL_UUID = dsviper.ValueUUId
_COUNTER = itertools.count(1)


class _DeterministicUUId(metaclass=_UUIdMeta):
    """`ValueUUId`, except that `create()` with no argument counts instead of drawing."""

    def __new__(cls, *args, **kwargs):
        return _REAL_UUID(*args, **kwargs)

    @staticmethod
    def create(*args):
        if args:
            return _REAL_UUID.create(*args)
        return _REAL_UUID.create(f'00000000-0000-4000-8000-{next(_COUNTER):012x}')


# -- the two spellings ----------------------------------------------------------------------------

class Api:
    """What the scenario needs that the two generations spell differently."""

    def __init__(self, root: Path):
        sys.path.insert(0, str(root))
        dsviper.ValueUUId = _DeterministicUUId   # before any generated module is imported
        if (root / 'gei').is_dir():
            from gei import definitions, graph
            self.definitions = definitions()
            self.business = 'ge'
            self._graph = graph
        else:
            from ge.definitions import definitions
            import ge.data as data
            self.definitions = definitions()
            self.business = 'model'
            self._graph = None
            self._data = data

    def module(self, name: str):
        return __import__(f'{self.business}.{name}', fromlist=[name])

    def position(self, x: float, y: float):
        if self._graph:
            return self._graph.Position(x=x, y=y)
        p = self._data.Graph_Position()
        p.x, p.y = x, y
        return p

    def rectangle(self, x: float, y: float, w: float, h: float):
        if self._graph:
            return self._graph.Rectangle(x=x, y=y, w=w, h=h)
        r = self._data.Graph_Rectangle()
        r.x, r.y, r.w, r.h = x, y, w, h
        return r

    def color(self, r: float, g: float, b: float):
        if self._graph:
            return self._graph.Color(red=r, green=g, blue=b)
        c = self._data.Graph_Color()
        c.red, c.green, c.blue = r, g, b
        return c


# -- the record -----------------------------------------------------------------------------------

def plain(value):
    """A reading function's answer, as JSON: keys by instance id, collections sorted."""
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if hasattr(value, 'instance_id'):
        return str(value.instance_id())
    if isinstance(value, dict):
        return {str(plain(k)): plain(v) for k, v in value.items()}
    if hasattr(value, '__iter__'):
        items = [plain(v) for v in value]
        return sorted(items, key=json.dumps) if not isinstance(value, (list, tuple)) else items
    return str(value)


def _attachment_name(attachment) -> str:
    return f'{attachment.type_key().representation()} {attachment.representation()}'


def documents(getting) -> dict:
    """Every document of every attachment, through the dynamic API only."""
    out = {}
    # Two concepts can carry an attachment of the same name -- Graph::topology on a graph and on
    # an edge -- so an attachment is named with its key type too.
    for attachment in sorted(getting.definitions().attachments(), key=_attachment_name):
        docs = {}
        for key in getting.keys(attachment):
            doc = getting.get(attachment, key)
            if not doc.is_nil():
                docs[str(key.instance_id())] = json.loads(dsviper.Value.json_encode(doc.unwrap()))
        if docs:
            out[_attachment_name(attachment)] = dict(sorted(docs.items()))
    return out


# -- the scenario ---------------------------------------------------------------------------------

def scenario(api: Api):
    m = lambda name: api.module(name)   # noqa: E731
    state = dsviper.CommitState(api.definitions)
    mutable = dsviper.CommitMutableState(state)
    mut = mutable.attachment_mutating()
    get = mut
    record = []

    def step(name: str, answers: dict | None = None):
        record.append({'step': name, 'answers': plain(answers or {}), 'documents': documents(get)})

    random.seed(7)
    gk = m('graph').create(mut, 'golden')
    step('graph.create')

    m('script_random').random_graph(mut, gk, 12, 16, api.rectangle(0, 0, 800, 600))
    step('script_random.random_graph', {
        'has_vertices': m('graph_topology').has_vertices(get, gk),
        'has_edges': m('graph_topology').has_edges(get, gk),
        'next_value': m('tools').next_vertex_value(get, gk)})

    va = m('vertex').add(mut, gk, 100, api.position(10, 20), api.color(0.1, 0.2, 0.3))
    vb = m('vertex').add(mut, gk, 101, api.position(30, 40), api.color(0.4, 0.5, 0.6))
    ek = m('edge').add(mut, gk, va, vb)
    step('vertex.add, edge.add', {
        'has_edge': m('graph_topology').has_edge(get, gk, va, vb),
        'edge_label': m('tools').edge_label(get, ek),
        'vertex_label': m('tools').vertex_label(get, va)})

    m('random').tag(mut, gk)
    m('random').tag(mut, gk)
    m('random').comment(mut, gk)
    m('random').comment(mut, gk)
    step('random.tag, random.comment')

    m('selection_mixed').select_all(mut, gk)
    step('selection_mixed.select_all', {'has_selected': m('selection_mixed').has_selected(get, gk)})
    m('selection_mixed').invert(mut, gk)
    step('selection_mixed.invert', {'has_selected': m('selection_mixed').has_selected(get, gk)})

    m('selection_random').mixed(mut, gk)
    step('selection_random.mixed', {
        'vertices': m('selection_vertices').selected(get, gk),
        'edges': m('selection_edges').selected(get, gk)})

    m('selection_vertices').select(mut, gk, va)
    m('selection_vertices').combine(mut, gk, vb, True)
    m('selection_edges').select(mut, gk, ek)
    step('selection select/combine', {
        'vertices': m('selection_vertices').selected(get, gk),
        'edges': m('selection_edges').selected(get, gk)})

    m('selection_vertices').increment_value(mut, gk, 5)
    step('selection_vertices.increment_value')

    selected = m('selection_vertices').selected(get, gk)
    m('graph_vertices').move(mut, selected, api.position(3, -2))
    m('graph_vertices').increment_value(mut, selected, 2)
    step('graph_vertices.move, increment_value', {'referenced': m('graph_vertices').referenced_keys(get, gk)})

    m('selection_edges').invert(mut, gk)
    m('selection_vertices').invert(mut, gk)
    step('selection invert edges then vertices')

    m('graph_bug').create_with_missing_vertex(mut, gk)
    m('graph_bug').create_with_missing_vertex_properties(mut, gk)
    try:
        m('graph_bug').create_with_error(mut, gk)
        raised = None
    except RuntimeError as error:   # the model's voluntary crash, part of what it does
        raised = str(error)
    step('graph_bug', {'remaining_edges': m('graph_topology').has_remaining_edges(get, gk),
                       'create_with_error raised': raised})

    m('script_integrity').restore_by_creating(mut, gk)
    step('script_integrity.restore_by_creating')
    m('graph_bug').create_with_missing_vertex(mut, gk)
    m('script_integrity').restore_by_deleting(mut, gk)
    step('script_integrity.restore_by_deleting')
    m('graph_bug').create_with_missing_vertex_properties(mut, gk)
    m('script_integrity').restore_by_respawning(mut, gk)
    step('script_integrity.restore_by_respawning')

    m('selection_random').vertices(mut, gk)
    m('script_delete_selection').delete_selection(mut, gk)
    step('script_delete_selection.delete_selection', {'has_selected': m('selection_mixed').has_selected(get, gk)})

    m('selection_random').edges(mut, gk)
    m('selection_integrity').restore(mut, gk)
    step('selection_random.edges, selection_integrity.restore')

    m('graph_killer').shoot(mut, gk, 3)
    step('graph_killer.shoot')

    m('graph_topology').clear(mut, gk)
    step('graph_topology.clear', {'has_vertices': m('graph_topology').has_vertices(get, gk)})
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--root', type=Path, default=HERE.parent.parent, help='the checkout to run')
    parser.add_argument('--record', action='store_true', help='write golden.json from this run')
    args = parser.parse_args()

    record = scenario(Api(args.root.resolve()))
    if args.record:
        GOLDEN.write_text(json.dumps(record, indent=1, sort_keys=True) + '\n')
        print(f'recorded {len(record)} steps in {GOLDEN.name}')
        return 0

    golden = json.loads(GOLDEN.read_text())
    ok = True
    for expected, got in itertools.zip_longest(golden, json.loads(json.dumps(record, sort_keys=True))):
        name = (expected or got)['step']
        same = expected == got
        ok &= same
        print(f"  {'ok   ' if same else 'DIFF '} {name}")
        if not same:
            for part in ('answers', 'documents'):
                if (expected or {}).get(part) != (got or {}).get(part):
                    print(f'        {part} differ')
            break
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
