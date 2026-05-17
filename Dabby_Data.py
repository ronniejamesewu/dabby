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
class EquipmentConfig:
    insert: str                    # "quartz", "sapphire"
    carb_cap: str                  # specific model, e.g. "Cloud Vortex 21.0",
                                   # "Gemlock joystick" — NOT a category; string
                                   # equality drives run comparability (Guardrail 3)
    pearl_diameter_mm: int | None  # None = no pearl (explicit); 6, etc.
    # No field defaults: a default would let an unspecified run silently validate
    # as some config. Every run states its config explicitly (see _SPINNER/_GEMLOCK).

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
    hold_seconds: int = 65
    endpoint_note: str = ""          # "steady (no ramp)", "same as Run 1", etc.

    # Session content (currently string literals in build_html() — migrated in Step 3)
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
    terpene_table_rows: list | None = None   # only MB9ZST currently
    terpene_table_note: str = ""     # note above terpene table (MB9ZST only)

    # Current "What to Try Next" — revisable strain-level guidance (N5)
    # Today these are inline args to what_to_try_next_html(); Step 3 makes them explicit.
    # NOT sourced from any run's frozen analysis.
    next_dab_notes: str = ""
    next_ai_analysis: str = ""
    next_waypoints: list | None = None

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
    ("Insert",       "20mm (quartz current; sapphire profiles to be added when acquired)"),
    ("Technique",    "Cold start — pre-load into cold insert before every session"),
    ("Load Size",    "Rice grain (small)"),
    ("Offset Est.",  "Probably small under most operating conditions. Dominant uncertainties are vaporization cooling and dynamic lag during steep ascent. At flat or slowly-ascending phases the system approaches equilibrium. Setpoints are reasonable proxies for material contact temperature."),
    ("Draw Style",   "Long, slow draws throughout session"),
    ("Terp Tools",   "Gemlock joystick (as of MB9ZST Run 1, May 13, 2026). Prior sessions: Cloud Vortex 21.0 spinner cap + 6mm quartz pearl in insert."),
    ("Session End",  "Stop when vapor production drops — do not ride timer on small loads"),
]

BASELINE_CURVE = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]

WWZ_INFO = [
    ("Strain",      "WW Z (White Widow × Zkittlez lineage — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Piney with sweet undertone (weak secondary signal only)"),
]
WWZ_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — minor, inferred"),
    ("Alpha-Pinene",  "311°F / 155°C", "Pine — inferred dominant; weakly supported by nose observation"),
    ("Myrcene",       "334°F / 168°C", "Earthy, sweet — inferred"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, floral — inferred (Z lineage)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
]
WWZ_RUN1 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=378, note="Extended flat — low-boiling terpene zone (~311°F pinene region)"),
    Waypoint(time_s=40, temp_f=395, note="Mid ascent — mid-range terpene zone (~334°F myrcene region)"),
    Waypoint(time_s=65, temp_f=440, note="Endpoint — upper terpene zone + THC completion"),
]

CAG_INFO = [
    ("Strain",      "Caramel Apple Gelato (Gelato lineage: Sunset Sherbet × Thin Mint GSC — inferred)"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Nose",        "Muted — no distinct notes (weak secondary signal, consistent with heavier terpene profile)"),
]
CAG_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred, low room-temp volatility explains muted nose"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred from Gelato lineage"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
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
    ("Nose",        "Not yet recorded"),
]
OC_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred, low room-temp volatility"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred dominant, orange character"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred secondary"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
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
HIVE1_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred secondary (both parents)"),
    ("Myrcene",       "334°F / 168°C", "Earthy, tropical — inferred dominant (both parents' fruit character)"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred (tropical fruit character consistent with lineage)"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, floral — inferred (Papaya lineage)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred, minor"),
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

