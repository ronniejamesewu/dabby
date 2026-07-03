# Project Audit — July 3, 2026

One-time whole-project audit per `AUDIT_CHARTER.md` (Session 144; charter
deleted in this PR — its scope decisions are summarized in the preamble below,
same disposal pattern as `DABBY_ARCHITECTURE.md`, Session 109). Executed in a
fresh frontier-class session that did not author the July 3 changes.

**This report records findings; it fixes nothing.** Each finding becomes a
backlog item or PR only after user review.

---

## Preamble — method actually followed

**Charter scope, in one paragraph:** the audit covered the four code files
(`Dabby_Core.py`, `Dabby_Log_Generator.py`, `pending_dab.py`,
`jar_manifest.py`), the three skills plus the lineage reference, the prose docs
(`CLAUDE.md`, `Dabby_Handoff_Notes.md`, `HANDOFF_WISDOM.md` both pages,
`Dabby_Methodology.md`, `Dabby_UI_Principles.md`, `DESIGN_BRIEF.md`,
`jar_return_check.md`, `switch2_thermal_model.md`,
`register_leak_diagnostic_exercise.md`), the three workflows, and a light
scope-2 pass on `style.css`. Out of scope: generated outputs (`index.html`,
`HANDOFF_STATE.md` — the generator was audited instead), full prose reads of
`jars/*.py` (spot-checked only where a finding demanded it), git history, and
`register_leak_diagnostic_answer.md` (never opened — the blinded exercise
stays intact).

Method, in charter order: session open per `CLAUDE.md` (all three mandatory
reads, wisdom paged to the end) → built `citecheck.py` → full fresh read of
the corpus → scope 2 (prose vs. reality) → scope 1 (mechanization sweep) →
this report.

**Deviations from the charter:**
- Shipped on the harness-designated branch (`claude/audit-charter-4kios9`)
  rather than a hand-named `project-audit` branch — same effect, one branch.
- `style.css` pass was targeted greps against the doc claims about it (no
  green anywhere; oklch tokens; `--action` = `oklch(46% 0.095 38)`) rather
  than a line-by-line read. All claims verified.
- Jar spot-checks: `dbrb`, `watermellos` (R9), `fw106`/`bb364` (June 17
  timestamps), plus grep sweeps across all jars for `BASELINE_CURVE`
  references. Each was demanded by a specific finding, per the charter's
  spot-check rule.
- The charter's optional step 7 (adversarial verification agent) was left as
  written — user decides at PR time.

**Citation-checker summary (`citecheck.py`, committed in this PR):**
- **Run citations: 287 checked, 0 unresolved.** Every short-form citation in
  `HANDOFF_WISDOM.md` / `Dabby_Handoff_Notes.md` / `Dabby_Methodology.md`
  (`FW106 R26`, `WM R16–18`, `BB36 #2 R4`, `Hive1 R2-5`, `CAG Run 1`, …)
  resolves to a real jar and a run number within that jar's `len(RUNS)`. The
  wisdom layer's evidence trail is fully sound. (The checker's alias table is
  derived from `jar_manifest.py`'s inline comments, with a tiny hand-seeded
  irregular set — `WM`, `BB36 #N` — documented in the script. Negative tests
  confirmed it flags out-of-range citations.)
- **Filenames: 268 checked, 6 to triage — all dispositioned benign:**
  `Dabby_Data.py` (wisdom:73) and `DABBY_ARCHITECTURE.md` (wisdom:96) are
  deliberate historical references in failure-mode/decision rows;
  `yes-but-why-not-hazy-hippo.md` / `sprightly-churning-moonbeam.md`
  (notes:271) are named as retired design docs; `AUDIT.md` (notes:324, twice)
  is the future artifact this PR creates.
- **Identifiers: 144 checked, 3 to triage — all dispositioned benign:**
  `_check_dormancy` / `load_active_jars` (notes:153) are named *as deleted* in
  the Session 112 decision row; `BASELINE_420` (notes:304) is a
  planned-but-unbuilt constant the backlog item itself says must be defined
  first.

The checker also directly serves pass 3's guardrail 2 ("every citation dropped
from wisdom must be verifiable") — that was a design requirement of the
charter, now met.

---

## Scope 2 — stale, contradictory, or confusing prose (ranked)

Severity labels: **contradiction** (two sources disagree), **stale** (describes
a world that no longer exists), **confusing** (true but structured to mislead a
fresh session).

