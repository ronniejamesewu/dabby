"""Dabby session data — all run records, strain info, and validation."""

from datetime import datetime, date, timezone
from dataclasses import dataclass
from typing import Literal

# ── DATACLASSES ────────────────────────────────────────────────────────────

@dataclass
class Waypoint:
    time_s: int
    temp_f: int
    note: str

@dataclass
class Insert:
    brand: str       # "Dr. Dabber", "OM Quartz", etc.
    model: str       # "stock", "Sapphire Plus (v2)", etc.
    material: str    # "quartz", "sapphire"

@dataclass
class CarbCap:
    brand: str       # "Cloud Vortex", "Gemcup Glass"
    model: str       # "21.0", "Gemlock joystick"
    airflow: str     # "stock" by default — variant string when known

@dataclass
class Pearl:
    diameter_mm: int
    material: str    # "quartz" — future materials TBD

@dataclass
class EquipmentConfig:
    insert: Insert
    carb_cap: CarbCap
    pearls: list[Pearl]   # empty list = no pearls; sorted in __post_init__ for stable equality
    glass_top: str        # flat string — no sub-dimensions to track yet
    # Guardrail 3: all four fields contribute to nested-dataclass equality.
    # pearls is sorted in __post_init__ so list order doesn't matter.
    # Insert / carb cap / pearls / glass top are all confound boundaries when comparing runs.

    def __post_init__(self):
        self.pearls = sorted(self.pearls, key=lambda p: (p.diameter_mm, p.material))

@dataclass
class CompletedRun:
    strain: str
    run_date: date | None
    sessions_prior_today: int | None
    utc_logged_at: datetime | None
    waypoints: list
    # Python-level optional only; validate() rejects None so every shipped run
    # carries explicit equipment — None never means "inherit a session default".
    equipment: EquipmentConfig = None

    # Semantic status — drives amber styling; amber is presentation, too_hot is the fact
    too_hot: bool = False

    # Curve description
    duration_seconds: int = 65
    endpoint_note: str = ""          # "steady (no ramp)", "same as Run 1", etc.

    # Session content — all fields live here; generator is rendering-only (Step 3)
    swab: str = ""
    session_char: str = ""
    intensity: str | None = None
    read: str = ""                   # interpretation
    verdict: str = ""
    extra_rows: list | None = None   # genuinely one-off result rows (e.g. OC R5 "Observation:")

    # Analysis (currently string literals in build_html() — migrated in Step 3)
    dab_notes: str = ""              # user's read
    analysis: str = ""               # AI synthesis (historically stable, rendered read-only)
    proposed_waypoints: list | None = None

    # Title date override for runs where run_date=None (pre-dataclass era entries logged as "May 2026")
    date_label: str = ""             # when set, used instead of derived run_date string in section title

@dataclass
class StrainStatus:
    name: str
    profile_anchor: str
    next_text: str                   # hand-maintained dashboard one-liner (current revisable state)
    accent: str | None
    slug: str

    # Profile content (currently string literals in build_html() — migrated in Step 3)
    info: list | None = None         # rows for info_table()
    terpene_note: str = ""           # <p class="note"> in profile section

    # Current "What to Try Next" — revisable strain-level guidance (N5)
    # Today these are inline args to what_to_try_next_html(); Step 3 makes them explicit.
    # NOT sourced from any run's frozen analysis.
    next_dab_notes: str = ""
    next_ai_analysis: str = ""
    next_waypoints: list | None = None
    jar_index: str = ""         # Jar Index for finished jars — rendered in strain profile

@dataclass
class TerpeneEntry:
    name: str
    alias: str
    bp_f: int
    bp_c: int
    band: Literal["Low", "Mid", "High"]
    aroma: str
    qualities: str
    found_in: str

# ── DATA ────────────────────────────────────────────────────────────────────

GLOBAL_INFO = [
    ("Device",       "Switch² (Dabby the House Rig)"),
    ("All Material", "Hash Rosin — ice water extracted, solventless. Consistency varies by jar — noted in each strain profile."),
    ("Insert",       "20mm — quartz or sapphire. Sapphire requires fresh calibration from scratch; do not scale from quartz curves."),
    ("Technique",    "Cold start — pre-load into cold insert before every session"),
    ("Load Size",    "Rice grain (small)"),
    ("Offset Est.",  "Probably small under most operating conditions. Dominant uncertainties are vaporization cooling and dynamic lag during steep ascent. At flat or slowly-ascending phases the system approaches equilibrium. Setpoints are reasonable proxies for material contact temperature."),
    ("Draw Style",   "Long, slow draws throughout session"),
    ("Session End",  "Stop when vapor production drops — do not ride timer on small loads"),
]

BASELINE_CURVE = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]

CAG_INFO = [
    ("Strain",      "Caramel Apple Gelato (Gelato lineage: Sunset Sherbet × Thin Mint GSC — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Muted — no distinct notes (weak secondary signal, consistent with heavier terpene profile)"),
]
CAG_RUN1 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=10, temp_f=380, note="Short flat phase"),
    Waypoint(time_s=30, temp_f=395, note="Mid ascent"),
    Waypoint(time_s=50, temp_f=420, note="Upper terpene zone"),
    Waypoint(time_s=65, temp_f=450, note="ENDPOINT TOO HOT — see diagnosis"),
]
CAG_RUN2 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=10, temp_f=380, note="Short flat phase"),
    Waypoint(time_s=30, temp_f=395, note="Mid ascent"),
    Waypoint(time_s=50, temp_f=415, note="Upper terpene zone"),
    Waypoint(time_s=55, temp_f=430, note="Conservative endpoint"),
]

OC_INFO = [
    ("Strain",      "Orange Candy (Philosopher Seeds lineage: Naran J × Tropimango — unconfirmed)"),
    ("Producer",    "Nikka T"),
    ("Input",       "90 micron full melt bubble hash"),
    ("Consistency", "Cold cure"),
    ("Nose",        "Strong orange note at cold nose"),
]
OC_RUNS12 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=378, note="Flat phase"),
    Waypoint(time_s=40, temp_f=395, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=450, note="Endpoint — raised to compensate for estimated thermal offset"),
]
OC_RUN3 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=378, note="Flat phase"),
    Waypoint(time_s=35, temp_f=410, note="Steeper climb — faster progression through mid terpene zones"),
    Waypoint(time_s=65, temp_f=440, note="Endpoint — reduced; flatter tail allows insert surface to approach equilibrium"),
]
OC_RUN4 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open — raised 5°F to increase opening vapor density"),
    Waypoint(time_s=15, temp_f=390, note="Halfway between open and mid waypoint"),
    Waypoint(time_s=35, temp_f=410, note="Halfway between open and endpoint"),
    Waypoint(time_s=65, temp_f=440, note="Endpoint — unchanged"),
]
OC_RUN5 = [
    Waypoint(time_s=0,  temp_f=350, note="Session open — lower opening setpoint under exploration"),
    Waypoint(time_s=30, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=50, temp_f=440, note="Upper zone"),
    Waypoint(time_s=65, temp_f=460, note="Endpoint"),
]
OC_RUN6 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=35, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint — down 10°F from Runs 3–4"),
]
OC_RUN7 = [
    Waypoint(time_s=0,  temp_f=430, note="Steady hold — flat 430°F from session open"),
    Waypoint(time_s=60, temp_f=430, note="Endpoint"),
]
OC_RUN8 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=10, temp_f=400, note="Fast early climb"),
    Waypoint(time_s=20, temp_f=420, note="Endpoint — 420°F in 20s, 2°F/sec"),
    Waypoint(time_s=50, temp_f=420, note="Hold"),
]
OC_RUN9_NEXT = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=10, temp_f=400, note="Fast early climb"),
    Waypoint(time_s=20, temp_f=415, note="Endpoint — down 5°F from Run 8"),
    Waypoint(time_s=50, temp_f=415, note="Hold"),
]
OC_RUN9 = OC_RUN9_NEXT
OC_RUN11_NEXT = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=10, temp_f=400, note="Fast early climb"),
    Waypoint(time_s=20, temp_f=417, note="Endpoint — up 2°F from Runs 9–10"),
    Waypoint(time_s=50, temp_f=417, note="Hold"),
]
OC_RUN11 = OC_RUN11_NEXT
OC_RUN12 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=10, temp_f=400, note="Fast early climb"),
    Waypoint(time_s=20, temp_f=416, note="Endpoint — 416°F in 20s, 2°F/sec"),
    Waypoint(time_s=50, temp_f=416, note="Hold"),
]