FEMBOT3_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy, tropical — inferred secondary"),
    ("Limonene",      "349°F / 176°C", "Citrus-candy — inferred, consistent with melon/tropical lineage"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, fruity, floral — inferred likely dominant (Fuzzy Melon character)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
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
MS23_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy, tropical — inferred secondary"),
    ("Limonene",      "349°F / 176°C", "Citrus, orange peel — inferred likely dominant (SB36 tangie-like front end)"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, candy-tropical — inferred prominent (SB36 candy-forward character)"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
]

MBD_INFO = [
    ("Strain",      "Maple Bacon Donut"),
    ("Consistency", "Cold cure"),
    ("Producer",    "Quasi Farms (Michigan)"),
    ("Micron",      "Not recorded"),
    ("Nose",        "Not yet recorded"),
]
MBD_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
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
RF_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor"),
    ("Myrcene",       "334°F / 168°C", "Earthy — inferred"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred"),
    ("Terpinolene",   "367°F / 186°C", "Sweet — inferred"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
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
BB36_1_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred secondary (DJ Short's Blueberry lineage)"),
    ("Alpha-Pinene",  "311°F / 155°C", "Pine — inferred secondary (DJ Short's Blueberry lineage)"),
    ("Myrcene",       "334°F / 168°C", "Earthy, sweet — inferred dominant (DJ Short's Blueberry lineage)"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, floral — inferred minor"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
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

MB9ZST_INFO = [
    ("Strain",      "Mango Banana #9 + Z + Sour Tangie"),
    ("Product",     "Persy Neapolitan — three-strain cold-cure blend, 2g jar"),
    ("Consistency", "Cold cure"),
    ("Producer",    "710 Labs"),
    ("Extraction",  "90μ full-melt bubble hash, hand-pressed"),
    ("Blend",       "Mango Banana #9 (SB 36 × Forbidden Banana) · Z (Zkittlez lineage) · Sour Tangie (Sour Diesel × Tangie)"),
    ("Character",   "Sativa-leaning hybrid — uplifting from Sour Tangie, tropical melon from Mango Banana, sweet/gas balance from Z. Neapolitan format means three separate layers in one jar; actual session character driven by which portion you pull from."),
    ("Nose",        "Not yet recorded"),
]
MB9ZST_TERPS = [
    ("Caryophyllene", "266°F / 130°C", "Spicy — inferred minor across all three components"),
    ("Myrcene",       "334°F / 168°C", "Earthy, tropical — inferred, Mango Banana lineage contribution"),
    ("Limonene",      "349°F / 176°C", "Citrus — inferred likely prominent (Sour Tangie + Mango Banana shared contribution)"),
    ("Terpinolene",   "367°F / 186°C", "Sweet, fruity — inferred, Sour Tangie and Z character"),
    ("Linalool",      "388°F / 198°C", "Floral — inferred minor"),
]
MB9ZST_BASELINE = [
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=15, temp_f=390, note="Early ascent"),
    Waypoint(time_s=40, temp_f=410, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=430, note="Endpoint"),
]
MB9ZST_RUN1 = MB9ZST_BASELINE
MB9ZST_RUN2 = MB9ZST_BASELINE
MB9ZST_RUN3 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=420, note="Endpoint"),
    Waypoint(time_s=65, temp_f=420, note="Hold at 420°F"),
]
MB9ZST_RUN4 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=415, note="Endpoint — down 5°F from Run 3"),
    Waypoint(time_s=65, temp_f=415, note="Hold at 415°F"),
]
MB9ZST_NEXT = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=25, temp_f=400, note="Mid climb"),
    Waypoint(time_s=45, temp_f=410, note="Endpoint — down 5°F from Run 4"),
    Waypoint(time_s=65, temp_f=410, note="Hold at 410°F"),
]

# ── DASHBOARD DATA ────────────────────────────────────────────────────────────

FIRST_RUN_DATE = date(2026, 5, 2)

# ── EQUIPMENT ─────────────────────────────────────────────────────────────────
# Two regimes in the log so far. The cutover is MB9ZST Run 1 (May 13, 2026):
# the Gemlock joystick replaced the Cloud Vortex spinner cap and the 6mm pearl
# was retired. Insert has been quartz throughout (sapphire not yet acquired).
# Named constants, not per-call literals: the 24 pre-cutover runs were genuinely
# one physical config, so one definition to verify beats 24 transcriptions.

_SPINNER = EquipmentConfig(insert="quartz", carb_cap="Cloud Vortex 21.0", pearl_diameter_mm=6)
_GEMLOCK = EquipmentConfig(insert="quartz", carb_cap="Gemlock joystick",  pearl_diameter_mm=None)

