# Wisdom Layer Replacement — Design
*Produced by a clean-context designer from the problem statement + seven verbatim samples. It did not read HANDOFF_WISDOM.md, the handoff notes, the backlog, or any skill file.*

## 0. Architecture choice

Two architectures were weighed:

- **A. Split markdown documents** — a hand-maintained always-read summary plus hand-maintained per-topic detail docs. Rejected: requirement 5 (no drift between layers) cannot be met for hand-maintained prose pairs except by discipline, and discipline-only rules have a documented failure record here. There is no cheap mechanical check that a markdown summary sentence still matches a markdown evidence essay.
- **B. Generated-from-data** — the house precedent, applied a second time. Wisdom entries become typed Python data in keyed files; the bounded always-read surface is *generated* from them by the existing generator, so summary/detail drift is structurally impossible; validators and a manifest preflight fail the build on structural mistakes. This is the same three-ingredient solution that already fixed unbounded growth for run data, and the jars prove the house is comfortable keeping long structured prose in Python string fields (`jars/sourtangie.py` is 33k chars of exactly that) — which also fixes the stated pain of 3,800-char essays living in markdown table cells.

**Committed: B.** Within B, sharding was weighed as one-file-per-topic-domain vs. one-file-per-entry. Committed: **one file per entry**, mirroring one-file-per-jar — it gives the smallest possible read for the frequent session-close edit, a trivially deterministic key→file rule, and reuses the row-split move (sample 3) as a file-split move when an entry gets heavy.

---

## 1. Artifact layout

```
wisdom_core.py            # dataclasses + validators + brief renderer (stable layer; rarely grows)
wisdom/
  manifest.py             # LIVE / COMPRESSED key lists + load_all_entries() with preflight
  entries/<key>.py        # one file per entry, exporting ENTRY (a WisdomEntry)
WISDOM_BRIEF.md           # GENERATED — the bounded unconditional read; committed, never hand-edited
```

`HANDOFF_WISDOM.md` is deleted (replaced by a 3-line tombstone for one release cycle pointing at `WISDOM_BRIEF.md` and `wisdom/entries/`, then removed).

### Schema (`wisdom_core.py`)

```python
@dataclass
class Citation:                      # one primary-data instance
    run: str                         # canonical key: "<jar-slug> R<n>", e.g. "fw106 R26"
    role: Literal['confirms', 'counters', 'context']
    gist: str                        # what happened, in the entry's own words (verbatim from
                                     #   migration where applicable) — length-unbounded
    confounds: str                   # per-instance confounds; "none noted" is explicit, "" invalid
    provenance: Literal['user-verbatim', 'ai-authored', 'mixed']
    provenance_note: str = ""        # which field the fact came from ("dab_notes", "analysis", ...)
    added: str = ""                  # session / date label
    struck: bool = False
    struck_note: str = ""            # REQUIRED when struck: date + why (validator-enforced)

@dataclass
class Position:                      # one dated prose paragraph — the append-log container
    stated: str                      # "Session 91", "July 6-7, 2026", ...
    text: str                        # full paragraph, length-unbounded
    status: Literal['current', 'superseded'] = 'current'
    superseded_note: str = ""        # REQUIRED when superseded ("Retired by WM R16: ...")

@dataclass
class WisdomEntry:
    key: str                         # == filename stem; lowercase-hyphen; never renamed
    kind: Literal['pattern', 'equipment', 'failure-mode', 'decision', 'theory']
    claim: str                       # <= 240 chars — the one-sentence position (brief-rendered)
    grade: Literal['speculative', 'low', 'directional', 'established']
    grade_basis: str                 # <= 200 chars — "2 runs one strain, plus an OC pair" (brief-rendered)
    guidance: str                    # <= 320 chars — what a session should do / not do / not
                                     #   re-litigate (brief-rendered)
    strains: list[str]               # jar slugs with evidence in this entry (brief-rendered)
    evidence: list[Citation]         # NOT brief-rendered; brief shows counts only
    positions: list[Position]        # NOT brief-rendered (dated analysis prose, supersession history)
    counter_reading: str = ""        # strongest alternative reading; REQUIRED for grade above 'low'
    watch_for: str = ""              # <= 200 chars — what evidence would move it (brief-rendered)
    first_observed: str = ""         # session ref
    updated: str = ""                # session refs, comma list
    resolution: str = ""             # <= 200 chars; REQUIRED for COMPRESSED entries — the one-liner
    split_from: str = ""             # lineage note when an entry was split from another key
```

