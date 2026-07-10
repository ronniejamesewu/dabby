"""Donny Burger + Rainbow Belts — jar file (slug: dbrb)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
DBRB_HOLD10_DESCENT_GENTLE = [
    Waypoint(time_s=0,  temp_f=440, note='Session open — hot open'),
    Waypoint(time_s=10, temp_f=440, note='Hold at peak — one draw at 440°F'),
    Waypoint(time_s=35, temp_f=420, note='Gentle descent midpoint'),
    Waypoint(time_s=60, temp_f=400, note='Floor'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Donny Burger + Rainbow Belts',
        run_date=date(2026, 7, 9),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 7, 10, 1, 54, 21, tzinfo=timezone.utc),
        waypoints=DBRB_HOLD10_DESCENT_GENTLE,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Open:</strong> 440°F &nbsp;|&nbsp; <strong>Floor:</strong> 400°F — 10s hold at 440°F, then gentle descent; jar opener, baseline skipped',
        swab='golden',
        session_char='Golden swab, minimal reclaim; full first cycle plus one draw of a second, ended on satiety rather than harshness; heavy terp coughing on draw 1; mild harshness at end of cycle 1, second cycle clean; both strains present on draw 1 — garlic-cheese and lemon-pledge/lime; big intensity',
        intensity='big',
        dab_notes='Definitely a garlic funk cold nose. Not getting a lot of fruit but it\'s still cold from the fridge. [Post-dab:] Godamn that was great. [Report:] I succeeded in getting both strains. So there was this garlicky cheesy note, and then there was also this lemon pledge note. Maybe a squeeze of lime. But tasting all that was in between coughing really hard on the terps. I kind of wonder if the terps are the thing causing harshness. It was mild, not sure when it showed up even, because of the coughing, but it was there at the end. I took a thirty second break and ran second cycle. Took a good hit, still tasty, but at that point I\'d had enough. I terminated the cycle. Sean\'s were golden, minimal reclaim. Intensity is big, let\'s see how heavy it gets. [Clarified: harshness was end of first cycle, second cycle clean as far as could tell; load normalish, maybe a tad bigger; "Sean\'s" logged as "swabs".]',
        analysis='Run 1, jar opener, deviating from the on-file baseline plan: the bounded 10s-440°F hold with gentle descent to 400°F that delivered on Banana Punch #4 + Randy Watzon #13 R12 two nights earlier — same rig, so equipment is controlled on that comparison. Same shape of result: golden swab, minimal reclaim, big immediate intensity, and the session ended one draw into cycle 2 on satiety rather than harshness — a fourth strain consistent with the descent-curve direction in the wisdom layer (limiting factor shifts from harshness to intensity; all Rig 6, cross-rig untested). Mild harshness at the end of cycle 1, onset obscured by heavy draw-1 terp coughing (terpene-load cough documented on Rig 6 — Hive #1 R8); user\'s hypothesis, at single-data-point weight: the terps themselves may be causing the harshness. Both strains read through on draw 1 — garlicky-cheese (Donny Burger) and lemon pledge with a squeeze of lime (Rainbow Belts) — a single-session flavor observation on a format whose load zone isn\'t distinguishable; noted, not established. One run; no baseline reference exists for this jar.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Donny Burger + Rainbow Belts',
    profile_anchor='#dbrb-profile',
    next_text='Run 2: repeat the bounded 440°F hold (440→440@10s→420@35s→400@60s) — replicate the jar opener before changing anything',
    accent=None,
    slug='dbrb',
    info=[
        ('Strains', 'Donny Burger (GMO × Han Solo Burger — Han Solo Burger: GMO × Larry OG F8; Larry OG: SFV OG × OG Kush) + Rainbow Belts (Z × Moonbow)'),
        ('Format', 'Close Friends Persy Thumbprint — two strains: outer ring cold cure badder (Donny Burger), center jam (Rainbow Belts). 90μ persy-tier. Load position not reliably distinguishable.'),
        ('Producer', '710 Labs'),
        ('710 Notes', 'Donny Burger brings sweet GMO funk with garlic, onion, and spice. Rainbow Belts cuts through with lemon-lime, floral Z, and a smooth exhale. Gas, funk, and bright fruit.'),
        ('Nose', 'Garlic funk cold nose straight from the fridge; fruit quiet (pre-Run 1 — early read, jar still fridge-cold)'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Caryophyllene inferred dominant from GMO and OG lineage on the Donny Burger side (funky, gassy, garlic-onion character); limonene inferred from Rainbow Belts Z side (lemon-lime, citrus). Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='I kind of wonder if the terps are the thing causing harshness.',
    next_ai_analysis='Repeat the exact curve, same load class — one big clean delivery on a jar opener is a single data point, and this jar adds a two-strain load-position lottery to normal run-to-run noise. Track what draw 1 tastes like each run: the garlic/citrus split is the only strain-identification signal this format offers, and it only becomes informative across runs. Expected: golden swab, big intensity, mild-at-most late harshness. Surprising: a dark swab or hard early harshness — that would point at load or zone scooped, not the curve.',
    next_waypoints=DBRB_HOLD10_DESCENT_GENTLE,
    jar_index='',
)
