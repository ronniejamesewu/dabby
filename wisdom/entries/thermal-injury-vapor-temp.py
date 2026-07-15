from wisdom_core import *

ENTRY = WisdomEntry(
    key='thermal-injury-vapor-temp',
    kind='theory',
    claim="Working theory: if harshness tracks hot vapor hitting tissue (per maté "
          "esophageal cancer research), it may be a harm-reduction signal, not just "
          "an experience signal. Throat vapor temperature is unmeasured; a working "
          "concern, not resolved.",
    guidance="Hold as a working concern, not a resolved finding. Do not treat harshness "
             "as purely an experience metric until throat vapor temperature is known. "
             "The water-cooling-vs-efficiency tradeoff is flagged but not yet "
             "discussed further.",
    grade='speculative',
    grade_basis="Single session (57); external research (maté/IARC) applied by "
                "analogy; no direct measurement of vapor temperature at the throat.",
    evidence=[
        Citation(
            source='session:57',
            role='context',
            provenance='ai-authored',
            gist="Session 57 analysis: cannabinoids dominate the volatile fraction at "
                 "~60–80%, heat is the primary driver of both intensity and "
                 "harshness.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Session 57',
            text="The maté throat/esophageal cancer research is relevant harm "
                 "reduction context. The cancer association is thermal, not chemical "
                 "— risk tracks with drinking temperature, not consumption "
                 "volume. IARC classified hot beverages above 65°C (149°F) "
                 "as Group 2A (probably carcinogenic) in 2016, substantially on maté "
                 "data. Mechanism: repeated thermal insult to mucosal epithelium "
                 "→ chronic inflammation → increased malignant "
                 "transformation risk.",
        ),
        Position(
            stated='Session 57',
            text="Applied to dabbing: if harshness tracks primarily with hot vapor "
                 "hitting tissue — and it appears to (Session 57 analysis: "
                 "cannabinoids dominate the volatile fraction at ~60–80%, heat "
                 "is the primary driver of both intensity and harshness) — then "
                 "harshness is not just an experience signal. It may be the signal "
                 "of the thing worth minimizing on harm reduction grounds.",
        ),
        Position(
            stated='Session 57',
            text="Key unknown: actual vapor temperature at the throat. Insert "
                 "temperature ≠ vapor temperature — water and pathway "
                 "cooling is significant and rig-dependent. Whether vapor arrives "
                 "above 65°C (149°F) at the throat is unknown. Fast ramp "
                 "with dense vapor likely arrives warmer than a slow ramp. This is "
                 "worth holding as a working concern, not a resolved finding.",
        ),
        Position(
            stated='Session 57',
            text="Open question flagged Session 57: water cooling that reduces "
                 "vapor temperature enough to protect tissue may also condense some "
                 "target volatiles (cannabinoids, terpenes) before they're inhaled "
                 "— a real tradeoff between harm reduction and delivery "
                 "efficiency. Not yet discussed.",
        ),
    ],
    watch_for="Actual throat vapor temperature (unmeasured); whether fast-ramp/dense "
              "vapor arrives warmer at the throat than slow-ramp; resolution of the "
              "cooling-vs-efficiency tradeoff (not yet discussed).",
    updated='Session 57',
)