HIVE1_INFO = [
    ("Strain",      "The Hive #1 (Honey Banana × Papaya — Bloom Seed Co)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Myxed Up (washed and pressed)"),
    ("Input",       "159–73 micron ice water hash"),
    ("Nose",        "Very fragrant at cold nose. Spice noticeable (consistent with caryophyllene — weak secondary signal only)."),
]

HIVE1_RUN1 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=35, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=440, note="Endpoint"),
]
HIVE1_RUN2 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=35, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=440, note="Endpoint — repeated from Run 1"),
]
HIVE1_RUN3 = [
    Waypoint(time_s=0,  temp_f=430, note="Steady hold — flat 430°F from session open"),
    Waypoint(time_s=45, temp_f=430, note="Endpoint"),
]
HIVE1_RUN4 = [
    Waypoint(time_s=0,  temp_f=430, note="Steady hold — flat 430°F from session open"),
    Waypoint(time_s=60, temp_f=430, note="Endpoint — extended from Run 3's 45s"),
]
HIVE1_RUN5 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=35, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint — 430°F with ramp (down from 440°F in Runs 1–2)"),
]

FEMBOT3_INFO = [
    ("Strain",      "Fembot #3 (Fuzzy Melon × Rambutan — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Riptide (CO)"),
    ("Input",       "169–73 micron ice water hash"),
    ("Character",   "Sativa-dominant — uplifting, energetic character inferred from lineage. Phenotype and wash quality drive actual experience."),
    ("Nose",        "Subtle garlic note at cold nose; strong overall fragrance, less distinct individual character"),
]

FEMBOT3_RUN1 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
FEMBOT3_RUN2 = [
    Waypoint(time_s=0,  temp_f=430, note="Steady hold — flat 430°F from session open"),
    Waypoint(time_s=60, temp_f=430, note="Endpoint"),
]
FEMBOT3_RUN3 = [
    Waypoint(time_s=0,  temp_f=420, note="Steady hold — flat 420°F from session open"),
    Waypoint(time_s=60, temp_f=420, note="Endpoint"),
]
HIVE1_NEXT = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=35, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=425, note="Endpoint — down 5°F from Run 5"),
]

MS23_INFO = [
    ("Strain",        "Mango Starburst #23 (Starburst 36 #217 × Starburst 36 #1)"),
    ("Consistency",   "Cold cure"),
    ("Producer",      "Terps Over Yields (CO)"),
    ("Jar",           "14 of 23"),
    ("Base genetics", "SB36 line — Starburst OG × '97 KC36"),
    ("Character",     "Sativa-dominant — upbeat, euphoric, flavor-forward character inferred from SB36 lineage. KC36 influence leans energetic rather than sedating. Phenotype and wash quality drive actual experience."),
    ("Nose",          "Diesel note pronounced at cold nose; sweetness underneath"),
]
MS23_RUN1 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
MBD_INFO = [
    ("Strain",      "Maple Bacon Donut"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Micron",      "Not recorded"),
    ("Nose",        "Not yet recorded"),
]
MBD_RUN1 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
MBD_RUN2 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open — same curve as Run 1"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
MBD_RUN3 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=385, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=55, temp_f=420, note="Approach endpoint — down 10°F from prior runs"),
    Waypoint(time_s=65, temp_f=420, note="Hold at 420°F for 10 seconds"),
]
MBD_RUN4 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open — same as Runs 1 and 2"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
MBD_NEXT = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=405, note="Steeper early ascent"),
    Waypoint(time_s=35, temp_f=440, note="Mid climb"),
    Waypoint(time_s=60, temp_f=460, note="Endpoint — up 30°F, faster ramp"),
]

RF_INFO = [
    ("Strain",      "Rain Fruit"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Micron",      "Not recorded"),
    ("Nose",        "Not yet recorded"),
]
RF_RUN1 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
RF_RUN2 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open — 5°F below baseline, testing lower open"),
    Waypoint(time_s=15, temp_f=385, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
RF_RUN3 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=385, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=55, temp_f=420, note="Approach endpoint — down 10°F"),
    Waypoint(time_s=65, temp_f=420, note="Hold at 420°F for 10 seconds"),
]
RF_RUN4_NEXT = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=385, note="Early ascent"),
    Waypoint(time_s=40, temp_f=412, note="Mid ascent — up 2°F"),
    Waypoint(time_s=55, temp_f=422, note="Approach endpoint — up 2°F"),
    Waypoint(time_s=65, temp_f=423, note="Endpoint — up 3°F from Run 3"),
]

BB36_1_INFO = [
    ("Strain",      "Blueberry 36 #1 (DJ Short's Blueberry base genetics — producer-specific pheno designation)"),
    ("Consistency", "Badder"),
    ("Micron",      "90μ"),
    ("Growers",     "Matt & Oliver"),
    ("Washer",      "Three Blind Trichs"),
    ("Nose",        "LOUD at cold nose; no distinct flavor notes discernible"),
]
BB36_1_RUN1 = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
BB36_1_RUN2 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=415, note="Endpoint"),
    Waypoint(time_s=65, temp_f=415, note="Hold at 415°F"),
]
BB36_1_RUN3 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=415, note="Endpoint — repeated from Run 2"),
    Waypoint(time_s=65, temp_f=415, note="Hold at 415°F"),
]
BB36_1_NEXT = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=410, note="Endpoint — down 5°F from Run 3"),
    Waypoint(time_s=65, temp_f=410, note="Hold at 410°F"),
]

# ── DASHBOARD DATA ────────────────────────────────────────────────────────────

FIRST_RUN_DATE = date(2026, 5, 2)

# ── EQUIPMENT ─────────────────────────────────────────────────────────────────
# Three rigs to date, sequenced RIG_N. Schema carries all content; the Rig Reference
# table on the rendered log documents each rig's meaning for human readers.
# New rigs get the next sequence number — no renames needed when new variables appear.
# Run comparability: two runs share a config when all four EquipmentConfig fields
# are equal. pearls is sorted in __post_init__ so list order doesn't matter.
# Insert / carb cap / pearls / glass top are all confound boundaries when comparing runs.

# Rig 1: Pre-Gemlock era. Dr. Dabber stock quartz insert, Cloud Vortex 21.0 spinner
# (stock airflow), 6mm quartz pearl, stock Dr. Dabber bubbler top. May 2 – May 13, 2026.
RIG_1 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="stock", material="quartz"),
    carb_cap=CarbCap(brand="Cloud Vortex", model="21.0", airflow="stock"),
    pearls=[Pearl(diameter_mm=6, material="quartz")],
    glass_top="Dr. Dabber stock bubbler",
)

# Rig 2: Gemlock era. Dr. Dabber stock quartz insert, Gemcup Glass Gemlock joystick
# (stock airflow), no pearls, stock Dr. Dabber bubbler top. May 13 – May 21, 2026.
# Joystick broke mid-session May 21.
RIG_2 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="stock", material="quartz"),
    carb_cap=CarbCap(brand="Gemcup Glass", model="Gemlock joystick", airflow="stock"),
    pearls=[],
    glass_top="Dr. Dabber stock bubbler",
)

# Rig 3: Sapphire era. Dr. Dabber Sapphire Plus (v2) insert (new May 22, 2026);
# Cloud Vortex 21.0 spinner returning (stock airflow); 6mm quartz pearl; stock
# Dr. Dabber bubbler top. In use as of May 22, 2026.
RIG_3 = EquipmentConfig(
    insert=Insert(brand="Dr. Dabber", model="Sapphire Plus (v2)", material="sapphire"),
    carb_cap=CarbCap(brand="Cloud Vortex", model="21.0", airflow="stock"),
    pearls=[Pearl(diameter_mm=6, material="quartz")],
    glass_top="Dr. Dabber stock bubbler",
)

