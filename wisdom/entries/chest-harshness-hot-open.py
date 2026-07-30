from wisdom_core import *

ENTRY = WisdomEntry(
    key='chest-harshness-hot-open',
    kind='pattern',
    claim="In-session chest-located harshness on hot-open curves — chest "
          "location documented across 16 hot-open runs (13 Rig 6, 2 Rig 7, 1 Rig 8); "
          "the chest-and-lingers conjunction is tracked separately (row B) and rests on "
          "3 instances.",
    guidance="Chest location is the tracked signal here; persistence is tracked "
             "separately in row (B) — do not fold them together. Do not treat the "
             "chest-and-lingers conjunction as more than its 3 instances. Mechanism "
             "unresolved; the hot-open-delivers-deeper-aerosol reading is speculative "
             "— do not promote it to cause.",
    grade='observation',
    grade_basis="Low — chest location on 13 hot-open Rig 6 runs plus 2 on Rig 7 "
                "(papzp22 R10, lunarz R6) and 1 on Rig 8 (lhbh R11); Sour Tangie R3 the "
                "weakest, R7 the hottest open at 450°F and a first-dab instance.",
    evidence=[
        Citation(
            source='papzp22 R7',
            role='confirms',
            provenance='mixed',
            gist="June 27, 2026 — 440°F open → 400°F floor descent — \"It felt lower "
                 "in my chest than my normal throat\"; NO persistence statement in "
                 "the record — the post-session event was a productive hit on the "
                 "still-hot insert, i.e. material, not harshness.",
            confounds="First dab, larger load.",
        ),
        Citation(
            source='bp4rw13 R8',
            role='confirms',
            provenance='user-verbatim',
            gist="July 1, 2026 — same descent shape — \"a little bit of harshness, it "
                 "was in chest though. Late and after\" — chest + persisted, "
                 "user-verbatim.",
            confounds="Second dab, normal load.",
        ),
        Citation(
            source='lunarz R1',
            role='confirms',
            provenance='user-verbatim',
            gist="July 10, 2026 — bounded 10s-440°F hold then gentle descent — chest "
                 "harshness on the second cycle, \"it lingered\".",
            confounds="Jar opener, 3rd dab, slightly-larger load.",
        ),
        Citation(
            source='sourtangie R3',
            role='confirms',
            provenance='ai-authored',
            gist="July 11, 2026 — bounded 10s-440°F hold then gentle descent — mild "
                 "throat-and-chest harshness in cycle 1 that resolved by the second "
                 "cycle and did not return on the spent-material hot-air draw; chest "
                 "location, in-session only, no persistence — a weak instance, mild "
                 "and self-resolving. Provenance untagged in source.",
            confounds="First dab, two cycles.",
        ),
        Citation(
            source='lunarz R2',
            role='confirms',
            provenance='ai-authored',
            gist="July 11, 2026 — 430°F bounded hold then descent — mild-to-medium "
                 "heartburn-like chest harshness in cycle 1, resolved by water "
                 "between cycles, no persistence; first chest instance below a 440°F "
                 "peak. Provenance untagged in source.",
            confounds="3rd dab, large load.",
        ),
        Citation(
            source='lunarz R3',
            role='confirms',
            provenance='ai-authored',
            gist="July 12, 2026 — 430°F bounded hold then descent — mild-to-medium "
                 "chest harshness ~30s into cycle 1; a water sip reduced but did not "
                 "eliminate it, a muddy partial-persistence-despite-water case, not a "
                 "clean chest-and-lingers instance. Provenance untagged in source.",
            confounds="4th consecutive dab of a continuous night, normal load.",
        ),
        Citation(
            source='sourtangie R5',
            role='confirms',
            provenance='ai-authored',
            gist="July 12, 2026 — teal 430°F bounded-hold descent — escalating "
                 "mild→medium chest-and-throat harshness that a water sip did *not* "
                 "clear; in-session, no persistence reported, so chest-location only, "
                 "another below-440 chest instance like LunarZ R2/R3. Provenance "
                 "untagged in source.",
            confounds="2nd dab, bigger-than-normal load, two cycles.",
        ),
        Citation(
            source='sourtangie R6',
            role='confirms',
            provenance='ai-authored',
            gist="July 12, 2026 — teal 430°F bounded-hold descent — harshness built "
                 "from ~20s left in cycle 1 to a solid medium in cycle 2, "
                 "throat-and-chest; no water taken; in-session, no persistence "
                 "reported, so chest-location only, another below-440 instance like "
                 "LunarZ R2/R3 and Sour Tangie R5. Provenance untagged in source.",
            confounds="3rd dab, two cycles.",
        ),
        Citation(
            source='sourtangie R7',
            role='confirms',
            provenance='ai-authored',
            gist="July 13, 2026 — grey 450°F bounded-hold + shorter descent — "
                 "throat-and-chest harshness present alongside a distinct terpene-load "
                 "cough the user explicitly separated as its own mechanism; "
                 "in-session, no persistence reported, so chest-location only; the "
                 "hottest open logged for the group at 450°F, and a first-dab "
                 "instance. Provenance untagged in source.",
            confounds="First dab, two cycles, bigger-than-modest load — chest "
                      "location without the later-dab order confound R5/R6 carried, "
                      "though two cycles and a bigger load keep within-session "
                      "cumulative exposure live.",
        ),
        Citation(
            source='bp4rw13 R9',
            role='counters',
            provenance='ai-authored',
            gist="throat and chest, resolved with water. Provenance untagged in "
                 "source.",
            confounds="none noted",
        ),
        Citation(
            source='bp4rw13 R11',
            role='counters',
            provenance='ai-authored',
            gist="throat and chest, no persistence *reported* — same "
                 "absence-of-statement standard as papzp22 R7. Provenance untagged in "
                 "source.",
            confounds="none noted",
        ),
        Citation(
            source='hive1 R10',
            role='counters',
            provenance='ai-authored',
            gist="throat-and-chest at end of draw 2, eased off on draw 3. Provenance "
                 "untagged in source.",
            confounds="none noted",
        ),
        Citation(
            source='sourtangie R9',
            role='counters',
            provenance='ai-authored',
            gist="July 14, 2026 — first hot-open Rig 6 run on this jar with no chest "
                 "at all: a clean modest single-cycle first dab (450°F, beige swab). "
                 "(provenance untagged in source)",
            confounds="The draw-technique read is confounded — short draws co-vary "
                      "with thinner vapor (density); modest load.",
        ),
        Citation(
            source='sourtangie R10',
            role='counters',
            provenance='ai-authored',
            gist="July 14, 2026 — bigger load over two cycles but short draws through "
                 "the dense phase; still no chest. (provenance untagged in source)",
            confounds="Short draws co-vary with thinner vapor (density); the "
                      "hard-draw-on-a-full-load cell stays untested — R10's only long "
                      "draw hit a spent insert.",
        ),
        Citation(
            source='sourtangie R11',
            role='counters',
            provenance='user-verbatim',
            gist="July 15, 2026 — grey 450°F bounded-hold + shorter descent, first "
                 "dab, modest load, single cycle — clean, no chest, despite *long* "
                 "draws (the short-draw plan was forgotten). The "
                 "long-draw-through-a-present-modest-cycle cell R9/R10 never "
                 "isolated; staying clean weakens draw length as what keeps chest "
                 "away.",
            confounds="Modest load, single cycle — a present cycle but not a full "
                      "load; the hard-draw-on-a-full-load cell stays untested.",
        ),
        Citation(
            source='sourtangie R12',
            role='counters',
            provenance='user-verbatim',
            gist="July 15, 2026 — same grey 450°F curve, larger two-cycle load, "
                 "throat-only mild harshness in the last third of cycle 1, no chest "
                 "— sits in the R7/R8 load/cycle territory that threw chest and "
                 "stayed chest-free.",
            confounds="2nd dab, larger taffy load (imprecise portioning), two cycles.",
        ),
        Citation(
            source='sourtangie R13',
            role='counters',
            provenance='user-verbatim',
            gist="July 15, 2026 — same grey 450°F curve, normal load, throat "
                 "harshness building (read as day-accumulation), no chest.",
            confounds="3rd dab, two cycles (stopped one hit into the second).",
        ),
        Citation(
            source='papzp22 R8',
            role='counters',
            provenance='user-verbatim',
            gist="July 16, 2026 — grey 450°F bounded-hold descent, first run of "
                 "this curve on the strain — 'no harshness' at all, and no chest "
                 "during or after (post-session window confirmed at logging); the "
                 "Sour Tangie R9/R11 clean modest-single-cycle cell reproducing on "
                 "a second strain.",
            confounds="2nd dab; load per plan (modest) — not restated by user.",
        ),
        Citation(
            source='papzp22 R9',
            role='counters',
            provenance='user-verbatim',
            gist="July 16, 2026 — grey 450°F cycle 1 into a teal 430°F cycle 2 — "
                 "mild throat-only harshness, no chest during or after either of "
                 "the day's sessions (asked at logging); normal load, two cycles, "
                 "3rd dab — the load/cycle/order territory that has thrown chest "
                 "elsewhere, staying chest-free.",
            confounds="Chest not asked at session time — the during-session "
                      "negative rests on the throat-stated location plus the "
                      "logging-time ask (retroactive-ask provenance).",
        ),
        Citation(
            source='lhbh R8',
            role='counters',
            provenance='user-verbatim',
            gist="July 17, 2026 — grey 450°F bounded-hold descent, this jar's "
                 "first hot open — 'Throat harshness' when asked throat vs chest; "
                 "no chest in-session on a big-load, 3.5-cycle first dab, the "
                 "load/cycle territory that has thrown chest elsewhere. "
                 "Post-session window asked but not answered — logged as not "
                 "stated, not as a checked negative.",
            confounds="First dab; big load; 3.5 cycles; heavy terpene-load "
                      "coughing masked harshness reads.",
        ),
        Citation(
            source='sourtangie R15',
            role='confirms',
            provenance='user-verbatim',
            gist="July 19, 2026 — grey 450°F bounded-hold descent, first dab, normal "
                 "load, single cycle — \"slight heartburn about halfway through\" and, "
                 "asked, \"in session and after\": chest/heartburn present in-session "
                 "AND persisting past session end. The 3rd chest-and-lingers "
                 "conjunction instance (after bp4rw13 R8, LunarZ R1) and the "
                 "least-confounded of the three — the clean replication the watch_for "
                 "called for.",
            confounds="First dab, normal load, single cycle — the cleanest conjunction "
                      "instance yet; heavy terpene coughing alongside.",
        ),
        Citation(
            source='lunarz R4',
            role='counters',
            provenance='user-verbatim',
            gist="July 19, 2026 — 430°F 15s extended-hold descent (\"purple\"), 2nd "
                 "dab, large load, three cycles — no chest/heartburn at all, the first "
                 "LunarZ run of four without it; throat-only \"super dry\" harshness "
                 "that a water sip reset. A no-chest instance on a large load, where "
                 "the load-drives-chest read predicts chest.",
            confounds="2nd dab, large load, three cycles; heavy terpene coughing may "
                      "have masked a harshness read (LHBH R8 precedent).",
        ),
        Citation(
            source='lunarz R5',
            role='confirms',
            provenance='user-verbatim',
            gist="July 19, 2026 — same purple 430°F 15s extended-hold descent, 3rd "
                 "dab, normal load, 2.5 cycles — chest/heartburn plus "
                 "bottom-of-throat harshness, in-session, no persistence reported → "
                 "chest-location only. Paired with R4 same day/curve/rig: chest on the "
                 "later normal-load dab, absent on the earlier large-load dab.",
            confounds="3rd dab, normal load, 2.5 cycles; persistence not "
                      "asked/reported.",
        ),
        Citation(
            source='oc R15',
            role='confirms',
            provenance='user-verbatim',
            gist="July 17, 2026 — \"purple\" 430°F 15s-hold descent, big (~double) "
                 "load, two cycles, 2nd dab — chest/heartburn present with no throat "
                 "component, did not climb, softened partially with water and resolved "
                 "post-session (in-session only, no persistence → chest-location only, "
                 "does not add to the conjunction). A new strain (OC's first "
                 "descent/hot-open ever) and a below-440 chest instance like LunarZ "
                 "R2/R3/R5 and Sour Tangie R5/R6.",
            confounds="2nd dab, big load, two cycles — chest on a 2nd-dab big-load "
                      "run; load×cycle cumulative exposure is the common thread with "
                      "the other below-440 instances.",
        ),
        Citation(
            source='fw106 R32',
            role='confirms',
            provenance='user-verbatim',
            gist="July 20, 2026 — grey 450°F bounded-hold descent, FW106's debut on "
                 "the curve and its first chest instance — heartburn set in after "
                 "cycle 1 during gag-level terpene coughing; hottest open FW106 has "
                 "run. A new strain in the group, confirming occurrence without "
                 "isolating the open as cause.",
            confounds="First dab, large load, two cycles — the cumulative-exposure "
                      "territory the counter-reading names; post-cycle onset during "
                      "violent coughing (cough-provoked reflux not excluded); "
                      "cough-vs-heat asked at logging, not disambiguated.",
        ),
        Citation(
            source='papzp22 R10',
            role='confirms',
            provenance='user-verbatim',
            gist="July 22, 2026 — grey 450°F bounded-hold descent, Rig 7 (SAML RBR wet "
                 "top) debut, first dab, large load, two cycles — chest/heartburn onset "
                 "early (~8s, at the 450°F peak, the jar's earliest) and lingering after "
                 "session end; a water sip only partially reduced it. First chest "
                 "instance on a non-bubbler top, and the first where posture varied "
                 "within the session: cycle 1 in the old slouch threw the heartburn, "
                 "cycle 2 deliberately upright showed next to no added heartburn.",
            confounds="New rig/top (RBR debut) and posture both introduced this run; "
                      "large load, two cycles; cycle-2 relief confounds posture with "
                      "water and cycle depletion. Technically satisfies chest-and-lingers "
                      "but is the most confounded such instance — not firmed into the "
                      "conjunction.",
        ),
        Citation(
            source='lhbh R11',
            role='confirms',
            provenance='user-verbatim',
            gist="July 28, 2026 — smoothed 440°F bounded-hold descent (the 35s corner "
                 "removed, so a cooler middle than Runs 9–10), Rig 8 (Calibear Fab "
                 "Recycler wet top), 3rd dab, larger-than-normal load, two cycles. "
                 "Chest/heartburn at the end of cycle 1, no throat harshness at any "
                 "point; a water sip dampened it and cycle 2 brought it back; \"faded "
                 "slowly after session.\" This jar's first chest instance in eleven "
                 "runs and the first on a third airpath/posture condition (neither the "
                 "stock bubbler nor the RBR).",
            confounds="3rd dab of the day and a larger-than-normal load both moved "
                      "toward this run — squarely the cumulative-exposure territory the "
                      "counter-reading names. Post-session read is a slow fade rather "
                      "than persistence, the same shape as OC R15, which was not "
                      "counted toward the conjunction — not counted here either, so "
                      "n=3 is unchanged.",
        ),
        Citation(
            source='lunarz R6',
            role='confirms',
            provenance='user-verbatim',
            gist="July 29, 2026 — smoothed 440°F bounded-hold descent (\"orange\"), Rig 7 "
                 "(SAML RBR wet top), FIRST dab of the day, larger-than-normal load, two "
                 "cycles. Cycle 1 throat-only and explicitly not chest (\"tiny bit of "
                 "harshness at base of throat. Hasn't gone to chest\"); heartburn arrived "
                 "during cycle 2 alongside the throat harshness and cleared after a few "
                 "drinks of water. This jar's first genuine first dab in six runs — Runs "
                 "1–5 were all 2nd-dab-or-later — and chest came anyway, removing "
                 "between-dab day accumulation as the explanation the R4/R5 pair pointed "
                 "at. Cycle-2 onset after a chest-free cycle 1 leaves within-session "
                 "cumulative exposure intact. Also a first-dab instance on the smoothed "
                 "440°F curve, though on a different strain and top than lhbh R11.",
            confounds="Three variables moved off the planned test at once — curve "
                      "(smoothed 440°F rather than the purple 430°F), top (Rig 7 rather "
                      "than Rig 6), and load (larger-than-normal rather than modest) — so "
                      "the 440°F open is neither implicated nor cleared, and this is not "
                      "the clean modest single-cycle LunarZ run the watch_for asked for. "
                      "Two cycles and a larger load keep within-session exposure live. "
                      "Heavy terpene coughing again (as lunarz R4), here during the "
                      "chest-free cycle 1.",
        ),
        Citation(
            source='lunarz R7',
            role='counters',
            provenance='user-verbatim',
            gist="July 29, 2026 — the same smoothed 440°F bounded hold (\"orange\") on the "
                 "same Rig 7 RBR as R6, three and a half hours later: modest load, single "
                 "cycle, 2nd dab of the day. \"No harshness\" — none anywhere, throat or "
                 "chest, asked directly. The closest matched pair this entry holds: strain, "
                 "curve and top all held from the immediately preceding run, with only load "
                 "and cycle count moved down — and the dab slot moved the *wrong* way for a "
                 "cumulative-day reading, since R6 threw chest on a first dab and R7 stayed "
                 "clean on a second. Supplies the modest-single-cycle half of the cell the "
                 "watch_for asked for.",
            confounds="Load and cycle count moved together, so neither is isolated. Not the "
                      "first-dab modest single cycle the watch_for wants — R6 gave the "
                      "first dab, R7 gives the modest single cycle, and no run has given "
                      "both. Single cycle also means low within-session exposure by "
                      "construction, which is the counter-reading's own prediction rather "
                      "than an independent test of it.",
        ),
    ],
    positions=[
        Position(
            stated='July 11, 2026 audit',
            text="Split from the old \"chest-located, persisting\" row after the "
                 "audit found its core claim overstated: it asserted \"Both "
                 "confirming instances (papzp22 R7, bp4rw13 R8) ... persisted past "
                 "when the heating cycle ended,\" but papzp22 R7's record contains no "
                 "persistence statement in any field (its own analysis calls it "
                 "\"Two separable signals\" — late onset + chest location — never "
                 "persistence). Chest location is the tracked signal here; "
                 "persistence is tracked separately in row (B). All Rig 6; mechanism "
                 "unresolved (hot open delivering denser aerosol deeper into the "
                 "airway is speculative). Watch for a clean chest+lingers replication "
                 "to move the conjunction off two instances.",
        ),
        Position(
            stated='Sessions 158-162',
            text="The chest-AND-lingers *conjunction* still has exactly 2 verbatim "
                 "instances (bp4rw13 R8, LunarZ R1) — LunarZ R2 didn't linger, LunarZ "
                 "R3 only partially persisted despite water, and Sour Tangie R5, R6, "
                 "and R7 reported no persistence, so none cleanly adds to the "
                 "conjunction.",
        ),
        Position(
            stated='Session 164 (July 14, 2026)',
            text="Sour Tangie R9/R10 (July 14, 2026) are the first hot-open Rig 6 runs "
                 "on this jar with no chest at all — R9 a clean modest single-cycle "
                 "first dab (450°F, beige swab), R10 a bigger load over two cycles but "
                 "short draws through the dense phase; boundary condition — chest is "
                 "not obligatory on a hot open, it is absent when the draws stay short. "
                 "The chest/heartburn-quality component is now tracked against the "
                 "participant's esophageal anatomy as candidate locus (mechanism kept "
                 "out of rendered fields — see Do-Not-Re-Litigate in the handoff notes; "
                 "detail in a separate private writeup). Counter-reading: the "
                 "draw-technique read is confounded — short draws co-vary with thinner "
                 "vapor (density), and the hard-draw-on-a-full-load cell stays untested "
                 "(R10's only long draw hit a spent insert) — directional, not "
                 "established. [Transposed verbatim from the Session 164 row update "
                 "during the July 15 migration merge.]",
        ),
        Position(
            stated='Session 165 (July 15, 2026)',
            text="Sour Tangie R11–R13 extend the chest absence to five straight "
                 "(R9–R13) across modest-to-larger loads and one/two cycles. R11 "
                 "drew *long* through a present modest cycle and stayed clean, so "
                 "draw length is no longer the leading explanation for the absence "
                 "— the R9/R10 draw-technique read is weakened. What flipped at R9 "
                 "and has held: the insert deep-clean and the material beginning to "
                 "cure, two changes that moved together (confounded); intermittent "
                 "chest is also consistent with noise (R4, pre-clean, was itself "
                 "chest-free, so the boundary isn't absolute). The deep-clean/curing "
                 "coincidence is the live candidate at observation weight; the "
                 "no-provoke test is whether chest re-emerges as insert residue "
                 "rebuilds before the next deep clean. Separately, within-day "
                 "*throat* harshness (distinct from the chest facet) escalated R11 "
                 "clean → R12 mild → R13 building, consistent with within-day "
                 "cumulative exposure.",
        ),
        Position(
            stated='Session 169 (July 16, 2026)',
            text="papzp22 R8/R9 (July 16, 2026) put the no-chest boundary on a "
                 "second strain: the grey 450°F bounded-hold descent ran a modest "
                 "single-cycle 2nd dab (R8) and a normal-load two-cycle 3rd dab "
                 "(R9) with no chest during or after — R9's post-session window "
                 "explicitly checked at logging, the first checked negative in the "
                 "window where Sour Tangie R14's chest arrived. Consistent with "
                 "the counter-reading (chest co-varies with load/cycle/residue, "
                 "not the hot open itself); papz's own R7 chest instance was its "
                 "larger-load descent.",
        ),
        Position(
            stated='Session 170 (July 17, 2026)',
            text="lhbh R8 puts the no-chest boundary on a third strain — a "
                 "big-load, 3.5-cycle first dab at a 450°F open with throat-only "
                 "harshness. Unlike papzp22 R9, the post-session window was asked "
                 "and not answered, so it stays a location-only counter, not a "
                 "checked negative.",
        ),
        Position(
            stated='Session 171 (July 19, 2026)',
            text="Sour Tangie R15 is the clean chest-and-lingers replication the "
                 "watch_for called for — the conjunction moves from 2 to 3 instances "
                 "(bp4rw13 R8, LunarZ R1, Sour Tangie R15), and R15 is the "
                 "least-confounded of the three (first dab, normal load, single "
                 "cycle). Held at observation regardless: n=3 is still thin and the "
                 "mechanism is unresolved. Separately, LunarZ R4/R5 are a within-day "
                 "pair on the same purple 430°F 15s extended-hold descent, same rig: "
                 "chest absent on R4 (2nd dab, large load) and present on R5 (3rd dab, "
                 "normal load) — chest tracked the later dab slot / cumulative "
                 "day-exposure, not the bigger load, supporting the counter-reading "
                 "that chest co-varies with cumulative session exposure rather than "
                 "the hot open or per-dab load. Confound: R4's heavy terpene coughing "
                 "may have masked its chest.",
        ),
        Position(
            stated='Session 172 (July 17, 2026)',
            text="oc R15 adds Orange Candy as a new chest-location strain (430°F "
                 "15s-hold \"purple\" descent, 2nd dab, big load, two cycles; chest "
                 "with no throat, in-session only — does not add to the conjunction). "
                 "A 2nd-dab big-load run throwing chest cuts mildly against the "
                 "LunarZ R4/R5 day-position-not-load read; cumulative load×cycle "
                 "exposure reconciles both. 430°F isn't hot, so this stays consistent "
                 "with the counter-reading that hot-open is a proxy for exposure.",
        ),
        Position(
            stated='Session 173 (July 20, 2026)',
            text="FW106 R32 puts a new strain in the hot-open chest group — its first "
                 "chest/heartburn instance, on the grey 450°F curve's FW106 debut. It "
                 "confirms occurrence on a new strain but isolates nothing: large load "
                 "+ two cycles is exactly the cumulative-exposure territory the "
                 "counter-reading names, onset was post-cycle-1 during gag-level "
                 "coughing (cough-provoked reflux not excluded), and the cough-vs-heat "
                 "question was asked at logging and left undisambiguated. Not a "
                 "conjunction instance — persistence past session end wasn't "
                 "established, so the n=3 chest-and-lingers count is unchanged. Held at "
                 "observation. The next FW106 run repeats the curve as a first-dab "
                 "modest single cycle — the clean isolation that shed chest on Sour "
                 "Tangie R9/R11 and papzp22 R8.",
        ),
        Position(
            stated='Session 174 (July 22, 2026)',
            text="papzp22 R10 is the first chest instance on a non-bubbler top (Rig 7, "
                 "SAML RBR wet top). Two updates. (1) The RBR cools/conditions the vapor "
                 "harder than the bubbler, yet chest/heartburn came earlier (~8s, at the "
                 "450°F peak — the jar's earliest chest onset) and lingered — the "
                 "opposite of what a hot-vapor-on-tissue driver predicts (see "
                 "thermal-injury-vapor-temp). (2) Posture surfaced as a newly-visible "
                 "candidate: every prior chest instance across this jar, Sour Tangie, and "
                 "LunarZ ran on the stock bubbler, which forces a slouched, chin-down "
                 "posture — posture was a hidden constant, never a variable. On the RBR "
                 "the user need not hunch; cycle 1 in the old body-memory slouch threw "
                 "the heartburn, cycle 2 deliberately upright showed next to none. The "
                 "user's mechanism: slouching keeps some of the draw from fully reaching "
                 "the lungs, routing vapor toward the esophageal/chest locus already "
                 "tracked as the candidate site. One heavily-confounded session (new top, "
                 "posture, water, and cycle depletion all moved together) — a direction, "
                 "not a finding. R10 also technically satisfies chest-and-lingers but is "
                 "the most confounded such instance, so the conjunction stays at 3. Held "
                 "at observation. Discriminating test (papzp22 R11, next_ai_analysis): "
                 "posture should beat temperature and load — an upright, breath-conscious "
                 "grey run on the RBR with no water should come back chest-free; a "
                 "deliberately slouched run at a lower, cooler endpoint should bring it "
                 "back.",
        ),
        Position(
            stated='July 28, 2026 (lhbh R11)',
            text="The strongest within-jar support the counter-reading has yet drawn, "
                 "and it comes from the curve moving the wrong way. lhbh R9, R10 and "
                 "R11 are three consecutive runs on the same rig (Rig 8) at dab slots "
                 "1, 2 and 3; chest appeared only on the third — and R11 ran the "
                 "*cooler* curve, the smoothed 440°F descent whose corner removal cut "
                 "roughly nine seconds off the time at or above 430°F per cycle and "
                 "lowered the integrated time above 400°F below both R9 and R10. A "
                 "hot-open or peak-dwell driver predicts the opposite ordering. Load "
                 "also rose on R11, so dab slot and load remain unseparated (as they "
                 "have all jar), but the curve — the one variable deliberately changed "
                 "— is the least likely of the three. Chest location count 14 → 15; "
                 "first instance on a third airpath/posture condition, which also means "
                 "the Rig 8 entry's \"no chest in either window\" reading from R9/R10 no "
                 "longer holds for the top. Conjunction unchanged at 3: the "
                 "post-session read was a slow fade, the OC R15 shape, not persistence. "
                 "Held at observation.",
        ),
        Position(
            stated='July 29, 2026 (lunarz R6)',
            text="The dab-slot reading this entry drew from LunarZ R4/R5 does not "
                 "survive its own jar. R6 is LunarZ's first genuine first dab in six "
                 "runs — R1–R5 were all 2nd-dab-or-later, which is why the Session 171 "
                 "position could read chest as tracking the later slot / within-day "
                 "cumulative exposure — and chest came anyway. Between-dab day "
                 "accumulation is therefore not necessary for chest on this strain. What "
                 "survives is the narrower within-session version of the counter-reading: "
                 "cycle 1 was throat-only and explicitly chest-free, and the heartburn "
                 "arrived during cycle 2 on a larger-than-normal load, so exposure "
                 "accumulating inside the session still fits. Three variables moved off "
                 "the planned test together (curve, top, load), so the 440°F open is "
                 "neither implicated nor cleared, and this is not the clean modest "
                 "single-cycle run the watch_for wanted — that cell is still owed and is "
                 "now what LunarZ R7 is set against, cut to a single cycle. Chest "
                 "location count 15 → 16; second Rig 7 instance. Conjunction unchanged at "
                 "3: the chest cleared with water rather than persisting. Held at "
                 "observation.",
        ),
        Position(
            stated='July 29, 2026 (lunarz R7)',
            text="The cleanest support the counter-reading has drawn anywhere in the log, "
                 "and it arrived the same evening as R6. R6 and R7 are the same strain, the "
                 "same smoothed 440°F curve and the same Rig 7 top, three and a half hours "
                 "apart: R6 threw chest in cycle 2 on a larger-than-normal load, R7 came "
                 "back with no harshness at all on a modest load and a single cycle. Every "
                 "other pair this entry cites moves curve, strain, top or rig alongside the "
                 "condition of interest; this one does not. Two readings die on it and one "
                 "survives. Dab slot dies — the later dab was the clean one, which R6 had "
                 "already weakened by throwing chest on a first dab and R7 now closes from "
                 "the other side. The 440°F open dies as sufficient — the identical open "
                 "ran chest-free. What survives is within-session cumulative exposure, "
                 "which is the only variable that moved in the direction the outcome did. "
                 "Held at observation, and the honest limit is that load and cycle count "
                 "moved together, so the pair points at exposure without resolving whether "
                 "it is the material, the time at temperature, or the number of draws. "
                 "Chest-location count unchanged at 16. The watch_for cell is still not "
                 "whole: R6 supplied the first dab, R7 supplied the modest single cycle, "
                 "and no LunarZ run has yet supplied both. Worth generalizing beyond this "
                 "jar: a same-evening repeat holding strain, curve and top fixed and "
                 "moving only load and cycle count is the shape that produced this, and it "
                 "is cheap to reproduce in any jar — most of the entry's twenty-eight "
                 "citations would have been worth more if they had been half of a pair "
                 "like it.",
        ),
    ],
    counter_reading="The throat-and-chest counters (bp4rw13 R9/R11, Hive #1 R10) and "
                    "the load / dab-order / cycle confounds carried on nearly every "
                    "instance leave open that chest location co-varies with "
                    "within-session cumulative exposure rather than the hot open "
                    "itself — hot-open may be a proxy.",
    watch_for="More chest-and-lingers instances to firm n=3; a LunarZ run that is both a "
              "first dab and a modest single cycle — R6 and R7 each gave one half; a "
              "first-dab smoothed-440°F run within lhbh.",
    updated="Sessions 137, 139; split July 11, 2026 audit; updated Sessions 158, 159, 160, 161, 162.; Session 164 merged July 15, 2026; Session 165 (July 15, 2026); Session 169 (July 16, 2026); Session 170 (July 17, 2026); Session 171 (July 19, 2026); oc R15 Session 172 (July 17, 2026); fw106 R32 Session 173 (July 20, 2026); papzp22 R10 Session 174 (July 22, 2026); lhbh R11 July 28, 2026 — chest location 14 → 15; lunarz R6 July 29, 2026 — chest location 15 → 16, first-dab instance retires the day-slot reading; lunarz R7 July 29, 2026 — counter, the R6/R7 matched pair",
)
