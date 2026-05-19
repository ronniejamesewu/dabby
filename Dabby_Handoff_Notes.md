# Dabby — Conversation Handoff Notes
## Last updated: May 18, 2026 — Session 53

---

## Session Logging Protocol

**Tone:** Smart, dry, and funny when something earns it — don't force a bit every turn. Comedic references: Patrice O'Neal, Jimmy Norton, Sarah Silverman (dark, observational, willing to go there), Sheng Wang, Nate Bargatze (deadpan, quiet, almost accidental), Mike Birbiglia (self-deprecating storytelling), Doug Benson (loose, associative), Seth Rogen (intelligent stoner energy, warm, laughs at himself). Working blue is fine when it's genuinely funnier than the clean version — not as a default mode.

**Run logging is a confirmed-interpretation conversation.** When the user reports a completed run, the AI never silently translates loose input into frozen log content. The pre-write readback has two beats:

**Beat 1 — factual confirmation:** dates, curve, swab, equipment. State what you parsed — always, unconditionally, not gated on the AI feeling unsure (this project's documented failure mode is over-confidence). Users scan this for errors.

**Beat 2 — interpretation check (when applicable):** surfaces observations from `dab_notes` that are both **ambiguous** (multiple plausible meanings the AI must choose between) and **consequential** (the choice between meanings would produce meaningfully different analysis). Always at the end of the readback, clearly separated from Beat 1, at most one or two items. The invitation is the last line of the message — never buried. Observations that are ambiguous but not consequential: acknowledge in `analysis` as unclear — do not make an undisclosed interpretive choice. Observations that are imprecise but unambiguous: synthesize with confidence calibrated to evidence weight, no question needed.

Then:

- **Necessity-class fields — swab color and the curve numbers — cannot be logged vague.** Protocol is "do not log without the swab"; the chart and curve table can't degrade on a vague endpoint. Resolve vagueness there before writing, asking as many clarifying questions as it takes. Run date: ask if missing, `None` only if genuinely unrecoverable. Strain is never vague (it's which jar).
- **Two question types.** *Clarifying* — resolve ambiguity in what the user meant; as many as needed to record faithfully (necessity-bounded, not a count); stop as soon as it can be recorded faithfully. *Thread-pull* — **optional, zero or one, default none**: asked only when a single "that's curious" fork would materially move the recommendation or reveal a cross-run/cross-strain pattern. It may land on swab or fine sensory taxonomy if that is genuinely where it leads ("I don't know" is a complete answer — the epistemic flag governs how much weight the answer gets, not whether the question may be asked).
- **The user ends it anytime.** "Just log it" / no substantive answer → write as read; unresolved *prose* vagueness is logged verbatim, never sharpened into a confident claim.
- **AI Analysis** is the AI's own labeled synthesis — not a logging gate the user must endorse to proceed, but fully open to challenge; a challenge that exposes a weak inference revises it (per "push back genuinely before agreeing").

Runs are logged with exact date (not month only) when known.

**Swab protocol clarification:** A swab is always taken — it is the standard insert-cleaning step after every session, not an optional measurement. "Not recorded" means the color wasn't noted, not that no swab was taken. Always ask for swab color if not reported.

**Duration typo:** If the user reports a session time of 69 seconds, assume it is a typo for 60 seconds, log it as 60, and note the assumption in your output — tell the user to complain if you assumed wrong. Do not stop to ask for confirmation.

**sessions_prior_today:** Count entries with the same `run_date` in `COMPLETED_RUNS` — silently, no narration. This applies whether logging same-day or post-date.

When the count is zero (first of the day), say so in the confirmation beat and bring some real celebratory energy — this is a step up from the baseline wit, not just a dry aside. One or two sentences synthesized from whatever's present in the run context — strain, endpoint, what's being tested, time of day, run number, cross-strain patterns, anything. Working blue is encouraged when it lands. A setup and a punchline is fine. Leave the door open for correction.

When the count is greater than zero, state it matter-of-factly ("3rd dab of the day") — no fanfare.

**Optional field register:** When prompting for optional or hard-to-recall fields (sessions prior today when post-date, load size, anything that may not be fresh in memory), use a casual register: "Do you happen to remember X?" This signals that the field is genuinely optional without making it feel like a required checkbox.

**Intensity:** When logging a run, ask for effect intensity if not reported: "How hard did it hit?" — anchor options are light / moderate / strong, freeform notes welcome. Keep in mind that effects unfold over hours and logging usually happens minutes post-dab, so this captures the immediate read only.

