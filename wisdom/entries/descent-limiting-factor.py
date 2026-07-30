from wisdom_core import *

ENTRY = WisdomEntry(
    key='descent-limiting-factor',
    kind='pattern',
    claim="Descent curve changes limiting factor from harshness to intensity.",
    guidance="A descent curve (open hot, move off peak immediately) front-loads the "
             "terpene bolus and shifts the stopping condition off harshness — expect "
             "depletion, intensity, or satiety instead. No longer all first-dab or "
             "single-rig: three instances sit off Rig 6 across two tops. Load varied, "
             "unresolved.",
    grade='observation',
    grade_basis="Low — nine strains; all Rig 6 except lhbh R9/R10 and fw106 R36 (Rig 8) "
                "and lunarz R6/R7 (Rig 7); later-dab instances from papzp22 R8/R9, oc R15, "
                "lhbh R10; three tops, Rig 8 now two strains.",
    evidence=[
        Citation(
            source='fw106 R23',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6, 440→350°F over 30s, hold to 60s, first dab, normal load — no "
                 "harshness, clean cycle 1, material spent in 2 draws. (provenance "
                 "untagged in source)",
            confounds="none noted",
        ),
        Citation(
            source='watermellos R16',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6; same descent shape, first dab, larger load — clean cycle 1 "
                 "throughout, no harshness despite 440°F open, 350°F floor too low as "
                 "failure mode. (provenance untagged in source)",
            confounds="corrected July 2, 2026 from mislogged Rig 5.",
        ),
        Citation(
            source='bp4rw13 R5',
            role='confirms',
            provenance='ai-authored',
            gist="Rig 6; 440→400°F over 60s, first dab, big load — no harshness cycle "
                 "1, terpene-load cough, session ended on intensity after 3 cycles not "
                 "harshness. (provenance untagged in source)",
            confounds="corrected July 2, 2026 from mislogged Rig 5.",
        ),
        Citation(
            source='dbrb R1',
            role='confirms',
            provenance='ai-authored',
            gist="July 9, 2026 — Rig 6, bounded 10s-440°F hold then gentle descent to "
                 "400°F, first dab, jar opener, normalish-plus load — mild harshness at "
                 "end of cycle 1, session ended one draw into cycle 2 on satiety, not "
                 "harshness. (provenance untagged in source)",
            confounds="dbrb R1 fits with caveats: mild harshness did appear at end of "
                      "cycle 1 (just wasn't limiting), and its curve was the "
                      "bounded-hold variant rather than the pure descent — shape isn't "
                      "identical across the four.",
        ),
        Citation(
            source='papzp22 R8',
            role='confirms',
            provenance='user-verbatim',
            gist="July 16, 2026 — grey 450°F bounded-hold + shorter descent, "
                 "single cycle — 'no harshness'; session ended at depletion "
                 "('Load was depleted by end of cycle'). First non-first-dab "
                 "instance in the set.",
            confounds="2nd dab; bounded-hold variant, not the pure descent; load "
                      "per plan (modest) — not restated by user.",
        ),
        Citation(
            source='lhbh R8',
            role='confirms',
            provenance='user-verbatim',
            gist="July 17, 2026 — grey 450°F bounded-hold descent, first dab, big "
                 "deliberate load, 3.5 cycles — session ended on satiety with "
                 "material remaining ('stopped halfway through as I'd had enough. "
                 "Reclaim on the swab suggests I could have kept going'); throat "
                 "harshness present but not limiting (dbrb R1-style caveat), hard "
                 "to distinguish from terpene-load coughing.",
            confounds="Big load; 3.5 cycles; bounded-hold variant, not the pure "
                      "descent.",
        ),
        Citation(
            source='papzp22 R9',
            role='confirms',
            provenance='user-verbatim',
            gist="July 16, 2026 — grey 450°F cycle 1 into teal 430°F cycle 2, "
                 "normal load, 3rd dab — stopped with ~14s left on 'seemed wispy' "
                 "and having had enough (satiety), not harshness; mild cycle-1 "
                 "throat harshness appeared but wasn't limiting (dbrb R1-style "
                 "caveat).",
            confounds="3rd dab, two cycles, mid-dab curve switch; bounded-hold "
                      "variant.",
        ),
        Citation(
            source='oc R15',
            role='confirms',
            provenance='user-verbatim',
            gist="July 17, 2026 — \"purple\" 430°F open, 15s hold, gentle descent to "
                 "a 400°F floor, big (~double) load, two cycles — cycle-1 "
                 "\"fireworks\" (front-loaded terpene bolus), stopped on satiety with "
                 "material still in the load (\"there might be more in there but I "
                 "don't want more\"), not harshness. OC's first descent curve in 15 "
                 "runs; seventh strain, and the set's first sub-440°F open (430°F).",
            confounds="2nd dab; big load; two cycles; bounded-hold variant, not the "
                      "pure descent.",
        ),
        Citation(
            source='lhbh R9',
            role='confirms',
            provenance='user-verbatim',
            gist="July 28, 2026 — 440°F 15s bounded hold descending through 430°F at "
                 "35s to a 400°F floor, first dab, slightly larger than normal load, "
                 "three cycles on Rig 8 (Calibear Fab Recycler debut). Session ended "
                 "on thinning vapor across cycle 3 (\"one more nice but thin hit\"), "
                 "not harshness — and harshness was absent entirely, throat and "
                 "chest, during and after. First instance in the set off Rig 6 and "
                 "Rig 7; second instance for this strain after R8.",
            confounds="Rig debut (Rig 8) with a top new to the log; curve new to the "
                      "jar; slightly large load; three cycles; bounded-hold variant, "
                      "not the pure descent.",
        ),
        Citation(
            source='lhbh R10',
            role='confirms',
            provenance='user-verbatim',
            gist="July 28, 2026 — the same 440°F 15s bounded hold and Rig 8 as R9, "
                 "second dab, moderate load, single cycle. Session ended on material "
                 "depletion (\"It was depleted by about 12 seconds left\"), not "
                 "harshness — harshness absent entirely, throat and chest, asked in "
                 "both windows. Second Rig 8 instance and the second in the set to end "
                 "on clean depletion rather than satiety.",
            confounds="Second dab, so not session-order matched to R9; bounded-hold "
                      "variant, not the pure descent. Fewer confounds than most in the "
                      "set — single cycle, moderate load, curve and rig both held from "
                      "the prior run — but the load moved with the session order, so it "
                      "isolates neither.",
        ),
        Citation(
            source='lunarz R6',
            role='confirms',
            provenance='user-verbatim',
            gist="July 29, 2026 — the same smoothed 440°F 15s bounded hold as lhbh R11, "
                 "run on Rig 7 (SAML RBR wet top), first dab, larger-than-normal load, "
                 "two cycles. Cycle 2 stopped with 15s left on the curve — \"it was wispy "
                 "and I had enough\" — satiety on thinning vapor with material left "
                 "(reclaim \"plentiful\"), not harshness. Eighth strain and the set's "
                 "first Rig 7 instance, so the off-Rig-6 leg is now two tops rather than "
                 "one.",
            confounds="Larger-than-normal load; two cycles; bounded-hold variant, not the "
                      "pure descent; curve and top both new to this strain. Harshness was "
                      "present and not limiting (the dbrb R1-style caveat) — throat in "
                      "cycle 1, chest in cycle 2 — so this is a stopping-condition "
                      "instance, not a no-harshness one.",
        ),
        Citation(
            source='lunarz R7',
            role='confirms',
            provenance='user-verbatim',
            gist="July 29, 2026 — the same smoothed 440°F bounded hold on the same Rig 7 "
                 "RBR as lunarz R6, modest load, single cycle, 2nd dab. Stopped with under "
                 "10 seconds left on thinning vapor; \"no harshness\" anywhere, throat or "
                 "chest. The least-confounded instance in the set: curve, rig and strain "
                 "all held from the immediately preceding run, so nothing about the setup "
                 "moved except load and cycle count. Second Rig 7 instance, and the "
                 "clean-no-harshness shape (lhbh R9/R10) rather than R6's "
                 "harshness-present-but-not-limiting shape.",
            confounds="Same strain as R6, so no new strain. Load and cycle count moved "
                      "together. 2nd dab. Bounded-hold variant, not the pure descent. A "
                      "single modest cycle is a short session by construction, so ending "
                      "before harshness is the low bar of the pattern, not its hard case.",
        ),
        Citation(
            source='fw106 R36',
            role='confirms',
            provenance='user-verbatim',
            gist="July 30, 2026 — the same smoothed 440°F 15s bounded hold as lhbh R11 and "
                 "lunarz R6/R7, on Rig 8, first dab, single cycle. \"The load almost "
                 "perfectly matched the cycle time\" — the session ended on material "
                 "depletion arriving at the 60s terminus, not harshness. A very small "
                 "base-of-throat harshness came in about three-quarters through and was "
                 "not limiting (the dbrb R1 / lunarz R6 shape). Second strain on the Rig 8 "
                 "leg, which until now was lhbh alone.",
            confounds="Load class never stated — \"matched the cycle time\" describes when "
                      "it ran out, not how big it was. Curve new to this jar. Bounded-hold "
                      "variant, not the pure descent. A single cycle is a short session by "
                      "construction, so ending before harshness is the pattern's easy "
                      "case, not its hard one. Depletion coinciding with the programmed "
                      "terminus makes the stopping condition slightly ambiguous between "
                      "material and clock.",
        ),
    ],
    positions=[
        Position(
            stated='Sessions 130, 131, 137, 152',
            text="All four ended on something other than a harshness threshold — "
                 "material depletion (FW106 R23), overwhelming intensity (WM R16, "
                 "bp4rw13 R5), or satiety (dbrb R1) was the stopping condition instead. "
                 "Opening hot and moving away from peak temperature immediately "
                 "front-loads the terpene bolus without sustaining high-temperature "
                 "exposure through the session. Cross-strain consistency is directional "
                 "— but all four runs are Rig 6 (WM R16 and bp4rw13 R5 corrected July "
                 "2, 2026); no descent run has actually been logged on Rig 5, so "
                 "cross-rig generalization is untested. All four were first-dab runs "
                 "(session-order confound absent). Load varied; load size is an "
                 "unresolved secondary variable. dbrb R1 fits with caveats: mild "
                 "harshness did appear at end of cycle 1 (just wasn't limiting), and "
                 "its curve was the bounded-hold variant rather than the pure descent — "
                 "shape isn't identical across the four.",
        ),
        Position(
            stated='Session 172 (July 17, 2026)',
            text="oc R15 adds a seventh strain and the set's first sub-440°F open — a "
                 "430°F 15s-hold descent that still front-loaded a cycle-1 bolus and "
                 "stopped on satiety with material remaining, not harshness. "
                 "Consistent direction; still all Rig 6, load varied.",
        ),
        Position(
            stated='July 28, 2026 (lhbh R9)',
            text="First instance in the set off Rig 6 — a 440°F 15s bounded hold on "
                 "Rig 8 (Calibear Fab Recycler debut) that ended on thinning vapor "
                 "across cycle 3 rather than harshness, with harshness absent "
                 "entirely in both the throat and chest windows. The single-rig limit "
                 "named since Session 130 now has one exception, which is a crack in "
                 "it rather than a cross-rig result: the run is a rig debut carrying "
                 "a curve new to the jar and a slightly large load, so it cannot "
                 "isolate the descent shape from any of them. The watch_for asking "
                 "for a Rig 5 descent is unchanged — Rig 5 remains the untested case, "
                 "and its sapphire-plus-pearls geometry is the one that motivated the "
                 "question. Held at observation.",
        ),
        Position(
            stated='July 28, 2026 (lhbh R10)',
            text="Rig 8's second instance, and one of the least confounded in the set: "
                 "curve and rig held from R9, single cycle, moderate load, ending on "
                 "clean material depletion with the curve still running. It does not "
                 "fix R9's debut problem — load moved with session order, so nothing is "
                 "isolated — but it removes the rig-debut objection from the Rig 8 leg, "
                 "since the top is no longer new. Rig 5 remains the untested case the "
                 "watch_for wants. Held at observation.",
        ),
        Position(
            stated='July 29, 2026 (lunarz R6)',
            text="Eighth strain, and the off-Rig-6 leg widens from one top to two: the "
                 "same smoothed 440°F bounded hold that lhbh R9–R11 ran on Rig 8, now on "
                 "Rig 7's RBR, stopping on thinning vapor and satiety with material still "
                 "in the load. That answers the narrower objection to the Rig 8 leg — one "
                 "strain on one curve on one top — without touching the Rig 5 case the "
                 "watch_for actually wants. Worth recording that harshness was present "
                 "here and simply not the stopping condition (throat in cycle 1, chest in "
                 "cycle 2), the dbrb R1 / lhbh R8 shape rather than the clean "
                 "no-harshness shape of lhbh R9/R10 — the pattern is about what ends the "
                 "session, and this run is a cleaner example of that distinction than the "
                 "runs where harshness was simply absent. Load and cycle count both moved "
                 "from the plan, so load remains unisolated. Held at observation.",
        ),
        Position(
            stated='July 29, 2026 (lunarz R7)',
            text="The set's least-confounded instance, and it arrives as a same-evening "
                 "repeat of R6 with the setup untouched: same strain, same smoothed 440°F "
                 "curve, same Rig 7 top, only load and cycle count moved down. Stopped on "
                 "thinning vapor with under ten seconds left, harshness absent entirely — "
                 "the clean shape of lhbh R9/R10 rather than R6's harshness-present-but-"
                 "not-limiting shape, which means this jar has now produced both shapes on "
                 "the same curve and rig within one evening. That is worth more to the "
                 "entry than another strain would be: the pattern's weak point has always "
                 "been that its instances change several things at once, and this pair "
                 "changes almost nothing. The honest deflation is that a modest single "
                 "cycle is the pattern's easy case — a short session ending before "
                 "harshness is close to what a short session means — so R7 confirms the "
                 "direction without stressing it. Rig 5 remains the untested rig the "
                 "watch_for wants. Held at observation.",
        ),
        Position(
            stated='July 30, 2026 (fw106 R36)',
            text="Ninth strain, and the narrower thing it buys is on the Rig 8 leg: that "
                 "leg was three runs of one jar on one curve family, and it is now two "
                 "strains. The same objection lunarz R6 answered for the off-Rig-6 leg "
                 "generally — one strain, one top — is answered here for Rig 8 "
                 "specifically. The instance itself is ordinary: harshness present, small, "
                 "and not what ended the session, which was the load running out as the "
                 "curve reached its floor. Two deflations worth stating. A single cycle is "
                 "the easy case, the same caveat lunarz R7 carries. And the load depleting "
                 "at the exact moment the programmed cycle ended leaves the stopping "
                 "condition mildly ambiguous — material or clock — where the set's cleaner "
                 "instances (lhbh R10 at ~12s left, lunarz R7 at under 10s) stopped with "
                 "curve still running. Rig 5 remains the untested rig the watch_for wants. "
                 "Held at observation.",
        ),
    ],
    watch_for="A descent run on Rig 5 — the last untested rig; off-Rig-6 is two tops, and "
              "Rig 8 is now two strains. Holding load constant would isolate load; lunarz "
              "R6/R7 came closest and still moved cycles.",
    updated='Sessions 130, 131, 137, 152; rig corrections July 2, 2026; dbrb R1 July 9, 2026; papzp22 R8/R9 Session 169 (July 16, 2026); lhbh R8 Session 170 (July 17, 2026); oc R15 Session 172 (July 17, 2026); lhbh R9 July 28, 2026 — first instance off Rig 6; lhbh R10 July 28, 2026; lunarz R6 July 29, 2026 — eighth strain, first Rig 7 instance; lunarz R7 July 29, 2026 — least-confounded instance in the set; fw106 R36 July 30, 2026 — ninth strain',
)
