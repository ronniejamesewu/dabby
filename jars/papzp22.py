"""Papaya + Z Pie #22 — jar file (slug: papzp22)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
PAPZP22_425 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=4,  temp_f=400, note="Steep early climb"),
    Waypoint(time_s=8,  temp_f=425, note="Endpoint — up 5°F from Run 1"),
    Waypoint(time_s=60, temp_f=425, note="Hold"),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain="Papaya + Z Pie #22",
        run_date=date(2026, 6, 14),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 6, 14, 19, 17, 0, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_5,
        too_hot=False,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 420°F — baseline; three cycles',
        swab="golden amber (inconsistent — some spots approaching amber)",
        session_char="Three cycles at baseline. Within-draw density drop throughout; adapted to short draws, stopping when density dropped. Harshness-free in cycle 1; harshness entered in last part of cycle 2; definitely harsh in cycle 3. Very tasty.",
        intensity="very very high",
        dab_notes="Very tasty, density drop intra draw again, never got harsh. There's more in there, I adjusted my draws to stop whenever density dropped. So I haven't swabbed it. I'm going to rerun cycle again without altering it and continue just drawing the dense vapor. [After three cycles:] I went three cycles! Swabs were a bit darker than the dark golden, but less reclaim. Harshness in last part of second cycle and definitely in third. I did just pull the vapor and that kept it going with less harshness building, so maybe short draws are better for that? Anyway, very very high. [Aside:] Hey there's a note here not to go hard on first run of a jar, unknown potency. Whooeee. [Swab:] Golden amber? It wasn't consistently amber but had some spots that might meet that.",
        analysis="First run — no prior strain history. Three cycles at baseline on Rig 5. Within-draw density drop throughout: consistent with LHBH Run 1 (June 13, same rig, same baseline curve) — that cross-strain pair puts 420°F below the Rig 5 vapor-density threshold; LHBH Run 2 resolved it at 425°F with the same ramp. Harshness entered in the tail of cycle 2 and was definite in cycle 3; cycle 1 was clean. Consistent with the accumulated-exposure framing — three consecutive 60s cycles is significant cumulative hot-insert time, not a 420°F ceiling signal. Swab golden amber (inconsistent) tracks with multi-cycle exposure rather than material condition; single-cycle at this endpoint would likely come in lighter, consistent with the WM second-cycle-drives-dark-gold pattern. Stopping draws at the within-draw density drop reduced harshness accumulation — the 'stop at the depletion signal' principle applied intra-draw. Load position (Papaya outer ring vs. Z Pie #22 center) wasn't distinguishable at load time. 'Very tasty' — no specific flavor descriptors. 710 Labs first-run potency note discovered post-hoc; 'very very high' is the empirical confirmation.",
    ),
    CompletedRun(
        strain="Papaya + Z Pie #22",
        run_date=date(2026, 6, 14),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 6, 14, 22, 21, 0, tzinfo=timezone.utc),
        waypoints=PAPZP22_425,
        equipment=RIG_5,
        too_hot=False,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 425°F — up 5°F from Run 1',
        swab="light golden, couple amber spots",
        session_char="Vapor dense throughout; within-draw density drop resolved. Harshness entered at ~31s; vapor faded in last 2s of 60s hold. Single cycle.",
        intensity="medium, possibly building",
        dab_notes="So that was very different. Tasty, vapor stayed dense, harshness in the last 29 seconds, vapor faded by the end of 60 seconds within maybe last 2. Less reclaim lines up with sense of more complete vaporization. A couple amber spots on a light golden swab. Medium intensity right now but maybe growing.",
        analysis="Within-draw density drop resolved at 425°F — matches LHBH Run 2 (June 13, same rig and ramp, same +5°F fix): two strains on Rig 5 now show this same resolution. Cross-strain directional: 420°F sits below the Rig 5 vapor-density threshold; 425°F clears it. Less reclaim than Run 1 consistent with more complete vaporization at the higher endpoint. Harshness entered at ~31s with vapor still dense through ~58s — not a depletion signal; material was present for another 27 seconds after harshness onset. Consistent with the accumulated exposure / airway sensitization framing: prolonged continuous exposure crosses the harshness threshold somewhere in the 30s range. Swab light golden with couple amber spots — lighter than Run 1's golden amber; single cycle vs. three cycles explains most of it.",
    ),
    CompletedRun(
        strain="Papaya + Z Pie #22",
        run_date=date(2026, 6, 14),
        sessions_prior_today=2,
        utc_logged_at=datetime(2026, 6, 15, 0, 49, 0, tzinfo=timezone.utc),
        waypoints=PAPZP22_425,
        equipment=RIG_5,
        too_hot=False,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 425°F — repeat of Run 2; full cycle + ~2/3 of second',
        swab="light golden, couple amber spots",
        session_char="One full 60s cycle plus ~2/3 of second cycle. Harshness entered at end of first draw; shorter draws managed both harshness and taste. Very very tasty throughout. Strong harshness by end.",
        intensity="big big high",
        dab_notes="Harshness entered at end of first draw. I kept it at bay by shortening my draws, and that seemed to help a lot. Both with harshness and taste. But by the end harshness was strong. Maybe it's this material? Very very tasty throughout, even through 2/3 of a second cycle before I quit. Swab the same golden with a couple amber spots. My suspicion is the spots are pressure points that are pressing the reclaim against the still hot insert. Pretty intense! [Updated:] Big big high.",
        analysis="Harshness entered at end of first draw — earlier than Run 2's ~31s clock-time read, though the comparison is draw-length-dependent: if the first draw ran ~20s, onset was earlier; if ~30s, roughly comparable. Third dab of the day is a real confound — cumulative airway exposure from Runs 1 and 2 earlier today plausibly lowers the harshness threshold relative to Run 2 (which was the second dab). Clean timing comparison against Run 2 is not possible here. Shorter draws helped with both harshness and taste — the more actionable finding. This extends Run 1's intra-draw observation (stop at the within-draw density drop) and is now two within-strain data points on draw discipline as a working lever. Consistent with the vapor density hypothesis: shorter draws deliver less aerosol per breath, delaying threshold crossing; flavor reads improve because each draw captures the aromatic front before riding into the tail. Swab light golden, couple amber spots — identical to Run 2 at the same endpoint. Stable across two 425°F runs; not a heat-ceiling signal. User's pressure-point hypothesis for the amber spots is mechanically plausible — localized reclaim pressing against the still-hot insert during draws — and the inconsistency (spots rather than uniform color) supports a mechanical-artifact read over systematic overheating. 'Maybe it's this material?' — harshness pattern across three runs doesn't cleanly point to the material over the temperature and session length. Cross-strain parallel holds: LHBH R2 showed harshness on draw 3 at 425°F with material still present. The more interesting material-specific signal is the taste — 'very very tasty throughout, even through 2/3 of a second cycle' is three-run consistent and stands out.",
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Papaya + Z Pie #22',
    profile_anchor='#papzp22-profile',
    next_text='Run 4: 425°F, 8s ramp, 60s single cycle, shorter draws throughout — first dab of session',
    accent=None,
    slug='papzp22',
    info=[
        ('Strains', 'Papaya (clone-only, lineage unknown) + Z Pie #22 (Z × Georgia Pie — Georgia Pie: Gelato × Gushers-adjacent lineage)'),
        ('Format', 'Close Friends Persy Thumbprint — two strains: outer ring cold cure badder (Papaya), center jam (Z Pie #22). 90μ persy-tier. Load position not reliably distinguishable.'),
        ('Producer', '710 Labs'),
        ('710 Notes', 'Papaya brings sweet, tart exotic fruit. Z Pie #22 layers in Z, sour citrus, spice, and Georgia Pie. Bright fruit meets sour citrus funk.'),
        ('Nose', 'Loud gas but not super stinky. Subtle fruit note underneath.'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Terpinolene and ocimene inferred from Papaya (tropical clone-only cultivar); limonene and myrcene inferred from Z Pie #22 (Z × Georgia Pie — Zkittlez lineage: limonene/myrcene; Georgia Pie typically Gelato × Gushers-adjacent: limonene/myrcene/linalool). Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='Nose at room temp (~few hours out of fridge): garlicky in a good way (June 14, 2026).',
    next_ai_analysis='Three runs, no clean harshness-window read yet — Run 2 gave ~31s onset, Run 3 gave earlier onset but draw-length management was in play and third-dab-of-day is a real confound. The actionable finding from Run 3 is that shorter draws kept both harshness and taste in a better place — worth testing deliberately. Run 4: 425°F, 8s ramp, 60s single cycle, shorter draws throughout from draw 1, first dab of a session. Question: does the draw-discipline approach keep 60s harshness-free? If yes, 425°F works with discipline. If harshness still enters in the first 30s, pull the endpoint to 422–423°F.',
    next_waypoints=PAPZP22_425,
    jar_index='',
)
