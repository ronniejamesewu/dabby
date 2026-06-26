# Dabby the House Rig — Methodology & Thermal Reasoning

Dr. Dabber Switch². All conclusions are working hypotheses grounded in physics and empirical session results, not formally measured values.

---

## 1. Device Architecture

**Induction heating:** Helical coil wraps full circumference and base of titanium cup. Omnidirectional heating — titanium heats evenly from sidewalls and base. Insert (quartz or sapphire) sits inside titanium cup and receives heat conductively. Insert is not inductively heated.

**IR sensor:** Reads titanium cup temperature, not insert surface temperature. No visible port for direct insert measurement. The setpoint is a proxy for material contact temperature, not a direct measurement. All setpoints are calibrated empirically via swab results.

**Thermal path:** Induction field → titanium cup → contact interface → insert surface → material. Each transition has thermal resistance. Physical contact points between titanium and quartz are the primary conduction path.

**Air gap:** Unavoidable in principle — insert material and titanium have different thermal expansion coefficients, and clearance is required for insertion/removal. In practice, the insert sits on and against titanium contact points that conduct efficiently. Air conductivity ~0.025 W/m·K (vs quartz ~1.4, sapphire ~25–35), but the air gap is not the dominant resistance when contact geometry is intact.

**Insert equilibration:** The quartz insert wall is approximately 1mm thick. At ~1.4 W/m·K, the bulk thermal time constant is under one second. The insert equilibrates internally almost instantly. This means the insert surface tracks titanium temperature closely under stable or slowly-changing conditions.

**Titanium-to-insert offset:** Probably small under most operating conditions. The dominant remaining uncertainties are vaporization cooling — phase change draws heat from the insert surface locally during active vaporization — and dynamic lag during steep ascent phases, where titanium is always ahead of insert. At flat or slowly-ascending phases, the system approaches equilibrium and offset approaches its minimum. Do not assume a large fixed offset. Setpoints are reasonable proxies for material contact temperature.

---

## 2. Insert Materials

| Property | Quartz (current) | Sapphire (not yet acquired) |
|---|---|---|
| Thermal conductivity | ~1.4 W/m·K | ~25–35 W/m·K (~20x better) |
| Heat capacity | Lower | Higher — more stable on material contact |
| Mohs hardness | 7 | 9 |

**Sapphire advantage:** Two mechanisms, neither of which is primarily closing a large titanium-to-insert interface resistance.

First: higher volumetric heat capacity. Sapphire absorbs the cold material contact perturbation at session open more stably — when material first contacts the insert, sapphire resists the temperature drop better than quartz.

Second: better surface temperature uniformity during vaporization. Sapphire's ~20x higher bulk conductivity replenishes heat from surrounding areas faster when local vaporization creates cold spots, keeping the insert surface more uniform throughout the session.

The Reddit community consensus that sapphire allows 10–20°F lower setpoints for equivalent results is consistent with this model. Surface finish of sapphire is irrelevant to either mechanism.

**Quartz-to-sapphire scaling:** Does not work. Offset reduction is non-uniform across curve shape — varies with ascent rate and absolute temperature. Sapphire requires fresh empirical calibration from scratch.

---

## 3. Cold Start Technique

Material pre-loaded into cold insert before heating begins. Material and insert co-heat from ambient together.

**Implications:**
- No thermal shock event. Material and insert are always at the same temperature — no cold-material-on-hot-surface perturbation.
- Offset is a stable calibration constant, not a variable dependent on loading timing.
- Do not reason about cold-material thermal shock. It does not apply.

---

## 4. Terpene & Temperature Reference

**Boiling points (standard pressure — orientation points, not hard switches):**

| Terpene | Boiling Point |
|---|---|
| Caryophyllene | 266°F / 130°C |
| Alpha-Pinene | 311°F / 155°C |
| Myrcene | 334°F / 168°C |
| Limonene | 349°F / 176°C |
| Terpinolene | 367°F / 186°C |
| Linalool | 388°F / 198°C |
| THC onset | 315°F / 157°C (progressive to ~428°F / 220°C) |

**Terpene profile inference — hard limits:**
- Profiles are inferred from strain genetics, not measured. Do not present as specifications.
- The same five or six terpenes appear across nearly all strains. This is the generic cannabis palette, not strain-specific knowledge.
- Meaningful variation lives in terpene ratios and minor terpenes — neither is inferable from strain name.
- User nose is weak secondary signal only. Non-discerning palate. Use genetics as primary source.

**Terpene density ≠ heat sensitivity.** Terpene-dense material has more to lose from overheating but degradation physics are properties of the compounds, not their concentration. Do not conflate these.

