"""Blueberry 36 #1 — jar file (slug: bb361)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
BB36_1_RUN1 = [
    Waypoint(time_s=0, temp_f=380, note='Session open'),
    Waypoint(time_s=15, temp_f=390, note='Early ascent'),
    Waypoint(time_s=40, temp_f=410, note='Mid ascent'),
    Waypoint(time_s=65, temp_f=430, note='Endpoint'),
]
BB36_1_RUN2 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=25, temp_f=400, note='Mid climb'),
    Waypoint(time_s=45, temp_f=415, note='Endpoint'),
    Waypoint(time_s=65, temp_f=415, note='Hold at 415°F'),
]
BB36_1_RUN3 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=25, temp_f=400, note='Mid climb'),
    Waypoint(time_s=45, temp_f=415, note='Endpoint — repeated from Run 2'),
    Waypoint(time_s=65, temp_f=415, note='Hold at 415°F'),
]
BB36_1_NEXT = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=25, temp_f=400, note='Mid climb'),
    Waypoint(time_s=45, temp_f=410, note='Endpoint — down 5°F from Run 3'),
    Waypoint(time_s=65, temp_f=410, note='Hold at 410°F'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Blueberry 36 #1',
        run_date=date(2026, 5, 15),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 5, 16, 1, 53, tzinfo=timezone.utc),
        waypoints=BB36_1_RUN1,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 430°F — baseline',
        swab='Super light golden — very clean.',
        session_char='Not the most flavorful. Hard in the tail.',
        intensity='Medium',
    ),
    CompletedRun(
        strain='Blueberry 36 #1',
        run_date=date(2026, 5, 15),
        sessions_prior_today=1,
        utc_logged_at=datetime(2026, 5, 16, 5, 48, tzinfo=timezone.utc),
        waypoints=BB36_1_RUN2,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 415°F with 20-second hold — ramp 375→400→415°F',
        swab='Very light golden — clean.',
        session_char='Not a lot of distinct flavor. Throat irritation at the tail. Spicy note at the end — like hot spice.',
        intensity='Medium and climbing',
        extra_rows=[
            ('Effect:', 'Waves of anxiety / possible paranoia emerging post-session. User notes Blueberry strains hit harder than they look — this has come up before on this lineage.'),
        ],
    ),
    CompletedRun(
        strain='Blueberry 36 #1',
        run_date=date(2026, 5, 16),
        sessions_prior_today=0,
        utc_logged_at=datetime(2026, 5, 17, 5, 32, tzinfo=timezone.utc),
        waypoints=BB36_1_RUN3,
        equipment=RIG_2,
        endpoint_note='<strong>Endpoint:</strong> 415°F with 20-second hold — repeated from Run 2',
        swab='Golden and light — clean.',
        session_char='Taste still mild, not a lot of distinct flavor. Tad bit of harshness in the throat at the end.',
        intensity='Pretty big at the moment.',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Blueberry 36 #1',
    profile_anchor='#bb361-profile',
    next_text='Try 410°F endpoint on Run 4 — tail harshness consistent at 415°F across Runs 2 and 3',
    accent=None,
    slug='bb361',
    info=[
        ('Strain', 'Blueberry 36 #1 (Higher Ground Seed Bank — DJ Short Blueberry lineage unconfirmed despite the name)'),
        ('Provenance', "Pheno #1 of Matt's 4-seed pop — 1 male culled, surviving females jarred as #1, #2, #4"),
        ('Consistency', 'Badder'),
        ('Micron', '90μ'),
        ('Growers', 'Matt & Oliver'),
        ('Washer', 'Three Blind Trichs'),
        ('Nose', 'LOUD at cold nose; no distinct flavor notes discernible'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Myrcene inferred from Blueberry-type character (lineage unconfirmed — Higher Ground Seed Bank, not DJ Short confirmed); caryophyllene and alpha-pinene as secondaries. LOUD cold nose with no distinct discernible notes — nose is a weak secondary signal only. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='Run 3 repeated the 415°F curve (375→400→415, 20s hold): golden and light swab. Taste still mild, not a lot of distinct flavor. Tad bit of harshness in the throat at the end. Pretty big intensity.',
    next_ai_analysis="Tail harshness at 415°F is now consistent across two runs (Runs 2 and 3) — no longer a single-run signal. Swab has been very light golden across all three runs, consistent with the Gemlock efficiency pattern. Intensity landed big on Run 3 despite the lower endpoint, which is notable. 'Not a lot of distinct flavor' has been the read at both 430°F (Run 1) and 415°F (Runs 2–3) — this looks like the phenotype's character, not a temperature signal. Next: drop to 410°F endpoint, same ramp shape. Two consistent runs at 415°F with harshness — time to step down.",
    next_waypoints=BB36_1_NEXT,
    jar_index='',
)