COMPLETED_RUNS = [
    CompletedRun(strain="Caramel Apple Gelato", run_date=None, sessions_prior_today=None, utc_logged_at=None, equipment=RIG_1, waypoints=CAG_RUN1,
        date_label="May 2026",
        too_hot=True, duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 450°F',
        swab="Amber shading toward light brown.",
        extra_rows=[
            ("Vapor:",      "Limited flavor. Session did not express distinct character."),
            ("Diagnosis:",  "Endpoint of 450°F likely too aggressive — supported by swab darkening. Limited flavor may reflect endpoint temperature degrading terpene fraction at session tail, or may reflect moderate terpene content in this material independent of temperature. Both explanations are plausible; endpoint reduction will help distinguish them."),
            ("Adjustment:", "Pull endpoint back to 430°F. Shorten hold to 55 seconds to reduce risk of outlasting small load."),
        ],
    ),
    CompletedRun(strain="Orange Candy", run_date=None, sessions_prior_today=None, utc_logged_at=None, equipment=RIG_1, waypoints=OC_RUNS12,
        date_label="May 2026",
        too_hot=True, duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 450°F',
        swab="Not recorded.",
        extra_rows=[
            ("Result:", "Working well but first 40 seconds felt too flat and slow. Low vapor density in opening phase. Same result on Run 2."),
        ],
    ),
    CompletedRun(strain="Orange Candy", run_date=None, sessions_prior_today=None, utc_logged_at=None, equipment=RIG_1, waypoints=OC_RUNS12,
        date_label="May 2026",
        too_hot=True, duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 450°F — same as Run 1',
        swab="Not recorded.",
        extra_rows=[
            ("Result:",    "Same as Run 1 — opening too flat, low vapor density first 40s."),
            ("Diagnosis:", "Opening too flat — low vapor density in first 40s. Steeper climb 15–35s drives earlier vapor production. Flatter tail 35–65s closes the offset — a slowly-arrived-at 440°F delivers more heat to the material than a steeply-arrived-at 450°F."),
        ],
    ),
    CompletedRun(strain="Orange Candy", run_date=None, sessions_prior_today=None, utc_logged_at=None, equipment=RIG_1, waypoints=OC_RUN3,
        date_label="May 2026",
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 440°F',
        swab="Light golden/tan. Clean. Minimal peripheral darkening at tip edge — consistent with insert wall cooling, not degradation.",
        session_char="Very nice. Strong effects. Opening draws wispy but flavorful. Good progression through session.",
        intensity="Strong",
        analysis="Clean swab, strong result. Wispy opening draws suggest opportunity to raise opening setpoint slightly to improve vapor density at session start without affecting the clean tail.",
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 5), sessions_prior_today=1, utc_logged_at=None, equipment=RIG_1, waypoints=OC_RUN4,
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 440°F',
        swab="Light golden. Clean both times.",
        session_char="Fine. Not noticeably different from Run 3. Run repeated twice on May 5, 2026 — consistent results across both.",
        analysis="Clean swab confirmed. Results stable. Lower opening setpoint (350°F) under exploration for Run 5 as next variable to test.",
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 6), sessions_prior_today=0, utc_logged_at=None, equipment=RIG_1, waypoints=OC_RUN5,
        too_hot=True, duration_seconds=65, endpoint_note='<strong>Open:</strong> 350°F &nbsp;|&nbsp; <strong>Endpoint:</strong> 460°F',
        swab="Darker than target — direction consistent with endpoint too hot.",
        session_char="Last portion tad harsh, consistent with elevated endpoint. Effect notably stronger than prior runs.",
        extra_rows=[
            ("Observation:", "User's hypothesis: higher temperature produced stronger effect. Logged as stated — one data point, not a confirmed finding. Confounders include session-to-session variability in tolerance, load size, and conditions."),
            ("Next:",        "Returned to ramp curve for Run 6 — see results below."),
        ],
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 9), sessions_prior_today=3, utc_logged_at=None, equipment=RIG_1, waypoints=OC_RUN6,
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 430°F',
        swab="Light golden. Clean.",
        session_char="Very nice.",
        extra_rows=[
            ("Next:", "Repeat to confirm, or test 350°F open / 460°F endpoint curve when ready."),
        ],
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 9), sessions_prior_today=4, utc_logged_at=None, equipment=RIG_1, waypoints=OC_RUN7,
        duration_seconds=60, endpoint_note='<strong>Setpoint:</strong> 430°F steady (no ramp)',
        swab="Plain amber — clean.",
        session_char="Pleasant overall. Not as tasty as the ramp from lower temp. Harsh in the last 20 seconds.",
        analysis="Swab is clean, so harshness is a session character signal, not a floor indicator. Comparing to Run 6 (ramp to 430°F, light golden, very nice) — the flat hold at the same endpoint produces clearly more harshness and less flavor character. Consistent with the pattern seen on Fembot #3: flat holds at 430°F track hotter in session feel than ramps to the same endpoint, even with a clean swab.",
        extra_rows=[
            ("Next:", "Ramp curve (Run 6 shape) is outperforming the flat hold at 430°F. Repeat Run 6 ramp to confirm, or try 420°F flat hold to find the flat-hold ceiling."),
        ],
    ),
    CompletedRun(strain="The Hive #1", run_date=date(2026, 5, 7), sessions_prior_today=0, utc_logged_at=None, equipment=RIG_1, waypoints=HIVE1_RUN1,
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 440°F',
        swab="Light golden — clean. No darkening.",
        session_char="Nice flavors on the way up through the arc. Heavy indica effect.",
        analysis="Clean swab on first run — curve appears well-matched to this material. Repeated as Run 2 to confirm.",
    ),
    CompletedRun(strain="The Hive #1", run_date=date(2026, 5, 7), sessions_prior_today=1, utc_logged_at=None, equipment=RIG_1, waypoints=HIVE1_RUN2,
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 440°F — identical to Run 1',
        swab="Very light — cleaner than Run 1.",
        session_char="Really nice. Consistent with Run 1.",
        analysis="Two clean runs, consistent character, swab lighter on repeat. 440°F endpoint may be higher than needed — material is fully expressing before the endpoint. Run 3: trying steady 430°F flat hold (no ramp) to test whether curve shape affects the result.",
    ),
    CompletedRun(strain="The Hive #1", run_date=date(2026, 5, 8), sessions_prior_today=0, utc_logged_at=None, equipment=RIG_1, waypoints=HIVE1_RUN3,
        duration_seconds=45, endpoint_note='<strong>Setpoint:</strong> 430°F steady (no ramp)',
        swab="Light golden — clean.",
        session_char="First half: lots of flavor, low throat irritation. Second half: irritation increased, flavor faded to generic dab vapor — never harsh or burnt, just less distinct. Effect notably strong.",
        analysis="At a flat 430°F from the open, all terpene fractions (pinene through linalool, all below 430°F) are available simultaneously — first hit may be the full palette combining at once rather than staged. The ramp climbs through each fraction sequentially, which may be what gives those runs more distinct flavor progression across the arc. 45 seconds was too short — vapor was still producing at session end. Not a temperature issue, just cut off early. One data point. Directionally supports the ramp producing more distinct staged flavor vs. the flat hold combining everything at once. If revisiting the flat hold, extend to 60 seconds. Next planned: repeat the Run 1–2 ramp (380→390→410°F) with 430°F endpoint to compare directly on the same endpoint.",
    ),
    CompletedRun(strain="The Hive #1", run_date=date(2026, 5, 8), sessions_prior_today=1, utc_logged_at=None, equipment=RIG_1, waypoints=HIVE1_RUN4,
        duration_seconds=60, endpoint_note="<strong>Setpoint:</strong> 430°F steady (no ramp) — extended from Run 3's 45s",
        swab="Light golden — clean. Consistent with Run 3.",
        session_char="Similar to Run 3. Extended hold confirmed vapor was still producing at 45s in Run 3 — 60s felt more complete.",
        analysis="Two flat-hold data points, both clean swabs, consistent character. Next: ramp to 430°F endpoint (380→390→410→430°F) — the original planned experiment — to compare curve shape on the same endpoint.",
    ),
    CompletedRun(strain="The Hive #1", run_date=date(2026, 5, 8), sessions_prior_today=2, utc_logged_at=None, equipment=RIG_1, waypoints=HIVE1_RUN5,
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 430°F (ramp — same shape as Runs 1–2, endpoint reduced from 440°F)',
        swab="Light golden — a tad lighter than the flat-hold 430°F runs (Runs 3–4). Clean.",
        session_char="Nice distinct flavors through the first two-thirds. Harsh in the last ~10 seconds. Effects quite potent.",
        analysis="Distinct staged flavor character is consistent with the ramp — each terpene fraction vaporizes as the curve climbs through it, rather than all at once as in the flat hold. Swab difference vs. Runs 3–4 is within noise (too many uncontrolled variables). Harshness at session tail is a directional signal that 430°F may still be slightly above ideal for this material on the ramp.",
        extra_rows=[
            ("Next:", "Try 420–425°F endpoint on Run 6. Keep ramp shape unchanged."),
        ],
    ),
    CompletedRun(strain="Fembot #3", run_date=date(2026, 5, 9), sessions_prior_today=0, utc_logged_at=None, equipment=RIG_1, waypoints=FEMBOT3_RUN1,
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 430°F',
        swab="Light golden — clean. Two heads mostly white, two with light golden coloring. No darkening.",
        session_char="Very tasty on the ascent. No visible vapor until mid-range. Slight harshness at the tail. Effects upbeat, creative, not too body-heavy — consistent with sativa-dominant character.",
        extra_rows=[
            ("Next:", "Try steady 420°F flat hold (60s) on Run 2 — drop endpoint and change curve shape to test both variables."),
        ],
    ),
    CompletedRun(strain="Fembot #3", run_date=date(2026, 5, 9), sessions_prior_today=1, utc_logged_at=None, equipment=RIG_1, waypoints=FEMBOT3_RUN2,
        duration_seconds=60, endpoint_note='<strong>Setpoint:</strong> 430°F steady (no ramp)',
        swab="Light golden — clean. Consistent with Run 1.",
        session_char="Very tasty, great effects. Harshness in the last third.",
        analysis="Harshness at the tail is consistent with Run 1 (ramp to 430°F endpoint) — two data points now pointing at 430°F as slightly above ideal for this material, regardless of curve shape. Swab is clean, so this is a session character signal rather than a floor indicator.",
        extra_rows=[
            ("Next:", "Try 420°F steady flat hold on Run 3."),
        ],
    ),
    CompletedRun(strain="Mango Starburst #23", run_date=date(2026, 5, 9), sessions_prior_today=2, utc_logged_at=None, equipment=RIG_1, waypoints=MS23_RUN1,
        duration_seconds=65, endpoint_note='<strong>Endpoint:</strong> 430°F',
        swab="Very clean — no darkening.",
        session_char="Very piney character throughout — almost pine sol. Tasty, though not to user's taste preference. Heady effects. No harshness.",
        extra_rows=[
            ("Note:",    "Strong pine-forward character noted on first run. The SB36 lineage inference weighted limonene and terpinolene as prominent — the pronounced pine character is consistent with pinene playing a larger role than the inference anticipated. Logged as one data point; flavor character is a weak signal and single-session observations carry high uncertainty."),
            ("Verdict:", "Clean swab on first run. Curve well-matched to this material. Repeat on Run 2 to confirm."),
        ],
    ),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 10), sessions_prior_today=0,    utc_logged_at=None,                                              equipment=RIG_1, waypoints=MBD_RUN1,
        endpoint_note="<strong>Endpoint:</strong> 430°F",
        swab="Darker golden — between light golden target and amber. Nothing tasted burnt. Flagged as something to watch on subsequent runs.",
        session_char="Tasty first half, second half faded to generic. Milder effect — likely tolerance after 5 sessions the prior day.",
        intensity="Mild — tolerance confound (5 sessions prior day)",
    ),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 10), sessions_prior_today=1,    utc_logged_at=None,                                              equipment=RIG_1, waypoints=MBD_RUN2,
        endpoint_note="<strong>Endpoint:</strong> 430°F — same as Run 1",
        swab="Lighter than Run 1 — closer to the light golden target.",
        session_char="Distinct bacon character on the first half. Effects came on noticeably after this session.",
        intensity="Moderate",
        analysis="Swab trending cleaner on repeat. Flavor expressed distinctly on the first half. No harshness on either run. The Run 1 milder effect reads as a tolerance confound — effects landed clearly on Run 2.",
    ),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 11), sessions_prior_today=2,    utc_logged_at=datetime(2026, 5, 12,  5, 24, tzinfo=timezone.utc), equipment=RIG_1, waypoints=MBD_RUN3,
        endpoint_note="<strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F, ramp from 375°F open",
        swab="Clean golden.",
        session_char="Little bit harsh in the last 5 seconds. No harshness earlier in the session.",
        intensity="Medium-hard",
    ),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 12), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 13,  2, 30, tzinfo=timezone.utc), equipment=RIG_1, waypoints=MBD_RUN4,
        endpoint_note="<strong>Endpoint:</strong> 430°F — same as Runs 1 and 2",
        swab="Light golden.",
        session_char="Tail harshness again, consistent with prior 430°F runs. Interesting bitter note throughout — citrus rind character.",
        intensity="Big effect, seemingly short duration.",
    ),
    CompletedRun(strain="Rain Fruit",                        run_date=date(2026, 5, 10), sessions_prior_today=2,    utc_logged_at=None,                                              equipment=RIG_1, waypoints=RF_RUN1,
        endpoint_note="<strong>Endpoint:</strong> 430°F — baseline ramp",
        swab="Notably clean — lighter than target. No darkening.",
        session_char="Really clear fruit notes throughout. Strong effects — pressure up and behind the eyes. No harshness.",
        intensity="Strong",
        analysis="Clean first run. Distinct fruit character, strong effect. No floor signal, no harshness. Repeat the same curve on Run 2 to confirm.",
    ),
    CompletedRun(strain="Rain Fruit",                        run_date=date(2026, 5, 11), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 11, 22, 44, tzinfo=timezone.utc), equipment=RIG_1, waypoints=RF_RUN2,
        endpoint_note="<strong>Endpoint:</strong> 430°F &nbsp;|&nbsp; Open 5°F below baseline — testing lower open",
        swab="Light golden — clean.",
        session_char="Tasty. Got a bit hot in the last 10 seconds.",
        intensity="Mild",
        analysis="Curve felt well-suited to the strain overall. Tail heat in the last 10 seconds is consistent with the cross-strain pattern at 430°F endpoints (Hive #1 Run 5, Fembot #3 Runs 1–2). Swab is clean so this is a session character signal, not a floor indicator. Effects milder than Run 1 — likely session-to-session variability rather than a curve signal.",
    ),
    CompletedRun(strain="Rain Fruit",                        run_date=date(2026, 5, 11), sessions_prior_today=1,    utc_logged_at=datetime(2026, 5, 12,  0, 30, tzinfo=timezone.utc), equipment=RIG_1, waypoints=RF_RUN3,
        endpoint_note="<strong>Endpoint:</strong> 420°F (10-second hold) — down 10°F from prior runs",
        swab="Clean golden.",
        session_char="Notably less harshness. Slow build to intensity — not hard hitting.",
        intensity="Mild-moderate",
        analysis="420°F endpoint resolved the tail harshness that appeared at 430°F on Run 2 — consistent with the cross-strain pattern. Clean swab means no floor signal. The slower, gentler build suggests some intensity lives in the higher-temperature band. The path forward is to walk the endpoint back up incrementally to find where harshness re-enters.",
    ),
    CompletedRun(strain="Blueberry 36 #1",                  run_date=date(2026, 5, 15), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 16,  1, 53, tzinfo=timezone.utc), equipment=RIG_2, waypoints=BB36_1_RUN1,
        endpoint_note="<strong>Endpoint:</strong> 430°F — baseline",
        swab="Super light golden — very clean.",
        session_char="Not the most flavorful. Hard in the tail.",
        intensity="Medium",
    ),
    CompletedRun(strain="Blueberry 36 #1",                  run_date=date(2026, 5, 15), sessions_prior_today=1,    utc_logged_at=datetime(2026, 5, 16,  5, 48, tzinfo=timezone.utc), equipment=RIG_2, waypoints=BB36_1_RUN2,
        endpoint_note="<strong>Endpoint:</strong> 415°F with 20-second hold — ramp 375→400→415°F",
        swab="Very light golden — clean.",
        session_char="Not a lot of distinct flavor. Throat irritation at the tail. Spicy note at the end — like hot spice.",
        intensity="Medium and climbing",
        extra_rows=[("Effect:", "Waves of anxiety / possible paranoia emerging post-session. User notes Blueberry strains hit harder than they look — this has come up before on this lineage.")],
    ),
    CompletedRun(strain="Blueberry 36 #1",                  run_date=date(2026, 5, 16), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 17,  5, 32, tzinfo=timezone.utc), equipment=RIG_2, waypoints=BB36_1_RUN3,
        endpoint_note="<strong>Endpoint:</strong> 415°F with 20-second hold — repeated from Run 2",
        swab="Golden and light — clean.",
        session_char="Taste still mild, not a lot of distinct flavor. Tad bit of harshness in the throat at the end.",
        intensity="Pretty big at the moment.",
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 22), sessions_prior_today=0, utc_logged_at=datetime(2026, 5, 22, 23, 36, tzinfo=timezone.utc), equipment=RIG_3, waypoints=OC_RUN8,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 420°F — fast ramp (20s, 2°F/sec); 30s hold &nbsp;|&nbsp; <strong>Equipment:</strong> Inaugural Rig 3 (sapphire) run',
        swab="Ultra clean — essentially white/cream, no visible coloration.",
        session_char="Smooth and flavorful first draw through ~23s. Harshness in throat starting at ~31s (11s into 420°F hold), built through end.",
        intensity="Very very intense, delayed ~5 min onset.",
        dab_notes="Big cold nose orange note just now as I opened jar. Swabs look ultra clean to me. Hit was flavorful and smooth up for first draw which lasted until timer showed 27 seconds left. Next draw got harsh in throat at 19 left on timer and that built through the end. I probably could have stopped hitting it earlier, which maybe points to loading bigger dabs and not trying to be super efficient about vaporizing it, just vaporize the sweet spot and leave the rest to the swab. Which would mean that swab color doesn't matter anymore. Would maybe be a difficult habit to break, the thinking is to not waste any of this precious and expensive stuff. Very very intense after about 5 mins.",
        analysis="Inaugural Rig 3 run on OC — first sapphire data point in the log. Ultra-clean swab and very strong delayed effect are consistent: sapphire extracting efficiently, 420°F delivering more than 420°F on quartz would. If sapphire runs 10–20°F hotter in effective temperature (per methodology note), this sits in the 430–440°F equivalent zone — which maps onto OC's quartz history: Run 6 (ramp to 430°F) was clean but at the edge. Ramp phase smooth; harshness entered 11 seconds into the 420°F hold. Shape working — this is a hold-temperature issue. Strong cold nose orange note at jar open; flavor in vapor was 'flavorful and smooth' without named character — whether the orange came through in vapor is unresolved. User suggested loading bigger and stopping at the sweet spot rather than riding the tail, noting this would make swab color less meaningful as a floor indicator — logged as a hypothesis, not a finding.",
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 22), sessions_prior_today=1, utc_logged_at=datetime(2026, 5, 23, 2, 45, tzinfo=timezone.utc), equipment=RIG_3, waypoints=OC_RUN9,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 415°F — down 5°F from Run 8',
        swab="Golden clean — not as light as Run 8's near-white.",
        session_char="First draw ~25s clean but wispy; second draw ~10s, trace harshness as load ran out. Load done after ~35s.",
        intensity="Mild",
        dab_notes="First draw went 25 seconds, no harshness, kind of wispy vapor. Second draw was about 10 seconds, felt like it was knocking on the harshness but was just barely there. And then the load was definitely done. I think I probably loaded less rather than more. See it's going to be a hard habit to break. Swabs were golden clean but not as light as previous run. Effects mild so far but that would also fit with smaller dab load. It stayed mild.",
        analysis="OC Run 9 on sapphire at 415°F — directionally cleaner than Run 8. Run 8 (420°F) had harshness entering 11 seconds into the hold; Run 9 had a clean 25-second first draw and trace harshness only as the load ran out. That's a meaningful difference, but the small load is a confound — less material vaporizes over a shorter window, which means less time at endpoint temperature before the load is spent. Can't attribute the cleaner tail to 415°F alone. Wispy vapor on the first draw is consistent with a small load; could also suggest 415°F is slightly below the sapphire's vapor production sweet spot. Swab came back golden clean — slightly darker than Run 8's near-white, which may just be run-to-run variation, or slightly more material left at the lower endpoint. Intensity mild, consistent with smaller load.",
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 23), sessions_prior_today=0, utc_logged_at=datetime(2026, 5, 23, 19, 24, tzinfo=timezone.utc), equipment=RIG_3, waypoints=OC_RUN9,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 415°F — same as Run 9; ~25% larger load',
        swab="Very light golden — a bit more reclaim than prior runs.",
        session_char="No harshness on two full draws across 50 seconds.",
        intensity="Medium (delayed onset ~5 min).",
        dab_notes="Very light golden, maybe a bit more reclaim than prior runs. Harshness never really entered on two big draws across 50 seconds. Effect right after is very light. It grew to a medium I think. This is maybe why increase in temp is warranted.",
        analysis="415°F on Rig 3 with a ~25% larger load — clean across two full draws, no harshness. This resolves Run 9's load-size confound: a fuller load at 415°F still produced no harshness, confirming 415°F is within the clean range on the sapphire. Run 8 (420°F, normal load) had harshness at 11s into the hold — 5°F made the difference. Swab came back very light golden with slightly more reclaim than prior runs, consistent with slightly less complete vaporization at the lower endpoint. Effect grew from very light to medium over ~5 minutes — delayed onset pattern consistent with Run 8. Medium ceiling vs. Run 8's \"very very intense\" may reflect the lower endpoint, but run-to-run variability and tolerance are real confounders; single data point. User flagged this as a reason to inch the temperature up.",
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 23), sessions_prior_today=1, utc_logged_at=datetime(2026, 5, 23, 23, 38, tzinfo=timezone.utc), equipment=RIG_3, waypoints=OC_RUN11,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 417°F — up 2°F from Runs 9–10',
        swab="Very light golden, slightly more reclaim than Run 10.",
        session_char="Clean through first draw; harshness entered at exactly 417°F (end of first draw, ~20s), mild but present and slowly building through the hold.",
        intensity="Very hard — eyes blurring, body feels like it's vibrating ~14 minutes post-session.",
        dab_notes="Same golden as last time, maybe more reclaim than last time too. Harshness hit exactly at the end of the first draw which was also exactly when temp hit 417. It was mild but present and slowly increasing through rest of the draw. Very hard. Eyes are blurring, body feels like it's vibrating — about 14 minutes after session open.",
        analysis="417°F on Rig 3, slightly larger load than Run 10. Harshness appeared at exactly the moment the temperature reached 417°F — end of the first draw (~20s), immediate on endpoint arrival, not a hold-duration accumulation effect. Mild but present and building through the hold. Run 10 (415°F, comparable load) was clean across two full draws. Two-degree difference, clean outcome vs. immediate harshness onset: the ceiling is located at 415–417°F, and this run puts the top edge there. Swab came back very light golden with slightly more reclaim than Run 10 — consistent with less complete vaporization at a lower endpoint, though the read is noisy at this level of difference. Effect landed very hard — a meaningful potency step up from Run 10's medium. The intensity trade-off across 2°F is real.",
    ),
    CompletedRun(strain="Orange Candy", run_date=date(2026, 5, 23), sessions_prior_today=2, utc_logged_at=datetime(2026, 5, 24, 4, 21, tzinfo=timezone.utc), equipment=RIG_3, waypoints=OC_RUN12,
        duration_seconds=50, endpoint_note='<strong>Endpoint:</strong> 416°F — up 1°F from Runs 9–10, down 1°F from Run 11',
        swab="Light golden.",
        session_char="First draw flavorful with bitter citrus note; harshness entered ~35s in (15s into 416°F hold), mild and never acute.",
        intensity="Medium.",
        dab_notes="Got harsh at about 15 seconds left on the timer, and never got super harsh. Swabs were light golden. Intensity medium right now. First draw was flavorful, that increasingly familiar bitter citrus note came through from the beginning.",
        analysis="416°F on Rig 3 — between Run 10's clean 415°F and Run 11's immediate-harshness 417°F. Harshness entered at ~35s, 15 seconds into the hold, mild and never acute. For comparison, Run 11 (417°F) had harshness at endpoint arrival (~20s, immediately). The gradient is clear across three adjacent endpoints: 415°F clean, 416°F mild harshness entering mid-hold, 417°F immediate on arrival. Swab light golden, consistent with the sapphire OC pattern. Intensity medium — same read as Run 10 at 415°F, though this was the third session of the day, so the lack of intensity gain over 415°F is hard to read cleanly. Bitter citrus note from the first draw — consistent with OC's orange lineage expressing in vapor; the same cross-strain citrus note has appeared in MB9ZST R1 (tangerine) and MBD R4 (citrus rind), though the connection is not established.",
    ),
]

