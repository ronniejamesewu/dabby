"""Sourene — jar file (slug: sourene)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = []

# ── Status ──
STATUS = StrainStatus(
    name='Sourene',
    profile_anchor='#sourene-profile',
    next_text='No runs yet — start from baseline curve',
    accent=None,
    slug='sourene',
    info=[
        ('Strain', 'Sourene (Irene × Sour Diesel IBL — stated by In House; Irene: clone-only, lineage undocumented)'),
        ('Consistency', 'Badder (user\'s read, jar unopened — not confirmed)'),
        ('Grade', 'Full Spectrum live rosin, 1g'),
        ('Producer', 'In House (grower undisclosed)'),
        ('Nose', 'Not yet recorded — jar unopened'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Caryophyllene, limonene, and myrcene inferred from the Sour Diesel side (diesel/gas lineage). Irene is clone-only with undocumented lineage — a rumored OG Kush descent is a lead only, so nothing is inferred from it. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='Start from the baseline curve (380°F → 400°F @4s → 420°F @8s, hold to 60s). First run of the jar — keep the load modest until the first session reads potency. Sour Diesel also sits in Sour Tangie\'s lineage (as East Coast Sour Diesel); no claimant ties the two cuts together, so watch whether the gas side reads similarly — a shared name, not a mechanism. Expected: a clean baseline run. Surprising: early harshness on a modest load.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
