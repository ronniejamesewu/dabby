from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig7-saml-rbr',
    kind='equipment',
    claim="Rig 7 (Rig 6 + SAML RBR 'Refined Bell Recycler' wet top): conditions/cools "
          "vapor harder and didn't reduce the chest/heartburn facet across two runs; "
          "taste read splits (muted on R10, held on R7), no matched comparison.",
    guidance="Two runs, taste read unresolved — muted on R10, held on R7; the "
             "matched-load matched-curve test is still owed. Don't credit the RBR with "
             "preserving or costing taste as settled. As the first non-bubbler top it "
             "removes the forced slouch, making posture a variable — see "
             "chest-harshness-hot-open, thermal-injury-vapor-temp.",
    grade='observation',
    grade_basis="Two runs (papzp22 R10, bb362 R7), two strains, two curves — the taste "
                "reads split across them and no matched comparison exists; everything "
                "still confounded by load, clean state, posture, and strain.",
    evidence=[
        Citation(
            source='papzp22 R10',
            role='confirms',
            provenance='user-verbatim',
            gist="July 22, 2026 — RBR debut, grey 450°F bounded-hold descent, first dab, "
                 "large load, two cycles. Taste 'definitely muted' vs. loud on R8/R9 "
                 "(same curve, stock bubbler) — a clean within-strain read pointing at "
                 "the top, and the large load cuts the right way (a bigger scoop should "
                 "give more flavor, not less). Big effect, but the large load owns that, "
                 "so no potency read. Beige ultra-clean swab, confounded by a deep clean "
                 "done just before. Chest/heartburn came early and lingered despite the "
                 "extra cooling, and eased with upright posture in cycle 2.",
            confounds="Large load, fresh deep clean, posture change across cycles, two "
                      "cycles — nothing isolated; thumbprint load-zone lottery also live "
                      "on the flavor read.",
        ),
        Citation(
            source='bb362 R7',
            role='counters',
            provenance='user-verbatim',
            gist="July 23, 2026 — second run on the RBR (BB36 #2's last dab, purple "
                 "430°F descent, 4th dab). Flavor held big — \"no issue with flavor at "
                 "all,\" great throughout — where R10 read taste 'definitely muted.' "
                 "Not a matched comparison (different strain, cooler 430°F vs 450°F "
                 "open, heavy terpene load all favor flavor surviving), so it does not "
                 "overturn the mute read — but the recycler plainly did not cost this "
                 "flavor-standout jar its taste. Chest/heartburn present again, "
                 "consistent with the top not reducing that facet.",
            confounds="Different strain and curve than R10 — no matched-load "
                      "matched-curve comparison across the two tops yet; BB36 #2 is the "
                      "flavor-standout jar, so flavor surviving is expected regardless "
                      "of top; 4th dab.",
        ),
    ],
    positions=[
        Position(
            stated='Session 174 (July 22, 2026)',
            text="RBR debut. The wet top delivered on its design bet — muted taste, the "
                 "cleanest read available because R8/R9 ran this exact grey 450°F curve "
                 "on the stock bubbler with loud flavor, so the constant-curve / "
                 "changed-top contrast points at the RBR, and a large load throwing less "
                 "flavor points harder still. No potency conclusion: the big effect is "
                 "explained by the large load alone; matched loads across the two tops "
                 "are needed. The more consequential effect was indirect — as the first "
                 "non-bubbler top it removed the forced slouch and surfaced posture as a "
                 "chest-facet lever (chest/heartburn came earlier and lingered despite "
                 "harder cooling, then nearly cleared upright in cycle 2). One "
                 "heavily-confounded run.",
        ),
        Position(
            stated='July 23, 2026 (bb362 R7)',
            text="Second RBR run, and the taste read split: BB36 #2 R7 (the jar's "
                 "flavor standout) held its flavor fully on the RBR where papzp22 R10 "
                 "read 'definitely muted.' Not a refutation — different strain, a cooler "
                 "430°F vs 450°F open, and a heavy terpene load all cut toward flavor "
                 "surviving regardless of top — but the clean one-run mute read no "
                 "longer stands alone. The chest facet showed again (consistent with "
                 "R10). Still no matched-load matched-curve comparison across the two "
                 "tops; the muted-taste claim is now strain/curve-confounded rather than "
                 "a single clean signal. Held at observation.",
        ),
    ],
    counter_reading="Both runs are confounded and unmatched: R10's muted taste could "
                    "carry a thumbprint load-zone component, R7's held flavor is a "
                    "different strain at a cooler open, and the potency question is "
                    "unanswerable with loads unmatched. Direction only.",
    watch_for="A modest-load matched-curve RBR run to clean up taste and open the "
              "potency question; the upright-vs-slouched test (papzp22 R11) tying the "
              "chest change to posture, not the top.",
    updated='papzp22 R10 (July 22, 2026) — RBR debut; bb362 R7 (July 23, 2026) — second run, flavor held.',
)