**`dab_notes` (per-run record, `CompletedRun.dab_notes`):** Populate with the user's verbatim words at logging time — not a paraphrase, not a structured extraction. This is the primary freeform record of what happened. The structured fields (`swab`, `session_char`, `intensity`) are extracted from it, not substitutes for it. If the user gives a sparse report, log what was said — do not fill in language they didn't use.

**`analysis` (per-run record, `CompletedRun.analysis`):** Draft in conversation after the user confirms the readback — show both `analysis` and `next_ai_analysis` in chat for user review before writing to `Dabby_Data.py`, then write everything in one shot after approval. Synthesize the `dab_notes` just captured, the full strain history (all prior runs and their analyses), cross-strain patterns from the wisdom layer, and equipment context — the current run's observations are one input, not the whole picture. Once written it is historically stable: correctable by exception when genuinely wrong, never casually overwritten when thinking changes. Revisions to current strategy go to `StrainStatus.next_ai_analysis`, not into a prior run's frozen `analysis`. Note: `read` and `verdict` are superseded by `analysis` — do not populate them for new runs.

Every claim in `analysis` must trace to one of: (a) what the user reported this session, (b) prior run history for this strain, or (c) the wisdom layer — cross-strain patterns and equipment observations. Before drawing on (b) or (c), check per-run `EquipmentConfig`: if equipment differs across compared runs, flag it as a confound rather than asserting the comparison. Match confidence to evidence: "user reported X" for single-session observations; "consistent with Run N" for single corroboration; "pattern across runs X/Y/Z" for confirmed patterns. A hypothesis in `dab_notes` — whether from the initial dump or a conversational aside — is treated as "user suggested X" at single-data-point weight. It does not become a working position in `analysis` until subsequent runs test and support it.

A run that doesn't follow the prior suggestion is more data, not a deviation. What to Try Next tracks accumulated state of understanding, not prescriptions.

**`endpoint_note` (per-run record, `CompletedRun.endpoint_note`):** AI-authored inline HTML describing the curve's key characteristic — endpoint temperature, shape note, and optionally a cross-run comparison. Rendered on the Mode line as its third segment. Use `<strong>` labels; convention from Step 3 migration:
- Ramp runs: `'<strong>Endpoint:</strong> 430°F'` + optional note (e.g. `'— same as Run 1'`, `'— down 10°F from prior runs'`)
- Flat hold runs: `'<strong>Setpoint:</strong> 430°F steady (no ramp)'`
- Cold start with explicit open point: `'<strong>Open:</strong> 350°F &nbsp;|&nbsp; <strong>Endpoint:</strong> 460°F'`
Populate at logging time alongside the other content fields. Do not leave blank — the Mode line renders a dangling `|` separator if empty.

**What to Try Next — AI Analysis (`StrainStatus.next_ai_analysis`):** The AI Analysis field in each strain's What to Try Next section is not a summary of what happened — that belongs in the run results. It should state a concrete recommendation with the reasoning behind it. Before writing AI Analysis, draw on all four artifacts: `HANDOFF_WISDOM.md` (cross-strain patterns, equipment observations), `Dabby_Methodology.md` (thermal model and session process reasoning), the full run history for the strain, and the user's Dab Notes just added. Cross-strain patterns are often the most valuable input — flag them when relevant. Name confounders where they affect the recommendation. Flag clearly when a recommendation is based on a single data point. Keep it tight — concrete recommendation and the key reasoning, nothing more. If it runs more than 4–5 sentences, cut it down. Signal should dominate.

---

## Decisions — Do Not Re-Litigate

- Blueberry 36 phenotypes are logged as separate strains, not grouped.
- Dashboard is implemented. Do not redesign from scratch — iterate from the current generator code.
- Calibration framing retired. This is a session log, not a calibration program. Do not re-introduce "dialed," "in calibration," status badges, or status columns anywhere in the log or dashboard.
- Contents/TOC section removed. The searchable strain browser on the dashboard serves as navigation. Do not re-add a separate Contents section.
- Do not merge `Dabby_Data.py` and `Dabby_Log_Generator.py` back together.
- `_ACCENT_RESOLVED` requires an explicit `from Dabby_Data import _ACCENT_RESOLVED` line in the generator alongside the wildcard import. Do not delete the explicit import line "to clean up the duplication" — it is load-bearing.
- `DABBY_ARCHITECTURE.md` is a committed living **proposed plan** — not settled architecture, not "do not re-litigate," and not a throwaway planning doc. Keep and update it as steps complete; do not delete it; do not treat it as settled.
- `STRAIN_STATUS` badge fields (`badge_class`, `badge_text`) are gone — do not add them back. Do not revert to tuple form.
- Run `analysis` lives on `CompletedRun`, is frozen and historically stable. Correctable by exception when genuinely wrong; never casually overwritten when thinking changes. Revisions to current strategy go to `StrainStatus.next_ai_analysis`, not into a prior run's frozen `analysis`.
- Current "What to Try Next" renders from revisable `StrainStatus` fields (`next_dab_notes`, `next_ai_analysis`, `next_waypoints`) — not derived from any run's frozen `analysis`.
- Dashboard temp stat cards (avg open, avg endpoint, most time spent) confirmed correct in Session 53 — linear interpolation into 5°F buckets, computed fresh from `COMPLETED_RUNS` each generate. Do not re-audit.
- No emojis on stat cards — tried all 9 in Session 53, removed. Cards are clean without them. Do not re-introduce.
- Stat card labels use "avg" not "average" — consistent with existing cards (avg open, avg endpoint). Applied to "avg first dab of the day" in Session 53.

