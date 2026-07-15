from wisdom_core import *

ENTRY = WisdomEntry(
    key='load-size-effects',
    kind='pattern',
    claim="Load size may influence both harshness and effect strength, but the "
          "cross-strain direction is split and unresolved.",
    guidance="Do not treat load size as a settled harshness driver across strains. "
             "Process fix going forward: state the load class out loud at logging so it "
             "lands in dab_notes verbatim.",
    grade='observation',
    grade_basis="Low — 6 strains; WW Z, LHBH, FW106, and bp4rw13 show larger load → "
                "earlier/more harshness or intensity; BB36 #2 and Hive1 counter; "
                "direction split, unresolved",
    evidence=[
        Citation(
            source='fw106 R26',
            role='confirms',
            provenance='ai-authored',
            gist="First dab, larger load — load class AI-recorded in the run's analysis, "
                 "not dab_notes; harshness ~50s.",
            confounds="Load class AI-recorded in the run's analysis, not dab_notes. Both "
                      "loads in the R26-vs-R28 pair are \"larger\"-class, so the "
                      "heavier/lighter ordering within the pair is soft.",
        ),
        Citation(
            source='fw106 R28',
            role='confirms',
            provenance='user-verbatim',
            gist="First dab, \"Larger load, maybe too large\" — user-verbatim; harshness "
                 "~32s. Same curve (FW106_DESCENT_GENTLE), same rig (Rig 6) as R26.",
            confounds="Both loads in the R26-vs-R28 pair are \"larger\"-class, so the "
                      "heavier/lighter ordering within the pair is soft.",
        ),
        Citation(
            source='fw106 R27',
            role='struck',
            provenance='ai-authored',
            gist="FW106 R27-vs-R29 struck as a load comparison, July 11, 2026 audit: "
                 "R27's own record carries no load statement in any field — its \"larger "
                 "load\" label traces only to R28/R29's comparison analyses — and R27's "
                 "frozen analysis attributes the early harshness to session order; the "
                 "pair remains a session-order data point.",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R5',
            role='confirms',
            provenance='ai-authored',
            gist="Big load — AI-recorded in analysis, not dab_notes; overwhelming "
                 "intensity, memory gap. Same descent curve, same rig (Rig 6 — corrected "
                 "July 2, 2026 from mislogged Rig 5) as R6/R7.",
            confounds="Load class AI-recorded in analysis, not dab_notes; rig corrected "
                      "July 2, 2026 from mislogged Rig 5.",
        ),
        Citation(
            source='bp4rw13 R6',
            role='confirms',
            provenance='user-verbatim',
            gist="\"It was lighter load\" — user-verbatim; medium intensity.",
            confounds="R6-vs-R7 is the best load-provenance pair in the log but is "
                      "order-asymmetric (R6 2nd dab, R7 next-day 1st dab) and its "
                      "harshness timings barely differ — the contrast is mostly "
                      "intensity, where R6's tolerance confound is live.",
        ),
        Citation(
            source='bp4rw13 R7',
            role='confirms',
            provenance='user-verbatim',
            gist="\"a little bigger than normal\" — user-verbatim; medium-high intensity.",
            confounds="R6-vs-R7 is the best load-provenance pair in the log but is "
                      "order-asymmetric (R6 2nd dab, R7 next-day 1st dab) and its "
                      "harshness timings barely differ — the contrast is mostly "
                      "intensity.",
        ),
        Citation(
            source='wwz R5',
            role='confirms',
            provenance='ai-authored',
            gist="Earlier comparison in the FW106 direction, R5/R6 pair — R5 the lighter "
                 "leg; provenance untagged in source. See the frozen analyses.",
            confounds="R6 is both bigger-load and second-dab, so the pair's load contrast "
                      "is confounded by dab order.",
        ),
        Citation(
            source='wwz R6',
            role='confirms',
            provenance='ai-authored',
            gist="Earlier comparison in the FW106 direction, R5/R6 pair — R6 both "
                 "bigger-load and second-dab; provenance untagged in source. See the "
                 "frozen analyses.",
            confounds="R6 is both bigger-load and second-dab, so the pair's load contrast "
                      "is confounded by dab order.",
        ),
        Citation(
            source='wwz R8',
            role='confirms',
            provenance='ai-authored',
            gist="Earlier comparison in the FW106 direction, R8/R9 pair; load classes "
                 "AI-recorded. See the frozen analyses.",
            confounds="Load classes AI-recorded, not dab_notes.",
        ),
        Citation(
            source='wwz R9',
            role='confirms',
            provenance='ai-authored',
            gist="Earlier comparison in the FW106 direction, R8/R9 pair; load classes "
                 "AI-recorded. See the frozen analyses.",
            confounds="Load classes AI-recorded, not dab_notes.",
        ),
        Citation(
            source='lhbh R3',
            role='confirms',
            provenance='ai-authored',
            gist="Earlier comparison in the FW106 direction, R3/R4 pair; provenance "
                 "untagged in source. See the frozen analyses.",
            confounds="R4 (the other half of the pair) is session-order confounded.",
        ),
        Citation(
            source='lhbh R4',
            role='confirms',
            provenance='ai-authored',
            gist="Earlier comparison in the FW106 direction, R3/R4 pair, the latter "
                 "session-order confounded; provenance untagged in source. See the "
                 "frozen analyses.",
            confounds="Session-order confounded.",
        ),
        Citation(
            source='bb362 R4',
            role='counters',
            provenance='ai-authored',
            gist="Larger-than-normal load, slight draw-2 harshness (provenance untagged "
                 "in source).",
            confounds="Identical outcomes across very different loads (Rig 5, documented "
                      "jar variability; order-asymmetric — R4 first dab, R5 second).",
        ),
        Citation(
            source='bb362 R5',
            role='counters',
            provenance='user-verbatim',
            gist="\"I loaded as little as I could\" — user-verbatim; same slight draw-2 "
                 "harshness as R4.",
            confounds="Identical outcomes across very different loads (Rig 5, documented "
                      "jar variability; order-asymmetric — R4 first dab, R5 second).",
        ),
        Citation(
            source='hive1 R6',
            role='counters',
            provenance='ai-authored',
            gist="First dab, uncertain/smaller load, harsh at ~43s; load class "
                 "AI-recorded (endpoint_note/analysis), neither in dab_notes.",
            confounds="Same curve, same rig (Rig 6), session-order matched; both load "
                      "classes AI-recorded (endpoint_note/analysis), neither in dab_notes.",
        ),
        Citation(
            source='hive1 R8',
            role='counters',
            provenance='ai-authored',
            gist="First dab, larger load, very little harshness; load class AI-recorded, "
                 "neither in dab_notes.",
            confounds="Same curve, same rig (Rig 6), session-order matched; both load "
                      "classes AI-recorded (endpoint_note/analysis), neither in dab_notes.",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 59, 122, 124 (updated Sessions 136, 138)',
            text="Strongest available leg: FW106 R26 (harshness ~50s) vs R28 (harshness "
                 "~32s) at the same curve (FW106_DESCENT_GENTLE) and rig (Rig 6), both "
                 "\"larger\"-class so the within-pair ordering is soft. bp4rw13 R5 vs R6 "
                 "vs R7 on the same descent curve and rig form a gradient in the same "
                 "direction, with R6-vs-R7 the best load-provenance pair in the log "
                 "though order-asymmetric. Two earlier comparisons point the FW106 way "
                 "too — WW Z R5/R6 (R6 both bigger-load and second-dab), WW Z R8/R9, and "
                 "LHBH R3/R4 (the latter session-order confounded). Counters: BB36 #2 "
                 "R4/R5 (identical outcomes across very different loads) and Hive1 R6/R8 "
                 "(less harshness on the larger load).",
        ),
        Position(
            stated='July 11, 2026 audit',
            text="July 11, 2026 audit: load classes for five cited runs across three "
                 "jars (FW106 R26/R29, bp4rw13 R5, WW Z R8/R9) plus both halves of the "
                 "Hive1 R6/R8 counter-pair exist only in AI-authored fields, not the "
                 "user's words — provenance now marked per run in Evidence, and the "
                 "quantified \"~14–18s earlier on the heavier load\" claim is retired "
                 "with the R27 strike. The surviving FW106 leg (R26-vs-R28) and the "
                 "bp4rw13 gradient still point the same direction: bigger load tracks "
                 "bigger effect, though portioning on this runny thumbprint is admittedly "
                 "imprecise (see Decisions — Do Not Re-Litigate) and no pair in the log "
                 "is free of order or provenance weaknesses. Combined: four strains show "
                 "larger load → more/earlier harshness or intensity (WW Z, LHBH, FW106, "
                 "bp4rw13); two show less or no change (BB36 #2, Hive1). No settled "
                 "cross-strain direction. Do not treat load size as a settled harshness "
                 "driver across strains. Process fix going forward: state the load class "
                 "out loud at logging so it lands in dab_notes verbatim.",
        ),
    ],
    counter_reading="Two strains counter outright — BB36 #2 R4/R5 show identical outcomes "
                    "across very different loads, and Hive1 R6/R8 show less harshness on "
                    "the larger load — and every confirming pair carries an order or "
                    "provenance weakness, so the split may be noise rather than a real "
                    "load effect.",
    updated='Sessions 59, 122, 124, updated Sessions 136, 138; July 11, 2026 audit',
)
