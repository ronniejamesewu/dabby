# Switch² Insert Thermal Model — Reasoning Review Request

We are modeling the thermal behavior of a Dr. Dabber Switch² e-rig during a dab session. We want you to check our physics reasoning, flag errors, and identify anything we may have missed or overclaimed. Please be direct about any mistakes.

---

## Device Architecture

- **Heating mechanism:** Induction coil wraps the outside of a titanium cup. Only the titanium is inductively heated; the insert is not.
- **Temperature sensing:** IR sensor reads the interior titanium cup temperature — not the insert surface. All programmed setpoints are titanium setpoints.
- **PID control:** The device uses a PID controller to maintain the titanium at the programmed setpoint curve. The heater can only add heat; it cannot actively cool. Descent is passive only.
- **Insert:** A ceramic cup (quartz or sapphire) sits inside the titanium cup. It is heated conductively through the titanium-insert contact interface.
- **Cold start:** Material is pre-loaded into the cold insert before the heating cycle begins. Material and insert co-heat from ambient.

---

## Session Timing

- The countdown timer starts when the first waypoint temperature is achieved on the titanium — not when heating begins.
- Pre-heat from room temperature to the first waypoint occurs before t=0.
- At t=0, the insert is assumed to be fully equilibrated to the opening setpoint (justified below).
- The first draw typically begins at or immediately after t=0.
- The app displays seconds **remaining** in the cycle, so observations are reported as time-remaining rather than elapsed.

---

## Insert Geometry and Material Properties

**Geometry (approximate):**
- Outer diameter: 20mm
- Wall thickness: ~1mm (measured/logged)
- Height: 15mm
- Lateral wall area: A_wall = π × 0.020 × 0.015 = 9.42 × 10⁻⁴ m²

**Material properties:**

| Property | Quartz | Sapphire | Titanium |
|---|---|---|---|
| Thermal conductivity k (W/m·K) | 1.4 | 30 | ~22 |
| Density ρ (kg/m³) | 2650 | 3980 | 4500 |
| Specific heat cp (J/kg·K) | 740 | 750 | 520 |
| CTE (×10⁻⁶ /°C) | ~0.55 | ~5–7 | ~8.6 |
| Insert heat capacity C_total (J/K) | 2.2 | 3.4 | — |

---

## Two-Node Thermal Model

We model the insert as two lumped nodes:
- **Outer node (bulk):** represents the titanium-contact side of the wall. Heated by titanium through the interface conductance G_interface. Heat capacity 60% of total.
- **Inner node (surface):** represents the material-contact side of the wall. Heated by outer node through the wall conductance G_wall. Heat capacity 40% of total. Q_draw exits here.

**Governing equations (Euler integration, dt=0.02s):**

```
dT_outer/dt = (G_interface × (T_ti − T_outer) − G_wall × (T_outer − T_surface)) / C_outer
dT_surface/dt = (G_wall × (T_outer − T_surface) − Q_draw) / C_surface
```

T_ti is held at the programmed setpoint (PID-perfect assumption).

**Initial conditions:** Both nodes start at the opening setpoint at t=0, justified by the pre-heat equilibration time constant (τ = C/G_interface ≈ 0.6–1s) being much shorter than the pre-heat duration.

---

## Interface Conductance G_interface

This is the conductance from the titanium cup to the insert outer wall. It has two geometric components:

### Sidewall (lateral surface)
The insert fits snugly inside the titanium cup — snugly enough that a trapped air column cushions the insert's descent when placed inside (observed behavior). This constrains the radial air gap to approximately 0.005–0.02mm per side.

Air conductance across the gap:
- h = k_air / gap, where k_air ≈ 0.025–0.038 W/m·K (ambient to operating temperature)
- G_sidewall = h × A_wall

At 0.01mm gap: G_sidewall ≈ 2.5–3.6 W/K (ambient to hot air)

