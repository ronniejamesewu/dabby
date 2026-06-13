"""Fembot #3 — jar file (slug: fembot3)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
FEMBOT3_RUN1 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
FEMBOT3_RUN2 = [
    Waypoint(time_s=0, temp_f=430, note='Steady hold — flat 430°F from session open'),
    Waypoint(time_s=60, temp_f=430, note='Endpoint'),
]
FEMBOT3_RUN3 = [
    Waypoint(time_s=0, temp_f=420, note='Steady hold — flat 420°F from session open'),
    Waypoint(time_s=60, temp_f=420, note='Endpoint'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Fembot #3',
        run_date=date(2026, 5, 9),
        sessions_prior_today=0,
        utc_logged_at=None,
        waypoints=FEMBOT3_RUN1,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F',
        swab='Light golden — clean. Two heads mostly white, two with light golden coloring. No darkening.',
        session_char='Very tasty on the ascent. No visible vapor until mid-range. Slight harshness at the tail. Effects upbeat, creative, not too body-heavy — consistent with sativa-dominant character.',
        extra_rows=[
            ('Next:', 'Try steady 420°F flat hold (60s) on Run 2 — drop endpoint and change curve shape to test both variables.'),
        ],
    ),
    CompletedRun(
        strain='Fembot #3',
        run_date=date(2026, 5, 9),
        sessions_prior_today=1,
        utc_logged_at=None,
        waypoints=FEMBOT3_RUN2,
        equipment=RIG_1,
        duration_seconds=60,
        endpoint_note='<strong>Setpoint:</strong> 430°F steady (no ramp)',
        swab='Light golden — clean. Consistent with Run 1.',
        session_char='Very tasty, great effects. Harshness in the last third.',
        extra_rows=[
            ('Next:', 'Try 420°F steady flat hold on Run 3.'),
        ],
        analysis='Harshness at the tail is consistent with Run 1 (ramp to 430°F endpoint) — two data points now pointing at 430°F as slightly above ideal for this material, regardless of curve shape. Swab is clean, so this is a session character signal rather than a floor indicator.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Fembot #3',
    profile_anchor='#fembot3-profile',
    next_text='Not my jar — closed after 2 runs. If it shows up again: try 420°F flat hold.',
    accent=None,
    slug='fembot3',
    info=[
        ('Strain', 'Fembot #3 (Fuzzy Melon × Rambutan — inferred)'),
        ('Consistency', 'Cold cure'),
        ('Producer', 'Riptide (CO)'),
        ('Input', '169–73 micron ice water hash'),
        ('Character', 'Sativa-dominant — uplifting, energetic character inferred from lineage. Phenotype and wash quality drive actual experience.'),
        ('Nose', 'Subtle garlic note at cold nose; strong overall fragrance, less distinct individual character'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Terpinolene inferred likely dominant from Fuzzy Melon character; Fuzzy Melon × Rambutan lineage. Standard cannabis palette otherwise — not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='Not my jar — two dabs from Matt\'s. Both showed harshness at 430°F across a ramp and a flat hold. The 420°F flat hold was the logical next test but didn\'t happen. If this strain shows up again: start there.',
    next_waypoints=FEMBOT3_RUN3,
    jar_index='',
)
