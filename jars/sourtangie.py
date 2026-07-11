"""Sour Tangie — jar file (slug: sourtangie)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
# No runs yet — first run starts from BASELINE_CURVE.

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = []

# ── Status ──
STATUS = StrainStatus(
    name='Sour Tangie',
    profile_anchor='#sourtangie-profile',
    next_text='No runs yet — start from baseline curve',
    accent=None,
    slug='sourtangie',
    info=[
        ('Strain', 'Sour Tangie (East Coast Sour Diesel × Tangie — DNA Genetics / Crockett; Tangie: California Orange × Skunk #1; Sour Diesel: Chemdawg \'91 × Super Skunk, disputed)'),
        ('Consistency', 'Live rosin (Persy tier)'),
        ('Producer', '710 Labs'),
        ('Nose', 'Super faint — jar cold from dispensary freezer; no distinct notes yet. Weak secondary signal; expect it to open as it warms.'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene inferred dominant from the Tangie side (California Orange × Skunk #1 — citrus/orange lineage); caryophyllene and myrcene from the Sour Diesel side (Chemdawg \'91 × Super Skunk — diesel/gas, though DNA hedges this cross and a competing "DNL" origin exists). Consistent with the limonene-forward bitter-citrus/tangerine character logged when Sour Tangie ran as a layer in the closed Mango Banana #9 + Z + Sour Tangie jar. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='Start from the current baseline curve (380°F → 400°F @4s → 420°F @8s, hold to 60s). First run of a 710 Labs jar — keep the load modest until the first session reads potency (the Donny Burger + Rainbow Belts opener ran heavy and produced post-session dizziness; 710\'s packaging flags first-run caution). Sour Tangie has prior data here: as a blend layer in the closed Mango Banana #9 + Z + Sour Tangie jar it read limonene-forward — bitter citrus with a tangerine edge — so watch whether that citrus signature shows up on its own.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
