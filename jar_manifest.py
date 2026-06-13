"""Jar manifest — tracks which lifecycle tier each jar is in.

The move primitive: relocate a slug between ACTIVE / PAUSED / CLOSED. The jar
file itself is never touched. List order within a tier is display order; within
a jar, RUNS order sets run numbering.
"""
import importlib
import os

# ── Tier lists ────────────────────────────────────────────────────────────────

ACTIVE = [
    'cag',
    'oc',
    'hive1',
    'fembot3',
    'ms23',
    'mbd',
    'rainfruit',
    'bb361',
    'bb362',
    'fw106',
    'watermellos',
    'dbrb',
    'lhbh',
    'bp4rw13',
    'papzp22',
]

PAUSED = []

CLOSED = [
    'wwz',
    'mb9zst',
]

# ── Load functions ────────────────────────────────────────────────────────────

def _validate_manifest_preflight():
    """Check for duplicate slugs and missing/orphan jar files BEFORE importing.
    Raises SystemExit on any error — fail fast with clear diagnostics."""
    all_list = ACTIVE + PAUSED + CLOSED
    errors = []

    seen = set()
    for slug in all_list:
        if slug in seen:
            errors.append(f"Duplicate slug in manifest: '{slug}'")
        seen.add(slug)

    jar_dir = os.path.join(os.path.dirname(__file__), 'jars')
    for slug in all_list:
        jar_path = os.path.join(jar_dir, f'{slug}.py')
        if not os.path.isfile(jar_path):
            errors.append(f"Manifest slug '{slug}' has no jar file: {jar_path}")

    if os.path.isdir(jar_dir):
        jar_files = {f[:-3] for f in os.listdir(jar_dir)
                     if f.endswith('.py') and f != '__init__.py'}
        orphans = jar_files - seen
        if orphans:
            errors.append(f"Jar files not in manifest: {orphans}")

    if errors:
        print("MANIFEST ERRORS:")
        for e in errors:
            print(f"  {e}")
        raise SystemExit(1)

def _load_jar(slug):
    """Import a jar module and return its (RUNS, STATUS)."""
    try:
        mod = importlib.import_module(f'jars.{slug}')
    except Exception as e:
        raise RuntimeError(f"Failed loading jar '{slug}'") from e
    if not hasattr(mod, 'RUNS'):
        raise RuntimeError(f"Jar '{slug}' missing RUNS export")
    if not hasattr(mod, 'STATUS'):
        raise RuntimeError(f"Jar '{slug}' missing STATUS export")
    return mod.RUNS, mod.STATUS

def load_all_jars():
    """Load all jars across all tiers. Returns (all_runs, all_statuses).
    Order: closed, then paused, then active — matching the prior
    ARCHIVED + ACTIVE concatenation so render order and accent colors are stable."""
    _validate_manifest_preflight()
    all_runs = []
    all_statuses = []
    for slug in CLOSED + PAUSED + ACTIVE:
        runs, status = _load_jar(slug)
        all_runs.extend(runs)
        all_statuses.append(status)
    return all_runs, all_statuses

def load_active_jars():
    """Load only active jars. For dormancy checks that don't need archived data."""
    _validate_manifest_preflight()
    all_runs = []
    all_statuses = []
    for slug in ACTIVE:
        runs, status = _load_jar(slug)
        all_runs.extend(runs)
        all_statuses.append(status)
    return all_runs, all_statuses
