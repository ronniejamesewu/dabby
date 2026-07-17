from wisdom_core import *

ENTRY = WisdomEntry(
    key='chest-harshness-hot-open',
    kind='pattern',
    claim="In-session chest-located harshness on hot-open curves, Rig 6 — chest "
          "location documented across 9 hot-open runs; the chest-and-lingers "
          "conjunction is tracked separately (row B) and still rests on only 2 "
          "instances.",
    guidance="Chest location is the tracked signal here; persistence is tracked "
             "separately in row (B) — do not fold them together. Do not treat the "
             "chest-and-lingers conjunction as more than its 2 instances. Mechanism "
             "unresolved; the hot-open-delivers-deeper-aerosol reading is speculative "
             "— do not promote it to cause.",
    grade='observation',
    grade_basis="Low — chest location documented on 9 hot-open Rig 6 runs; Sour "
                "Tangie R3 the weakest (mild, resolved in-session), R7 the hottest "
                "open at 450°F and a first-dab instance.",
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
    ],
    counter_reading="The throat-and-chest counters (bp4rw13 R9/R11, Hive #1 R10) and "
                    "the load / dab-order / cycle confounds carried on nearly every "
                    "instance leave open that chest location co-varies with "
                    "within-session cumulative exposure rather than the hot open "
                    "itself — hot-open may be a proxy.",
    watch_for="A clean chest+lingers replication to move the conjunction off two "
              "instances.",
    updated="Sessions 137, 139; split July 11, 2026 audit; updated Sessions 158, 159, 160, 161, 162.; Session 164 merged July 15, 2026; Session 165 (July 15, 2026); Session 169 (July 16, 2026); Session 170 (July 17, 2026)",
)
