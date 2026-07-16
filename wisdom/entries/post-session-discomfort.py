from wisdom_core import *

ENTRY = WisdomEntry(
    key='post-session-discomfort',
    kind='pattern',
    claim="Post-session airway discomfort (onset or persistence after session end) "
          "recurs cross-curve and cross-rig. Occurs on 380°F opens as "
          "well as hot opens, so opening temperature is one candidate among several, "
          "not the tracking variable.",
    guidance="Read each new post-session-discomfort instance against the documented "
             "confounds, not against a memory of the others. Do not treat opening "
             "temperature as the tracking variable. Distinct from row (A): (A) is where "
             "harshness is felt in-session; (B) is whether anything is felt after it ends.",
    grade='observation',
    grade_basis="Low — 9 instances across 4 rigs and multiple curve shapes; mechanism "
                "open; the counters share curves/rigs with confirming instances.",
    evidence=[
        Citation(
            source='watermellos R1',
            role='confirms',
            provenance='mixed',
            gist="\"afterward it was pronounced for a long time\" — 380-open ramp, Rig 4. "
                 "[discomfort-observation provenance untagged in source; the confound is "
                 "user-verbatim]",
            confounds="Confound, user's own attribution: \"I totally did more draws than "
                      "I should have.\"",
        ),
        Citation(
            source='watermellos R2',
            role='confirms',
            provenance='ai-authored',
            gist="Mild, \"Afterward I can feel some harshness in my throat\" — 380-open, "
                 "Rig 5. [provenance untagged in source]",
            confounds="2nd dab (session order).",
        ),
        Citation(
            source='watermellos R9',
            role='confirms',
            provenance='ai-authored',
            gist="\"Significant throat soreness after\" — 460 descent open, Rig 5. "
                 "[provenance untagged in source]",
            confounds="Load finished early — depletion not separable — and 2nd dab.",
        ),
        Citation(
            source='fw106 R4',
            role='confirms',
            provenance='ai-authored',
            gist="\"It's lingering now a few minutes later\" — 380-open fast ramp, Rig 5. "
                 "Listed here for the post-session persistence observation only. "
                 "[provenance untagged in source]",
            confounds="2nd dab; the in-session harshness attribution is settled as "
                      "session-order-driven — Session 82 Do-Not-Re-Litigate; listed here "
                      "for the post-session persistence observation only.",
        ),
        Citation(
            source='fw106 R11',
            role='confirms',
            provenance='ai-authored',
            gist="\"Definitely hot in that afterward\" — programmed-460, Rig 5 (logged as "
                 "a pair with R12: \"hot in throat afterward\"). [provenance untagged in "
                 "source; quote-to-run split within the R11/R12 pair is assumed]",
            confounds="Both deliberate above-ceiling too_hot=True runs.",
        ),
        Citation(
            source='fw106 R12',
            role='confirms',
            provenance='ai-authored',
            gist="\"hot in throat afterward\" — programmed-460, Rig 5 (logged as a pair "
                 "with R11: \"Definitely hot in that afterward\"). [provenance untagged in "
                 "source; quote-to-run split within the R11/R12 pair is assumed]",
            confounds="Both deliberate above-ceiling too_hot=True runs.",
        ),
        Citation(
            source='hive1 R13',
            role='confirms',
            provenance='ai-authored',
            gist="Heartburn-like, chest and throat, post-session onset — in-session "
                 "harshness resolved by end — 440 gentle descent, Rig 6. [provenance "
                 "untagged in source]",
            confounds="1st dab, same day as R14.",
        ),
        Citation(
            source='hive1 R14',
            role='confirms',
            provenance='ai-authored',
            gist="Heartburn-like, chest and throat, post-session onset — in-session "
                 "harshness resolved by end — 440 gentle descent, Rig 6. [provenance "
                 "untagged in source]",
            confounds="2nd dab, same day as R13.",
        ),
        Citation(
            source='lunarz R1',
            role='confirms',
            provenance='ai-authored',
            gist="\"it lingered\" — bounded hold, Rig 6. [provenance untagged in source]",
            confounds="3rd dab, slightly-larger load.",
        ),
        Citation(
            source='bb362 R2',
            role='confirms',
            provenance='ai-authored',
            gist="\"My throat is burning a bit still\" — BASELINE_416 ramp, Rig 5. "
                 "[provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='lunarz R3',
            role='confirms',
            provenance='ai-authored',
            gist="July 12, 2026 — mild-to-medium chest harshness that a water sip "
                 "reduced but did not eliminate; 430°F bounded hold, 4th consecutive dab, "
                 "normal load. [provenance untagged in source]",
            confounds="Partial persistence with water as the confound; 4th consecutive dab.",
        ),
        Citation(
            source='watermellos R10',
            role='counters',
            provenance='user-verbatim',
            gist="\"No post-session throat soreness\" — user-verbatim.",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R15',
            role='counters',
            provenance='mixed',
            gist="No heartburn; session_char record, user's words \"I feel pretty good\"; "
                 "same curve as R13/R14.",
            confounds="First dab, large load; same curve as the R13/R14 confirming pair.",
        ),
        Citation(
            source='lunarz R2',
            role='counters',
            provenance='user-verbatim',
            gist="\"I don't feel it now\" — user-verbatim; 430°F bounded hold, 3rd dab, "
                 "large load.",
            confounds="Water between cycles, so the non-persistence isn't a clean counter "
                      "to R1; 3rd dab, large load.",
        ),
    ],
    positions=[
        Position(
            stated="July 11, 2026 audit (consolidated — absorbs the former Methodology "
                   "\"post-session soreness thread\"); updated Sessions 158, 159",
            text="Occurs on ordinary 380°F opens (WM R1, WM R2, FW106 R4, bb362 R2) as "
                 "well as hot opens — so opening temperature is one candidate among "
                 "several, not the tracking variable (this retires the old \"opening "
                 "temperature tracks most clearly\" framing). The confound column is the "
                 "point of this row: it exists so each new post-session-discomfort "
                 "instance is read against the documented confounds, not against a memory "
                 "of the others. Distinct from row (A): (A) is where the harshness is "
                 "felt during the session; (B) is whether anything is felt after it ends.",
        ),
    ],
    updated="Consolidated July 11, 2026 audit; updated Sessions 158, 159",
)
