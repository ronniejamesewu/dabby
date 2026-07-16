"""dump_run_facts.py -- mechanical, verbatim extraction of run facts from jars/*.py.

Purpose: a future session should be able to read run history from a flat,
faithful dump instead of trusting the lossy summaries in HANDOFF_STATE.md or
re-reading full jar-file prose across every strain. This script INTERPRETS
NOTHING. It does not classify, summarize, conclude, connect runs, or flag
patterns -- it renders CompletedRun/StrainStatus fields as-is, tagging each
piece of prose with where it came from (user words vs. extracted structure
vs. AI synthesis vs. deprecated field).

Never fill a silence: an empty or None field renders as exactly "not stated"
in the per-jar markdown -- never a plausible reconstruction.

Outputs (into run_facts/, gitignored):
  run_facts/<slug>.md   -- one file per jar, one block per run, run list order
  run_facts/index.csv   -- one row per run, all jars, struct fields only

Usage: python3 dump_run_facts.py   (Windows: python dump_run_facts.py)
"""

import ast
import csv
import dataclasses
import os
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from Dabby_Core import CompletedRun, _fmt_equipment_display, denver_local, denver_abbrev
from jar_manifest import ACTIVE, CLOSED, _load_jar

JARS_DIR = os.path.join(REPO_ROOT, 'jars')
OUT_DIR = os.path.join(REPO_ROOT, 'run_facts')

NOT_STATED = "not stated"
EM_DASH = "\N{EM DASH}"

# ── Field map ─────────────────────────────────────────────────────────────
# Every CompletedRun field must land in exactly one of these three buckets.
# The assertion below checks that against dataclasses.fields(CompletedRun)
# at import time, so if a field is ever added to the dataclass and this
# script isn't updated, it fails loudly instead of silently dropping data.
#
# STRUCT_FIELDS        -- rendered directly as key: value lines
# STRUCT_TAGGED_FIELDS -- short values rendered inline but carrying a
#                         provenance tag (they are extracted/derived, not
#                         raw user words, even though they're short)
# PROSE_FIELDS         -- longer text, each under its own heading, tagged
#                         with its provenance class per the task contract

STRUCT_FIELDS = [
    'strain', 'run_date', 'utc_logged_at', 'sessions_prior_today',
    'equipment', 'waypoints', 'duration_seconds', 'too_hot', 'date_label',
]
STRUCT_TAGGED_FIELDS = {
    'swab': 'EXTRACTED',
    'intensity': 'EXTRACTED',
}
PROSE_FIELDS = {
    'dab_notes': 'USER-VERBATIM',
    'session_char': 'EXTRACTED',
    'analysis': 'AI-AUTHORED',
    'endpoint_note': 'AI-AUTHORED',
    'extra_rows': 'AI-AUTHORED',
    'read': 'SUPERSEDED',      # SUPERSEDED fields render only when non-empty
    'verdict': 'SUPERSEDED',
}

_known = set(STRUCT_FIELDS) | set(STRUCT_TAGGED_FIELDS) | set(PROSE_FIELDS)
_actual = {f.name for f in dataclasses.fields(CompletedRun)}
if _known != _actual:
    missing = sorted(_actual - _known)
    extra = sorted(_known - _actual)
    raise SystemExit(
        "dump_run_facts.py's field map is out of sync with CompletedRun -- "
        "the dataclass changed and this script wasn't updated.\n"
        f"  In CompletedRun but unmapped here: {missing or 'none'}\n"
        f"  Mapped here but not in CompletedRun: {extra or 'none'}\n"
        "Update STRUCT_FIELDS / STRUCT_TAGGED_FIELDS / PROSE_FIELDS above."
    )


# ── AST line anchors (stretch goal) ──────────────────────────────────────
# Best-effort: maps each RUNS[i] to (line number of the CompletedRun( call,
# name of the waypoints= constant if it's a bare identifier). Returns None
# for the whole jar if the source doesn't parse in the expected shape --
# callers must tolerate a None anchor list.

