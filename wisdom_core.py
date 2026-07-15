"""Wisdom core — dataclasses, validators, and brief renderer for the wisdom layer.

Per-entry data lives in wisdom/entries/<key>.py; wisdom/manifest.py assembles them.
WISDOM_BRIEF.md is GENERATED from these entries by the generator — never hand-edited.
Design rationale and the calls behind this shape: wisdom/design/DECISIONS.md.

Field policy (the rule behind the small schema): git preserves, it does not inform.
A field is typed only when a validator guards a documented failure mode through it;
anything a future session needs to weigh an entry lives in prose fields IN the entry;
purely forensic history lives in git. Do not add fields without one of those two
justifications.
"""

import re
from dataclasses import dataclass, field
from typing import Literal

# ── DATACLASSES ──────────────────────────────────────────────────────────────

@dataclass
class Citation:
    """One primary-data instance backing (or countering) an entry.

    source forms:
      "fw106 R26"          — run key; validated against jar_manifest and run count
      "session:106"        — session-level evidence that exists in no jar
                             (e.g. the empty-insert control)
      "conversation:<ref>" — user remarks never run-logged (e.g. fridge-nose reports)
    Strike reasons, audit dates, and lineage notes go in gist — they change how a
    future session weighs the citation, so they live here, not in git.
    """
    source: str
    role: Literal['confirms', 'counters', 'context', 'struck']
    provenance: Literal['user-verbatim', 'ai-authored', 'mixed']
    gist: str        # what happened, verbatim-moved prose; length-unbounded
    confounds: str   # REQUIRED non-empty; "none noted" must be explicit

@dataclass
class Position:
    """One dated prose paragraph — the append-log container for evolving analysis."""
    stated: str      # "Session 91", "July 6-7, 2026", ...
    text: str        # full paragraph; length-unbounded
    status: Literal['current', 'superseded'] = 'current'
    superseded_note: str = ""   # REQUIRED when superseded ("Retired by WM R16: ...")

@dataclass
class WisdomEntry:
    key: str                    # == filename stem; lowercase-hyphen; never renamed
    kind: Literal['pattern', 'equipment', 'failure-mode', 'decision', 'theory']
    claim: str                  # <=240 chars; brief-rendered
    guidance: str               # <=320 chars; brief-rendered
    # House epistemic ladder (Recipe 8): observation = 1 run, directional = 2
    # consistent, tested = survives disconfirmation across strains. None for
    # decision/failure-mode kinds — rulings and hazards are not confidence-graded.
    grade: Literal['speculative', 'observation', 'directional', 'tested'] | None = None
    grade_basis: str = ""       # <=200 chars; brief-rendered
    evidence: list[Citation] = field(default_factory=list)   # NOT brief-rendered (counts only)
    positions: list[Position] = field(default_factory=list)  # NOT brief-rendered
    counter_reading: str = ""   # REQUIRED above 'observation': strongest alternative reading
    watch_for: str = ""         # <=200 chars; what evidence would move it; brief-rendered
    updated: str = ""           # session/date refs; how stale is this entry?
    resolution: str = ""        # <=200 chars; REQUIRED for COMPRESSED tier — the one-liner

# ── SESSION-CLOSE CHECKLIST ──────────────────────────────────────────────────
# Rendered as the brief's footer. This is the instruction set for updating the
# wisdom layer; it lives here so it is versioned with the schema it operates on.

SESSION_CLOSE_CHECKLIST = """\
**Before writing to any entry:** Read `wisdom/entries/<key>.py` first, and check whether
an existing entry (or citation within one) should be updated instead of a new one added.
Citations name a specific source with inline observations and explicit confounds — never
vague phrases like "multiple strains." Trim to the strongest examples.

1. Did any cross-strain pattern emerge or get confirmed? A grade promotion
   (observation→directional, directional→tested, or wording that functions as one)
   requires updating `counter_reading` with the strongest counter-reading of the
   evidence and why it fails — the validator rejects promotions without one. A session
   that can't produce a counter-reading it believes in flags the promotion for user
   review instead of manufacturing one.
2. Did equipment configuration change or produce a new observation? (equipment entries)
3. Did a failure mode occur this session — data integrity or process? (failure-mode
   entries; AI behavioral failure modes stay in Dabby_Handoff_Notes.md)
4. Was any methodology position tested, confirmed, or revised? (theory entries —
   append a dated Position; supersede in place, don't delete)
5. Were any decisions made that shouldn't be re-litigated? (decision entries)
6. Were any open BACKLOG.md items rendered obsolete this session, or has a scheduled
   revisit date arrived?
7. Did any jar close this session? Confirm the slug moved ACTIVE→CLOSED in
   jar_manifest.py.

Each "yes" edits the relevant entry file (or BACKLOG.md for Q6). Then update
Dabby_Handoff_Notes.md's header date and run `python3 Dabby_Log_Generator.py` — it
re-validates everything and regenerates this brief alongside HANDOFF_STATE.md."""

# ── VALIDATION ───────────────────────────────────────────────────────────────