---

## Known Claude Failure Modes — This Project

- **Narrating instead of proposing.** Presenting an interpretation or plan and then immediately executing is not confirmation — it is narration with extra steps. This applies to all actions: editing files, running the generator, committing, updating methodology or collaboration notes. The correct behavior is always: present the plan, ask for approval or corrections, wait for a response, then act.

- **Not reading the required files at session start.** CLAUDE.md explicitly requires reading `HANDOFF_STATE.md`, `HANDOFF_WISDOM.md`, `Dabby_Handoff_Notes.md`, and `Dabby_Data.py` before taking any action. This was skipped in Session 15 and again in Session 27 — both times because the user's opening message pointed to a specific file and the startup sequence was bypassed. Read all four required files before responding to any request, every session, regardless of what the opening message asks.

- **Treating product format names as strain names.** "Persy Neapolitan" is a 710 Labs product type (three-strain cold-cure jar). The strain name is the component strains listed on the jar. When a user hands you a product description, check whether the product name and the strain name are the same thing before logging.

- **Force pushes are blocked in this environment.** `git push --force-with-lease` returns HTTP 403. Do not attempt it — it wastes time. Do not amend already-pushed commits either (same problem). When a branch needs correction after being pushed, cut a fresh branch from `origin/main`, apply the fix there, and push that as a new branch.

- **PR preview going stale after the first commit.** If the preview comment stops updating on subsequent pushes, check whether the PR has merge conflicts (`mergeable_state: dirty`). A dirty PR blocks the `synchronize` workflow trigger — GitHub can't compute the merge commit. Fix by merging main into the feature branch, resolving conflicts, and pushing. The preview workflow will fire again on the next push.

- **Putting color and design decisions in CLAUDE.md.** Color rules (no greens, minimum hue separation, no miami-vice saturation) belong as validation code in the generator, not as prose in CLAUDE.md. CLAUDE.md is for session-to-session behavioral instructions. When a rule is mechanical and checkable, write it as code.

- **Opening a separate PR for a handoff update when a PR is already open.** When the session-close handoff update is written and there is an open PR from the same session, push the handoff to that branch — do not open PR #N+1 just for the handoff.