def _run_anchors(slug):
    path = os.path.join(JARS_DIR, f'{slug}.py')
    try:
        with open(path, encoding='utf-8') as fh:
            tree = ast.parse(fh.read(), filename=path)
    except (OSError, SyntaxError):
        return None
    for node in ast.walk(tree):
        is_runs_assign = (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == 'RUNS'
        )
        if is_runs_assign and isinstance(node.value, ast.List):
            anchors = []
            for elt in node.value.elts:
                wp_name = None
                if isinstance(elt, ast.Call):
                    for kw in elt.keywords:
                        if kw.arg == 'waypoints' and isinstance(kw.value, ast.Name):
                            wp_name = kw.value.id
                anchors.append((getattr(elt, 'lineno', None), wp_name))
            return anchors
    return None


# ── Rendering helpers ────────────────────────────────────────────────────

def _scalar(value):
    """Render a plain scalar (non-prose) field. None or blank -> NOT_STATED."""
    if value is None:
        return NOT_STATED
    if isinstance(value, str) and value.strip() == '':
        return NOT_STATED
    return str(value)


def _quoted(value):
    if value is None or (isinstance(value, str) and value.strip() == ''):
        return NOT_STATED
    return f'"{value}"'


def _prose_block(field_name, tag, value, omit_if_empty=False):
    """Render one PROSE_FIELDS heading + body. Quoted exactly, never paraphrased."""
    is_empty = value is None or value == '' or value == []
    if is_empty:
        if omit_if_empty:
            return []
        return [f"### {field_name} [{tag}]", "", NOT_STATED, ""]

    if field_name == 'extra_rows':
        body = []
        for item in value:
            if isinstance(item, (tuple, list)) and len(item) == 2:
                label, text = item
                body.append(f'- **{label}** "{text}"')
            else:
                body.append(f"- {item!r}")
        return [f"### {field_name} [{tag}]", ""] + body + [""]

    return [f"### {field_name} [{tag}]", "", f'"{value}"', ""]


def _rig_label(eq):
    """Short form for the CSV: 'Rig N' when the equipment matches a known
    RIG_N constant, else the full descriptive string _fmt_equipment_display
    produces for an unmatched inline config."""
    if eq is None:
        return NOT_STATED
    full = _fmt_equipment_display(eq)
    if EM_DASH in full:
        return full.split(EM_DASH, 1)[0].strip()
    return full


