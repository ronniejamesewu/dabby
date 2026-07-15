# Phase 4 Retarget Spec — what replaced HANDOFF_WISDOM.md

*For workers updating skills/docs. The wisdom layer is now typed data; this spec is the
target state every reference must point at. Full rationale: DECISIONS.md.*

## The new shape

- **`WISDOM_BRIEF.md`** — GENERATED (never hand-edited) by `python3 Dabby_Log_Generator.py`.
  The bounded always-read surface: one Read (~33k chars). Carries every entry's claim,
  grade, guidance, watch-for, evidence counts, and jar list — plus decision one-liners,
  compressed one-liners, and the session-close checklist as its footer. Replaces
  HANDOFF_WISDOM.md as the mandatory session-open read.
- **`wisdom/entries/<key>.py`** — one file per entry (keys visible in the brief):
  full evidence (citations with role/provenance/confounds), dated positions,
  counter-readings, supersession history. The on-demand detail layer.
- **`wisdom/manifest.py`** — LIVE / COMPRESSED tier lists. Compressing a settled entry =
  move its key, set its `resolution` one-liner; the entry file is untouched.
- **Validators** run inside every generator invocation; a bad edit fails the build.

## Rules that references must now express

1. **Session open:** Read `WISDOM_BRIEF.md` (one Read). Never read all entry files at open.
2. **Detail rule:** before finalizing any analysis or draft that cites, compares against,
   or would change a wisdom entry — Read `wisdom/entries/<key>.py` for each such key
   first. Instance-level claims (run details, confounds, provenance) may only be written
   from an entry file or a jar file, never from the brief.
3. **Session-close wisdom edits:** run the checklist in the brief's footer; each "yes"
   edits the relevant entry file (append a Citation or dated Position; update claim/
   guidance/grade in place). Grade promotions above 'observation' require a
   counter_reading — the validator rejects them without one. Then run the generator
   (it regenerates the brief) and commit entry file + brief together.
4. **Gap-marking:** when the record is silent, write the silence (`none noted`,
   `undated in source`, "provenance untagged") — never a plausible fill.
5. **New pattern/observation with no matching key:** new entry file from an existing
   entry's shape + one manifest line in LIVE. Kinds: pattern / equipment / failure-mode /
   decision / theory. Grades (pattern/equipment/theory only): speculative / observation /
   directional / tested.
6. **Audit:** re-derive per entry from jar files — enumerate `wisdom/manifest.py`,
   fan out one worker per entry key with only that entry + its cited jars.

## Editing constraints for workers

- Do NOT edit YAML frontmatter `description:` fields unless they literally name
  HANDOFF_WISDOM.md; if you must touch one, keep it a single line, avoid ": " inside
  plain scalars (documented parser failure), and preserve the existing trigger language.
- Preserve dated rescope/history notes in skill bodies — update their file references,
  never delete the notes.
- Sweep by meaning as well as name: "wisdom table", "wisdom row", "cross-strain patterns
  table", "check the wisdom layer" are all references even without the filename.
  A "row" is now an "entry"; "the wisdom file" is now "the brief + entry files".