### S2-1. CONTRADICTION — the BASELINE_CURVE-change protocol's grep discriminator is wrong; following it verbatim corrupts three STATUS blocks

`HANDOFF_WISDOM.md:74` (failure-mode row, the protocol future sessions are told
to follow when the baseline changes):

> "(2) Grep `jars/*.py` for `waypoints=BASELINE_CURVE,` (with trailing comma)
> and replace_all with `waypoints=BASELINE_XXX,` — **the comma distinguishes
> these from `next_waypoints=BASELINE_CURVE` in a jar's STATUS**, which
> correctly points to the new baseline and must not be changed."

The comma does not distinguish them. STATUS blocks are dataclass kwargs — their
`next_waypoints` lines also end in a comma. On disk right now:

- `jars/bb364.py`, `jars/dbrb.py`, `jars/lhbh.py` each contain
  `next_waypoints=BASELINE_CURVE,` (trailing comma present).

A replace_all on the string `waypoints=BASELINE_CURVE,` matches *inside*
`next_waypoints=BASELINE_CURVE,` and would rewrite all three to
`next_waypoints=BASELINE_XXX,` — pinning current what-to-try-next guidance to
the retired curve, silently, which is precisely the corruption class this
protocol exists to prevent. The safe discriminator is anchoring on the field
name (`grep -n '^\s*waypoints=BASELINE_CURVE,'` — 10 hits today, all
run-level) or editing with the leading whitespace/field boundary included.
This row is the project's booby-trapped fire extinguisher: it only fires when
the baseline changes, and when it fires it damages exactly what it promises to
protect. See S1-4 for the mechanization that retires the manual protocol
entirely.

### S2-2. CONTRADICTION — the session-close checklist has seven questions; three other places say six

`HANDOFF_WISDOM.md:10–16` lists **Q1–Q7** (Q7, jar-close manifest check, added
with the two-tier lifecycle work). But:

- `CLAUDE.md:160`: "Run the checklist in `HANDOFF_WISDOM.md` (**six questions**
  at the top)"
- `Dabby_Handoff_Notes.md:224` (Session 145 failure-mode entry): "when any of
  the **six questions** plainly resolves to 'yes' mid-session"
- `Dabby_Handoff_Notes.md:304` (skill-library backlog, item 2): "harness for
  the **six-question checklist** at the top of `HANDOFF_WISDOM.md`"