def render_run_block(slug, i, run, anchor):
    lineno, wp_name = anchor if anchor else (None, None)

    lines = []
    header = f"## Run {i}"
    if lineno:
        header += f" (jars/{slug}.py:{lineno})"
    lines.append(header)
    lines.append("")

    # -- struct fields --
    lines.append(f"- strain: {_scalar(run.strain)}")
    lines.append(f"- run_date: {run.run_date.isoformat() if run.run_date else NOT_STATED}")
    lines.append(f"- date_label (title override when run_date is not stated): {_scalar(run.date_label)}")
    if run.utc_logged_at:
        local = denver_local(run.utc_logged_at)
        tz = denver_abbrev(run.utc_logged_at)
        lines.append(f"- utc_logged_at: {run.utc_logged_at.isoformat()} (Denver: {local.isoformat()} {tz})")
    else:
        lines.append(f"- utc_logged_at: {NOT_STATED}")
    lines.append(f"- sessions_prior_today: {_scalar(run.sessions_prior_today)}")

    eq_str = _fmt_equipment_display(run.equipment) if run.equipment is not None else NOT_STATED
    lines.append(f"- equipment: {eq_str}")

    wp_suffix = f" (constant: {wp_name})" if wp_name else " (constant: not resolved)"
    lines.append(f"- waypoints{wp_suffix}:")
    if run.waypoints:
        for wp in run.waypoints:
            note = f"  [{wp.note}]" if wp.note else ""
            lines.append(f"    - {wp.time_s}s -> {wp.temp_f}F{note}")
    else:
        lines.append(f"    - {NOT_STATED}")

    lines.append(f"- duration_seconds: {_scalar(run.duration_seconds)}")
    lines.append(f"- too_hot: {run.too_hot}")
    lines.append(f"- swab [EXTRACTED]: {_quoted(run.swab)}")
    lines.append(f"- intensity [EXTRACTED]: {_quoted(run.intensity)}")
    lines.append("")

    # -- prose blobs, each tagged with provenance --
    lines += _prose_block('dab_notes', PROSE_FIELDS['dab_notes'], run.dab_notes)
    lines += _prose_block('session_char', PROSE_FIELDS['session_char'], run.session_char)
    lines += _prose_block('analysis', PROSE_FIELDS['analysis'], run.analysis)
    lines += _prose_block('endpoint_note', PROSE_FIELDS['endpoint_note'], run.endpoint_note)
    lines += _prose_block('extra_rows', PROSE_FIELDS['extra_rows'], run.extra_rows)
    lines += _prose_block('read', PROSE_FIELDS['read'], run.read, omit_if_empty=True)
    lines += _prose_block('verdict', PROSE_FIELDS['verdict'], run.verdict, omit_if_empty=True)

    return "\n".join(lines).rstrip() + "\n"


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    csv_rows = []
    csv_fieldnames = [
        'slug', 'strain', 'run_number', 'run_date', 'utc_logged_at',
        'sessions_prior_today', 'rig_label', 'curve_open_f', 'curve_endpoint_f',
        'duration_seconds', 'too_hot', 'swab', 'intensity',
        # Extra columns beyond the suggested set -- see report.
        'date_label', 'waypoints_const', 'jar_line',
    ]

    jar_summaries = []  # (slug, tier, run_count) for the report

    for tier_name, slug_list in (('CLOSED', CLOSED), ('ACTIVE', ACTIVE)):
        for slug in slug_list:
            runs, status = _load_jar(slug)
            anchors = _run_anchors(slug)
            if anchors is not None and len(anchors) != len(runs):
                # AST parse found a differently-shaped RUNS list than what
                # importlib loaded -- don't trust partial anchors.
                anchors = None

            out_path = os.path.join(OUT_DIR, f'{slug}.md')
            parts = [
                f"# {status.name} (slug: {slug}, tier: {tier_name})",
                "",
                f"Mechanically extracted from jars/{slug}.py by dump_run_facts.py. "
                f"{len(runs)} run(s), in RUNS list order (run number = 1-based index, "
                "not a stored field).",
                "",
            ]
            for i, run in enumerate(runs, start=1):
                anchor = anchors[i - 1] if anchors else None
                parts.append(render_run_block(slug, i, run, anchor))

                lineno, wp_name = anchor if anchor else (None, None)
                wps = run.waypoints or []
                csv_rows.append({
                    'slug': slug,
                    'strain': run.strain or '',
                    'run_number': i,
                    'run_date': run.run_date.isoformat() if run.run_date else '',
                    'utc_logged_at': run.utc_logged_at.isoformat() if run.utc_logged_at else '',
                    'sessions_prior_today': run.sessions_prior_today if run.sessions_prior_today is not None else '',
                    'rig_label': _rig_label(run.equipment),
                    'curve_open_f': wps[0].temp_f if wps else '',
                    'curve_endpoint_f': wps[-1].temp_f if wps else '',
                    'duration_seconds': run.duration_seconds,
                    'too_hot': run.too_hot,
                    'swab': run.swab or '',
                    'intensity': run.intensity or '',
                    'date_label': run.date_label or '',
                    'waypoints_const': wp_name or '',
                    'jar_line': lineno or '',
                })

            with open(out_path, 'w', encoding='utf-8', newline='\n') as fh:
                fh.write("\n".join(parts).rstrip() + "\n")

            jar_summaries.append((slug, tier_name, len(runs)))

    csv_path = os.path.join(OUT_DIR, 'index.csv')
    with open(csv_path, 'w', encoding='utf-8', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=csv_fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)

    total_runs = sum(c for _, _, c in jar_summaries)
    print(f"Wrote {len(jar_summaries)} jar files to {OUT_DIR}")
    print(f"Wrote {csv_path} ({len(csv_rows)} rows)")
    print(f"Total runs dumped: {total_runs}")
    for slug, tier, count in jar_summaries:
        print(f"  {slug:14s} {tier:6s} {count:3d} runs")


if __name__ == '__main__':
    main()