STRAIN_STATUS = [
    StrainStatus(name="Caramel Apple Gelato", profile_anchor="#cag-profile", next_text="Try 430°F endpoint", accent=None, slug="cag",
        info=CAG_INFO,
        terpene_note='<strong>Terpene inference:</strong> Limonene and myrcene inferred from Gelato lineage. Muted nose consistent with heavier, less-volatile terpene profile. See <a href="#terpene-ref">Terpene Reference</a>.',
        next_dab_notes="",
        next_ai_analysis="One data point at 450°F with an amber-toward-brown swab — reliable floor signal. Pull the endpoint back to 430°F. Nothing subtle here, it was just too hot.",
        next_waypoints=CAG_RUN2,
    ),
    StrainStatus(name="Orange Candy", profile_anchor="#oc-profile", next_text="Repeat 416°F as first dab of the day — clean intensity read vs. 415°F", accent=None, slug="oc",
        info=OC_INFO,
        terpene_note='<strong>Terpene inference:</strong> Limonene inferred dominant from orange character (Naran J × Tropimango lineage — unconfirmed). See <a href="#terpene-ref">Terpene Reference</a>.',
        next_dab_notes="Got harsh at about 15 seconds left on the timer, and never got super harsh. Swabs were light golden. Intensity medium right now. First draw was flavorful, that increasingly familiar bitter citrus note came through from the beginning.",
        next_ai_analysis="416°F delivered mild late harshness (entering 15s into the hold) as the third dab of the day — the intensity comparison to 415°F was muddied by tolerance. Next: repeat 416°F as the first dab of the day to get a clean read. If intensity steps up meaningfully over 415°F with the same harshness profile, 416°F becomes a real preference option. If not, 415°F is the call.",
        next_waypoints=OC_RUN12,
    ),
    StrainStatus(name="The Hive #1", profile_anchor="#hive1-profile", next_text="Try 420–425°F endpoint on Run 6", accent=None, slug="hive1",
        info=HIVE1_INFO,
        terpene_note='<strong>Terpene inference:</strong> Myrcene and terpinolene inferred from tropical fruit character; Honey Banana × Papaya lineage (Bloom Seed Co). Terpene ratios not inferable from genetics — standard palette as orientation only. See <a href="#terpene-ref">Terpene Reference</a>.',
        next_dab_notes="Try 420–425°F endpoint, keep ramp shape.",
        next_ai_analysis="Flat-hold 430°F was clean twice. Ramp to 430°F showed tail harshness once. Harshness is directional but one data point — the flat holds didn't show it at the same endpoint. 425°F ramp is a reasonable conservative step; could also repeat the ramp at 430°F first to confirm the harshness was real.",
        next_waypoints=HIVE1_NEXT,
    ),
    StrainStatus(name="Fembot #3", profile_anchor="#fembot3-profile", next_text="Try 420°F steady hold on Run 3", accent=None, slug="fembot3",
        info=FEMBOT3_INFO,
        terpene_note='<strong>Terpene inference:</strong> Terpinolene inferred likely dominant from Fuzzy Melon character; Fuzzy Melon × Rambutan lineage. Standard cannabis palette otherwise — not measured. See <a href="#terpene-ref">Terpene Reference</a>.',
        next_dab_notes="",
        next_ai_analysis="Strongest signal in the log — harshness at 430°F on both a ramp and a flat hold. Two shapes, same outcome. 430°F is above ideal for this material. 420°F flat hold is the clear next test.",
        next_waypoints=FEMBOT3_RUN3,
    ),
    StrainStatus(name="Mango Starburst #23", profile_anchor="#ms23-profile", next_text="Repeat Run 1 curve to confirm", accent=None, slug="ms23",
        info=MS23_INFO,
        terpene_note="<strong>Terpene inference:</strong> Limonene and terpinolene weighted from SB36 line's citrus-candy character; pronounced pine on Run 1 suggests pinene may be more prominent than inferred. Not measured. See <a href=\"#terpene-ref\">Terpene Reference</a>.",
        next_dab_notes="",
        next_ai_analysis="One run, clean swab, no harshness. Pine-forward character was noted but single-session flavor observations are noisy. Repeat the same curve before changing anything — if it's pine again on Run 2, that's real.",
        next_waypoints=MS23_RUN1,
    ),
    StrainStatus(name="Maple Bacon Donut",                 profile_anchor="#mbd-profile",      next_text="Try faster ramp to 460°F on Run 5",                                                    accent=None, slug="mbd",
        info=MBD_INFO,
        terpene_note="<strong>Terpene inference:</strong> Genetics not documented — no strain-specific inference available. Standard cannabis palette as orientation only. See <a href=\"#terpene-ref\">Terpene Reference</a>.",
        next_dab_notes="Run 4 back to 430°F: light golden swab, tail harshness consistent with prior 430°F pattern, interesting bitter/citrus rind note throughout, big effect, seemingly short duration.",
        next_ai_analysis="Tail harshness at 430°F is consistent across runs. Run 5 moves in a different direction — faster ramp to 460°F — rather than continuing to work the lower end. That's an exploratory step; the session character at 460°F is unknown for MBD. The citrus rind note is worth watching on Run 5 to see whether it changes with the faster climb. The short duration observation from Run 4 is a single data point, unclear if it means anything. Swab has been clean throughout, so the harshness is coming from endpoint temperature, not material condition.",
        next_waypoints=MBD_NEXT,
    ),
    StrainStatus(name="Rain Fruit",                        profile_anchor="#rainfruit-profile",next_text="Walk endpoint up incrementally — try 423°F on Run 4",                                  accent=None, slug="rainfruit",
        info=RF_INFO,
        terpene_note="<strong>Terpene inference:</strong> Genetics not documented — no strain-specific inference available. Standard cannabis palette as orientation only. See <a href=\"#terpene-ref\">Terpene Reference</a>.",
        next_dab_notes="420 hold worked — notably less harshness, clean golden swabs. Not hard hitting but slow build to intensity. Want to slowly walk up the curve.",
        next_ai_analysis="The 420°F endpoint confirmed the hypothesis: dropping 10°F from the 430°F runs eliminated tail harshness without producing a floor signal. The trade-off is real — effects were milder and slower-building, suggesting the higher-temperature band contributes to intensity. Next step is to probe incrementally upward: try 423°F endpoint (same ramp shape, +3°F) to begin finding where harshness re-enters. Small steps keep the signal clean — each run is one data point on the harshness-intensity curve.",
        next_waypoints=RF_RUN4_NEXT,
    ),
    StrainStatus(name="Blueberry 36 #1",                  profile_anchor="#bb361-profile",    next_text="Try 410°F endpoint on Run 4 — tail harshness confirmed at 415°F across Runs 2 and 3", accent=None, slug="bb361",
        info=BB36_1_INFO,
        terpene_note="<strong>Terpene inference:</strong> Myrcene inferred dominant from DJ Short's Blueberry base genetics; caryophyllene and alpha-pinene as secondaries. LOUD cold nose with no distinct discernible notes — nose is a weak secondary signal only. See <a href=\"#terpene-ref\">Terpene Reference</a>.",
        next_dab_notes="Run 3 repeated the 415°F curve (375→400→415, 20s hold): golden and light swab. Taste still mild, not a lot of distinct flavor. Tad bit of harshness in the throat at the end. Pretty big intensity.",
        next_ai_analysis="Tail harshness at 415°F is now confirmed across two runs (Runs 2 and 3) — no longer a single-run signal. Swab has been very light golden across all three runs, consistent with the Gemlock efficiency pattern. Intensity landed big on Run 3 despite the lower endpoint, which is notable. 'Not a lot of distinct flavor' has been the read at both 430°F (Run 1) and 415°F (Runs 2–3) — this looks like the phenotype's character, not a temperature signal. Next: drop to 410°F endpoint, same ramp shape. Two confirmed runs at 415°F with harshness — time to step down.",
        next_waypoints=BB36_1_NEXT,
    ),
]