### Base (bottom surface)
The insert rests on the titanium cup floor. Thermal expansion is axial here — the cup floor and insert bottom both expand upward, maintaining contact. **The base contact is not affected by CTE mismatch.** Contact conductance for dry ceramic-on-metal: h_contact ≈ 500–5000 W/m²·K. Base area ≈ 3.1 × 10⁻⁴ m². Estimated G_base ≈ 0.3–1.5 W/K.

### Total G_interface
Estimated range: **1.5–6 W/K**. This is the softest number in the model. We cannot calculate it precisely without knowing the exact gap size.

### CTE asymmetry at operating temperature
At operating temperature (~180°C above ambient), differential thermal expansion opens the sidewall gap:

```
Gap_increase_per_side = R × ΔT × (α_Ti − α_insert)
```

- Quartz: 0.010 × 180 × (8.6 − 0.55) × 10⁻⁶ = **+0.0145mm per side**
- Sapphire: 0.010 × 180 × (8.6 − 6.0) × 10⁻⁶ = **+0.0047mm per side**

Quartz's near-zero CTE means the titanium cup relaxes away from the insert when hot, substantially opening the sidewall gap. Sapphire's CTE is close to titanium's, so its gap barely changes.

**Consequence:** G_interface is not the same for quartz and sapphire at operating temperature. G_interface_quartz < G_interface_sapphire, with the asymmetry residing entirely in the sidewall component (base contact is identical for both materials).

The PID maintains T_ti at setpoint but cannot bridge the interface resistance. A larger gap for quartz means a larger drop between titanium and insert bulk during draws.

---

## Q_draw Estimation

Heat extracted from the insert surface during a draw has two components:

### Convective cooling (airflow)
The carb cap in current primary use (Wym Stick Piston) has a known bore of 0.094" = 2.388mm. The carb cap hole is the restrictive orifice governing airflow.

Orifice equation:
```
Q_vol = Cd × A_bore × √(2ΔP/ρ)
```
- Cd = 0.6 (sharp-edged orifice)
- A_bore = π × (0.001194)² = 4.48 × 10⁻⁶ m²
- ρ_air = 1.2 kg/m³ (ambient)
- ΔP = inhalation pressure differential, estimated 30–100 Pa for a gentle-to-moderate dab draw

| ΔP (Pa) | Q_vol (mL/s) | Q_conv (W) |
|---|---|---|
| 30 | 19.0 | 4.1 |
| 50 | 24.5 | 5.3 |
| 100 | 34.7 | 7.5 |

Q_conv = m_dot × Cp_air × ΔT, where m_dot = Q_vol × 1.2 kg/m³, ΔT ≈ 180°C.

Justification for ΔT ≈ 180°C (near-complete equilibration): residence time of air in the insert (~0.3s) is much longer than the thermal time constant of the air volume (~0.04s), so air exits near insert temperature.

Airflow is primarily inside the insert (not in contact with the titanium cup directly), so nearly all convective heat is extracted from the insert surface — not split between titanium and insert.

### Vaporization enthalpy
THC enthalpy of vaporization: 93–120 kJ/mol (experimental; Lovestead & Bruno 2017, 2024 correlation GC study). At MW = 314 g/mol: 300–380 J/g.

Estimated ~0.05g vaporized per 10s draw: Q_vap ≈ 1.7 W. This is secondary to convective cooling.

### Total Q_draw
**Central estimate: 7–9 W** for a moderate draw. Convection dominates (~80%); vaporization is secondary (~20%).

---

## Wall Conductance G_wall

```
G_wall = k × A_wall / (L_wall / 2)
```

- Quartz: G_wall = 1.4 × 9.42×10⁻⁴ / 5×10⁻⁴ = **2.64 W/K**
- Sapphire: G_wall = 30.0 × 9.42×10⁻⁴ / 5×10⁻⁴ = **56.6 W/K**

---

## Conductivity Advantage

At quasi-steady state during a sustained draw, the temperature drop from titanium setpoint to insert surface:

```
ΔT_total = Q_draw × (1/G_interface + 1/G_wall)
```

If G_interface is identical for both materials, it cancels out of the advantage:

```
Advantage = Q_draw × (1/G_wall_Q − 1/G_wall_S) × 1.8  [converting K to °F]
```