_KEY_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
_RUN_SOURCE_RE = re.compile(r'^([a-z0-9]+) R(\d+)$')
_KINDS = {'pattern', 'equipment', 'failure-mode', 'decision', 'theory'}
_GRADES = {'speculative', 'observation', 'directional', 'tested'}
_GRADED_KINDS = {'pattern', 'equipment', 'theory'}
_ROLES = {'confirms', 'counters', 'context', 'struck'}
_PROVENANCE = {'user-verbatim', 'ai-authored', 'mixed'}

_FIELD_CAPS = {'claim': 240, 'guidance': 320, 'grade_basis': 200,
               'watch_for': 200, 'resolution': 200}

BRIEF_HARD_CAP = 20_000   # chars; generator errors above this
BRIEF_SOFT_CAP = 16_000   # chars; generator warns above this
FULL_BLOCK_LIVE_WARN = 40  # full-block-rendered LIVE entries (decisions excluded)
ENTRY_FILE_WARN = 20_000  # chars per entry file; warn with the pressure valves


def _slug_of(citation_source):
    """Return the jar slug for a run-key source, or None for session:/conversation: forms."""
    m = _RUN_SOURCE_RE.match(citation_source)
    return m.group(1) if m else None


def validate_wisdom(entries, live_keys, compressed_keys, jar_run_counts):
    """Semantic validation over loaded entries. Returns a list of error strings.

    jar_run_counts: {slug: number_of_runs} — built by the manifest from jar files,
    so citation integrity is checked against primary data on every generate.
    """
    errors = []
    tiered = {**{k: 'LIVE' for k in live_keys},
              **{k: 'COMPRESSED' for k in compressed_keys}}

    for e in entries:
        who = f"wisdom entry '{e.key}'"

        if not _KEY_RE.match(e.key):
            errors.append(f"{who}: key must be lowercase-hyphen")
        if e.kind not in _KINDS:
            errors.append(f"{who}: unknown kind '{e.kind}'")
        if not e.claim.strip():
            errors.append(f"{who}: empty claim")

        for fname, cap in _FIELD_CAPS.items():
            val = getattr(e, fname) or ""
            if len(val) > cap:
                errors.append(f"{who}: {fname} is {len(val)} chars (cap {cap}) — "
                              f"instance detail belongs in evidence/positions, not "
                              f"brief-rendered fields")

        # Grade discipline: graded kinds must carry one; rulings/hazards must not.
        if e.kind in _GRADED_KINDS:
            if e.grade not in _GRADES:
                errors.append(f"{who}: kind '{e.kind}' requires a grade from {sorted(_GRADES)}")
        elif e.grade is not None:
            errors.append(f"{who}: kind '{e.kind}' must not carry a grade "
                          f"(rulings and hazards are not confidence-graded)")

        # Promotion gate: anything above observation needs a stated counter-reading.
        if e.grade in ('directional', 'tested') and not e.counter_reading.strip():
            errors.append(f"{who}: grade '{e.grade}' requires a non-empty counter_reading")

        # Evidence-weight floor, patterns only (encodes the Recipe 8 ladder).
        if e.kind == 'pattern' and e.grade in ('directional', 'tested'):
            confirms = [c for c in e.evidence if c.role == 'confirms']
            if len(confirms) < 2:
                errors.append(f"{who}: grade '{e.grade}' needs >=2 confirming citations "
                              f"(has {len(confirms)})")
            if e.grade == 'tested':
                slugs = {_slug_of(c.source) for c in confirms} - {None}
                if len(slugs) < 2:
                    errors.append(f"{who}: grade 'tested' means survives disconfirmation "
                                  f"across strains — needs confirming runs from >=2 jars "
                                  f"(has {sorted(slugs)})")

        for i, c in enumerate(e.evidence):
            cwho = f"{who} citation {i + 1} ({c.source!r})"
            if c.role not in _ROLES:
                errors.append(f"{cwho}: unknown role '{c.role}'")
            if c.provenance not in _PROVENANCE:
                errors.append(f"{cwho}: unknown provenance '{c.provenance}'")
            if not c.confounds.strip():
                errors.append(f"{cwho}: empty confounds — 'none noted' must be explicit")
            slug = _slug_of(c.source)
            if slug is not None:
                n = int(_RUN_SOURCE_RE.match(c.source).group(2))
                if slug not in jar_run_counts:
                    errors.append(f"{cwho}: no jar '{slug}' in the manifest")
                elif n < 1 or n > jar_run_counts[slug]:
                    errors.append(f"{cwho}: jar '{slug}' has {jar_run_counts[slug]} runs, "
                                  f"citation names R{n}")
            elif not (c.source.startswith('session:') or c.source.startswith('conversation:')):
                errors.append(f"{cwho}: source must be '<slug> R<n>', 'session:<ref>', "
                              f"or 'conversation:<ref>'")

        for i, p in enumerate(e.positions):
            if p.status not in ('current', 'superseded'):
                errors.append(f"{who} position {i + 1}: unknown status '{p.status}'")
            if p.status == 'superseded' and not p.superseded_note.strip():
                errors.append(f"{who} position {i + 1}: superseded without a "
                              f"superseded_note — the retirement reason is load-bearing")

        if tiered.get(e.key) == 'COMPRESSED' and not e.resolution.strip():
            errors.append(f"{who}: COMPRESSED tier requires a resolution one-liner")

    return errors