TERPENE_REFERENCE = [
    # Low band — below 356°F / 180°C
    TerpeneEntry(name="Humulene",          alias="alpha-humulene",              bp_f=225, bp_c=107, band="Low",  aroma="Woody, spicy-clove",                   qualities="Calming; appetite-suppressing character",   found_in="Hops, allspice, cloves, coriander"),
    TerpeneEntry(name="Alpha-Pinene",      alias="alpha-pinene",                bp_f=313, bp_c=156, band="Low",  aroma="Pine forest",                          qualities="Alerting; opens airways",                  found_in="Pine, rosemary, dill, basil, sage"),
    TerpeneEntry(name="Camphene",          alias="camphene",                    bp_f=318, bp_c=159, band="Low",  aroma="Cool camphor, musky earth",             qualities="Limited evidence",                         found_in="Fir, nutmeg, rosemary, sage"),
    TerpeneEntry(name="Beta-Pinene",       alias="beta-pinene",                 bp_f=331, bp_c=166, band="Low",  aroma="Pine forest, fresh",                   qualities="Alerting; focus-associated",               found_in="Pine, dill, basil, rosemary"),
    TerpeneEntry(name="Myrcene",           alias="beta-myrcene",                bp_f=333, bp_c=167, band="Low",  aroma="Musky, earthy, sweet herbal",           qualities="Relaxing, sedating",                       found_in="Mangoes, hops, lemongrass, thyme"),
    TerpeneEntry(name="Carene",            alias="delta-3-carene",              bp_f=340, bp_c=171, band="Low",  aroma="Musky citrus, sweet pine",              qualities="Uplifting; focus-associated",              found_in="Rosemary, cedar, basil, pepper"),
    TerpeneEntry(name="Phellandrene",      alias="alpha/beta-phellandrene",     bp_f=342, bp_c=172, band="Low",  aroma="Citrusy, peppermint",                  qualities="Uplifting character",                      found_in="Eucalyptus, dill, water fennel"),
    TerpeneEntry(name="Terpinene",         alias="alpha-terpinene",             bp_f=343, bp_c=173, band="Low",  aroma="Piney, smokey, herbaceous",             qualities="Supporting",                               found_in="Tea tree, eucalyptus, marjoram"),
    TerpeneEntry(name="Limonene",          alias="limonene",                    bp_f=349, bp_c=176, band="Low",  aroma="Citrus",                                qualities="Uplifting; stress-easing",                 found_in="Citrus rinds, juniper, peppermint"),
    TerpeneEntry(name="Eucalyptol",        alias="cineole",                     bp_f=349, bp_c=176, band="Low",  aroma="Cool camphor, minty",                  qualities="Alerting; opens airways",                  found_in="Eucalyptus, tea tree, mugwort"),
    TerpeneEntry(name="Cymene",            alias="p-cymene",                    bp_f=351, bp_c=177, band="Low",  aroma="Mild sweet aged wood, lemon",           qualities="Supporting",                               found_in="Thyme, oregano, cumin, cilantro"),
    TerpeneEntry(name="Ocimene",           alias="beta/trans-beta-ocimene",     bp_f=352, bp_c=178, band="Low",  aroma="Tropical fruit, woody green citrus",   qualities="Uplifting character",                      found_in="Basil, orchids, kumquats, parsley"),
    # Mid band — 356–446°F / 180–230°C
    TerpeneEntry(name="Terpinolene",       alias="alpha-terpinolene",           bp_f=369, bp_c=187, band="Mid",  aroma="Fresh, herbal, sweet, floral, piney",  qualities="Uplifting; sedating in isolation",         found_in="Limes, cumin, lilac, nutmeg"),
    TerpeneEntry(name="Linalool",          alias="linalool",                    bp_f=388, bp_c=198, band="Mid",  aroma="Floral, citrusy-sweet",                qualities="Calming, sedating",                        found_in="Lavender, citrus, rosemary, basil"),
    TerpeneEntry(name="Sabinene",          alias="sabinene hydrate / thujanol", bp_f=396, bp_c=202, band="Mid",  aroma="Woodsy, spicy",                        qualities="Supporting",                               found_in="Norway Spruce, nutmeg, holm oak"),
    TerpeneEntry(name="Fenchol",           alias="fenchyl alcohol",             bp_f=397, bp_c=203, band="Mid",  aroma="Lemon-lime, piney, camphor",           qualities="Supporting",                               found_in="Basil, aster flowers"),
    TerpeneEntry(name="Borneol",           alias="bornyl alcohol",              bp_f=414, bp_c=212, band="Mid",  aroma="Cool minty, camphor",                  qualities="Calming, sedating",                        found_in="Rosemary, mint, ginger, camphor"),
    TerpeneEntry(name="Isoborneol",        alias="exo-borneol",                 bp_f=414, bp_c=212, band="Mid",  aroma="Woody-sweet, spicy",                   qualities="Calming, sedating",                        found_in="Valerian, sage, thyme"),
    TerpeneEntry(name="Terpineol",         alias="alpha-terpineol",             bp_f=430, bp_c=221, band="Mid",  aroma="Lilac, floral blossom",                qualities="Calming, sedating",                        found_in="Pine oil, petitgrain, cajuput"),
    TerpeneEntry(name="Citronellol",       alias="beta-citronellol",            bp_f=435, bp_c=224, band="Mid",  aroma="Rose, citrus",                         qualities="Relaxing; variable",                       found_in="Citronella, roses, geraniums"),
    TerpeneEntry(name="Pulegone",          alias="pulegone",                    bp_f=435, bp_c=224, band="Mid",  aroma="Minty-camphor, resinous",              qualities="Calming, sedating",                        found_in="Catnip, pennyroyal, rosemary"),
    TerpeneEntry(name="Geraniol",          alias="geraniol",                    bp_f=446, bp_c=230, band="Mid",  aroma="Sweet floral, fruity",                 qualities="Supporting",                               found_in="Roses, lemongrass, citronella"),
    # High band — above 446°F / 230°C
    TerpeneEntry(name="Anethole",          alias="anethole",                       bp_f=454, bp_c=234, band="High", aroma="Licorice, sweet",                      qualities="Sedating character",                   found_in="Anise, fennel, star anise"),
    TerpeneEntry(name="Guaiene",           alias="alpha/beta-guaiene",             bp_f=455, bp_c=235, band="High", aroma="Sweet, woody, earthy, spicy",          qualities="Supporting",                           found_in="Palo Santo"),
    TerpeneEntry(name="Geranyl Acetate",   alias="geranyl acetate",                bp_f=468, bp_c=242, band="High", aroma="Sweet floral, pear-like",              qualities="Supporting",                           found_in="Lemongrass, coriander, geraniums"),
    TerpeneEntry(name="Elemene",           alias="alpha/beta/delta/gamma-elemene", bp_f=487, bp_c=253, band="High", aroma="Waxy, herbal",                         qualities="Limited research",                     found_in="Ginseng, Chinese Yu Jin"),
    TerpeneEntry(name="Caryophyllene",     alias="beta/trans-caryophyllene",       bp_f=493, bp_c=256, band="High", aroma="Spicy, peppery",                       qualities="Calming; CB2 receptor binding",        found_in="Black pepper, cloves, hops, oregano"),
    TerpeneEntry(name="Cedrene",           alias="alpha/beta-cedrene",             bp_f=505, bp_c=263, band="High", aroma="Light woodsy",                         qualities="Supporting",                           found_in="Cedarwood, juniper, cypress"),
    TerpeneEntry(name="Valencene",         alias="valencene",                      bp_f=520, bp_c=271, band="High", aroma="Sweet fresh citrus",                   qualities="Alerting, uplifting",                  found_in="Valencia oranges"),
    TerpeneEntry(name="Farnesene",         alias="alpha/beta-farnesene",           bp_f=523, bp_c=273, band="High", aroma="Green apple",                          qualities="Calming, sedating",                    found_in="Apple skins, pears"),
    TerpeneEntry(name="Nerolidol",         alias="cis/trans-nerolidol",            bp_f=529, bp_c=276, band="High", aroma="Woody bark, waxy, floral",             qualities="Calming, sedating",                    found_in="Neroli, jasmine, ginger, lavender"),
    TerpeneEntry(name="Caryophyllene Oxide", alias="beta-caryophyllene oxide",     bp_f=536, bp_c=280, band="High", aroma="Dry, fresh, spicy-sweet",              qualities="Calming; CB2 receptor binding",        found_in="Black pepper, caraway, cloves"),
    TerpeneEntry(name="Guaiol",            alias="guaiol",                         bp_f=550, bp_c=288, band="High", aroma="Piney, woody, rose-like",              qualities="Supporting",                           found_in="Cypress pines, guaiacum plant"),
    TerpeneEntry(name="Eudesmol",          alias="gamma/alpha/beta-eudesmol",      bp_f=574, bp_c=301, band="High", aroma="Woody-sweet",                          qualities="Mildly sedating",                      found_in="Cypress, valerian, eucalyptus"),
    TerpeneEntry(name="Bisabolol",         alias="alpha-bisabolol / levomenol",    bp_f=599, bp_c=315, band="High", aroma="Sweet floral, honey, mild coconut",    qualities="Calming, soothing",                    found_in="Chamomile"),
    TerpeneEntry(name="Phytol",            alias="phytol",                         bp_f=637, bp_c=336, band="High", aroma="Grassy",                               qualities="Mildly sedating",                      found_in="Green tea"),
]

