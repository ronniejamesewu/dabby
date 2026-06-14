"""Jar manifest — tracks which lifecycle tier each jar is in.

The move primitive: relocate a slug between ACTIVE / CLOSED. The jar file
itself is never touched. List order within a tier is display order; within
a jar, RUNS order sets run numbering.
"""
import importlib
import os
import re

# ── Tier lists ────────────────────────────────────────────────────────────────

ACTIVE = [
    'cag',         # Caramel Apple Gelato
    'hive1',       # The Hive #1
    'mbd',         # Maple Bacon Donut
    'rainfruit',   # Rain Fruit
    'bb361',       # Blueberry 36 #1
    'oc',          # Orange Candy
    'bb362',       # Blueberry 36 #2
    'fw106',       # Fire Water #106
    'watermellos', # Watermellos
    'dbrb',        # Donny Burger + Rainbow Belts
    'lhbh',        # Lemon Heads + Blueberry Haze
    'bp4rw13',     # Banana Punch #4 + Randy Watzon #13
    'papzp22',     # Papaya + Z Pie #22
]

CLOSED = [
    'wwz',     # WW Z
    'mb9zst',  # Mango Banana #9 + Z + Sour Tangie
    'fembot3', # Fembot #3
    'ms23',    # Mango Starburst #23
]

# ── Validation helpers ────────────────────────────────────────────────────────

_ALLOWED_IMPORT_RE = re.compile(
    r'^(from (datetime|Dabby_Core) import|import datetime\b)'
)
_RUN_REF_RE = re.compile(r'Run (\d+)', re.IGNORECASE)


def _check_closed_tier(slug, runs, status):
    """Return errors if a closed jar's status still contains forward-looking run references."""
    errors = []
    run_count = len(runs)
    for field_name in ('next_text', 'next_ai_analysis'):
        val = getattr(status, field_name, '') or ''
        for m in _RUN_REF_RE.finditer(val):
            if int(m.group(1)) > run_count:
                errors.append(
                    f"Closed jar '{slug}' ({run_count} runs): {field_name} "
                    f"references Run {m.group(1)} — forward-looking, jar is closed"
                )
    return errors

# ── Load functions ────────────────────────────────────────────────────────────

def _validate_manifest_preflight():
    """Check for duplicate slugs, missing/orphan jar files, and disallowed imports BEFORE importing.
    Raises SystemExit on any error — fail fast with clear diagnostics."""
    all_list = ACTIVE + CLOSED
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
            continue
        with open(jar_path, encoding='utf-8') as fh:
            for lineno, line in enumerate(fh, 1):
                stripped = line.strip()
                if stripped.startswith(('import ', 'from ')) and not _ALLOWED_IMPORT_RE.match(stripped):
                    errors.append(
                        f"Jar '{slug}' line {lineno}: disallowed import: {stripped!r}"
                    )

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
    Order: closed first, then active — closed jars render as historical archive."""
    _validate_manifest_preflight()
    all_runs = []
    all_statuses = []
    tier_errors = []

    for slug in CLOSED:
        runs, status = _load_jar(slug)
        all_runs.extend(runs)
        all_statuses.append(status)
        tier_errors.extend(_check_closed_tier(slug, runs, status))

    if tier_errors:
        print("TIER ERRORS:")
        for e in tier_errors:
            print(f"  {e}")
        raise SystemExit(1)

    for slug in ACTIVE:
        runs, status = _load_jar(slug)
        all_runs.extend(runs)
        all_statuses.append(status)

    return all_runs, all_statuses