A fresh session told "six questions" that runs Q1–Q6 and stops skips exactly
the question (Q7) whose row says "this is not enforced structurally." The
count should live in one place — or nowhere ("the checklist at the top of
`HANDOFF_WISDOM.md`", no number, survives future additions).

### S2-3. CONTRADICTION — Methodology's terpene table disagrees with `TERPENE_REFERENCE`; Caryophyllene is off by 227°F

`Dabby_Methodology.md:62`:

> "| Caryophyllene | 266°F / 130°C |"

`Dabby_Core.py:265`:

> `TerpeneEntry(name="Caryophyllene", ..., bp_f=493, bp_c=256, band="High", ...)`

Both render publicly (the Methodology table in the doc, `TERPENE_REFERENCE` on
the log's Terpene Reference block). 266°F/130°C is the widely-copied internet
value generally regarded as an error; Core's 493°F/256°C is consistent with the
literature. The same duplicated table also drifts on minor rows (Alpha-Pinene
311 vs 313°F, Myrcene 334 vs 333°F, Terpinolene 367 vs 369°F). Whichever
number is right, two in-repo sources of truth disagree — a fresh session doing
boiling-point reasoning gets a different answer depending on which file it
read. Mechanization companion: S1-3.

### S2-4. STALE — Methodology §2 still says sapphire is "not yet acquired"

`Dabby_Methodology.md:25`:

> "| Property | Quartz **(current)** | Sapphire **(not yet acquired)** |"

Sapphire has been the working insert since May 22, 2026 (Rig 3), and every rig
since Rig 3 is sapphire — `HANDOFF_STATE.md`'s most-recent-run line shows Rig 6
(Sapphire Plus v2). The same document's §5 already reasons from Rig 6 sapphire
descent runs (`Dabby_Methodology.md:127`), so §2 contradicts §5 within one
file. A fresh session reading §2 first would believe the project is
quartz-current and discount every sapphire-specific position.

### S2-5. CONTRADICTION — `switch2_thermal_model.md` claims the sapphire descent lag was "empirically observed on Rig 5"; the underlying run says "assumed," and the wisdom layer says no descent run exists on Rig 5

`switch2_thermal_model.md:207`:

> "Sapphire's higher heat capacity … making descent slower relative to the
> programmed curve. **This has been empirically observed on Rig 5.**"

The only Rig 5 descent-mode data point is Watermellos R9, whose own waypoint
note (`jars/watermellos.py:14`) reads "Endpoint — **assumed** ~1°F/sec cooling
(**device rate unmeasured**)" and whose frozen analysis repeats "cooling rate
assumed, not measured." Meanwhile `HANDOFF_WISDOM.md:255` states: "after the
equipment correction, **no descent run has actually been logged on Rig 5**"
(WM R9 was a passive-decay-shaped curve, not the programmed-descent-vs-lag
comparison the thermal model describes). The thermal model was written as a
review request for an external physics check — an overclaimed empirical anchor
is exactly what such a review would build on. Should say "consistent with the
assumed ~1°F/sec passive rate inferred on Rig 5 (WM R9, rate not measured)."

### S2-6. CONTRADICTION — the rendered 🔥 first-of-day marker is assigned by manifest order, not chronology; it is wrong on the live page today

`Dabby_Log_Generator.py:627–632`:

```python
_first_of_day = set()
for _r in COMPLETED_RUNS:
    if _r.run_date is not None and _r.run_date not in _seen_dates:
        _first_of_day.add(id(_r))
```

`COMPLETED_RUNS` is manifest-ordered, not chronological — the exact recency
trap `Dabby_Handoff_Notes.md:114` warns about ("never `COMPLETED_RUNS` list
position (it's manifest-ordered, not chronological — the Session 140 failure
mode)"). Reproducing the loop against the data: **2 of 59 flame dates are
wrong** —

- **May 11, 2026**: flame renders on Maple Bacon Donut R3, whose own
  `sessions_prior_today=2`; the actual first dab was Rain Fruit R2
  (`sessions_prior_today=0`).
- **June 17, 2026**: flame renders on Blueberry 36 #4 R1
  (`sessions_prior_today=1`, logged 11:38pm MDT); the actual first dab was
  Fire Water #106 R20 (`sessions_prior_today=0`, logged 6:47pm MDT).

The data already carries the answer twice over (`sessions_prior_today` is
validator-cross-checked; `utc_logged_at` orders the day) — the renderer just
doesn't use it. Fix is S1-1. Note the dashboard's "avg first dab of the day"
stat in the *same file* computes day-firsts correctly by `utc_logged_at`
(`Dabby_Log_Generator.py:169–172`) — the two code paths disagree.

### S2-7. CONFUSING/CONTRADICTION — a zero-run ACTIVE jar (dbrb) is invisible to both HANDOFF_STATE and the strain browser

`jars/dbrb.py` (Donny Burger + Rainbow Belts) is in `ACTIVE`
(`jar_manifest.py:24`) with `RUNS = []`. Two filters hide it:

- `Dabby_Log_Generator.py:689`: `active_strains = [ss for ss in STRAIN_STATUS
  if run_counts.get(ss.name, 0) > 0]` — so `HANDOFF_STATE.md` has **no dbrb
  section at all**: no "Next run: 1" line (which `log-run` step 2 says is the
  sole source for the run number), no baseline plan, no mention. The summary
  line "Total runs: 132 across 17 strains" counts strains-with-runs while 18
  jars exist — a fresh session inventorying jars from the state file misses
  one.
- `Dabby_Log_Generator.py:187–190`: the strain browser applies the same
  `> 0` filter — but `Dabby_UI_Principles.md:40` requires "**a list of all
  strains** with last-run recency and next-step preview," and §9 makes the
  browser the *only* navigation surface. dbrb's profile section *is* rendered
  in `index.html` (the strain-section loop iterates all of `STRAIN_STATUS`),
  so the page contains a section that its sole navigation system cannot
  reach.

The jar was created June-2026-era and simply hasn't had its first run — this
is the normal state every future new jar passes through. Fix is S1-2.

### S2-8. CONTRADICTION — strain browser sort order does not match `Dabby_UI_Principles.md`

`Dabby_UI_Principles.md:41`:

> "Sort order: active strains by run count descending; **closed jars follow
> with closed framing**"

`Dabby_Log_Generator.py:187–190` sorts *everything with runs* by run count
descending, no tier partition — so WW Z (closed, 9 runs) renders above
Papaya + Z Pie #22 (active, 7), Lemon Heads + Blueberry Haze (active, 7),
Blueberry 36 #2 (active, 6), and five more active jars. Either the generator
should partition (active desc, then closed) or the UI doc should bless the
interleave — report only; the user picks the direction.

### S2-9. STALE — the rendered Baseline Curve rationale says "seven strains"; the wisdom row it summarizes says eight

`Dabby_Log_Generator.py:617` (hardcoded prose on the public page):

> "420°F endpoint sits below the cross-strain harshness boundary (≥430°F
> produced tail harshness on **seven strains**)"

`HANDOFF_WISDOM.md:28` (the evidence row): "High — **8 strains**, consistent
across both ramp and flat-hold curve shapes" (OC, Hive1, Fembot3, MB9ZST, RF,
MBD, BB36#1, FW106). The generator prose predates FW106 R5's addition to the
row. A count in hardcoded prose will drift again — either drop the number
("multiple strains") or accept it as a hand-maintained fact; it is not
mechanizable because the source is a prose evidence cell.

### S2-10. STALE — `DESIGN_BRIEF.md` says four reference sections; there are five

`DESIGN_BRIEF.md:36`:

> "The **four** reference sections (Device Constants, Swab Color Reference,
> Baseline Curve, Terpene Reference) live as collapsible blocks…"

`CLAUDE.md` (Reference Sections): "The **five** reference sections (Device &
Session Constants, Swab Color Reference, Baseline Curve, Terpene Reference,
**Rig Reference**)…" — and the generator renders five. The brief predates the
Rig Reference block; a design agent briefed from it would omit a section.
(Same doc's "14+ strains across 88+ runs" at `DESIGN_BRIEF.md:5` is
floor-phrased and technically still true — noted, not a finding.)