COMPLETED_RUNS = [
    CompletedRun(strain="WW Z",                              run_date=date(2026, 5, 2),  sessions_prior_today=0,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=WWZ_RUN1),
    CompletedRun(strain="Caramel Apple Gelato",              run_date=None,              sessions_prior_today=None, utc_logged_at=None,                                              equipment=_SPINNER, waypoints=CAG_RUN1),
    CompletedRun(strain="Orange Candy",                      run_date=None,              sessions_prior_today=None, utc_logged_at=None,                                              equipment=_SPINNER, waypoints=OC_RUNS12),
    CompletedRun(strain="Orange Candy",                      run_date=None,              sessions_prior_today=None, utc_logged_at=None,                                              equipment=_SPINNER, waypoints=OC_RUNS12),
    CompletedRun(strain="Orange Candy",                      run_date=None,              sessions_prior_today=None, utc_logged_at=None,                                              equipment=_SPINNER, waypoints=OC_RUN3),
    CompletedRun(strain="Orange Candy",                      run_date=date(2026, 5, 5),  sessions_prior_today=1,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=OC_RUN4),
    CompletedRun(strain="Orange Candy",                      run_date=date(2026, 5, 6),  sessions_prior_today=0,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=OC_RUN5),
    CompletedRun(strain="Orange Candy",                      run_date=date(2026, 5, 9),  sessions_prior_today=3,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=OC_RUN6),
    CompletedRun(strain="Orange Candy",                      run_date=date(2026, 5, 9),  sessions_prior_today=4,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=OC_RUN7),
    CompletedRun(strain="The Hive #1",                       run_date=date(2026, 5, 7),  sessions_prior_today=0,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=HIVE1_RUN1),
    CompletedRun(strain="The Hive #1",                       run_date=date(2026, 5, 7),  sessions_prior_today=1,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=HIVE1_RUN2),
    CompletedRun(strain="The Hive #1",                       run_date=date(2026, 5, 8),  sessions_prior_today=0,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=HIVE1_RUN3),
    CompletedRun(strain="The Hive #1",                       run_date=date(2026, 5, 8),  sessions_prior_today=1,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=HIVE1_RUN4),
    CompletedRun(strain="The Hive #1",                       run_date=date(2026, 5, 8),  sessions_prior_today=2,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=HIVE1_RUN5),
    CompletedRun(strain="Fembot #3",                         run_date=date(2026, 5, 9),  sessions_prior_today=0,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=FEMBOT3_RUN1),
    CompletedRun(strain="Fembot #3",                         run_date=date(2026, 5, 9),  sessions_prior_today=1,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=FEMBOT3_RUN2),
    CompletedRun(strain="Mango Starburst #23",               run_date=date(2026, 5, 9),  sessions_prior_today=2,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=MS23_RUN1),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 10), sessions_prior_today=0,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=MBD_RUN1),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 10), sessions_prior_today=1,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=MBD_RUN2),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 11), sessions_prior_today=2,    utc_logged_at=datetime(2026, 5, 12,  5, 24, tzinfo=timezone.utc), equipment=_SPINNER, waypoints=MBD_RUN3),
    CompletedRun(strain="Maple Bacon Donut",                 run_date=date(2026, 5, 12), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 13,  2, 30, tzinfo=timezone.utc), equipment=_SPINNER, waypoints=MBD_RUN4),
    CompletedRun(strain="Rain Fruit",                        run_date=date(2026, 5, 10), sessions_prior_today=2,    utc_logged_at=None,                                              equipment=_SPINNER, waypoints=RF_RUN1),
    CompletedRun(strain="Rain Fruit",                        run_date=date(2026, 5, 11), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 11, 22, 44, tzinfo=timezone.utc), equipment=_SPINNER, waypoints=RF_RUN2),
    CompletedRun(strain="Rain Fruit",                        run_date=date(2026, 5, 11), sessions_prior_today=1,    utc_logged_at=datetime(2026, 5, 12,  0, 30, tzinfo=timezone.utc), equipment=_SPINNER, waypoints=RF_RUN3),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 13), sessions_prior_today=0,   utc_logged_at=datetime(2026, 5, 13, 23, 27, tzinfo=timezone.utc), equipment=_GEMLOCK, waypoints=MB9ZST_RUN1),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 13), sessions_prior_today=1,   utc_logged_at=datetime(2026, 5, 14,  4, 55, tzinfo=timezone.utc), equipment=_GEMLOCK, waypoints=MB9ZST_RUN2),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 14), sessions_prior_today=0,   utc_logged_at=datetime(2026, 5, 15,  2,  0, tzinfo=timezone.utc), equipment=_GEMLOCK, waypoints=MB9ZST_RUN3),
    CompletedRun(strain="Mango Banana #9 + Z + Sour Tangie", run_date=date(2026, 5, 14), sessions_prior_today=1,   utc_logged_at=datetime(2026, 5, 15,  4, 34, tzinfo=timezone.utc), equipment=_GEMLOCK, waypoints=MB9ZST_RUN4),
    CompletedRun(strain="Blueberry 36 #1",                  run_date=date(2026, 5, 15), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 16,  1, 53, tzinfo=timezone.utc), equipment=_GEMLOCK, waypoints=BB36_1_RUN1),
    CompletedRun(strain="Blueberry 36 #1",                  run_date=date(2026, 5, 15), sessions_prior_today=1,    utc_logged_at=datetime(2026, 5, 16,  5, 48, tzinfo=timezone.utc), equipment=_GEMLOCK, waypoints=BB36_1_RUN2),
    CompletedRun(strain="Blueberry 36 #1",                  run_date=date(2026, 5, 16), sessions_prior_today=0,    utc_logged_at=datetime(2026, 5, 17,  5, 32, tzinfo=timezone.utc), equipment=_GEMLOCK, waypoints=BB36_1_RUN3),
]

