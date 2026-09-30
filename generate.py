#!/usr/bin/env python3
"""Generate the Python package `gei`: the typed infrastructure of the Graph Editor model.

The model is GraphEditor's own -- dsviper-ge reads and writes the same databases -- so the
definitions come from the sibling `com.digitalsubstrate.ge` checkout, not from a copy.

Only the `Base` feature is rendered: the types, the attachments and the embedded definitions.
The model also declares function pools, which a pure Python application cannot build; they
belong to GraphEditor's C++ side and are left out.

Run from the repository root:

    python3 generate.py

The package is committed; only whoever regenerates it needs the sibling checkouts.
"""
import base64
import glob
import os
import re
import shutil
import subprocess
import sys
import zlib
from pathlib import Path

from dsviper import DSMBuilder

REPO = Path(__file__).resolve().parent
SIBLINGS = REPO.parent

# The kibo line this repository generates against. A generator from another line renders the
# same model differently, and nothing would say so: declare the line. KIBO_JAR overrides it,
# for a deliberate experiment.
KIBO_MAJOR = 2
TEMPLATES_MAJOR = 2

DEFINITIONS = Path(os.environ.get('GE_DEFINITIONS') or SIBLINGS / 'com.digitalsubstrate.ge' / 'definitions' / 'Ge')
TEMPLATES = Path(os.environ.get('KIBO_TEMPLATES') or SIBLINGS / 'devkit-codegen-test' / 'templates')
PYTHON_RUNTIME = Path(os.environ.get('KIBO_PYTHON_RUNTIME')
                      or SIBLINGS / 'devkit-codegen-test' / 'runtime-proposed' / 'python')

PACKAGE = 'gei'
FEATURES = ['Base']
OUTPUT = REPO / PACKAGE
DSM_PATH = REPO / 'GE.dsm.json'


def resolve_jar() -> str:
    if os.environ.get('KIBO_JAR'):
        return os.environ['KIBO_JAR']
    found = []
    for jar in glob.glob(str(SIBLINGS / 'kibo' / 'target' / 'kibo-*.jar')):
        m = re.match(r'^kibo-(\d+)\.(\d+)\.(\d+)\.jar$', os.path.basename(jar))
        if m and int(m.group(1)) == KIBO_MAJOR:
            found.append((tuple(int(g) for g in m.groups()), jar))
    if not found:
        raise SystemExit(f'No kibo {KIBO_MAJOR}.x jar under {SIBLINGS / "kibo" / "target"}. '
                         f'Build kibo, or set KIBO_JAR.')
    return max(found)[1]


def check_templates():
    stamp = re.compile(r'Templates: kibo-template-viper (\d+)\.(\d+)\.(\d+)')
    for stg in sorted(TEMPLATES.rglob('*.stg')):
        if found := stamp.search(stg.read_text()):
            if int(found.group(1)) != TEMPLATES_MAJOR:
                raise SystemExit(f'Templates at {TEMPLATES} are {".".join(found.groups())}; this '
                                 f'repository generates against the {TEMPLATES_MAJOR}.x line.')
            return
    raise SystemExit(f'No versioned template under {TEMPLATES}.')


def main():
    for needed in (DEFINITIONS, TEMPLATES, PYTHON_RUNTIME):
        if not needed.exists():
            raise SystemExit(f'{needed} is missing: check out the sibling repository, or set its variable.')
    jar = resolve_jar()
    check_templates()
    sys.path.insert(0, str(TEMPLATES))
    import resolve

    report, dsm, definitions = DSMBuilder.assemble(str(DEFINITIONS)).parse()
    if report.has_error():
        for error in report.errors():
            print(repr(error))
        raise SystemExit(1)
    DSM_PATH.write_text(dsm.json_encode())
    print(f'using kibo: {Path(jar).name}, definitions: {DEFINITIONS}')

    shutil.rmtree(OUTPUT, ignore_errors=True)
    OUTPUT.mkdir()
    for template in resolve.templates('python', FEATURES):
        subprocess.run(['java', '-jar', jar, '-c', 'python', '-n', PACKAGE, '-d', str(DSM_PATH),
                        '-t', str(template), '-o', str(OUTPUT)], check=True)

    (OUTPUT / 'resources.py').write_text(
        f'B64_DEFINITIONS = {base64.b64encode(zlib.compress(definitions.encode()))}')
    shutil.copytree(PYTHON_RUNTIME, OUTPUT / '_codegen',
                    ignore=shutil.ignore_patterns('__pycache__', '*.md'))


if __name__ == '__main__':
    main()