### S2-11. CONFUSING — Methodology §5's offset paragraph still argues for the staged mid-climb the project retired

`Dabby_Methodology.md:123`:

> "A slowly-arrived-at lower endpoint delivers more heat to the material than
> a steeply-arrived-at higher endpoint… **This is the rationale for preferring
> a steeper mid-climb with a flatter tail over a uniformly steep ascent to a
> higher endpoint.**"

`HANDOFF_WISDOM.md:247` (Curve Design Working Theory): "**No intermediate
ascent waypoints needed** … Staged waypoints on the ascent only slow the climb
below what the device would naturally do — they are not a design feature, they
are a drag." The current baseline is an 8-second near-max-rate ramp. The §5
physics (offset closes on flat tails) is still believed — it's the concluding
*preference* sentence that describes a retired curve-design position. A fresh
session doing curve design from Methodology alone would design staged ascents.

### S2-12. STALE (KNOWN ITEM, confirmed) — `CLAUDE.md`'s date/time protocol hardcodes UTC−6 and hand-derivation; the mechanical layer already does this DST-aware

`CLAUDE.md:120` ("America/Denver (MDT, UTC-6)"), `:124` ("subtracting 6 hours
(MDT) from UTC"), `:129` ("(UTC−6)") — all hardcode the summer offset.
`Dabby_Core.py`'s `denver_local()` handles MDT/MST correctly, and
`pending_dab.py consume` prints the paste-ready date lines so the subtraction
never happens by hand. The prose becomes actively wrong on November 1
(US DST end) — a session following CLAUDE.md literally instead of the skills
would log UTC−6 dates in MST. This is the already-backlogged "CLAUDE.md
integration pass" (skill-library item 6) — confirmed still real, and the
DST rollover gives it a deadline it didn't have before.

### S2-13. STALE (trivial) — "closed + paused + active" survives in two places; PAUSED was retired Session 112

`Dabby_Core.py:308` (comment in `_resolve_accent_colors`): "The generator
passes the combined (closed + **paused** + active) status list…" and
`Dabby_Handoff_Notes.md:139` (decision row): "…returns the combined (closed +
**paused** + active) list…" — vs. the Session 112 decision two screens later:
"Three-tier lifecycle (ACTIVE/PAUSED/CLOSED) collapsed to two." Word-level
staleness only; nothing behaves wrong.

### S2-14. CONFUSING (minor) — Methodology §6 calls the swab "the empirical ground truth"; the settled position is floor-indicator-only

