# Dataclasses Refactor — Task Handoff

## Context

`Dabby_Log_Generator.py` is a single-file static site generator that produces `index.html`.
It currently exceeds 35,000 tokens and cannot be read by Claude in a single pass. All data
structures are positional tuples with no named fields, no type enforcement, and no validation
that related structures are consistent with each other.

This refactor introduces four dataclasses to replace those tuples. It does not change any
behavior, output, or workflow — with one intentional exception: Step 4 also fixes the terpene
BP lines in chart JS, replacing a hardcoded array with one derived from `TERPENE_REFERENCE`.
That is a deliberate behavior change bundled into the refactor. Everything else should produce
identical rendered output (modulo any whitespace differences that don't affect rendering).

Read `Dabby_Handoff_Notes.md` and `CLAUDE.md` before starting. Follow the PR workflow:
feature branch → PR → preview URL → merge.

---

## Pros and Cons

**Pros**

- Named fields replace positional tuple access — a new run entry is self-documenting
- Type annotations make field intent explicit (e.g. `run_date: date | None` vs position 1)
- Adding a new field in the future (e.g. `load_size`, `effect_intensity`) is a one-line change
  with a default value, not a surgery on every existing tuple
- Strain name join between `COMPLETED_RUNS` and `STRAIN_STATUS` becomes validatable at build time
- String parsing (`time_str.replace('s','')`, `temp_str.replace('°F','')`) is eliminated —
  `Waypoint` stores typed numerics, removing redundant parsing in `curve_chart_html()` and
  `dashboard_html()`
- Terpene BP lines in chart JS can be derived from `TerpeneEntry.bp_f` instead of being
  hardcoded separately — fixes a latent data duplication bug
- No new dependencies — stdlib `dataclasses` only

**Cons**

- Large volume of mechanical changes: ~150 waypoint tuples, ~30 `COMPLETED_RUNS` entries,
  ~36 `TERPENE_REFERENCE` entries, ~9 `STRAIN_STATUS` entries
- High error surface — a single misplaced value in a waypoint conversion is silent until
  the chart renders wrong
- No behavior change means the only verification signal is "does it still look right" —
  there are no tests to run
- Slightly more verbose data definitions (constructor calls vs bare tuples)

---

## The Four Dataclasses

Define these near the top of the file, after imports, before any data.

```python
from dataclasses import dataclass, field
from typing import Literal

@dataclass
class Waypoint:
    time_s: int       # seconds — e.g. 0, 15, 40, 65
    temp_f: int       # fahrenheit — e.g. 380, 430 (all existing waypoints are whole numbers)
    note: str

@dataclass
class CompletedRun:
    strain: str
    run_date: date | None
    sessions_prior_today: int | None  # sessions run before this one on the same calendar day
    utc_logged_at: datetime | None
    waypoints: list[Waypoint]

@dataclass
class StrainStatus:
    name: str
    profile_anchor: str
    next_text: str
    accent: str | None
    slug: str

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
```

---

## Migration Sequence

Do these steps in order. Run the generator after each step to catch errors early.

### Step 1 — Define dataclasses

Add the four dataclass definitions above to the file, after imports. Do not change any
data yet. Confirm `python3 Dabby_Log_Generator.py` still runs cleanly.

### Step 2 — Migrate STRAIN_STATUS

Replace each tuple with a `StrainStatus` constructor call. Example:

Before:
```python
("WW Z", "#wwz-profile", "—", None, "wwz"),
```

After:
```python
StrainStatus(name="WW Z", profile_anchor="#wwz-profile", next_text="—", accent=None, slug="wwz"),
```

Update `_resolve_accent_colors()` and `validate_accent_colors()` to use attribute access
instead of tuple unpacking. Run generator. Verify dashboard renders correctly.

### Step 3 — Migrate TERPENE_REFERENCE

Replace each tuple with a `TerpeneEntry` constructor call. Example:

Before:
```python
("Linalool", "linalool", 388, 198, "Mid", "Floral, citrusy-sweet", "Calming, sedating", "Lavender, citrus, rosemary, basil"),
```

After:
```python
TerpeneEntry(name="Linalool", alias="linalool", bp_f=388, bp_c=198, band="Mid",
             aroma="Floral, citrusy-sweet", qualities="Calming, sedating",
             found_in="Lavender, citrus, rosemary, basil"),
```

Update `terpene_reference_html()` to use attribute access. Run generator.

### Step 4 — Migrate waypoint curve variables

This is the highest-volume step. Every curve variable (WWZ_RUN1, OC_RUN3, HIVE1_RUN5, etc.)
is a list of 3-tuples that becomes a list of `Waypoint` objects.

**Full inventory of curve variables to migrate** (read the file to confirm this list is
current — new runs may have been added since this document was written):

```
BASELINE_CURVE
WWZ_RUN1
CAG_RUN1, CAG_RUN2
OC_RUNS12, OC_RUN3, OC_RUN4, OC_RUN5, OC_RUN6, OC_RUN7
HIVE1_RUN1, HIVE1_RUN2, HIVE1_RUN3, HIVE1_RUN4, HIVE1_RUN5, HIVE1_NEXT
FEMBOT3_RUN1, FEMBOT3_RUN2, FEMBOT3_RUN3
MS23_RUN1
MBD_RUN1, MBD_RUN2, MBD_RUN3, MBD_RUN4, MBD_NEXT
RF_RUN1, RF_RUN2, RF_RUN3, RF_RUN4_NEXT
MB9ZST_BASELINE, MB9ZST_RUN1, MB9ZST_RUN2
```

**Watch out for aliases.** `MB9ZST_RUN1 = MB9ZST_BASELINE` and `MB9ZST_RUN2 = MB9ZST_BASELINE`
are variable aliases — they point to the same list object as `MB9ZST_BASELINE`. When you
convert `MB9ZST_BASELINE` to a list of `Waypoint` objects, `MB9ZST_RUN1` and `MB9ZST_RUN2`
are automatically updated too. Do not attempt to convert them again separately — you will
get a double-conversion error or end up with `Waypoint` objects being passed to `Waypoint()`.
Leave the alias lines exactly as they are.

Before:
```python
WWZ_RUN1 = [
    ("0s",  "375°F", "Session open"),
    ("15s", "378°F", "Extended flat"),
    ("40s", "395°F", "Mid ascent"),
    ("65s", "440°F", "Endpoint"),
]
```

After:
```python
WWZ_RUN1 = [
    Waypoint(time_s=0,  temp_f=375, note="Session open"),
    Waypoint(time_s=15, temp_f=378, note="Extended flat"),
    Waypoint(time_s=40, temp_f=395, note="Mid ascent"),
    Waypoint(time_s=65, temp_f=440, note="Endpoint"),
]
```

**Critical:** strip the `s` from time and the `°F` from temp when converting — store
bare numbers. `"0s"` → `0`, `"375°F"` → `375`. Do not store `"0s"` or `"375°F"` as
strings in the dataclass — the point is to eliminate string parsing downstream.

**Also update the inline proposed waypoint lists** inside `what_to_try_next_html()` calls
at the bottom of `build_html()`. These are not named variables — they are anonymous lists
defined inline as arguments. There are several; search for `proposed_waypoints=[` to find
them all. Each one follows the same conversion pattern.

Example — before:
```python
proposed_waypoints=[
    ("0s",  "380°F", "Session open"),
    ("65s", "420°F", "Endpoint"),
],
```

After:
```python
proposed_waypoints=[
    Waypoint(time_s=0,  temp_f=380, note="Session open"),
    Waypoint(time_s=65, temp_f=420, note="Endpoint"),
],
```

**x-axis max caveat.** The chart x-axis maximum is currently set from the last waypoint's
time string: `waypoints[-1][0].replace('s','')`. After migration this becomes
`waypoints[-1].time_s`. Make sure this line is updated — if it is not, the chart will
either crash or render with a broken x-axis scale.

After migrating all curves, update `curve_chart_html()` and `curve_table()` to use
`wp.time_s`, `wp.temp_f`, `wp.note` instead of string parsing. The string parsing
lines to remove:

```python
# Remove these — no longer needed
t = int(time_str.replace('s',''))
temp = float(temp_str.replace('°F','').replace('°f',''))
```

Replace with direct attribute access:
```python
t = wp.time_s
temp = wp.temp_f
```

Similarly update the aria-label fallback text in `curve_chart_html()` which currently
references `waypoints[0][1]` and `waypoints[-1][1]` — use `waypoints[0].temp_f` etc.

Update `dashboard_html()` which also parses waypoint strings:
```python
# Before
pts = [(int(t.replace('s', '')), float(v.replace('°F', ''))) for t, v, _ in wps]
# After
pts = [(wp.time_s, wp.temp_f) for wp in wps]
```

Run generator after this step. This is where most errors will surface — check all charts
render and the x-axis max is correct.

**Also fix the terpene line hardcoding here.** This is the one intentional behavior change
in this refactor — verify it separately from the waypoint conversion. If the charts look
wrong after Step 4, isolate whether the issue is a waypoint conversion error or the terpene
change before debugging further.

The chart currently has this hardcoded in the JS template string:

```javascript
var terps=[{y:311,l:"Pinene"},{y:334,l:"Myrcene"},{y:349,l:"Limonene"},{y:367,l:"Terpinolene"},{y:388,l:"Linalool"}];
```

Replace with a Python-generated JS array derived from `TERPENE_REFERENCE`, filtered to
the terpenes you want to show on charts. A reasonable filter is the five common cannabis
terpenes: Pinene (Alpha-Pinene), Myrcene, Limonene, Terpinolene, Linalool. Build the JS
array in `curve_chart_html()` like:

```python
CHART_TERPS = ["Alpha-Pinene", "Myrcene", "Limonene", "Terpinolene", "Linalool"]
chart_terp_entries = [t for t in TERPENE_REFERENCE if t.name in CHART_TERPS]
terps_js = '[' + ','.join(f'{{y:{t.bp_f},l:"{t.name.replace("Alpha-","")}"}}' 
                          for t in chart_terp_entries) + ']'
```

Use `terps_js` in place of the hardcoded string. Note: the `replace("Alpha-","")` label
transform is a known rough edge — it works for the current terpene names but would silently
mangle any future entry whose name happens to start with "Alpha-" for unrelated reasons. Good
enough for now; fix if it causes trouble.

### Step 5 — Migrate COMPLETED_RUNS

Replace each tuple with a `CompletedRun` constructor call. Example:

Before:
```python
("Rain Fruit", date(2026, 5, 11), 1, datetime(2026, 5, 12, 0, 30, tzinfo=timezone.utc), RF_RUN3),
```

After:
```python
CompletedRun(strain="Rain Fruit", run_date=date(2026, 5, 11), sessions_prior_today=1,
             utc_logged_at=datetime(2026, 5, 12, 0, 30, tzinfo=timezone.utc),
             waypoints=RF_RUN3),
```

Update `dashboard_html()` and `build_html()` to use attribute access:
```python
# Before
for strain, run_date, sessions_prior, utc_logged_at, wps in COMPLETED_RUNS:
# After
for run in COMPLETED_RUNS:
    run.strain, run.run_date, run.sessions_prior_today, run.utc_logged_at, run.waypoints
```

Run generator.

### Step 6 — Add a validate() function

Now that the data model is explicit, add a validation function that runs at build time.
Call it from the top of `build_html()`, alongside the existing `validate_accent_colors()`.

```python
def validate():
    strain_names = {s.name for s in STRAIN_STATUS}
    errors = []

    # Cross-structure join: every run must reference a known strain
    for i, run in enumerate(COMPLETED_RUNS):
        if run.strain not in strain_names:
            errors.append(f"COMPLETED_RUNS[{i}] strain '{run.strain}' not found in STRAIN_STATUS")

    # Waypoint sanity checks — catches conversion errors before they silently break charts
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

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(f"  {e}")
        raise SystemExit(1)
```

---

## What NOT to Change

- All HTML helper functions (`info_table`, `curve_table`, `result_row`, `collapsible_section`,
  `what_to_try_next_html`, `accent_header`, etc.)
- The CSS constant
- `dashboard_html()` structure — only the tuple unpacking inside it
- `build_html()` assembly logic — only the tuple unpacking inside it
- The `_resolve_accent_colors()` and `_hsl_to_hex()` color logic — only attribute access
- `CLAUDE.md`, `Dabby_Handoff_Notes.md`, `Dabby_Methodology.md`
- The GitHub Pages / PR workflow

---

## Verification

After each step, run:
```
python3 Dabby_Log_Generator.py
```

A clean run prints `Written: index.html` with no errors or warnings (other than any
pre-existing accent color warnings).

Final verification: open `index.html` in a browser and check:
- Dashboard stat cards show correct numbers
- All strain rows appear in the browser with correct run counts and dates
- All charts render (curve line, terpene BP lines, THC band)
- All collapsible sections open and close
- → Next and ↑ Last pills navigate to correct anchors
- Proposed curve charts in What to Try Next sections render

If the terpene BP lines look wrong on any chart, check that `CHART_TERPS` filter matches
the names exactly as they appear in `TERPENE_REFERENCE`.

---

## Cleanup

When the refactor is done and merged:
1. Delete this file (`REFACTOR_DATACLASSES.md`)
2. Update `Dabby_Handoff_Notes.md` to note that dataclasses are now in use and tuple
   unpacking is gone — future Claude instances should use attribute access when adding runs
