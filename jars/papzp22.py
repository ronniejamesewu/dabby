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
]

# ── Status ──
STATUS = StrainStatus(
    name='Papaya + Z Pie #22',
    profile_anchor='#papzp22-profile',
    next_text='Try 425°F on Run 2 — test whether endpoint bump resolves within-draw density drop',
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
    next_dab_notes='REMINDER: Heard a pop while cleaning after Run 1 — inspect rig thoroughly before loading (insert, pearls, glass top, all joints). Confirm everything looks right before proceeding.',
    next_ai_analysis='Try 425°F, same 8s ramp, single cycle. LHBH Run 2 (June 13, same rig and ramp) resolved the within-draw density drop with exactly this change — 5°F up, ramp held constant, cleanest available isolation. Single cycle only: harshness in cycles 2 and 3 was accumulated exposure, not a 420°F ceiling. Let Run 2 establish what this strain does at 425°F before stacking cycles.',
    next_waypoints=PAPZP22_425,
    jar_index='',
)
