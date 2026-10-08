"""Dulce De Papaya (90u) — jar file (slug: ddp90)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = []

# ── Status ──
STATUS = StrainStatus(
    name='Dulce De Papaya (90u)',
    profile_anchor='#ddp90-profile',
    next_text='No runs yet — start from baseline curve',
    accent=None,
    slug='ddp90',
    info=[
        ('Strain', 'Dulce De Papaya (Papaya × Dulce De Uva — stated by Erva; Dulce De Uva: Ice Cream Cake × (Grape Pie × Wedding Crasher), stated by Bloom; Papaya cut unattributed — 2/3 confirmed, see terpene note)'),
        ('Consistency', 'Badder (user\'s read, jar unopened — not confirmed)'),
        ('Grade', '90μ live rosin, 1g'),
        ('Grower', 'Erva'),
        ('Processor', 'In House'),
        ('Nose', 'Not yet recorded — jar unopened'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Caryophyllene and limonene inferred from the Dulce De Uva side (Ice Cream Cake / Wedding Crasher — cake-and-grape lineage). Nothing is inferable from the Papaya side: Erva names no breeder or source for its Papaya cut, and the breeder of the cross is uncredited. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='Start from the baseline curve (380°F → 400°F @4s → 420°F @8s, hold to 60s). First run of the jar — keep the load modest until the first session reads potency. Sister jar to Dulce De Papaya (Full Spectrum): same strain and grower at a different grade; neither label says whether it is the same harvest or press, so a difference between the two jars is grade plus batch, not grade alone. Expected: a clean run at baseline — the baseline\'s general record, not a prior on this strain. Surprising: harshness at 420°F on a modest load.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
