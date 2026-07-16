from wisdom_core import *

ENTRY = WisdomEntry(
    key='rig5-dual-ruby',
    kind='equipment',
    claim="Rig 5 (sapphire + two 5mm ruby pearls): draw-3 harshness consistent "
          "at 416°F, mechanism unresolved; a 425°F endpoint resolves the "
          "within-draw density drop for LHBH and papzp22 but appears "
          "material-specific; sapphire retains heat post-cycle.",
    guidance="Treat draw-3 harshness onset at 416°F as consistent but not "
             "mechanistically settled. Do not assume the 425°F density-drop fix "
             "generalizes beyond LHBH and papzp22. At elevated temperatures read "
             "session character, not swab color. Sapphire heat retention applies "
             "to rigs 3, 4, 5.",
    grade='directional',
    grade_basis="Moderate — sixteen runs, five strains; draw-3 harshness pattern "
                "consistent; FW106 R11-12 first above-ceiling points; LHBH "
                "R2/papzp22 R2 confirmed endpoint fix; FW106 R18 counters.",
    evidence=[
        Citation(
            source='watermellos R2',
            role='confirms',
            provenance='ai-authored',
            gist="Watermellos R2–R4 (May 25, 2026 — beige swabs; R4: rig and "
                 "curve held constant, draws 1–2 clean, harshness entered on "
                 "exactly draw 3 at 14s remaining). [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='lhbh R2',
            role='confirms',
            provenance='ai-authored',
            gist="LHBH R2 and papzp22 R2 (June 13–14, 2026 — within-draw density "
                 "drop at 420°F resolved at 425°F on both strains, ramp held "
                 "constant). [provenance untagged in source]",
            confounds="none noted",
        ),
        Citation(
            source='fw106 R18',
            role='counters',
            provenance='ai-authored',
            gist="FW106 R18–R19 (June 15, 2026 — density drop persisted at 425°F; "
                 "harshness escalated draw-by-draw with density high throughout). "
                 "[provenance untagged in source]",
            confounds="Short draw technique a plausible confound; single run.",
        ),
        Citation(
            source='fw106 R11',
            role='confirms',
            provenance='ai-authored',
            gist="FW106 R11–R12 (June 5, 2026 — programmed 460°F not reached at "
                 "the 40s terminus, estimated high-440s actual; toasty taste, "
                 "light gold swab, repeated on 2nd dab). [provenance untagged in "
                 "source]",
            confounds="Programmed 460°F not reached at the 40s terminus (sapphire "
                      "thermal lag); actual endpoint estimated high-440s, not measured.",
        ),
        Citation(
            source='fw106 R3',
            role='context',
            provenance='ai-authored',
            gist="plus eleven further runs (FW106 R3, R13, R17; WM R9–R11; BB36 "
                 "#2 R2; OC R13–R14; LHBH R1; papzp22 R1) — see the frozen "
                 "analyses. [provenance untagged in source]",
            confounds="none noted",
        ),
    ],
    positions=[
        Position(
            stated='May 25 – June 15, 2026 (observed effect)',
            text="Dual ruby pearls on the sapphire insert. (1) Harshness "
                 "entering around draw 3 is consistent at 416°F — mechanism "
                 "unresolved (see Session 99 epistemic audit and Tail Harshness "
                 "Mechanism). (2) Inaugural WM R2 swab was beige — lighter than "
                 "Rig 4's golden on the same strain and curve; whether dual pearl "
                 "vaporizes more completely or the difference is draw-count-driven "
                 "remains unresolved — the Rig 4→5 comparison at same draw count "
                 "still hasn't happened. (3) FW106 R3's clean beige matched "
                 "FW106's Rig 4 pattern — first same-strain cross-rig swab "
                 "comparison, supports swab character being strain-specific rather "
                 "than rig-driven; WM R9 held clean beige even at a 460°F descent "
                 "open, consistent with the floor-indicator framing. (4) "
                 "Post-session heat retention (BB36 #2 R2 — productive draws into "
                 "cooldown to ~390°F): sapphire's higher thermal mass (~5x quartz) "
                 "holds temperature after the heating cycle ends; applies to all "
                 "sapphire rigs (3, 4, 5).",
        ),
        Position(
            stated='Through July 2, 2026 (notes)',
            text="Within-draw density drop at the 420°F baseline appeared on "
                 "multiple strains (LHBH R1, papzp22 R1 — same dense-then-wispy "
                 "pattern as Rig 4 FW106 R16; earlier, wispy vapor with material "
                 "remaining on BB36 #2 and OC at the prior baseline, where ramp "
                 "and endpoint changed together so faster ramp and/or higher "
                 "endpoint was the best framing available). LHBH R2 is the "
                 "cleanest isolation yet of endpoint temperature as the driver — "
                 "same 8s ramp, endpoint up 5°F, dropoff gone, ruling out pearl "
                 "count and ramp speed for that strain; papzp22 R2 confirmed the "
                 "fix on a second strain. FW106 R18 counters — the drop persisted "
                 "at 425°F (short draw technique a plausible confound; single "
                 "run) — and WM R10's fast-ramp improvement did not replicate, so "
                 "the 425°F endpoint fix appears material-specific rather than "
                 "universal. Endpoint temperature is the strongest current "
                 "framing, qualified: it resolves the drop for LHBH and papzp22, "
                 "and may not generalize. FW106 R11–12: Rig 5 cannot reach the "
                 "programmed 460°F at the 40s terminus (sapphire thermal lag); "
                 "both runs showed above-ceiling session character while the swab "
                 "stayed light gold — session character, not swab color, is the "
                 "operative signal on Rig 5 at elevated temperatures; a longer "
                 "session window or different insert is needed to probe that "
                 "endpoint. FW106 R17 (60s): dark golden swab, first departure "
                 "from FW106's consistent beige at 40s — duration is a plausible "
                 "driver; load size an unresolved confound. Density-harshness "
                 "pairing (FW106 R18–R19) and draw velocity as an uncontrolled "
                 "variable: see Tail Harshness Mechanism, vapor density. The "
                 "bp4rw13 R5–R7 cycle-count/swab gradient formerly cited in this "
                 "row was corrected to Rig 6 on July 2, 2026 (stale equipment "
                 "default) — see the Rig 6 row.",
        ),
    ],
    counter_reading="The endpoint-temperature fix may not be a Rig 5 property: "
                    "FW106 R18 shows the density drop persisting at 425°F and WM "
                    "R10's fast-ramp improvement did not replicate, so the 425°F "
                    "fix appears material-specific rather than universal. Likewise "
                    "the draw-3 harshness, beige swab, and fuller vaporization "
                    "could be draw-count- or strain-driven rather than dual-pearl "
                    "properties — the Rig 4→5 comparison at the same draw count "
                    "still hasn't happened, so pearl count is not isolated.",
    watch_for="The Rig 4→5 swab comparison at matched draw count; whether the "
              "425°F density-drop fix generalizes beyond LHBH and papzp22; a "
              "longer session window to probe the 460°F endpoint on Rig 5.",
    updated='WM R2 (May 25, 2026) through July 2, 2026 audit correction.',
)
