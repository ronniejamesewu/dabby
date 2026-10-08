"""Black Lemon — jar file (slug: blacklemon)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = []

# ── Status ──
STATUS = StrainStatus(
    name='Black Lemon',
    profile_anchor='#blacklemon-profile',
    next_text='No runs yet — start from baseline curve',
    accent=None,
    slug='blacklemon',
    info=[
        ('Strains', 'Perle Di Sole (TMZ × Orange Mints — stated by Bloom and In House; Orange Mints undisclosed by Bloom) + Death Coast (Death Star × East Coast Sour Diesel — stated by In House; Death Star: Sensi Star × Sour Diesel, corroborated across sources, not producer-confirmed)'),
        ('Format', 'Two-strain co-press (Perle Di Sole + Death Coast, stated on In House\'s drop menu) — Full Spectrum live rosin, 2g. Pressed together, not layered: no load can be attributed to one component.'),
        ('Consistency', 'Badder (user\'s read, jar unopened — not confirmed)'),
        ('Producer', 'In House (grower undisclosed)'),
        ('Nose', 'Not yet recorded — jar unopened'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene inferred from Perle Di Sole\'s Zkittlez line (TMZ; Bloom\'s tasting note on the cultivar: "pineapple, Z and OG"); caryophyllene and myrcene from Death Coast\'s Sour Diesel family. Orange Mints is undisclosed, so part of the Perle Di Sole side is unknown. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='Start from the baseline curve (380°F → 400°F @4s → 420°F @8s, hold to 60s). First run of the jar — keep the load modest until the first session reads potency. A co-press mixes both strains before pressing, so unlike a thumbprint jar no draw can be read as one component — the jar reads as one material. East Coast Sour Diesel is named in both Death Coast and Sour Tangie, cut unattributed — watch for similar gas character, nothing more. Expected: a clean baseline run. Surprising: early harshness on a modest load.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
