"""Wisdom manifest — tier lists and the loader that assembles wisdom entries.

Mirrors jar_manifest.py: the move primitive is relocating a key between LIVE and
COMPRESSED; the entry file itself is never touched by the move. List order within
a tier is brief render order. Design rationale: wisdom/design/DECISIONS.md.
"""
import importlib
import importlib.util
import os
import re

# ── Tier lists ────────────────────────────────────────────────────────────────

LIVE = [
    # pattern
    'bb36-retronasal-blueberry',
    # failure-mode
    'fm-bamboo-swab-artifact',
]

COMPRESSED = [
]

# ── Preflight ────────────────────────────────────────────────────────────────

_ALLOWED_IMPORT_RE = re.compile(
    r'^(from (datetime|wisdom_core) import|import datetime\b)'
)


def _validate_manifest_preflight():
    """Duplicate keys, missing/orphan entry files, disallowed imports, curly-quote
    contamination — checked BEFORE importing. SystemExit on any error."""
    all_keys = LIVE + COMPRESSED
    errors = []

    seen = set()
    for key in all_keys:
        if key in seen:
            errors.append(f"Duplicate key in wisdom manifest: '{key}'")
        seen.add(key)

    entries_dir = os.path.join(os.path.dirname(__file__), 'entries')
    for key in all_keys:
        path = os.path.join(entries_dir, f'{key}.py')
        if not os.path.isfile(path):
            errors.append(f"Manifest key '{key}' has no entry file: {path}")
            continue
        size = os.path.getsize(path)
        if size > 20_000:
            print(f"WISDOM WARNING: entry '{key}' is {size} bytes (warn at 20000) — "
                  f"split the entry (new keys, lineage note in prose) or compact "
                  f"fully-superseded positions to git with a pointer note.")
        with open(path, encoding='utf-8') as fh:
            for lineno, line in enumerate(fh, 1):
                stripped = line.strip()
                if stripped.startswith(('import ', 'from ')) and not _ALLOWED_IMPORT_RE.match(stripped):
                    errors.append(f"Entry '{key}' line {lineno}: disallowed import: {stripped!r}")
                if '\\“' in line or '\\”' in line:
                    errors.append(f"Entry '{key}' line {lineno}: backslash + curly quote — "
                                  f"Edit-tool contamination; fix by byte position with a "
                                  f"Python script, not the Edit tool.")

    if os.path.isdir(entries_dir):
        entry_files = {f[:-3] for f in os.listdir(entries_dir)
                       if f.endswith('.py') and f != '__init__.py'}
        orphans = entry_files - seen
        if orphans:
            errors.append(f"Entry files not in wisdom manifest: {sorted(orphans)}")

    if errors:
        print("WISDOM MANIFEST ERRORS:")
        for e in errors:
            print(f"  {e}")
        raise SystemExit(1)

# ── Loaders ──────────────────────────────────────────────────────────────────

def load_all_entries():
    """Preflight, then import every entry. Returns list of WisdomEntry in
    manifest order (LIVE then COMPRESSED)."""
    _validate_manifest_preflight()
    entries_dir = os.path.join(os.path.dirname(__file__), 'entries')
    entries = []
    for key in LIVE + COMPRESSED:
        # Keys are lowercase-hyphen (not valid dotted module names), so entries load
        # by file path. They execute with the repo root on sys.path — the generator's
        # invocation context — which is how `from wisdom_core import *` resolves.
        path = os.path.join(entries_dir, f'{key}.py')
        try:
            spec = importlib.util.spec_from_file_location(f'wisdom_entry_{key.replace("-", "_")}', path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        except Exception as e:
            raise RuntimeError(f"Failed loading wisdom entry '{key}'") from e
        if not hasattr(mod, 'ENTRY'):
            raise RuntimeError(f"Wisdom entry '{key}' missing ENTRY export")
        if mod.ENTRY.key != key:
            raise RuntimeError(f"Wisdom entry file '{key}' exports ENTRY.key="
                               f"'{mod.ENTRY.key}' — key must match filename/manifest")
        entries.append(mod.ENTRY)
    return entries


def jar_run_counts():
    """{slug: run count} from the jar layer, for citation-integrity validation."""
    import jar_manifest
    counts = {}
    for slug in jar_manifest.ACTIVE + jar_manifest.CLOSED:
        mod = importlib.import_module(f'jars.{slug}')
        counts[slug] = len(mod.RUNS)
    return counts
