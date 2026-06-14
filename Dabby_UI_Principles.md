# Dabby UI Principles

## Purpose

This document defines the structural UI rules for the Dabby Session Log. It is the source of truth for component roles, layout hierarchy, interaction boundaries, and rendering constraints. It distinguishes hard requirements from current implementation choices so designers have maximum creative space while the structural rules remain clear.

**Hard requirement** = must survive any redesign.
**Current implementation** = how it works now; a redesign may replace it.

---

## 1. Page Structure

The page has four distinct layers, in document order:

1. **Header** — identity
2. **Dashboard + Strain Browser** — system state and primary navigation
3. **Per-Strain Sections** — full run history and What to Try Next per strain
4. **Reference Sections** — collapsible reference blocks, always on main page

---

## 2. Component Roles

### Header

- Displays title and subtitle only
- No interaction, no links, no descriptive text
- Minimal vertical footprint — must not resemble a hero section

### Dashboard

- Passive system telemetry derived from run data — read-only, no clickable elements
- What telemetry is surfaced and how it is presented is open to redesign
- *Current implementation:* nine stat cards — runs over N days, most dabs in a day, unique strains, avg open, avg endpoint, most time spent, earliest dab, latest dab, avg first dab of the day

### Strain Browser

- **Primary navigation surface** — the only place internal navigation links originate
- Must include: a way to filter/search strains, a list of all strains with last-run recency and next-step preview, and a navigation path from each strain to its What to Try Next section
- Sort order: active strains by run count descending; closed jars follow with closed framing
- How these elements are presented is open to redesign
- *Current implementation:* text search input + scrollable rows, each with strain name link, session count + date, next-step preview text, → Next pill

### Per-Strain Sections

Each strain has a dedicated section. The following content must be present; layout and presentation are open:

- Strain identity (name, format, consistency, producer, nose)
- Terpene inference note — explicitly labeled as inferred, not measured
- Run history — individual runs must be collapsible/hideable by default; each run must include: the curve (visualized + machine-readable waypoint table), equipment, swab color, session character, intensity, AI Run Analysis
- What to Try Next — must be directly navigable from the strain list; contains next-step text, AI Analysis, proposed curve if applicable
- Jar Index (closed jars only) — Harper's Index format

### Reference Sections

Five reference blocks, always on the main page, never moved to a separate page. Must be collapsible/hideable. Open when navigated to directly.

1. Device & Session Constants
2. Swab Color Reference
3. Baseline Curve (visualized + machine-readable waypoint table)
4. Terpene Reference
5. Rig Reference

---

## 3. Hierarchy

Order of importance — visual weight must align with this:

1. Strain Browser (action)
2. Dashboard (state)
3. Header (identity)
4. Per-Strain Sections (content)
5. Reference Sections (supporting reference)

The Dashboard must never visually dominate the Strain Browser. The Header must never dominate either.

---

## 4. Accent Color System *(current implementation — optional in redesign)*

Each strain is currently assigned a unique accent color used to visually distinguish strains from each other. A redesign may retain this approach, replace it with a different differentiation mechanism, or eliminate per-strain color identity entirely.

If retained: colors should be auto-assigned, not hand-picked, and not semantically meaningful. Avoid green — the prior forest green theme is retired.

---

## 5. Curve Visualization *(current implementation — open to redesign)*

Run curves are currently rendered as Chart.js line charts (CDN) with terpene boiling point annotations and a THC band overlay. A redesign may use a different library, custom SVG, or a different visual form entirely.

**Hard requirement:** waypoint tables must always be present in the DOM alongside any visualization — they are the machine-readable equivalent and the semantic fallback. Do not remove them for visual reasons.

---

## 6. Collapsible Mechanism *(current implementation — open to redesign)*

Runs and reference sections are currently collapsed using native `<details>`/`<summary>` elements. A redesign may use any expand/collapse mechanism.

**Hard requirement:** runs must be collapsed/hidden by default. Reference sections must be collapsible. Navigating directly to a section via anchor must open it.

---

## 7. Typography *(current implementation — open to redesign)*

- Body: system sans-serif
- Monospace: DM Mono — used for chart axes, curve tables, and technical values

**Hard requirement:** technical values (temperatures, times, curve data) must use a monospace face for legibility and alignment. The specific font is open.

---

## 8. Semantic HTML *(hard requirement)*

An AI agent may consume this page for reasoning — semantic correctness is a hard constraint regardless of visual design.

- Data hierarchy must be reflected in markup, not only in visual layout
- Per-run and per-strain structure must be consistent: same template, same element choices across all strains and runs
- Information communicated visually (color, position) must also exist as text in the DOM
- Curve visualizations must have a text fallback and accessible label
- Waypoint tables must always be present (see Section 5)

---

## 9. What Not to Do *(hard requirements)*

- No Contents or TOC section — the Strain Browser is navigation
- No calibration framing, status badges, progress indicators, or "dialed in" language anywhere
- No terpene data table per strain — the generic cannabis terpene palette presented as strain-specific contradicts the project's epistemic standards; do not restore unless a strain ships with genuinely measured terpene data
- No skeuomorphic references — no paper textures, ruled lines, typewriter fonts, or analog visual metaphors
- Do not move reference sections to a separate page
