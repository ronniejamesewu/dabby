# Skill Library

## Authoring rules

- **Audience:** zero-context mid-level engineer or Sonnet-class model.
  Imperative runbook voice; copy-pasteable commands; every jargon term
  defined once; tables and checklists; each skill says when NOT to use it
  and which sibling to use instead.
- **Format:** `.claude/skills/<name>/SKILL.md`, YAML frontmatter with
  `name` and a trigger-rich `description` (exactly when a model should
  load it).
- **Ground truth only:** verify every command, flag, path, and claim
  against the repo before stating it. Wrong runbooks are worse than none.
- **Embed knowledge; don't reference private/user-specific paths as
  load-bearing sources.**
- **Date-stamp volatile facts;** end each skill with a "Provenance and
  maintenance" section containing one-line re-verification commands for
  anything that may drift.
- **No oversell:** unproven things stay labeled open/candidate. Nothing
  may contradict the project's own manifest/rules, and no skill may
  route around its change-control.
- **Write ONLY inside `.claude/skills/`;** the rest of the repo is
  read-only during skill authoring. No mutating git commands.

## Catalog

**Keep this current.** When a new skill is accepted, add it to the table
and the handoff graph below.

| Skill | Trigger | Hands off to |
|---|---|---|
| [dab](dab/SKILL.md) | User announces a dab starting — "about to hit it", "grabbing one", "party mode" | log-run (when user initiates logging), new-jar (strain named with no jar) |
| [log-run](log-run/SKILL.md) | User wants to log a completed run — "log it", "write that up" | new-jar (if no jar exists), new-rig (if equipment changed), analysis-toolkit (at step 5), close-jar (if user confirms the jar is done) |
| [new-jar](new-jar/SKILL.md) | Strain has no jar file — "new jar", "starting a new jar for X" | log-run (after jar created) |
| [analysis-toolkit](analysis-toolkit/SKILL.md) | Drafting per-run analysis at log-run step 5 | (returns to log-run) |
| [close-jar](close-jar/SKILL.md) | Jar is finished — "jar's done", "that was the last one" | log-run (first, if the final run isn't logged yet) |
| [new-rig](new-rig/SKILL.md) | Equipment doesn't match any existing RIG_N | log-run (after constant created) |
| [correct-frozen-data](correct-frozen-data/SKILL.md) | Error in a previously logged run — "that run had the wrong rig" | new-rig (if a correction reveals a novel equipment config) |
| [change-baseline](change-baseline/SKILL.md) | BASELINE_CURVE recommendation changing — rare, high-impact | (standalone) |

### Handoff graph

```
dab ──→ log-run ──→ new-jar (if no jar)
    │           ──→ new-rig (if equipment changed)
    │           ──→ analysis-toolkit (step 5)
    │           ──→ close-jar (if user confirms closure after final run)
    └──→ new-jar (strain named with no jar; user-initiated)

close-jar ──→ log-run (first, if the final run isn't logged yet; then back)

correct-frozen-data ──→ new-rig (if correction reveals novel equipment)

change-baseline (standalone, rare)
```

## Skill template

```markdown
---
name: {{kebab-case-slug}}
description: {{One paragraph. What this skill does, when to trigger it
(exact phrases a user would say), what it does NOT do. This is the
primary routing signal -- a model decides whether to load the skill
based on this text alone.}}
---

# {{Title}}

{{One-paragraph summary of what this skill does and where the procedure
comes from (PR number, handoff notes line, etc.).}}

## Terms

| Term | Meaning |
|---|---|
| {{term}} | {{definition — first and only definition in this file}} |

**Two registers.** {{List machine-side vocabulary (field names, constant
names, slugs, step labels) that must never appear in user-facing text.
State what the user sees instead.}}

## Hard rules

- {{Rule 1 — the invariants this skill must never violate.}}

## When NOT to use

- **{{Scenario}}** -- that's the {{sibling-skill}} skill
  (`.claude/skills/{{sibling}}/SKILL.md`).

## Workflow

**1. {{Step name.}}**
{{Imperative instructions. Copy-pasteable commands where applicable.}}

## Recovery paths (don't improvise these)

- **{{Error condition}}** -- {{exact remediation steps.}}

## Provenance and maintenance

Created {{date}}. {{Origin reference (PR, handoff notes line, etc.).}}
Verify these still hold if this skill starts giving results that don't
match reality:

\```
# {{what this checks}}:
{{one-line shell command}}
\```

Dogfood-test status: **Not yet tested.**
```
