from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig8-calibear-fab-recycler',
    kind='equipment',
    claim="Rig 8 (Calibear Fab Recycler wet top): four runs, two strains. Read better than "
          "the RBR on lhbh; the one strain outside lhbh read flavor down against its own "
          "bubbler baseline. Chest on one of four. No matched pair.",
    guidance="Do not credit this top with flavor: the only bubbler comparison on it (fw106 "
             "R36) reads down, converging with papzp22 R10 on the RBR. Keep comparative and "
             "absolute reads apart — the \"still tasty\" runs had no bubbler beside them. "
             "Four runs, three tops, no matched pair. OPERATIONAL: flowback risks thermal "
             "shock.",
    grade='observation',
    grade_basis="Four runs (lhbh R9/R10/R11, fw106 R36), two strains, two curves. R36 "
                "brings the second strain and the first comparative flavor read but ran a "
                "curve new to that jar. None isolates the top.",
    evidence=[
        Citation(
            source='lhbh R9',
            role='confirms',
            provenance='user-verbatim',
            gist="July 28, 2026 — Rig 8 debut, 440°F 15s bounded hold descending "
                 "through 430°F at 35s to a 400°F floor, first dab, slightly larger "
                 "than normal load, three cycles. Pull \"very clearly heavier than "
                 "the rbr\"; flavor \"seemed better than rbr\"; no harshness at all, "
                 "throat or chest, during or after (both windows asked explicitly). "
                 "Beige to light golden swab, minimal residue after three trips to "
                 "440°F. Big effect. User's open question, recorded unresolved: why "
                 "a piece holding more water would read better on both flavor and "
                 "draw weight, against the expectation that water costs terpenes and "
                 "adds drag.",
            confounds="Rig debut with no matched comparison — this jar has never run "
                      "on the RBR, so the RBR contrast crosses strain, curve, and "
                      "session order as well as top. Curve was also new to the jar "
                      "(first 440°F run) and the load ran slightly large, so the "
                      "clean harshness read is not attributable to the top. Recycler "
                      "and bell differ in airpath geometry, not only water volume, "
                      "so \"more water\" may not be the operative variable.",
        ),
        Citation(
            source='lhbh R10',
            role='confirms',
            provenance='user-verbatim',
            gist="July 28, 2026 — same curve and rig as R9, second dab, moderate load, "
                 "single cycle stopped on depletion with ~12s left. No harshness at "
                 "all, throat or chest, asked in both windows. Beige swab, next to no "
                 "reclaim. Intensity a creeping medium. User's read on the top "
                 "strengthened but stayed hedged: \"I hate to say it because this is "
                 "cheap lazy glass but the function might be my favorite so far. Too "
                 "early to say without trying other strains.\"",
            confounds="Still no matched comparison — both Rig 8 runs are this strain on "
                      "this curve, and this jar has never run on the RBR. Load and "
                      "session order both moved from R9, so the pair isolates nothing "
                      "about the top; the milder session (one cycle, less material) "
                      "also makes its clean harshness read less surprising than R9's. "
                      "Light swab off a single cycle is expected independent of the "
                      "top, and minimal reclaim on an observed-depleted load is close "
                      "to tautological.",
        ),
        Citation(
            source='fw106 R36',
            role='counters',
            provenance='user-verbatim',
            gist="July 30, 2026 — the first strain on this top other than lhbh, which is "
                 "the test the R10 position's own hedge asked for (\"too early to say "
                 "without trying other strains\"). Orange smoothed 440°F bounded hold, "
                 "first dab, single cycle, load and cycle running out together at 60s. "
                 "Flavor \"noticeably less flavor than with stock bubbler\" — same "
                 "character, \"just less of whatever was there\" — volunteered unprompted "
                 "against a baseline this jar has thirty-five runs of. Beige-to-light-gold "
                 "swab, minimal reclaim, medium-high intensity. Very small base-of-throat "
                 "harshness about three-quarters through, not the stopping condition. No "
                 "chest.",
            confounds="The orange curve was new to fw106, so this is not a matched pair — "
                      "the nearest bubbler comparators are the R26–R30 gentle descents "
                      "(440→420@30s→400@60s). That confound cuts against a curve "
                      "explanation rather than for it (orange holds 440°F ~15s longer "
                      "before descending, which should front-load more terpene, not less), "
                      "but it is not eliminated. Load class never stated. First dab on a "
                      "single cycle, so the no-chest result sits in exposure-light "
                      "territory and discriminates nothing. Flavor is a subjective read on "
                      "a self-described non-discerning palate.",
        ),
    ],
    positions=[
        Position(
            stated='July 28, 2026 (lhbh R9)',
            text="Rig 8 debut. Acquired deliberately as a cheap read on recycler / "
                 "multi-path straight-flow function against the RBR's bell design, "
                 "with a better piece to follow if the function is worth it — an "
                 "obsolete design still in stock. The run came back the jar's "
                 "cleanest in nine (second no-harshness run ever, first since Run 1) "
                 "with a light minimal swab after three cycles, but the rig debut "
                 "sits on top of a new curve and a slightly large load, and the RBR "
                 "comparison is cross-strain and cross-curve. Nothing here isolates "
                 "the top. The one thing the run does establish independent of the "
                 "flavor question: this is the first hot-open run on a top that is "
                 "neither the stock bubbler nor the RBR — a third airpath and "
                 "posture condition — and it threw no chest signal in either window. "
                 "Held at observation on one run.",
        ),
        Position(
            stated='July 28, 2026 (lhbh R10)',
            text="The rerun the debut asked for came back clean again and the user's "
                 "read on the top strengthened, but it did not deliver the match it "
                 "was set up for: load and session order both moved, so R9 and R10 "
                 "isolate nothing between them. What the second run does buy is "
                 "narrower than it looks — it removes the new-glass objection (the top "
                 "is no longer novel) and it shows the clean harshness result was not "
                 "a one-off. It buys nothing at all on the flavor and draw-weight "
                 "claims, which are the whole reason the top was acquired, because "
                 "both remain single-strain single-curve impressions with no RBR run "
                 "on this jar to sit beside them. Two runs is not two data points on "
                 "the top. Held at observation.",
        ),
        Position(
            stated='July 28, 2026 (lhbh R11)',
            text="Third run, and the first thing on Rig 8 that is not clean: "
                 "chest/heartburn at the end of cycle 1, no throat harshness, a water "
                 "sip that only dampened it, and a return on cycle 2. This retires the "
                 "one claim the R9 position made independent of the flavor question — "
                 "that a third airpath and posture condition threw no chest signal in "
                 "either window. It held for two runs and did not survive the third. It "
                 "is not evidence against the top either: R11 was the 3rd dab of the "
                 "day on a larger load and ran a different (smoothed) curve, so the "
                 "cumulative-exposure reading covers it at least as well — see "
                 "chest-harshness-hot-open, where this run is the counter-reading's "
                 "strongest within-jar support. Separately the swab picture narrows: "
                 "R9 and R10's beige swabs looked like they might be a Rig 8 "
                 "signature, and R11's dark golden with normal reclaim puts the swab "
                 "back in the range this jar occupied for its first eight runs — the "
                 "two light swabs were the outliers, not a baseline. Three runs, one "
                 "strain, two curves, still no matched pair against either other top. "
                 "Held at observation.",
        ),
        Position(
            stated='July 30, 2026 (fw106 R36)',
            text="The second strain finally landed — the one the R10 position's hedge "
                 "explicitly asked for — and it went the other way on the only thing this "
                 "top was acquired to test. Fire Water #106 came off the orange 440°F hold "
                 "with flavor \"noticeably less\" than the stock bubbler, same character "
                 "and less of it, volunteered without being asked, against a bubbler "
                 "baseline thirty-five runs deep. The sharper point is about what kind of "
                 "read that is. This entry and rig7-saml-rbr have been treating \"flavor "
                 "held\" and \"flavor was down\" as votes in one tally, and they are not: "
                 "lhbh R9/R10, bb362 R7 and lunarz R6 are absolute reads — the material "
                 "tasted good — taken on jars with no comparison run beside them, while "
                 "papzp22 R10 and fw106 R36 are comparative reads against a bubbler "
                 "baseline in the same strain. Sorted that way the record is not split at "
                 "all: every time anyone has actually compared a recycler top to the "
                 "bubbler, the recycler read quieter, and that is now two strains across "
                 "two different recycler tops. Directional, and only that — R36's curve "
                 "was new to its jar, one comparative read per top is thin, and flavor is a "
                 "subjective read the user rates their own palate poorly on. What it does "
                 "settle is that this top has stopped being a flavor argument in its own "
                 "favour; the heavier pull is the impression still standing unchallenged. "
                 "Held at observation.",
        ),
    ],
    counter_reading="Everything attributed to the top is equally explained by the curve "
                    "(this jar's only 440°F bounded hold), the load, or session order — "
                    "and the RBR baseline it is compared against is itself two unmatched "
                    "runs on other strains whose taste read already splits. R10 does not "
                    "answer this: it repeats the same strain on the same curve, so it "
                    "confirms the pairing is reproducible without showing the top caused "
                    "any of it. A skeptic reads all three Rig 8 runs as ordinary runs on "
                    "one curve family — two good, one with chest at the 3rd-dab slot — "
                    "with the glass contributing nothing demonstrable in either "
                    "direction; a reading the user's own hedge (\"too early to say "
                    "without trying other strains\") anticipates. The comparative/absolute "
                    "sorting cuts the other way too: it rests on two runs, one per top, "
                    "neither matched, and fw106 R36 ran a curve new to its jar against "
                    "bubbler comparators on a different curve — so \"every comparison says "
                    "the recycler is quieter\" may just mean nobody has made a real "
                    "comparison yet.",
    watch_for="The matched comparison, dodged four times: fw106 R37 puts R36's curve and "
              "slot back on the bubbler; lhbh R12 sits against R11's cell on the RBR. Any "
              "flowback reaching the insert.",
    updated='lhbh R9 (July 28, 2026) — Rig 8 debut; lhbh R10 (July 28, 2026) — second run, no matched comparison yet; lhbh R11 (July 28, 2026) — first chest instance on this top; fw106 R36 (July 30, 2026) — second strain, flavor down vs bubbler.',
)
