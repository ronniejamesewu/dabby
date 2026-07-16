# Handoff Notes Split — Design (pre-symptom)

*Written July 15, 2026, by the session that shipped the wisdom-as-data migration (PR
#250), while the full build context was still loaded. Status: DESIGN ONLY — no
execution trigger has fired. Execution is deliberately deferred to either (a) the
symptom (a paged Read of `Dabby_Handoff_Notes.md` at session open, or a session-close
hesitation about which home a new entry belongs in), or (b) an idle capable session
with nothing better to do. Before executing, run `NOTES_SPLIT_PICKUP_PROMPT.md` in
this directory — this design must re-earn its place against the problem as it actually
presents, not as predicted here.*

## The problem being pre-empted

`Dabby_Handoff_Notes.md` measured 62,189 chars on July 15, 2026 — 74% of the size at
which `HANDOFF_WISDOM.md` failed the single-Read cap and forced the wisdom migration.
It has the same failing shape: hand-maintained, mandatory-unconditional session-open
read, append-heavy (failure modes and decisions accrete most sessions), compressed
only by judgment-layer discipline. Second, independent force: since the wisdom layer
became typed, the notes/wisdom boundary leaks — decisions live in both homes, and the
"AI-behavioral vs. operational" failure-mode split is fuzzy enough that the
invented-specificity entry (July 15) went to the notes while its operational twin
class lives in `wisdom/entries/`. Every leak doubles a future session's lookup or
halves its coverage.

## The design in one sentence

The notes' *accreting* content types move into homes that already have structural
bounds (wisdom entries, skills); what remains is a small prose core that doesn't
accrete by nature; a generator tripwire makes any regrowth loud.

**No new schema. No new kinds. No new machinery except one size check.** The wisdom
migration's factory (schema, validators, transposition recipe, review workflow,
external-review brief — all in this directory) executes this split as-is. That is the
main reason this design is small: it is an application, not an architecture.

## Disposition by section (inventory by section name — re-verify against the live
file at execution; line numbers rot)

1. **Header date line** — stays. Session-close protocol artifact.
2. **Voice & Role** — STAYS, verbatim, prose, in the notes. Do not datafy
   personality: there is a standing do-not-re-litigate ruling against watering this
   section down, and identity is not knowledge — it has no citations, no confidence
   grade, no supersession semantics. It is also stable (grows rarely), so it
   contributes nothing to the regrowth problem. Turning the fart-joke clause into a
   dataclass field would be a category error and the funniest possible violation of
   the ruling.
3. **Session Logging Protocol** (Beat 1/2, necessity fields, question types,
   dab_notes verbatim rule, analysis/next_ai_analysis rules, field conventions,
   jar-done commemoration) — migrates to the **skills** that already operationalize
   it (log-run, dab, analysis-toolkit own most of this content in near-duplicate
   today). The notes keep a three-line pointer. Rationale: protocol is workflow, and
   workflow's home is the trigger-loaded layer — a non-logging session pays nothing
   for it, and a logging session gets it exactly when the skill fires. Two items in
   this section are *rules about rendered data*, not workflow, and go to wisdom
   `decision` entries instead: the personal-info guardrail (which fields render
   publicly) and the `read`/`verdict`-superseded rule if not already migrated.
4. **Equipment Protocol** — same treatment as 3: continuity-default and readback
   rules to the log-run/dab skills (mostly already there); the settled rules
   (chronology-not-list-position, first-run potency caution) are already wisdom
   entries or mechanized in `pending_dab.py`.
5. **Decisions — Do Not Re-Litigate** (~30 rulings) — become wisdom `decision`
   entries. Factory rerun: one entry per ruling, claim = the ruling, rationale = one
   Position, one-line brief render. This dissolves the two-home problem for
   decisions completely.
6. **Known Claude Failure Modes** — become wisdom `failure-mode` entries; the
   behavioral/operational boundary is retired on purpose. Structurally-resolved
   one-liners → COMPRESSED (one-liner → `resolution`); live judgment-layer modes →
   LIVE (war-story narratives → dated Positions; the long compression-drift and
   register-leak histories fit the Position container exactly). The session-close
   checklist's Q3 note ("AI behavioral failure modes stay in Dabby_Handoff_Notes.md")
   is updated as part of this split — that sentence is the boundary being deleted.
7. **Before Next Session** — stays in the remainder for now; its real fix is the
   backlogged mechanical reminder slot in `pending_dab.py` (a separate small build).
8. **Backlog pointer** — stays.

## Size accounting (estimates from the July 15 file — re-measure at execution)

Stays (voice + pointers + reminders + header): ~8–12k chars, stable by nature.
Leaves: decisions ~12k → entry files; failure modes ~20k → entry files; protocol
~22k → skills (much of it deduplicating against near-identical skill text rather
than adding). Post-split mandatory read: brief (~34k) + notes core (~10k) ≈ 44k chars
≈ ~16k tokens for a non-logging session — with every accreting type structurally
homed.

## Enforcement (the regrowth answer)

- Generator warns when `Dabby_Handoff_Notes.md` exceeds 20k chars, errors above 30k
  — same failure contract as the brief budget. The remainder is prose and
  hand-maintained, so the tripwire is the only mechanical guard available; it
  converts regrowth from "noticed by accident" to "fails the next generate."
- Brief budget pressure from absorbed entries: ~30 decision one-liners ≈ +3.5k chars
  and ~10 live failure modes ≈ +9k full blocks. **This does not fit the current 40k
  hard cap** (day-one brief is 34k). The split therefore requires one of: rendering
  live behavioral failure modes as one-liners (guidance in the entry file), a
  COMPRESSED-heavy tier assignment for the older modes, or a deliberate, recorded cap
  reprice. This is the design's one genuinely open sizing problem — flagged, not
  solved. Do not solve it by silently raising the cap; that is how tripwires die.

## Execution mechanics

Rerun the factory: inventory (this file) → tiered transposition workers with
`TRANSPOSITION.md` (unchanged contract — verbatim moves, gap-marking, provenance
defaults) → mechanical reference-check script → per-entry adversarial review →
external packet option → surface rewire (CLAUDE.md gate wording, checklist Q3, skill
cross-refs) → PR. Estimated tiering: Haiku for one-liners, Sonnet for decisions and
protocol dedup, Opus for the live failure-mode war stories and the review pass.
Orchestrator: Opus is sufficient — the judgment is in this document and its pickup
protocol; a Fable orchestrator is not required and was deliberately not budgeted.

## Open calls flagged for user triage at execution

(a) The brief-budget fit above — one-liner render vs. tier assignment vs. recorded
reprice. (b) Whether the protocol-to-skills move keeps a summary paragraph in the
notes core for the user's own reference reading, or a bare pointer. (c) Whether Voice
& Role should carry the notes-core file or move to CLAUDE.md — functionally
equivalent reads; aesthetic call. (d) Timing: symptom-triggered vs. idle-session.
