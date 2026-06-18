"""Blueberry 36 #4 — jar file (slug: bb364)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Blueberry 36 #4',
        run_date=date(2026, 6, 17),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 6, 18, 5, 38, 57, tzinfo=timezone.utc),
        waypoints=BASELINE_CURVE,
        equipment=RIG_6,
        duration_seconds=60,
        endpoint_note='<strong>Endpoint:</strong> 420°F — baseline',
        swab='Super clean light golden. Not a lot of reclaim.',
        session_char='Not super tasty. No harshness across 3–4 draws. Vapor density high throughout. Retronasal blueberry ~10 minutes post-session.',
        intensity='Heavy body, still building at logging time.',
        dab_notes="It wasn't super tasty, but also not harsh at all. Maybe a tiny bit of blueberry 10 minutes later from my throat. Heavy body intensity, let's see how high the high gets. Swabs were super clean light golden. And not a lot. Vapor density stayed high. 3 or 4 draws, never got harsh to the point I noticed it.",
        analysis="Clean debut on Rig 6 at baseline. No noticeable harshness across 3–4 draws at 420°F — notable given FW106 R20's harshness arriving on draw 2 on this same rig. Whether that's a strain-specific ceiling or a load/draw-style difference can't be resolved from one run. Vapor density high throughout — contrast with BB36 #2's persistent wispy vapor on the prior baseline curve on Rig 5, though rig change is a real confound. Swab came back super clean light golden with not a lot of reclaim — consistent with the BB36 family's light swab character across both sister jars. 'Not super tasty' tracks directly with BB36 #1's persistent 'not a lot of distinct flavor' across multiple runs and endpoints — phenotype character, not a temperature signal. Retronasal blueberry arriving ~10 minutes later from the throat is the same presentation as BB36 #2 R1 — two jars, same post-session olfactory pattern, starting to look like a BB36 family signature. Intensity read heavy body and still building at logging time; second-dab-of-day (FW106 R20 earlier) and the cross-strain switching effect (documented in BB36 #2 R6) both apply, so the intensity number is confounded.",
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Blueberry 36 #4',
    profile_anchor='#bb364-profile',
    next_text='Run 2: try 425°F — up 5°F from baseline, same 8s ramp and 60s hold',
    accent=None,
    slug='bb364',
    info=[
        ('Strain', 'Blueberry 36 #4 (Higher Ground Seed Bank — DJ Short Blueberry lineage unconfirmed despite the name)'),
        ('Provenance', "Pheno #4 of Matt's 4-seed pop — 1 male culled, surviving females jarred as #1, #2, #4"),
        ('Consistency', 'Badder'),
        ('Micron', '90μ'),
        ('Growers', 'Matt & Oliver'),
        ('Washer', 'Three Blind Trichs'),
        ('Nose', 'Pungent, fruity — loud cold nose'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Myrcene inferred from Blueberry-type character (lineage unconfirmed — Higher Ground Seed Bank, not DJ Short confirmed); caryophyllene and alpha-pinene as secondaries. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes="It wasn't super tasty, but also not harsh at all. Maybe a tiny bit of blueberry 10 minutes later from my throat. Heavy body intensity, let's see how high the high gets. Swabs were super clean light golden. And not a lot. Vapor density stayed high. 3 or 4 draws, never got harsh to the point I noticed it.",
    next_ai_analysis='One clean run at baseline on Rig 6 — no harshness, clean swab, high vapor density. Repeat the exact same curve before adjusting anything. BB36 #2 had documented run-to-run variability; one clean result is not enough to call the ceiling or the rig\'s working range for this phenotype.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
