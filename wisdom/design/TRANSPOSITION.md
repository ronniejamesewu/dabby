# Transposition Recipe — HANDOFF_WISDOM.md → wisdom/entries/<key>.py

*Instructions for migration workers. Read this fully, then your assigned source lines in
`HANDOFF_WISDOM.md`, then both exemplar entries
(`wisdom/entries/bb36-retronasal-blueberry.py`, `wisdom/entries/fm-bamboo-swab-artifact.py`),
then write your entry file. Schema definitions: `wisdom_core.py` (top of file).*

## The contract: transposition, not condensation

You are re-containering evidence, not editing it. Prose moves **verbatim** — do not
tighten, do not smooth, do not drop qualifiers, hedges, or confound clauses. Dropped
confounds are this project's most documented drift failure; an adversarial review will
diff your output against the source. When the source is awkward, the entry is awkward.

## Field-by-field

- **`key` / `kind` / tier / grade** — assigned in your task; do not change them. `grade`
  is omitted entirely (never `None` explicitly, just leave the kwarg out) for `decision`
  and `failure-mode` kinds.
- **`claim`** (≤240 chars) — the row's pattern statement / the section's current
  position, distilled. Newly authored: stay strictly at or below the source's confidence.
  Banned words: "confirmed", "established", "proves", "resolved" (unless the source says
  resolved).
- **`guidance`** (≤320 chars) — what a session should do or not do, taken from the
  source's operational language ("Do not treat X as settled", "check Y first").
- **`grade_basis`** (≤200 chars) — the source's own evidence-weight summary (the
  Confidence cell's first clause, e.g. "2 strains, paired same-day comparisons").
- **`evidence`** — one `Citation` per cited instance:
  - `source`: run key `"<slug> R<n>"` (slugs below), or `"session:<ref>"` for evidence
    that exists in no jar (e.g. the Session 106 empty-insert control), or
    `"conversation:<ref>"` for user remarks never run-logged.
  - `role`: `confirms` / `counters` / `context` / `struck`. Bracketed audit strikes
    (e.g. "[struck ... July 11, 2026 audit]") → `role='struck'` with the strike reason
    and date in `gist`.
  - `provenance`: `user-verbatim` (source marks it user-verbatim / quotes dab_notes),
    `ai-authored` (source marks it analysis-sourced / session_char / endpoint_note),
    `mixed` (both, or the source is explicit that parts differ). If the source doesn't
    say, use `ai-authored` — that is the pre-dab_notes-era default the July 11 audit
    established — and note "provenance untagged in source" in `gist`.
  - `gist`: that instance's description, moved verbatim (quotes stay quotes).
  - `confounds`: that instance's confound clauses, verbatim. If the source records
    none, write exactly "none noted".
- **`positions`** — the narrative that isn't per-instance: Notes-cell analysis, audit
  history, cross-run comparisons (R26-vs-R28 style pairs live here, not in gist),
  scope statements. One `Position` per dated paragraph/edit where dates are visible
  (`stated` = the session/date label; use the row's First Observed / Updated sessions
  when that's all there is). Retired-in-place paragraphs (e.g. "[Retired by WM R16]")
  → `status='superseded'` + `superseded_note` naming what retired it; keep the full
  retired text.
- **`counter_reading`** — REQUIRED for grade `directional`/`tested` (validator rejects
  without it). Use the source's own counter-language where present (counter rows,
  "Counters:" citations, scope caveats). Where you must author it fresh: state the
  strongest alternative reading of the evidence — the thing a skeptic would say — not a
  strawman. If you genuinely cannot construct one the source supports, write
  `counter_reading="FLAG: no counter-reading constructible from source — review"` and
  it will be triaged.
- **`watch_for`** (≤200 chars) — the source's "what would move it" / "watch for
  recurrence" language, if present; omit otherwise.
- **`updated`** — the source row's Session/date references (First Observed + updates),
  as a short string.
- **`resolution`** (COMPRESSED tier only, ≤200 chars) — the one-liner, essentially the
  source's own bolded line.

## Jar slugs (for run keys)

cag=Caramel Apple Gelato · mbd=Maple Bacon Donut · rainfruit=Rain Fruit ·
bb361=Blueberry 36 #1 · oc=Orange Candy · bb362=Blueberry 36 #2 · bb364=Blueberry 36 #4 ·
fw106=Fire Water #106 · watermellos=Watermellos (WM) · dbrb=Donny Burger + Rainbow Belts ·
lhbh=Lemon Heads + Blueberry Haze · bp4rw13=Banana Punch #4 + Randy Watzon #13 ·
papzp22=Papaya + Z Pie #22 · sourtangie=Sour Tangie · lunarz=LunarZ · wwz=WW Z ·
mb9zst=Mango Banana #9 + Z + Sour Tangie · fembot3=Fembot #3 · ms23=Mango Starburst #23 ·
hive1=The Hive #1

## Self-check before you finish

Run from the repo root (substitute your key):

    python3 -c "
    import importlib.util
    spec = importlib.util.spec_from_file_location('t', 'wisdom/entries/KEY.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    from wisdom_core import validate_wisdom
    from wisdom.manifest import jar_run_counts
    errs = validate_wisdom([m.ENTRY], [m.ENTRY.key], [], jar_run_counts())
    print('OK' if not errs else chr(10).join(errs))
    "

(For COMPRESSED-tier entries, pass `[], [m.ENTRY.key]` instead of `[m.ENTRY.key], []`.)
Fix anything it reports. Do NOT edit `wisdom/manifest.py` — the orchestrator registers
keys. Use straight quotes only; escape apostrophes carefully in Python strings.

## Your final report

One line: your key, OK/errors, plus any `FLAG:` items you embedded (ambiguous
provenance, unconstructible counter-reading, source text you weren't sure how to place).