# ── BRIEF RENDERER ───────────────────────────────────────────────────────────

_KIND_HEADINGS = [
    ('pattern', 'Cross-Strain Patterns'),
    ('equipment', 'Equipment Observations'),
    ('failure-mode', 'Live Failure Modes'),
    ('theory', 'Working Theory'),
]


def _entry_block(e):
    strains = sorted({_slug_of(c.source) for c in e.evidence} - {None})
    unstruck = [c for c in e.evidence if c.role != 'struck']
    n_confirm = sum(1 for c in unstruck if c.role == 'confirms')
    n_counter = sum(1 for c in unstruck if c.role == 'counters')
    n_struck = sum(1 for c in e.evidence if c.role == 'struck')

    grade_tag = f" | {e.grade}" if e.grade else ""
    lines = [f"### {e.key}  [{e.kind}{grade_tag}]", f"**Claim:** {e.claim}"]
    if e.grade_basis:
        lines.append(f"**Basis:** {e.grade_basis}")
    lines.append(f"**Guidance:** {e.guidance}")
    if e.counter_reading:
        lines.append(f"**Counter-reading:** {e.counter_reading}")
    if e.watch_for:
        lines.append(f"**Watch:** {e.watch_for}")
    ev = f"{len(e.evidence)} citations ({n_confirm} confirm / {n_counter} counter"
    ev += f" / {n_struck} struck)" if n_struck else ")"
    tail = [ev]
    if strains:
        tail.append(f"jars: {', '.join(strains)}")
    if e.updated:
        tail.append(f"upd {e.updated}")
    tail.append(f"detail: wisdom/entries/{e.key}.py")
    lines.append(f"*{' | '.join(tail)}*")
    return "\n".join(lines)


def render_brief(entries, live_keys, compressed_keys):
    """Return WISDOM_BRIEF.md content. Deterministic; renders capped and derived
    fields only — instance-level evidence never appears here by design."""
    by_key = {e.key: e for e in entries}
    live = [by_key[k] for k in live_keys]
    compressed = [by_key[k] for k in compressed_keys]

    out = [
        "# Dabby — Wisdom Brief",
        "*GENERATED by `Dabby_Log_Generator.py` from `wisdom/entries/` — never edit by "
        "hand.*",
        "*Detail rule: anything beyond what is on this page — instance evidence, "
        "confounds, provenance, position history — Read `wisdom/entries/<key>.py`. "
        "Instance-level claims may only be written from an entry file or a jar file, "
        "never from this brief.*",
        "",
    ]

    for kind, heading in _KIND_HEADINGS:
        block = [e for e in live if e.kind == kind]
        if not block:
            continue
        out.append(f"## {heading}")
        out.append("")
        for e in block:
            out.append(_entry_block(e))
            out.append("")

    decisions = [e for e in live if e.kind == 'decision']
    if decisions:
        out.append("## Decisions — Do Not Re-Litigate")
        out.append("*Rationale lives in each entry file.*")
        out.append("")
        for e in decisions:
            out.append(f"- **{e.key}** — {e.claim}")
        out.append("")

    if compressed:
        out.append("## Compressed")
        out.append("*Resolved / retired; full history in the entry file and git.*")
        out.append("")
        for e in compressed:
            out.append(f"- **{e.key}** — {e.resolution}")
        out.append("")

    out.append("## Session-Close Checklist")
    out.append("")
    out.append(SESSION_CLOSE_CHECKLIST)
    out.append("")
    return "\n".join(out)


def brief_size_problems(brief_text, entries, live_keys):
    """Return (errors, warnings) for the rendered brief's budget."""
    errors, warnings = [], []
    n = len(brief_text)
    if n > BRIEF_HARD_CAP:
        errors.append(f"WISDOM_BRIEF.md is {n} chars (hard cap {BRIEF_HARD_CAP}) — "
                      f"move entries LIVE->COMPRESSED or merge overlapping entries; "
                      f"do NOT delete detail (it lives in entry files, not here)")
    elif n > BRIEF_SOFT_CAP:
        warnings.append(f"WISDOM_BRIEF.md is {n} chars (soft cap {BRIEF_SOFT_CAP}) — "
                        f"consider compressing settled entries")
    by_key = {e.key: e for e in entries}
    full_block = [k for k in live_keys if by_key[k].kind != 'decision']
    if len(full_block) > FULL_BLOCK_LIVE_WARN:
        warnings.append(f"{len(full_block)} full-block LIVE entries "
                        f"(warn at {FULL_BLOCK_LIVE_WARN}) — compress or merge")
    return errors, warnings