Entry files import only `datetime` and `from wisdom_core import *` (preflight-enforced, mirroring the jar import rule). Entry keys are stable identity: created once, never renamed; splits create new keys with `split_from` lineage.

How the sample shapes land in this schema:

| Sample | Becomes |
|---|---|
| 1–3 (pattern rows) | one `kind='pattern'` entry each; every cited run → one `Citation` with role/confound/provenance; audit-strike brackets → `struck=True` + `struck_note`; the "Notes"/audit-narrative prose → `positions`; row-split history → `split_from` |
| 4 (rig config row) | `kind='equipment'` entry per rig-level claim; the run enumeration → `Citation`s; the "Observed Effect" narrative → `positions` |
| 5 (failure modes, two-tier) | live rows → LIVE `kind='failure-mode'` entries (mitigation in `guidance`); structurally-resolved one-liners → COMPRESSED entries whose `resolution` field is the one-liner (instance lists → citations; full prose stays in git as today) |
| 6 (settled rulings) | `kind='decision'` entries in LIVE; ruling → `claim`, "do not re-examine" → `guidance`, rationale → one `Position` |
| 7 (working-theory essay) | one `kind='theory'` entry (`curve-design-theory`); each dated paragraph → one `Position`, retired ones `status='superseded'` with the retirement note; current stance distilled into `claim` + `guidance` |

Cross-run *comparisons* (R26-vs-R28 pairs, gradients) go in `positions`; per-run facts go in `Citation.gist`. That keeps citations atomic and comparison narratives revisable.

### `wisdom/manifest.py`

```python
LIVE = [        # brief renders claim + grade + guidance + counts (~300-400 chars each)
    'harshness-threshold-crossing',
    'load-size-effects',
    'chest-harshness-hot-open',      # sample 3's row (A)
    ...
]
COMPRESSED = [  # brief renders resolution one-liner only (~100-140 chars each)
    'utc-date-as-run-date',
    'deploy-race-stale-site',
    ...
]
```

The compression move is the close-jar move: relocate a key LIVE→COMPRESSED, set `resolution`, entry file otherwise untouched, zero information loss. `load_all_entries()` runs a preflight (below) then imports every entry.

### `WISDOM_BRIEF.md` (generated)

Structure, top to bottom:

1. Header: "GENERATED — never hand-edit; regenerate with `python3 Dabby_Log_Generator.py`. Detail rule: anything more than what is on this page → Read `wisdom/entries/<key>.py`."
2. **Live entries**, grouped by kind (patterns; equipment; failure modes; decisions; theory). One block per entry:

   ```
   ### load-size-effects  [pattern | low]
   Claim: Larger load tracks earlier/more harshness or intensity; direction split across strains, unresolved.
   Basis: 6 strains — 4 confirm (wwz, lhbh, fw106, bp4rw13), 2 counter (bb362, hive1); no clean pair.
   Guidance: Do not treat load size as a settled harshness driver. State load class out loud at logging so it lands in dab_notes verbatim.
   Watch: a load-contrast pair that is session-order matched with user-verbatim load classes on both sides.
   Evidence: 9 citations (6 confirm / 2 counter / 1 struck) | strains: wwz, lhbh, fw106, bp4rw13, bb362, hive1 | upd S138 | detail: wisdom/entries/load-size-effects.py
   ```

   Every rendered field is either hard-capped (`claim`, `guidance`, `grade_basis`, `watch_for`) or derived (counts, strain list, pointer). No instance content ever renders here.
3. **Compressed entries** — one line each: `resolution` + pointer.
4. **Session-close checklist** (the Q1–Q6 questions) — moved here as a constant in `wisdom_core.py`, rendered as the brief's footer. Rationale: it is the instruction set for updating exactly this layer, it must survive `HANDOFF_WISDOM.md`'s deletion, and embedding it in the generated surface keeps it versioned in code and inside the size budget (~1k chars).

### Size budget (requirement 1 — proposed and justified)