STRAIN_STATUS = [
    StrainStatus(name="WW Z",                              profile_anchor="#wwz-profile",      next_text="—",                                                                                    accent=None, slug="wwz"),
    StrainStatus(name="Caramel Apple Gelato",              profile_anchor="#cag-profile",      next_text="Try 430°F endpoint",                                                                   accent=None, slug="cag"),
    StrainStatus(name="Orange Candy",                      profile_anchor="#oc-profile",       next_text="Ramp (Run 6) outperforming flat hold — repeat ramp to confirm, or try 420°F flat hold", accent=None, slug="oc"),
    StrainStatus(name="The Hive #1",                       profile_anchor="#hive1-profile",    next_text="Try 420–425°F endpoint on Run 6",                                                      accent=None, slug="hive1"),
    StrainStatus(name="Fembot #3",                         profile_anchor="#fembot3-profile",  next_text="Try 420°F steady hold on Run 3",                                                       accent=None, slug="fembot3"),
    StrainStatus(name="Mango Starburst #23",               profile_anchor="#ms23-profile",     next_text="Repeat Run 1 curve to confirm",                                                        accent=None, slug="ms23"),
    StrainStatus(name="Maple Bacon Donut",                 profile_anchor="#mbd-profile",      next_text="Try faster ramp to 460°F on Run 5",                                                    accent=None, slug="mbd"),
    StrainStatus(name="Rain Fruit",                        profile_anchor="#rainfruit-profile",next_text="Walk endpoint up incrementally — try 423°F on Run 4",                                  accent=None, slug="rainfruit"),
    StrainStatus(name="Mango Banana #9 + Z + Sour Tangie", profile_anchor="#mb9zst-profile",  next_text="Try 410°F endpoint on Run 5 — tail harshness still present at 415°F",                 accent=None, slug="mb9zst"),
    StrainStatus(name="Blueberry 36 #1",                  profile_anchor="#bb361-profile",    next_text="Try 410°F endpoint on Run 4 — tail harshness confirmed at 415°F across Runs 2 and 3", accent=None, slug="bb361"),
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

def _resolve_accent_colors():
    # Distribute hues evenly across non-green space (0–89° and 166–359°, avoiding 90–165°).
    # Strains with an explicit accent hex in STRAIN_STATUS use that color instead.
    NON_GREEN = [(0, 90), (166, 360)]
    total = sum(e - s for s, e in NON_GREEN)
    n = len(STRAIN_STATUS)
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
    for i, s in enumerate(STRAIN_STATUS):
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
        if run.equipment is None:
            errors.append(f"COMPLETED_RUNS[{i}] ({run.strain}): equipment is None — "
                           f"every run must carry an explicit EquipmentConfig "
                           f"(None never means 'inherit a session default')")

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
