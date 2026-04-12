---
name: gtd-maintainer
description: "Use when working with the user's GTD (Getting Things Done) personal productivity system. Helps maintain actions.md, Journal.md, and project plans according to canonical spec."
allowed-tools:
  - Read
  - Write
  - Edit
---

# GTD System Maintainer

Assist with the user's personal GTD system as specified in `gtd/docs/gtd-system-spec.md`.

## Core System

**Primary Files:**
- `actions.md` — Current commitments and next actions
- `Journal.md` — Completed work record
- `project-plans/` — Project-specific planning documents

**Key Structure:**
```
# GTD
## Checklists      (recurring items, keep history)
## Inbox           (raw capture, never journal automatically)
## Waiting         (delegated/blocked: "Waiting on X; follow up YYYYMMDD")
## Actions
  ### @Home
  ### @Online
  ### @Phone
  ### @Town
```

## Date Conventions

**Journal Format:**
- Line 1: `# Journal`
- Months: `## Month YYYY` (reverse chronological)
- Days: `YYYYMMDD Day` (reverse chronological within month)
- Example: `20260329 Sunday`

**Date Entry Rules:**
1. Check if month heading exists
2. Check if day line exists
3. Insert day below top month heading if new
4. Append entries under existing day if present

## Task Handling

**Task States:**
- Incomplete: `[ ] task description`
- Complete: `[x] task description`

**Project Headers:**
- Bold: `**Project Name**`
- Italic (meta): `*One-offs*` or `*Recurring*`

**Context Lines:**
- Start with `...` and no checkbox
- Belong to nearest project block above
- Preserve context meaning when journaling

## Journaling Rules

**When to Journal:**
- Meaningful completions (not every checkbox)
- Outcomes and context matter
- Project completions preserve project headers

**Format:**
```markdown
20260329 Sunday
**Project Name**
 [x] Completed task
 [x] Another task with context preserved
```

**One-offs:**
- Tasks without project headers → `*One-offs*` in journal

## Invariants (Never Violate)

1. **No automatic archival** — manual process only
2. **Inbox never journals** — refile/clarify first
3. **Work/personal separation** — no work ticket logic in personal repo
4. **Preserve context lines** — they explain "why"

## When to Use This Skill

- Adding new actions or projects
- Journaling completed work
- Reviewing/maintaining GTD structure
- Creating project plans from templates
- Clarifying inbox items

## What NOT to Do

- **Never** auto-archive completed items
- **Never** journal inbox items without clarification
- **Never** add work-only headers or ticket IDs
- **Never** assume automation is required

## Quick Reference

| Task | Action |
|------|--------|
| New journal entry | Check month → check day → insert/add |
| Complete task | Mark [x] → optionally journal |
| Inbox item | Clarify → move to Actions under context |
| Waiting item | Format: "Waiting on X; follow up YYYYMMDD" |
| Project plan | Use `project-plans/templates/any-project.md` |

**Work vs Personal:**
- Keep work-only filenames/logic out of gtd-personal
- Copy only generic structure improvements between systems
- When in doubt, leave in gtd-work only