- **Hard cap: 20,000 chars, build-failing.** Worst-case composition: 40 LIVE entries × ~400 chars + 30 COMPRESSED × ~120 chars + headers/checklist ~1.5k ≈ 20k. At the current density (~2.7 chars/token in this corpus) that is ~7.5k tokens — a single Read with >3× headroom under the 25k cap under either (chars or tokens) reading of the cap, and it cuts wisdom's share of session-open cost from ~31k tokens to ~7k.
- **Soft warn: 16,000 chars**, and **warn when `len(LIVE) > 40`** — the pressure valve is named in the warning text: merge overlapping entries or compress settled ones.
- The cap cannot be inflated by instance growth: instances are structurally absent from the brief. It can only grow with entry count and capped-field length, both validator-bounded.

---

## 2. Read policy per consumer moment

All triggers are mechanical — a condition a fresh session can evaluate without judgment.

| Moment | What is read | Deterministic trigger |
|---|---|---|
| **Session open, any type** | `WISDOM_BRIEF.md` only (one Read, ≤20k chars). Nothing under `wisdom/entries/` | CLAUDE.md session-start gate names `WISDOM_BRIEF.md` in place of `HANDOFF_WISDOM.md`. The brief carries claims, confidence grades, live hazards (`failure-mode` guidance lines), and settled rulings — the "don't hallucinate / re-derive / re-litigate" payload — with zero instance detail |
| **Drafting per-run analysis** | Brief (already in context) for claims/confidence/guidance; `wisdom/entries/<key>.py` for any entry the draft engages | Rule, written into the log-run and analysis-toolkit skills: *before finalizing a draft, list every entry key the draft cites, compares against, or would change; Read each key's entry file first.* Keys are visible in the brief; file path is derived (`wisdom/entries/<key>.py`). Instance-level claims ("R26 vs R28 same curve") may only be written from an entry file or a jar file, never from the brief |
| **Session-close edits** | The touched entry's file(s), full | *Editing entry K → Read `wisdom/entries/K.py` first.* This is not merely a rule: the Edit tool refuses to edit an unread file, so the trigger is harness-enforced. New-pattern case: no matching key in the brief → create a new entry file + manifest line (boilerplate below) |
| **Confidence promotion** | The entry's file, full | Changing `grade` is an edit → same read-before-edit trigger. The *stated counter-reading* requirement is validator-enforced: `grade` above `'low'` with empty `counter_reading` fails the build, so a promotion physically cannot land without one |
| **Full audit** | `wisdom/entries/*.py` (glob) + jar files | wisdom-audit skill: enumerate manifest, fan out per entry. Per-entry sharding makes the orchestrator/worker split natural — one worker per entry with only that entry + its cited jars in context |

---

## 3. Session-close edit workflow

Routine case — a run tonight bears on `load-size-effects`:

1. Read `wisdom/entries/load-size-effects.py` (~4–8k chars; one Read).
2. Edit: append one `Citation(run='sourtangie R8', role='confirms', gist=..., confounds=..., provenance='user-verbatim', added='Session 163')`; if the position shifted, append a dated `Position` and/or update `claim`/`guidance`/`grade_basis` in place; update `updated`.
3. Run `python3 Dabby_Log_Generator.py` — already the mandatory close step. It re-validates everything and rewrites `WISDOM_BRIEF.md` alongside `HANDOFF_STATE.md` and `index.html`.
4. Commit entry file + regenerated brief to the session's existing feature branch, same PR as the run.

Why it stays cheap: one small keyed file per touched entry; the edit is an append of a typed literal (same muscle as adding a `CompletedRun`); the summary updates itself; no cross-file coordination; the generator run and PR were happening anyway, so the wisdom edit adds zero new ceremony. New entry = copy boilerplate + one manifest line, exactly the new-jar two-file pattern the preflight already knows how to police.

---

## 4. Enforcement spec

**Where:** `wisdom/manifest.py` preflight (pre-import, mirrors jar preflight) + `wisdom_core.validate_wisdom(entries, jar_runs)` called from `build_html()` next to the existing `validate()`. **When:** every generator run — i.e., every run-logging session, every handoff close, and every CI run (`preview.yml` on every PR, `deploy.yml` on every push to main). **How failure surfaces:** `WISDOM ERRORS:` block printed, `SystemExit(1)` — a bad edit fails the generate step locally and turns the PR preview / deploy red, identical to `VALIDATION ERRORS:` today.

Preflight (before import):

- LIVE/COMPRESSED: no duplicate keys; every key has `wisdom/entries/<key>.py`; no orphan entry files; entry files import only `datetime` / `wisdom_core`; curly-quote contamination signature check (same bug class as jars).

Semantic validation (after import; jars are already loaded, so this is free):

