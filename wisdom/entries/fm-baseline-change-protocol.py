from wisdom_core import *

ENTRY = WisdomEntry(
    key='fm-baseline-change-protocol',
    kind='failure-mode',
    claim="Redefining `BASELINE_CURVE` waypoints in `Dabby_Core.py` without first "
          "assigning the old waypoints to a named constant — any run referencing "
          "`waypoints=BASELINE_CURVE` silently renders the new curve: wrong "
          "historical data, no error.",
    guidance="Before redefining BASELINE_CURVE, name the retiring curve by endpoint "
             "temp (e.g. BASELINE_416); rewrite run-level `waypoints=BASELINE_CURVE,` "
             "refs via a field-anchored grep, never replace_all (it also hits "
             "`next_waypoints=`, which must stay); redefine BASELINE_CURVE; update "
             "Methodology Section 5. Full protocol below.",
    evidence=[
        Citation(
            source='session:commit d5ab834',
            role='context',
            provenance='ai-authored',
            gist="Commit d5ab834 — changed BASELINE_CURVE from 380→390→410→430 "
                 "to 380→400→416; archive runs were already clean (individual "
                 "named constants), active runs at time of commit were affected. "
                 "[provenance untagged in source]",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Commit d5ab834 origin; discriminator corrected July 3, 2026',
            text=r"""**Invariant:** `BASELINE_CURVE` = current recommended starting point for new strains; it lives in `Dabby_Core.py`. **Protocol when changing it:** (1) Define the retiring constant by endpoint temperature in `Dabby_Core.py` (e.g. `BASELINE_416`, not by equipment era — equipment names break when the baseline changes without an equipment change). (2) Find run-level references with a field-anchored grep — `grep -n '^\s*waypoints=BASELINE_CURVE,' jars/*.py` — and rewrite each to `waypoints=BASELINE_XXX,`, anchoring the edit on the field name. Do NOT replace_all on the bare substring `waypoints=BASELINE_CURVE,`: it also matches inside `next_waypoints=BASELINE_CURVE,` (STATUS kwargs carry the same trailing comma) and would wrongly pin What to Try Next guidance to the retired curve. `next_waypoints=BASELINE_CURVE` correctly points at the new baseline and must not be changed. (Discriminator corrected July 3, 2026 — the audit found the previous comma-based rule matched three STATUS blocks.) (3) Redefine `BASELINE_CURVE` in `Dabby_Core.py` with the new waypoints. (4) Update `Dabby_Methodology.md` Section 5 table. (5) Closed jars reference shared `BASELINE_*` the same way — the grep over `jars/*.py` already covers them, so no separate archive check is needed.""",
        ),
    ],
    updated='Commit d5ab834; discriminator corrected July 3, 2026',
)