`Dabby_Methodology.md:141`: "**Swab result is the empirical ground truth.**"
vs. `HANDOFF_WISDOM.md:30` (High-confidence row): "Swab is a **floor
indicator, not a fine-grained calibration metric** … session character is the
operative signal," and Methodology's own §4 limits ("Do not over-interpret
clean swabs as fine-grained efficiency data"). "Ground truth" is defensible
for what §6 meant (empirics over terpene theory) but reads as a promotion of
the swab above session character — the opposite of the current position.
One-clause fix ("Swab and session character are the empirical ground truth").

### S2-15. STALE (count drift) — `log-run` step 6 says "the 8 existing `waypoints=BASELINE_CURVE,` references"; there are 10

`.claude/skills/log-run/SKILL.md:200`: "the **8 existing**
`waypoints=BASELINE_CURVE,` references in older jars don't read as
contradiction" — field-anchored grep finds **10** run-level references across
5 jars (bb364 1, bp4rw13 1, hive1 3, lhbh 4, papzp22 1); Hive #1 R9–R10 added
two since the skill was written, despite the same step telling new runs to
define local constants. Two readings, both worth having: the count is stale,
and the instruction isn't fully holding (see S1-4 — the preflight ban is the
fix with teeth). The backlog's "~8–10 across ~6 jars" estimate
(`Dabby_Handoff_Notes.md:304`) remains accurate.

---

## Scope 1 — mechanization opportunities (ranked)

Format per the charter: failure prevented (has it occurred?) / mechanism /
precedent / build cost.

### S1-1. Derive the 🔥 first-of-day marker from the data, not list position — **S**

- **Failure prevented:** wrong first-of-day attribution on the public log.
  **Occurred:** yes, live today on 2 of 59 dates (S2-6).
- **Mechanism:** in `build_html()`, mark first-of-day where
  `run.sessions_prior_today == 0` (validator-guaranteed correct), falling back
  to min-`utc_logged_at`-per-date for the handful of `None` entries. Delete
  the manifest-order loop.
- **Precedent:** the Session 140 fix itself — `HANDOFF_STATE.md`'s generated
  most-recent-run line replaced list-position recency; this is the same bug
  class inside the generator. The same file already does it right for the
  dashboard's avg-first-dab stat.
- **Cost:** S (a few lines).

### S1-2. Render zero-run ACTIVE jars in `HANDOFF_STATE.md` and the strain browser — **S**

- **Failure prevented:** a jar that exists but is invisible to the session
  working surface and to page navigation (S2-7). **Occurred:** yes — dbrb is
  invisible right now; `log-run` step 2's "take the run number from
  HANDOFF_STATE's `Next run: N`" has no line to read for a first run.
- **Mechanism:** in `generate_handoff_state()`, include ACTIVE jars with zero
  runs (header + "No runs yet — start from baseline curve" from `next_text`,
  "Next run: 1"); in `dashboard_html()`, include them in the browser with a
  "no runs yet" meta line (sorted last among active). Optionally reword the
  summary line to "132 runs across 17 strains (18 jars)".
- **Precedent:** generated facts replacing recall — the same pattern as the
  most-recent-run line and the canonical-baseline line.
- **Cost:** S.

### S1-3. Single source of truth for terpene boiling points — **S**

- **Failure prevented:** two public artifacts disagreeing on a reference
  number. **Occurred:** yes — 266°F vs 493°F for Caryophyllene (S2-3).