- `ENTRY.key` == filename stem == manifest key.
- **Citation integrity:** every `Citation.run` parses as `<slug> R<n>`, slug exists in `jar_manifest`, and `n <= len(RUNS)` for that jar — hallucinated or stale citations fail the build. This is the summary↔primary-data drift check.
- **Provenance:** typed field, so untagged citations are unrepresentable; `struck` ⇒ non-empty `struck_note`; `confounds` non-empty (explicit "none noted" required).
- **Supersession:** `Position.status=='superseded'` ⇒ non-empty `superseded_note`; every LIVE non-decision entry has ≥1 `current` position or empty positions.
- **Promotion gate:** `grade` above `'low'` ⇒ non-empty `counter_reading`, and for `kind='pattern'` ≥2 unstruck confirming citations spanning ≥2 slugs.
- **Field caps:** `claim` ≤240, `guidance` ≤320, `grade_basis` ≤200, `watch_for` ≤200, `resolution` ≤200 chars. These are the structural bound on the brief.
- **COMPRESSED** ⇒ non-empty `resolution`.
- **Brief size:** rendered brief >20,000 chars ⇒ error; >16,000 ⇒ warning; `len(LIVE) > 40` ⇒ warning naming the compression/merge moves.
- **Entry-file size:** any entry file >20k chars ⇒ warning naming the two pressure valves (split the entry — the sample-3 move, now a file+manifest operation with `split_from` lineage — or compact fully-superseded positions to git with a pointer note).
- **Stale-brief guard:** `deploy.yml` and `preview.yml` add `git diff --exit-code WISDOM_BRIEF.md` after generating — a committed brief that doesn't match its sources fails CI.

"Impossible to miss for ten days": the check runs on every generator invocation and every push. The July regrowth went unnoticed because nothing executed a size check; here the surface is generated under a hard cap, so regrowth beyond budget cannot even be *written*, let alone go unnoticed.

---

## 5. Migration plan

