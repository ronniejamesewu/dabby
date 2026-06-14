# Dabby Session Log — Design Brief

## What it is

A personal hash rosin vaporizer session log. The device is a Dr. Dabber Switch² — a programmable electronic rig that holds a temperature setpoint curve. Each session ("dab") is logged with the curve used, swab color, session notes, and effect quality. The log tracks 14+ strains across 88+ runs, building a per-strain thread of what was tried and what to do next.

The goal of the logging practice is empirical: find the optimal temperature curve for each strain incrementally, using swab color and session character as the primary signals.

---

## Who uses it and when

One person. The log is published publicly on GitHub Pages — not designed for an audience, no onboarding, no social features — but a stranger landing on it should be able to understand what they're looking at without explanation. The design should be coherent and legible to an outsider without catering to them.

**Two primary use moments:**

1. **Before a session** — check what curve to run and what the last run revealed. The strain browser and "What to Try Next" are the working surface.
2. **After a session** — review and log what happened.

Context: mobile, quick reference, likely while relaxed. Low friction is a hard requirement. The design should get out of the way.

**One anticipated future use case:** an AI agent consuming the public log for reasoning — reading strain history, run data, and What to Try Next to inform session recommendations. Semantic HTML is therefore a hard constraint (see below).

---

## UI hierarchy — non-negotiable

**Order of importance:**

1. **Strain Browser** — the primary action surface; strain selection, last run summary, What to Try Next
2. **Dashboard** — passive system stats; read-only, no navigation, no clickable elements
3. **Header** — identity only; minimal footprint

The Dashboard must never visually dominate the Strain Browser. The Header must not resemble a hero section. Visual weight should align with user intent, not data volume.

The four reference sections (Device Constants, Swab Color Reference, Baseline Curve, Terpene Reference) live as collapsible blocks on the main page — do not move them to a separate page.

---

## The design problem

The current styling (forest green dominant, heavy header) reads as a brand making a statement. This project isn't a brand. The visual weight is in the wrong places — the header is seen once per visit and commands the most real estate; the strain browser is the whole point and sits below it.

The redesign should invert that: the header disappears, the browser is immediately dominant, and the dashboard earns its space as a passive layer.

---

## Aesthetic target

**Functional, legible, clean. Any ornamentation must earn its place** — hierarchy, grouping, emphasis, wayfinding. Decoration for its own sake is a failure.

The register is a serious hobbyist's technical log — precise, personal, unsentimental. Think: a well-made personal site or a thoughtfully published technical document. The author clearly knows what they're doing; a stranger can follow along without being the target audience.

**Not:** a wellness app, a productivity dashboard, anything that signals "this is good for you," anything that performs caring or seriousness.

**Explicitly not skeuomorphic.** The register is not visual — no paper textures, ruled lines, typewriter fonts, handwritten elements, or any analog reference. The aesthetic should feel native to the web.

**Voice calibration:** Patrice O'Neal, Richard Feynman, Ron Bennington. Precise and irreverent. Dark when the moment calls for it. Drug-positive — this is a log about getting stoned, not a harm reduction pamphlet. The design should fit that personality without illustrating it.

---

## Hard constraints

- **Mobile-first** — most use is on a phone
- **No emojis on stat cards**
- **Charts must remain** — one Chart.js curve chart per strain, requires internet to render; the waypoint tables in the DOM are the machine-readable equivalent and must be preserved even if visually de-emphasized
- **Semantic HTML** — data hierarchy must be reflected in markup, not just visual layout; information communicated visually (color, position) must also exist as text in the DOM; consistent per-run and per-strain structure so an AI agent can parse any strain in the same shape as any other
- **No calibration framing** — no status badges, no "dialed in" language, no progress indicators implying the log is trying to reach a destination
- **No skeuomorphic design** — nothing that visually references notebooks, paper, or analog tools
