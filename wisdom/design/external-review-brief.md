# External Reviewer Brief — Wisdom Layer Migration Audit

You are auditing a data migration. You were deliberately chosen from outside the model family that performed the migration, to provide an independent check. You have no prior context on this project; everything you need is in this bundle.

## What happened

A personal logging project (dab sessions on a temperature-controlled vaporizer; run data lives in per-jar Python files not included here) kept its accumulated cross-run knowledge in a single markdown file. That file was migrated into typed Python data: one file per knowledge entry, each holding a short claim, a confidence grade, guidance, a list of evidence citations (each citing a specific run, with a role of confirms/counters/context/struck, a provenance tag of user-verbatim/ai-authored/mixed, prose describing what happened, and a required confounds statement), and dated position paragraphs including superseded ones.

The migration's contract: **transposition, not condensation.** Evidence prose was to be moved verbatim into the new containers. The only newly authored text is in five short fields per entry: `claim`, `guidance`, `grade_basis`, `watch_for`, and `counter_reading` — each meant to be a faithful distillation of what the source already said, never an upgrade or downgrade of its confidence.

## Your inputs

1. `HANDOFF_WISDOM_original.md` — the pre-migration file, frozen. Ground truth.
2. `wisdom_migrated.md` — the new entry files concatenated, plus the manifest (LIVE/COMPRESSED tier lists) and the generated summary brief.
3. `mechanical_check_results.txt` — output of a script that already verified: every run reference in the original appears somewhere in the new tree, provenance tag counts match, strike annotations survived. **Do not re-do this work.** Your job is what the script cannot judge.

## What to verify (per entry, both directions)

The documented failure mode you are hunting is **narrative-seeking drift during re-containering**: when this project's own models compress or restructure evidence prose, what gets dropped or softened tends to flatter the working narrative — in either direction. A prior incident dropped four confound clauses, every one of which made the counter-evidence to a hypothesis look cleaner. A prior audit applied a strict evidence standard where it struck claims and a loose one where it kept them. Check both directions explicitly:

- **Pass A — claims inflated:** does any `claim`, `grade_basis`, or `guidance` state more than the source row supported? Does any confound present in the source vanish or soften in the new entry? Was any hedge ("directional, not established", "single-run weight", "confound unresolved") dropped?
- **Pass B — counter-evidence cleaned:** does any countering citation read stronger in the new tree than in the source? Was any weakness *of a countering instance* (its own confounds, its provenance softness) dropped, making the counter-case look cleaner than the original recorded?

Also check:

- **Meaning fidelity of moved prose:** spot-check that "verbatim" was actually verbatim — paraphrase that changes epistemic weight counts as a finding (e.g., "body feels like it's vibrating" becoming "body vibrating" is a real prior incident — subjective report turned into physical assertion).
- **Supersession integrity:** every retired/struck framing in the original survives in the new tree *as retired/struck with its reason*, not silently deleted and not silently revived as current.
- **Settled decisions:** no "do not re-litigate" ruling from the original was weakened, dropped, or contradicted by newly authored text.
- **Nothing invented:** no citation, confound, quote, or qualifier in the new tree that has no basis in the original. Flag anything you cannot trace.
- **Grade mapping:** original confidence words (Low/Moderate/High) must map consistently to the new grade enum across all entries — flag any entry whose grade moved relative to its peers' mapping.

## What NOT to flag

The restructuring itself is approved and out of scope: reorganization, prose split across citation/position containers, field names, formatting, the summary brief's terseness. Only fidelity and epistemic drift are findings.

## Output format

Two lists, nothing else:

1. **Findings**, ordered by severity. Each: entry key → verbatim quote from the original → what the new tree says (or omits) → why it changes the epistemic picture.
2. **Checked clean** — every entry you actually examined and found faithful, by key. Do not claim coverage you didn't perform; if you sampled, say what you sampled and how you chose.