- **Mechanism:** delete the duplicated table from `Dabby_Methodology.md` §4
  and point at the rendered Terpene Reference / `TERPENE_REFERENCE` in
  `Dabby_Core.py` (the project's data-lives-in-code direction). Generating
  the markdown table from Core is possible but overkill for a doc that
  changes never — deletion is the honest fix. (Which of the two Caryophyllene
  values is correct should be settled explicitly in that PR; Core's 493°F is
  the defensible one.)
- **Precedent:** `terpene_table_rows` removal (Session 71) — per-strain
  terpene tables were already deleted for epistemic reasons; this is the
  cross-doc version.
- **Cost:** S.

### S1-4. BASELINE_CURVE-in-RUNS preflight ban (known item 4) — validated, priority raised — **M**

- **Failure prevented:** silent rewriting of historical curves when
  `BASELINE_CURVE` changes (commit d5ab834 class). **Occurred:** yes,
  historically (d5ab834) — and this audit found the documented manual
  protocol that currently guards it is itself defective (S2-1: the comma
  discriminator corrupts three STATUS blocks if followed verbatim).
- **Mechanism:** as specified in the backlog (`Dabby_Handoff_Notes.md:304`):
  define frozen `BASELINE_420`, migrate the 10 run-level references
  (field-anchored grep `^\s*waypoints=BASELINE_CURVE,` — **not** the
  comma-only grep), then add a manifest-preflight rule rejecting
  `waypoints=BASELINE_CURVE,` at run level in jar files.
- **Precedent:** manifest preflight already rejects disallowed imports and
  curly-quote contamination — same hook, same failure-fast shape.
- **Cost:** M (10 references across 5 jars + one preflight rule + retiring
  the S2-1 protocol row down to "handled structurally").
- **Note:** until this ships, S2-1's row should at minimum have its grep
  corrected — that's a one-line doc fix with real teeth.

### S1-5. Footer date on the public page: derive from Denver time, not the CI runner's UTC clock — **S**

- **Failure prevented:** "Document last updated: <tomorrow>" on the public
  log. **Occurred:** almost certainly, silently — `deploy.yml` regenerates in
  a UTC runner (`Dabby_Log_Generator.py:643` uses bare `datetime.now()`), so
  any merge after ~6pm Denver stamps the next calendar day. This is the
  project's flagship failure mode (UTC rollover) living on the deploy path.
- **Mechanism:** `denver_local(datetime.now(timezone.utc))` — the helper
  already exists in `Dabby_Core.py`.
- **Precedent:** the `validate()` UTC-rollover rejection; `pending_dab.py`'s
  display-form dates.
- **Cost:** S (one line).

### S1-6. Dashboard time-of-day stats: use `denver_local`, not a hardcoded UTC−6 — **S**

- **Failure prevented:** earliest/latest/avg-first-dab stats silently off by
  one hour for MST-era runs. **Occurred:** no — every run to date is in MDT.
  Fires automatically on November 1, 2026. Flagged honestly as preventive,
  but the trigger date is certain, not hypothetical.
- **Mechanism:** replace `MDT = timezone(timedelta(hours=-6))`
  (`Dabby_Log_Generator.py:162`) with per-run `denver_local()` conversion.
- **Precedent:** `denver_local()` exists precisely because hardcoded offsets
  failed; `CLAUDE.md`'s UTC−6 hardcode (S2-12) is the same class.
- **Cost:** S.

### S1-7. `next_ai_analysis` length tripwire in `validate()` — **S**, judgment-adjacent

- **Failure prevented:** the "recaps instead of recommends" failure mode
  (`Dabby_Handoff_Notes.md:206` — the convention is 4–5 sentences max).
  **Occurred:** yes (documented as a live failure mode).
- **Mechanism:** a generate-time *warning* (not error) when a strain's
  `next_ai_analysis` exceeds ~800 characters — crude proxy, catches the worst
  drift, never blocks.
- **Honest caveat per the Session 112 bar:** length is a proxy for the real
  failure (recap vs. recommendation), which is semantic and not mechanically
  checkable — same conclusion the pre-send semantic-check backlog item
  reached. If a crude tripwire feels like noise, skipping this is reasonable;
  the analysis-toolkit skill is the fuller answer.
- **Cost:** S.

### S1-8. Adopt `citecheck.py` as a session-close / pass-3 tool — **S** (already built)

- **Failure prevented:** wisdom/notes citations drifting from the jar data as
  runs accumulate and rows get trimmed; specifically pass 3's guardrail 2.
  **Occurred:** not yet in citations (287/287 clean — this audit is the
  evidence); the filename/identifier drift class *has* occurred (the 9
  triaged hits are all deliberate, but only because this audit checked).
- **Mechanism:** committed in this PR. Wire-in options, cheapest first: a
  line in the session-close checklist ("run `python3 citecheck.py`, triage
  new hits"), or a CI step on PRs touching the three prose docs (M — needs a
  baseline/allowlist so historical rows don't fail every run; hits are triage
  input by design, so CI-as-hard-gate is the wrong shape without one).
- **Cost:** S as a checklist line; M as CI.

### S1-9. Unreachable `read`/`verdict` render branches — flagged as aesthetic, recommend Leave It Alone

`Dabby_Log_Generator.py:461–464` still renders `run.read`/`run.verdict` rows,
but `validate()` (`Dabby_Core.py:513–518`) errors on any non-empty value, so
the branches are unreachable. Applying the project's own bar: the
justification for deleting them is aesthetic; no failure can occur while the
validator holds. Listed for completeness, not recommended as work.

---

## Known items — disposition table

| Known item (from the charter) | Disposition | Notes |
|---|---|---|
| CLAUDE.md integration pass (prose vs. mechanical layer) | **Confirmed** | S2-12: date/time protocol still hand-derivation + hardcoded UTC−6; no mention of `pending_dab.py` or the skills. DST end (Nov 1) gives it a real deadline. |
| Wisdom file exceeds the Read cap | **Confirmed** | Measured this session: 34,190 tokens vs 25,000 cap (two Read calls). Correctness input for pass 3 from this audit: all 287 run citations resolve — compression can proceed without a citation-repair pass; `citecheck.py` is guardrail 2. |
| Skills README | **Confirmed** | `.claude/skills/` contains only dab, log-run, new-jar. |
| BASELINE_CURVE-in-RUNS preflight ban | **Confirmed + amended** | Now 10 run-level refs across 5 jars (backlog said ~8–10/~6 — accurate). Amendment: priority raised — the manual protocol it replaces is defective (S2-1), and 2 new baseline-constant runs were added after log-run began telling sessions not to (S2-15). See S1-4. |
| Workflow simplification (optional PR for routine logging) | **Confirmed** | Unchanged; PR path still mandatory everywhere. No new evidence either way from this audit. |
| User Configuration block in CLAUDE.md | **Confirmed** | No such block exists; timezone/device/technique facts remain embedded in protocol prose. |
| `fmt_curve_table()` mobile overflow | **Confirmed** | `Dabby_Core.py:402–407` — one line per waypoint, no width cap, exactly as the backlog describes. |
| Model-check at dab-skill start | **Confirmed, still blocked** | Dab skill has no model step; the open mechanism question (can a skill read the active model programmatically?) is unresolved and is the real blocker, as the backlog says. |
| Pre-send check's semantic blind spot | **Confirmed** | Both skills' checks are purely syntactic ("anything backticked, snake_case, ALL_CAPS, a jar slug, or a protocol step name" — dab:165, log-run:157). The open question (can a semantic check be mechanical at all?) stands; this audit adds no mechanism that answers it. |
| Session 145 failure-mode entry (proactively surfacing the checklist) | **Confirmed** | Written at `Dabby_Handoff_Notes.md:224`, correctly scoped as judgment-layer. One amendment available: it says "six questions" — see S2-2. |

---

## Leave It Alone

Things that look like findings but are settled — checked against both
Decisions — Do Not Re-Litigate tables before anything above was flagged.

- **Jar-isolation waypoint duplication** (e.g. Watermellos carrying FW106
  curve copies) — settled by design; the isolation invariant is load-bearing.
- **Machine-side vocabulary inside skill files** — the two-registers design
  puts internal names *in* the skills on purpose; only chat output is
  policed.
- **Wisdom short-form run citations** (`FW106 R26`) — rendered convention,
  now verified resolvable by `citecheck.py` (287/287).
- **Frozen jar prose** — historical record; the WM R9 "assumed" note is
  *correct* and is what S2-5 says the thermal model should defer to.
- **The "Structurally resolved" failure-mode one-liners** — all verified
  against code this audit: the date validator, `sessions_prior_today`
  cross-check, swab/`read`/`verdict` invariants, curly-quote preflight,
  pending-dabs tripwire, generated most-recent-run and `Next run: N` lines
  all exist and do what the one-liners claim.
- **Dashboard temp stat cards** — Session 53 "do not re-audit" honored; the
  bucket math was not re-derived. (S1-6 touches the *time-of-day* cards only,
  which that decision doesn't cover.)
- **Accent color auto-assignment instability, `_resolve_accent_colors`
  explicit import, two-tier lifecycle, no-PAUSED** — all settled decisions;
  S2-13 is a two-word comment fix, not a re-litigation.
- **`citecheck.py`'s 9 triage hits** — all deliberate historical/future
  references, dispositioned in the preamble; do not "fix" them.
- **`register_leak_diagnostic_answer.md`** — not opened; the blinded exercise
  remains intact for a future session.
- **Charter sequencing** — audit → wisdom consolidation (pass 3) →
  analysis-toolkit skill remains the right order; nothing found here reorders
  it. Pass 3 can now start from a verified-citations baseline.
