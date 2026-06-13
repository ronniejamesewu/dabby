"""Caramel Apple Gelato — jar file (slug: cag)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
CAG_RUN1 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=10, temp_f=380, note='Short flat phase'),
    Waypoint(time_s=30, temp_f=395, note='Mid ascent'),
    Waypoint(time_s=50, temp_f=420, note='Upper terpene zone'),
    Waypoint(time_s=65, temp_f=450, note='ENDPOINT TOO HOT — see diagnosis'),
]
CAG_RUN2 = [
    Waypoint(time_s=0, temp_f=375, note='Session open'),
    Waypoint(time_s=10, temp_f=380, note='Short flat phase'),
    Waypoint(time_s=30, temp_f=395, note='Mid ascent'),
    Waypoint(time_s=50, temp_f=415, note='Upper terpene zone'),
    Waypoint(time_s=55, temp_f=430, note='Conservative endpoint'),
]

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = [
    CompletedRun(
        strain='Caramel Apple Gelato',
        run_date=None,
        sessions_prior_today=None,
        utc_logged_at=None,
        waypoints=CAG_RUN1,
        equipment=RIG_1,
        too_hot=True,
        endpoint_note='<strong>Endpoint:</strong> 450°F',
        swab='Amber shading toward light brown.',
        extra_rows=[
            ('Vapor:', 'Limited flavor. Session did not express distinct character.'),
            ('Diagnosis:', 'Endpoint of 450°F likely too aggressive — supported by swab darkening. Limited flavor may reflect endpoint temperature degrading terpene fraction at session tail, or may reflect moderate terpene content in this material independent of temperature. Both explanations are plausible; endpoint reduction will help distinguish them.'),
            ('Adjustment:', 'Pull endpoint back to 430°F. Shorten hold to 55 seconds to reduce risk of outlasting small load.'),
        ],
        date_label='May 2026',
    ),
]

# ── Status ──
STATUS = StrainStatus(
    name='Caramel Apple Gelato',
    profile_anchor='#cag-profile',
    next_text='Try 430°F endpoint',
    accent=None,
    slug='cag',
    info=[
        ('Strain', 'Caramel Apple Gelato (Gelato lineage: Sunset Sherbet × Thin Mint GSC — inferred)'),
        ('Consistency', 'Cold cure'),
        ('Producer', 'Quasi Farms (Michigan)'),
        ('Nose', 'Muted — no distinct notes (weak secondary signal, consistent with heavier terpene profile)'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene and myrcene inferred from Gelato lineage. Muted nose consistent with heavier, less-volatile terpene profile. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='One data point at 450°F with an amber-toward-brown swab — reliable floor signal. Pull the endpoint back to 430°F. Nothing subtle here, it was just too hot.',
    next_waypoints=CAG_RUN2,
    jar_index='',
)
