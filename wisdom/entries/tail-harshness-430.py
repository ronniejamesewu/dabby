from wisdom_core import *

ENTRY = WisdomEntry(
    key='tail-harshness-430',
    kind='pattern',
    claim="Tail harshness appears at curve endpoints ≥430°F across both ramp "
          "and flat-hold shapes — it is the temperature, not the shape. Rig 1–5 "
          "era; unmapped on Rig 6.",
    guidance="Treat endpoints ≥430°F as the harshness threshold on Rig 1–5. "
             "Do not extrapolate this row to Rig 6 without a deliberate test — the "
             "Rig 6 ceiling above 425°F is unmapped.",
    grade='tested',
    grade_basis="8 strains, both curve shapes; first-dab instances represented. Provenance: only WW Z R3/R4/R6 and FW106 R5 are user-verbatim — no user-verbatim record exists for the pre-dab_notes era.",
    evidence=[
        Citation(
            source='oc R7',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F.",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R5',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F.",
            confounds="none noted",
        ),
        Citation(
            source='fembot3 R1',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F (Fembot #3 R1-2).",
            confounds="none noted",
        ),
        Citation(
            source='fembot3 R2',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F (Fembot #3 R1-2).",
            confounds="none noted",
        ),
        Citation(
            source='mb9zst R1',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F (MB9ZST R1-2).",
            confounds="none noted",
        ),
        Citation(
            source='mb9zst R2',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F (MB9ZST R1-2).",
            confounds="none noted",
        ),
        Citation(
            source='rainfruit R2',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F.",
            confounds="none noted",
        ),
        Citation(
            source='mbd R4',
            role='confirms',
            provenance='ai-authored',
            gist="Tail-harshness instance at an endpoint ≥430°F.",
            confounds="none noted",
        ),
        Citation(
            source='wwz R3',
            role='confirms',
            provenance='user-verbatim',
            gist="430°F fast ramp.",
            confounds="none noted",
        ),
        Citation(
            source='wwz R4',
            role='confirms',
            provenance='user-verbatim',
            gist="430°F fast ramp.",
            confounds="none noted",
        ),
        Citation(
            source='wwz R6',
            role='confirms',
            provenance='user-verbatim',
            gist="430°F fast ramp.",
            confounds="none noted",
        ),
        Citation(
            source='bb361 R1',
            role='confirms',
            provenance='ai-authored',
            gist="\"Hard in the tail\".",
            confounds="Ambiguous phrasing, no explicit harshness language.",
        ),
        Citation(
            source='fw106 R5',
            role='confirms',
            provenance='user-verbatim',
            gist="440°F flat hold, harshness at ~28s.",
            confounds="none noted",
        ),
        Citation(
            source='papzp22 R6',
            role='counters',
            provenance='ai-authored',
            gist="Clean 60s first cycle at 430°F on Rig 6. (provenance untagged in source)",
            confounds="Preemptive-water confound; second cycle harsh.",
        ),
        Citation(
            source='sourtangie R2',
            role='counters',
            provenance='ai-authored',
            gist="Full 60s at 430°F on Rig 6, no harshness reported. (provenance untagged in source)",
            confounds="Occasional-user and load confounds.",
        ),
        Citation(
            source='hive1 R2',
            role='struck',
            provenance='ai-authored',
            gist="No harshness record — tightened out in the July 11, 2026 audit.",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R3',
            role='struck',
            provenance='ai-authored',
            gist="Reads \"never harsh, just less distinct\" — tightened out in the "
                 "July 11, 2026 audit.",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R4',
            role='struck',
            provenance='ai-authored',
            gist="Reads \"never harsh, just less distinct\" — tightened out in the "
                 "July 11, 2026 audit.",
            confounds="none noted",
        ),
        Citation(
            source='mbd R1',
            role='struck',
            provenance='ai-authored',
            gist="Harshness-absence at 430°F traces only to R2's analysis field — "
                 "tightened out in the July 11, 2026 audit.",
            confounds="none noted",
        ),
        Citation(
            source='mbd R2',
            role='struck',
            provenance='ai-authored',
            gist="Harshness-absence at 430°F traces only to R2's analysis field — "
                 "tightened out in the July 11, 2026 audit.",
            confounds="none noted",
        ),
        Citation(
            source='mbd R3',
            role='struck',
            provenance='ai-authored',
            gist="Showed mild harshness at 420°F (below the ≥430°F threshold) "
                 "— tightened out in the July 11, 2026 audit.",
            confounds="none noted",
        ),
        Citation(
            source='rainfruit R1',
            role='struck',
            provenance='ai-authored',
            gist="RF R1 (430°F) recorded \"No harshness\" — tightened out in the "
                 "July 11, 2026 audit.",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 9–14',
            text="Both curve shapes show harshness at this endpoint; it is the "
                 "temperature, not the shape.",
        ),
        Position(
            stated='July 11, 2026 audit',
            text="Scope: evidence is Rig 1–5 era. On Rig 6, two 430°F runs lack "
                 "the signature — papzp22 R6 (clean 60s first cycle; preemptive-water "
                 "confound, second cycle harsh) and Sour Tangie R2 (full 60s, no harshness "
                 "reported; occasional-user and load confounds). The Rig 6 ceiling above "
                 "425°F is unmapped — do not extrapolate this row to Rig 6 without "
                 "a deliberate test.",
        ),
    ],
    counter_reading="The two Rig 6 430°F runs (papzp22 R6, Sour Tangie R2) lack the "
                    "signature, so ≥430°F may be a Rig 1–5 artifact rather "
                    "than a temperature law; both counters carry confounds (preemptive "
                    "water; occasional-user/load), so neither cleanly disconfirms.",
    watch_for="A deliberate Rig 6 test above 425°F would map the ceiling and show "
              "whether the ≥430°F threshold holds off Rig 1–5.",
    updated='Sessions 9–14; citations tightened and scope added July 11, 2026 audit.',
)
