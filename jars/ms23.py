"""Mango Starburst #23 — jar file (slug: ms23)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
MS23_RUN1 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Mango Starburst #23',
        run_date=date(2026, 5, 9),
        sessions_prior_today=2,
        utc_logged_at=None,
        waypoints=MS23_RUN1,
        equipment=RIG_1,
        endpoint_note='<strong>Endpoint:</strong> 430°F',
        swab='Very clean — no darkening.',
        session_char="Very piney character throughout — almost pine sol. Tasty, though not to user's taste preference. Heady effects. No harshness.",
        extra_rows=[
            ('Note:', 'Strong pine-forward character noted on first run. The SB36 lineage inference weighted limonene and terpinolene as prominent — the pronounced pine character is consistent with pinene playing a larger role than the inference anticipated. Logged as one data point; flavor character is a weak signal and single-session observations carry high uncertainty.'),
            ('Verdict:', 'Clean swab on first run. Curve well-matched to this material. Repeat on Run 2 to confirm.'),
        ],
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Mango Starburst #23',
    profile_anchor='#ms23-profile',
    next_text='Repeat Run 1 curve to confirm',
    accent=None,
    slug='ms23',
    info=[
        ('Strain', 'Mango Starburst #23 (Starburst 36 #217 × Starburst 36 #1)'),
        ('Consistency', 'Cold cure'),
        ('Producer', 'Terps Over Yields (CO)'),
        ('Jar', '14 of 23'),
        ('Base genetics', "SB36 line — Starburst OG × '97 KC36"),
        ('Character', 'Sativa-dominant — upbeat, euphoric, flavor-forward character inferred from SB36 lineage. KC36 influence leans energetic rather than sedating. Phenotype and wash quality drive actual experience.'),
        ('Nose', 'Diesel note pronounced at cold nose; sweetness underneath'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene and terpinolene weighted from SB36 line\'s citrus-candy character; pronounced pine on Run 1 suggests pinene may be more prominent than inferred. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis="One run, clean swab, no harshness. Pine-forward character was noted but single-session flavor observations are noisy. Repeat the same curve before changing anything — if it's pine again on Run 2, that's real.",
    next_waypoints=MS23_RUN1,
    jar_index='',
)