# ── COLOR RESOLUTION ─────────────────────────────────────────────────────────

def _hex_to_hsl(hex_color):
    r, g, b = [int(hex_color.lstrip('#')[i:i+2], 16) / 255 for i in (0, 2, 4)]
    max_c, min_c = max(r, g, b), min(r, g, b)
    l = (max_c + min_c) / 2
    if max_c == min_c:
        return 0, 0, l * 100
    d = max_c - min_c
    s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
    if max_c == r:   h = (g - b) / d + (6 if g < b else 0)
    elif max_c == g: h = (b - r) / d + 2
    else:            h = (r - g) / d + 4
    return (h / 6) * 360, s * 100, l * 100

def _hsl_to_hex(h, s, l):
    s /= 100; l /= 100
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    if   0   <= h < 60:  r, g, b = c, x, 0
    elif 60  <= h < 120: r, g, b = x, c, 0
    elif 120 <= h < 180: r, g, b = 0, c, x
    elif 180 <= h < 240: r, g, b = 0, x, c
    elif 240 <= h < 300: r, g, b = x, 0, c
    else:                r, g, b = c, 0, x
    return '#{:02X}{:02X}{:02X}'.format(int((r+m)*255), int((g+m)*255), int((b+m)*255))

def _resolve_accent_colors(strain_list=None):
    # Distribute hues evenly across non-green space (0–89° and 166–359°, avoiding 90–165°).
    # Strains with an explicit accent hex in STRAIN_STATUS use that color instead.
    # strain_list defaults to the module-level STRAIN_STATUS (active strains only).
    # Pass a combined list from the generator to resolve across the full set.
    if strain_list is None:
        strain_list = STRAIN_STATUS
    NON_GREEN = [(0, 90), (166, 360)]
    total = sum(e - s for s, e in NON_GREEN)
    n = len(strain_list)
    step = total / n
    SAT, LGT = 38, 58
    auto_hues = []
    for i in range(n):
        pos = i * step
        for start, end in NON_GREEN:
            span = end - start
            if pos < span:
                auto_hues.append(start + pos)
                break
            pos -= span
    resolved = {}
    for i, s in enumerate(strain_list):
        resolved[s.name] = s.accent if s.accent is not None else _hsl_to_hex(auto_hues[i], SAT, LGT)
    return resolved