One migration branch; wisdom-edit freeze while it is open (runs can still be logged — run logging doesn't touch the wisdom file).

1. **Infrastructure first** (reviewable independently of content): `wisdom_core.py`, `wisdom/manifest.py`, entry boilerplate, generator hook, CI diff guard, validator suite. Verify with two hand-built entries.
2. **Transposition, not condensation.** Each current row/section becomes one entry file. Evidence prose is *moved verbatim* into `Citation.gist` / `Position.text` — the migration deliberately minimizes judgment: parsing a cell into citations is mechanical re-containering; rewriting its prose is not attempted. `claim` / `guidance` / `grade_basis` / `watch_for` are the only newly authored text (distillations of what each row's Pattern/Confidence/Notes columns already say).
3. **Tier assignment:** current "structurally resolved" one-liners → COMPRESSED (one-liner → `resolution`, cited instances → citations); everything live → LIVE.
4. **Generate; check budget.** If the initial brief exceeds 16k, the fix is tier moves and tighter capped fields — never deletion of detail.
5. **Clean-context adversarial diff review (requirement 8, mandatory):** a fresh-context reviewer receives the pre-migration `HANDOFF_WISDOM.md` and the new `wisdom/` tree, and verifies per entry: every run citation present with role preserved (confirm/counter/struck); every confound and provenance tag survived; every dated paragraph and retirement note survived with correct status; no citation invented; `claim`/`guidance` distillations don't overstate confidence (epistemic-flags check). Findings → user triage → fixes on the branch.
6. **Same-PR surface updates:** everything in section 6, plus delete `HANDOFF_WISDOM.md` (tombstone) and commit the first `WISDOM_BRIEF.md`.
7. **Merge via normal PR flow**; preview URL sanity check; post-merge the caps and CI guards are live.

---

## 6. Touched-surfaces list (requirement 7)

Sweep method: literal grep for `HANDOFF_WISDOM` **and** a meaning-level pass reading every skill and doc for conceptual references ("the wisdom layer", "cross-strain patterns", "accumulated patterns", "check wisdom first") — the known hazard is precisely that greps miss these.

1. **Project instructions file (CLAUDE.md)** — session-start gate (mandatory read #2 → `WISDOM_BRIEF.md`); the "Updating the Log" paragraph directing analysis-writers to check the wisdom layer and when to open closed jars; the session-close/handoff paragraph ("run the checklist in HANDOFF_WISDOM.md" → checklist's new home in the brief footer); the Architecture and Conditional Reads sections (add `wisdom/`, `wisdom_core.py`, `WISDOM_BRIEF.md` and the never-hand-edit rule).
2. **dab skill** (session-open ritual) — its mandatory-read sequence names the wisdom file; retarget to the brief.
3. **log-run skill** (analysis drafting + PR pipeline) — wisdom-consult step retargeted; add the deterministic detail-open rule (any entry cited/compared/changed → Read its file); session-close wisdom-update step now edits entry files.
4. **analysis-toolkit skill** — states the wisdom layer as a primary input to drafting; recipes that say "check the wisdom table for X" must reference brief-then-entry-file.
5. **wisdom-audit skill** — the deepest change: audits per-entry files instead of one document; its row-change proposal format becomes entry-diff format; its orchestrator/worker fan-out keys off the manifest.
6. **Session-close checklist (Q1–Q6)** — currently lives at the top of the artifact under redesign; moves into `wisdom_core.py` as the brief-footer constant (see §1).
7. **change-baseline skill** — references the wisdom failure-mode entry about changing `BASELINE_CURVE`; update pointer to the entry key.
8. **jar_manifest.py error strings** — two preflight messages literally say "see HANDOFF_WISDOM.md failure modes" (lines 97 and 108–110); repoint to `WISDOM_BRIEF.md` / entry keys. (Code, not docs — a doc-only sweep would miss it.)
9. **Dabby_Log_Generator.py** — brief generation + `validate_wisdom()` call.
10. **Dabby_Handoff_Notes.md** — cross-references (the failure-modes section explicitly cross-points between the two files; "Known Claude Failure Modes" boundary note must name the new home).
11. **Dabby_Methodology.md** — curve-design theory content overlaps sample 7's essay; any pointer into wisdom sections needs retargeting to `curve-design-theory`.
12. **BACKLOG.md** — items about wisdom consolidation/regrowth (this design resolves or reframes them) and the run-facts dump script item referenced by the audit decision entry.
13. **.claude/skills/README.md** — catalog and handoff-graph descriptions that name the wisdom layer.
14. **deploy.yml / preview.yml** — add the `git diff --exit-code WISDOM_BRIEF.md` stale-brief guard; no other change (they already run the generator).
15. **audit/ snapshots and correct-frozen-data / close-jar / new-jar skills** — frozen audit artifacts are not edited (frozen by design); the three skills get the meaning-level sweep — expected touches are pointer-only where their handoff prose names the wisdom file.

---

## 7. Regrowth answer, per mechanism

**1. Citation accretion.** Next instance = one `Citation` appended inside the entry's own file. The unconditional surface renders *counts derived from* the list, never the list — brief size is mathematically invariant to instance count. Entry-file growth is legitimate and absorbed; the 20k per-file warning names the pressure valve (entry split with `split_from` lineage — the sample-3 row-split, promoted to a first-class manifest operation), and even the heaviest current entry (~4k chars of evidence) has ~5× headroom before the warning fires.

**2. Provenance layer.** Accommodated, not trimmed: provenance is a typed *required* field on every citation, so the July audit's fix becomes unrepresentable to omit — no future audit pass ever needs to bolt it on again. Its weight (~40 chars/instance) lands entirely in conditional-read files; the unconditional surface carries zero provenance bytes. Bound: same as mechanism 1 — the brief never renders citations.

**3. Append-log prose.** Next dated paragraph = one `Position` appended in the entry's file. The brief renders only `claim` and `guidance` — replace-in-place fields with hard character caps — so accretion is structurally severed from the unconditional surface: a theory can accrete fifty dated paragraphs and the brief's cost for it stays ≤ ~600 chars. When an entry's positions push its file toward 20k, the warning offers position-compaction-to-git (allowed loss-to-git move) or entry split.

**4. Supersede-in-place.** Retiring a framing = flip its `Position` to `superseded` + required note (or `struck=True` + note on a citation); the full retired text stays in the entry file — zero loss — and the brief, which renders only current-status fields, *shrinks or holds* on supersession rather than growing. Whole-entry retirement = manifest move LIVE→COMPRESSED (one `resolution` line in the brief, full history untouched in the entry file). Bound on the unconditional surface overall: it is generated-only from capped and derived fields, hard-fails above 20k chars, warns at 16k and at 40 LIVE entries, and is CI-diffed against its sources on every push — so the failure mode that let 20k chars regrow unnoticed in ten days now cannot survive a single generator run.