- **Edit tool curly-quote contamination in HTML string attributes.** When a Python string containing HTML with escaped double-quote attributes (e.g. `style=\"...\"`) is written via the Edit tool, straight double quotes may be converted to curly quotes (U+201C/U+201D), leaving `\` + U+201D in the rendered HTML. The style attribute is then malformed and ignored by the browser. Fix: use single-quote HTML attributes in Python strings so no backslash escaping is needed (`style='...'`). If curly quotes appear in the file, use a Python script to replace them by byte position rather than the Edit tool.

- **Asking for or narrating sessions_prior_today when COMPLETED_RUNS can answer it.** Count entries with the same `run_date` silently — no narration, no asking. This applies same-day and post-date. When it's the first of the day, say so and riff; when it's not, state the count matter-of-factly.

- **Blaming GitHub Pages propagation lag without verifying deployed content.** When the user reports the live site hasn't updated, verify the pipeline end-to-end before attributing it to propagation delay: confirm gh-pages has a new commit with the expected timestamp, and grep the deployed file for content that should be in the new version. "Try a hard refresh" is not a first response; it's only appropriate after the pipeline is confirmed clean.

- **Caving to pushback rather than finding stronger reasoning.** When a recommendation is questioned, the instinct is to agree and pivot. The better move is to interrogate whether the recommendation was actually right for better reasons than initially stated. A position can be poorly argued and still correct. Push back genuinely before agreeing.

- **Byte-comparing a Windows working copy against an LF-deployed file (false CRLF mismatch).** Windows working copies are CRLF; git stores and deploys LF. A raw byte comparison of the on-disk working file against a deployed artifact will report a false mismatch. Correct deployed-content verification: compare against `git show HEAD:<file>`, not the working copy.

- **Echoing an internal `Dabby_Data.py` constant name to the user instead of resolving it.** When logging a run, state the equipment back to the user as readable text from `EquipmentConfig` fields — never echo `_SPINNER` or `_GEMLOCK`. Constant names are an implementation detail.

- **Writing `next_ai_analysis` that recaps instead of recommends.** The What to Try Next AI Analysis is a concrete recommendation with brief reasoning — not a summary of run history (that's what the run sections are for). If it takes more than 4–5 sentences to say what to try and why, it has too much noise.

- **Promoting a conversational hypothesis into a working analysis position.** A thought floated casually — "maybe it's asking for more heat," "could be the equipment" — gets anchored by the AI and incorporated into `analysis` as a working hypothesis rather than a logged observation. Capture verbatim in `dab_notes`; surface in Beat 2 if ambiguous and consequential; incorporate into `analysis` only as "user suggested X" at single-data-point weight. A hypothesis earns analysis weight only when subsequent runs test and support it.

- **Proposing chart or styling changes without before/after context, or coding before showing a mockup.** For chart styling and methodology edits, always propose the change with before/after context before executing. Render chart changes in mockup before touching the generator.

- **Auditing or distilling a document without cross-checking its claims against source already in context.** Every factual claim in an audited doc must be checked against the code/data, especially source already read this session. An audit that trusts the audited document is not an audit.

- **Trusting plan-doc claims about Python language behavior without verification.** Treat language-level claims (import semantics, attribute access, scoping) as hypotheses to verify on first run, not facts on the page.

- **Asserting infrastructure/pipeline facts without reading the pipeline.** Before asserting how CI/deploy behaves, open the workflow files. Do not infer it from the step description.

- **Using ambiguous abbreviations in branch names.** "fb" reads as "Facebook" in some UIs. Use full strain abbreviations — "fembot", "hive1", "ms23", etc.

---

## Backlog

- **SessionStart hook to enforce required file reads** — CLAUDE.md instructions alone have failed twice (Sessions 15, 27, and this session). A hook runs before the first turn and can't be bypassed by an attention-grabbing opening message. Tradeoff: Dabby_Data.py is ~800 lines of context overhead on every session start. Revisit when the skipped-read failure recurs or becomes costly.

- **Analysis preview in conversation** — Currently drafting both `analysis` and `next_ai_analysis` in chat for user review before writing to `Dabby_Data.py`. Revisit around May 24–25, 2026 whether to keep or remove this step.
- **Visual overhaul of the log** — forest green styling feeling heavyweight. Raise as agenda item at start of a future session. Do not make styling changes without raising this first. CSS is in `style.css` (independently editable).
- **Session date backfill** — CAG Run 1 and OC Runs 1–3 have `run_date = None`. Update if user can recall the dates.
- **End-of-jar comedian's set** — when a jar is finished, do a Harper's Index and a short comedian's set riffing on the run history. First attempt was MB9ZST (Session 51): Harper's Index landed, comedian set got laughs on second draft. Key notes: don't riff on premises the user taught you as if you discovered them; edgier beats charming; tight 4 minutes beats 5.
- **Dab Notes row in What to Try Next renders when empty** — shows "Dab Notes: Nothing recorded" for strains with no user notes for the next run. Should suppress the row when there is no meaningful content, or reconsider the label for that context.
- **THC boil-off vs. harshness trade-off** — higher endpoints complete more THC vaporization but produce tail harshness. Worth thinking through whether there's a way to characterize the trade-off empirically across strains, or whether it just becomes a preference call.
- **Quantify "rice grain" load descriptor** — weigh a few loads to establish a mg range (e.g. 0.05–0.15g). One-time calibration; update the global constants with the range.
- **Control water temperature and change frequency as variables** — standardize practice and log it.
- **Dashboard: style Next pill in strain accent color** — Last pill removed (Session 53). Next pill still uses default styling; consider accent color.
- **Dashboard: time-of-day stat cards** — built in Session 53. Three cards: ☀️ earliest dab, 🌙 latest dab, ⏰ average first dab of the day. Computed from `utc_logged_at` only — 13 of 33 runs, all May 11+. Git commit timestamps for the 20 None runs were ruled out (most were retroactive backfill, not real-time logging). Cards will fill in naturally as logging continues.
- **Visual distinction between What to Try Next and new-strain onboarding** — the two contexts (continuing calibration vs. opening a new strain) look identical but carry different intent.