**Swab color — limits:**
- Floor indicator within the normal operating range. Dark or burnt residue (amber-toward-brown or darker) is a reliable signal to reduce temperature. Within the light-golden-to-amber range, swab has too many uncontrolled variables — load size, material starting color, oxidation state, swab timing, pressure — to reliably distinguish between curve shapes or small endpoint differences.
- Do not compare swab color across strains. Use as within-strain calibration signal only.
- Do not over-interpret clean swabs as fine-grained efficiency data.

| Swab | Interpretation |
|---|---|
| Light golden/amber, fluid | Target — clean vaporization |
| Amber toward light brown | Too hot — reduce endpoint. Reliable floor signal. |
| Dark brown/black | Severely overheated — reduce setpoint significantly. |
| Cloudy/white crystalline | Possibly too cool (uncertain) |

---

## 5. Curve Design

**Device curve constraints (Switch² Custom mode):**

| Constraint | Limit |
|---|---|
| Max heating rate | +10°F/sec |
| Max cooling rate | −3°F/sec |
| Session hold time | 10–90 seconds (user-adjustable) |

Any number of waypoints may be defined within these constraints. The heating rate limit bounds how steeply a curve can ascend per second; the cooling rate limit bounds how quickly it can descend. The session hold time is the total profile window — all waypoints must fit within it.

**Baseline philosophy:** Single baseline curve for all hash rosin with cold start. The log handles strain-specific empirical calibration from that baseline. Do not design different starting curves based on strain name, inferred terpene profile, consistency, or provenance quality without empirical justification.

**Why ascending curves:** Cold start means material is at its lowest temperature at session open. An ascending curve continues that natural trajectory, working through terpene boiling points from most volatile to least volatile as the temperature climbs. This preserves the most heat-sensitive compounds early in the session.

**Construction parameters:**

| Parameter | Guidance |
|---|---|
| Opening setpoint | 380°F baseline |
| Ascent rate | Fast ramp to endpoint — 380→420°F in 8s (~5°F/sec). Hold for the remainder of the session. |
| Endpoint | 420°F baseline starting point |
| Hold time | 60s total session (8s ramp + hold). End when vapor drops — do not ride timer on small loads. |

**Hash rosin vs flower rosin:** Hash rosin vaporizes more cleanly at lower temperatures due to lower plant material contamination. This is an efficiency argument. Do not import curve assumptions from flower rosin contexts.

**Consistency:** Does not justify different baseline curves without empirical evidence. Fresh press may be a genuine exception — open question, not settled. Sauce with THCA diamonds is hydrocarbon extract, outside project scope.

**Ascent rate and offset:** The slower the ascent rate, the smaller the offset between titanium setpoint and material contact temperature. At a flat hold, the system approaches equilibrium and the offset approaches its minimum. During steep ascent, titanium is always ahead of the insert and material.

Practical implications: flat opening phases deliver the most accurate temperature to the material relative to setpoint. Steep mid-session climbs move the titanium through terpene zones faster than the material actually experiences them — the material catches up during subsequent flat or slower phases. A slowly-arrived-at lower endpoint delivers more heat to the material than a steeply-arrived-at higher endpoint, because the flat tail allows the offset to close. This is the rationale for preferring a steeper mid-climb with a flatter tail over a uniformly steep ascent to a higher endpoint.

**Torch comparison:** Traditional torch fired dab has a decaying temperature. Banger is superheated and then cold dab is applied when the decaying temperature reaches a desired start point. Consumption happens on decaying curve. Switch² Custom mode is opposite — controlled rise from lowest point.

**Descent curves on Switch²:** A programmed descent curve is not a simulation of torch passive decay. The Switch² PID controller stops the heater and allows passive heat loss — the mechanism is passive, but the controller tracks waypoints rather than free-decaying. A descent programmed as 440→350 over 30s is executed by holding the temperature to those waypoints as the insert passively cools. Sapphire's higher thermal mass means the insert lags the programmed curve (actual descent slower than specified), but the curve still executes — it does not free-decay at sapphire's ~1°F/sec passive rate. Descent curves via programmed waypoints are viable on Rig 5 and Rig 6. (WM R16, Session 132.)

---

## 6. Session Process

1. Start from baseline curve
2. Run session, end when vapor production drops naturally
3. Swab immediately while warm — dry swab first, then ISO
4. Observe swab color and session character (vapor density, harshness, when production peaked)
5. Adjust endpoint or ascent rate based on swab result
6. Log result in session log with swab observation and any adjustments
7. Each run informs the next — adjust based on swab result and session character, log the outcome.

Swab result is the empirical ground truth. Terpene profile reasoning is a starting framework, not a prediction.

**Timing precision:** The countdown timer within the cycle is the primary timing unit — when harshness onset or depletion is logged as "harshness at 22 seconds left," that comes from the app countdown and is reasonably precise. Draw count is a fallback when the countdown wasn't captured at the moment — useful for sequencing observations (harshness entered on draw 3) but lower-precision than timer-referenced events. Draw count without time reference cannot support precise cross-run comparison of onset timing.