| Q_draw (W) | Advantage (°F) |
|---|---|
| 5.0 | 3.3 |
| 7.5 | 4.9 |
| 9.0 | 5.9 |

If G_interface differs (CTE asymmetry), there is an additional interface term:

```
Advantage = Q_draw × [(1/G_int_Q − 1/G_int_S) + (1/G_wall_Q − 1/G_wall_S)] × 1.8
```

Both terms are positive (quartz has lower G at both interface and wall), so the CTE asymmetry compounds the wall conductivity difference.

Community consensus: sapphire allows 10–20°F lower setpoints for equivalent results. Our model produces ~5°F from wall conductivity alone at moderate draws. The CTE interface asymmetry adds an additional term that partially closes this gap but cannot be precisely quantified without knowing the exact gap sizes.

---

## Draw Dynamics

**During a draw:**
- Insert surface drops from setpoint toward quasi-steady equilibrium
- As insert cools, the gradient (T_ti − T_insert) increases, driving more heat from titanium into insert
- PID maintains T_ti at setpoint, compensating for heat extraction
- Quasi-steady equilibrium reached in τ = C_insert / G_interface ≈ 0.7–0.9s for both materials
- For a 10s draw, ~9s are spent at quasi-steady state; the transient is brief

**Between draws:**
- Insert equilibrates back to setpoint in ~5τ ≈ 4–5s
- Each draw starts from approximately the same insert temperature (setpoint)
- No significant thermal accumulation between draws
- Cross-draw comparison within a session is thermally clean; variation is material depletion, not thermal history

---

## Programmed Descent Curves

During a programmed descent, the PID lowers the setpoint and turns the heater off. The titanium cools passively. The insert, which has been holding heat, is now **hotter than the titanium**. Heat flows from insert back into the titanium cup, warming it and slowing the titanium's descent below the programmed curve.

The PID has no authority over this: it can withhold heat but cannot actively cool. The insert's thermal mass becomes a resistor against descent.

Sapphire's higher heat capacity (3.4 J/K vs quartz 2.2 J/K) means it stores more heat and feeds more back into the titanium, making descent slower relative to the programmed curve. This has been empirically observed on Rig 5.

During a draw on a descent curve: the draw extracts heat from the insert surface (cooling it) while the insert bulk is simultaneously feeding heat back into the titanium. The surface temperature during such a draw is the result of these two competing heat flows — more complex than a simple hold-phase draw.

---

## Key Uncertainties and Open Questions

1. **G_interface exact value:** Bounded to ~1.5–6 W/K from gap geometry reasoning; cannot be calculated precisely. This is the softest parameter.

2. **G_interface asymmetry magnitude:** The CTE gap opening is calculable in principle (we did so above) but depends on the initial cold gap size, which we do not know precisely.

3. **ΔP during draws:** 30–100 Pa is estimated; not measured. This is the primary driver of Q_draw uncertainty.

4. **Insert wall thickness:** Logged as ~1mm; approximate.

5. **Community 10–20°F claim:** Our model accounts for ~5°F from wall conductivity alone, with additional contribution from CTE-driven G_interface asymmetry. We cannot yet close the gap to 10–20°F from first principles at moderate draws without either harder draws (higher ΔP) or a measured G_interface asymmetry.

6. **Descent + draw interaction:** We have reasoned qualitatively about this but have not modeled it numerically.

---

## Specific Reasoning to Check

1. Is the air-cushion insertion observation correctly interpreted as implying a very small radial gap (0.005–0.02mm)?
2. Is the base contact correctly analyzed as being CTE-insensitive (axial expansion maintains contact)?
3. Is our claim that G_interface cancels from the advantage formula (when equal for both materials) correct?
4. Is the quasi-steady equilibrium time (τ ≈ C/G_interface) the right time constant for both the draw drop and the between-draw recovery?
5. Is the descent analysis correct — specifically that the insert becomes the heat source during descent rather than the heat sink?
6. Does the CTE asymmetry produce a genuinely meaningful additional advantage term, or is it second-order?
7. Are there any heat transfer mechanisms we have missed entirely?