_ACCENT_RESOLVED = _resolve_accent_colors()

# ── VALIDATION ───────────────────────────────────────────────────────────────

def validate():
    strain_names = {s.name for s in STRAIN_STATUS}
    errors = []

    for i, run in enumerate(COMPLETED_RUNS):
        if run.strain not in strain_names:
            errors.append(f"COMPLETED_RUNS[{i}] strain '{run.strain}' not found in STRAIN_STATUS")

    for i, run in enumerate(COMPLETED_RUNS):
        wps = run.waypoints
        if not wps:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): empty waypoints list")
            continue
        for j, wp in enumerate(wps):
            if not (200 <= wp.temp_f <= 650):
                errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}) waypoint {j}: "
                               f"temp_f={wp.temp_f} outside expected range 200–650°F")
        times = [wp.time_s for wp in wps]
        if times != sorted(times):
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): waypoint times not monotonically increasing: {times}")

    for i, run in enumerate(COMPLETED_RUNS):
        eq = run.equipment
        if eq is None:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment is None — "
                           f"every run must carry an explicit EquipmentConfig "
                           f"(None never means 'inherit a session default')")
            continue
        if not eq.glass_top:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment.glass_top is empty")
        if not eq.insert.brand:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment.insert.brand is empty")
        if not eq.insert.model:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment.insert.model is empty")
        if not eq.insert.material:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment.insert.material is empty")
        if not eq.carb_cap.brand:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment.carb_cap.brand is empty")
        if not eq.carb_cap.model:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment.carb_cap.model is empty")
        if not eq.carb_cap.airflow:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment.carb_cap.airflow is empty")
        for j, pearl in enumerate(eq.pearls):
            if pearl.diameter_mm <= 0:
                errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): pearl[{j}].diameter_mm={pearl.diameter_mm} must be > 0")
            if not pearl.material:
                errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): pearl[{j}].material is empty")

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(f"  {e}")
        raise SystemExit(1)

def validate_accent_colors():
    # Only check manually-overridden colors — auto-assigned ones are valid by construction.
    overrides = [(s.name, s.accent) for s in STRAIN_STATUS if s.accent is not None]
    if not overrides:
        return
    all_resolved = [(s.name, _ACCENT_RESOLVED[s.name]) for s in STRAIN_STATUS]
    warnings = []
    for strain, color in overrides:
        h, s, l = _hex_to_hsl(color)
        if 90 <= h <= 165:
            warnings.append(f"{strain} override {color}: hue {h:.0f}° in green range (90–165°) — clashes with UI chrome")
        if s > 50 and 35 <= l <= 70:
            warnings.append(f"{strain} override {color}: saturation {s:.0f}% too high — avoid miami vice brights")
        for other_strain, other_color in all_resolved:
            if other_strain == strain:
                continue
            oh, _, ol = _hex_to_hsl(other_color)
            hue_diff = min(abs(h - oh), 360 - abs(h - oh))
            if hue_diff < 30 and abs(l - ol) < 20:
                warnings.append(f"{strain} override {color} too close to {other_strain} {other_color}: {hue_diff:.0f}° apart")
    if warnings:
        print("ACCENT COLOR WARNINGS:")
        for w in warnings: print(f"  {w}")
