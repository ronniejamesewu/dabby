"""LunarZ — jar file (slug: lunarz)."""
from datetime import date, datetime, timezone
from Dabby_Core import *

# ── Waypoint constants (local to this jar) ──
# No runs yet — first run starts from BASELINE_CURVE.

# ── Runs (chronological; run numbers assigned positionally by the generator) ──
RUNS = []

# ── Status ──
STATUS = StrainStatus(
    name='LunarZ',
    profile_anchor='#lunarz-profile',
    next_text='No runs yet — start from baseline curve',
    accent=None,
    slug='lunarz',
    info=[
        ('Strain', 'LunarZ (Moonbow #112 × Planet Purple F2 #144 — bred by Archive, seed-hunted by 710 Labs; Moonbow: Zkittlez × Do-Si-Dos; Planet Purple: Sherbadough × Moonbow)'),
        ('Consistency', 'Live rosin badder (Persy tier)'),
        ('Producer', '710 Labs'),
        ('Nose', 'Faint gas — jar cold from dispensary freezer; some gas present but not loud. Weak secondary signal; expect it to open as it warms.'),
    ],
    terpene_note='<strong>Terpene inference:</strong> Limonene and caryophyllene inferred dominant from the Zkittlez × Do-Si-Dos / Sherbadough stack (Zkittlez, Do-Si-Dos, Sunset Sherbert) — sweet candy-fruit ("Z") over a gas/OG underside; linalool plausible from the Do-Si-Dos/Sherbert side. Only the immediate Moonbow × Planet Purple cross is 710 Labs-anchored; the parent generations and below are corroborated across independent sources, not producer-confirmed. Not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
    next_dab_notes='',
    next_ai_analysis='Start from the current baseline curve (380°F → 400°F @4s → 420°F @8s, hold to 60s). First run of a 710 Labs jar — keep the load modest until potency reads (same first-run caution as the recent dbrb opener). No direct effect data exists for LunarZ, but it shares Moonbow and Zkittlez ancestry with Rainbow Belts in the dbrb jar — worth watching whether similar Z-forward candy character shows up, though shared ancestry doesn\'t establish a mechanism.',
    next_waypoints=BASELINE_CURVE,
    jar_index='',
)
