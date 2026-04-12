---
name: decision-journal
description: Record and review significant decisions to improve decision quality over time. Use for architectural choices, tool selection dilemmas, approach trade-offs, or any decision with non-trivial consequences. Enables periodic review of decision outcomes and calibration.
---

# Decision Journal

Structured decision recording for learning from outcomes.

## When To Use

- Architectural or design decisions
- Tool/library selection dilemmas
- Approach trade-offs (speed vs. thoroughness, etc.)
- Any decision with nontrivial downstream consequences
- Before/after significant course corrections

## Core Workflow

### 1. Pre-Decision Capture

Before committing, document:
```markdown
## Decision: [brief description]
**Date**: [timestamp]
**Context**: [what situation led to this]

**Options Considered**:
1. [Option A] - pros/cons
2. [Option B] - pros/cons
3. [Option C] - pros/cons

**Decision**: [chosen option]
**Rationale**: [why this choice]
**Confidence**: [High/Medium/Low]
**Expected Outcome**: [what success looks like]

**Reversibility**: [Easy/Moderate/Hard] if wrong
```

### 2. Post-Outcome Review

After results are known:
```markdown
**Actual Outcome**: [what happened]
**Outcome Quality**: [Better/As Expected/Worse] than predicted
**Surprises**: [unexpected results]
**What Influenced Outcome**: [factors not anticipated]

**Decision Quality**: [Good/OK/Poor]
- If poor: what signal was missed?
- If good: what reasoning to replicate?

**Calibration Note**: [update confidence heuristics]
```

### 3. Periodic Review

Monthly/quarterly analysis:
- Review all decisions by confidence level
- Identify calibration gaps (over/under confident)
- Extract decision heuristics that work
- Note systematic biases

## Decision Quality Factors

Assess decisions on:
- **Process**: Was reasoning sound at the time?
- **Outcome**: Did it achieve desired result?
- **Learning**: What did we learn for next time?

Good process can have bad outcomes (unknown unknowns).
Bad process with good outcomes is dangerous (lucky, not skilled).

## Reference Files

- `references/decision-templates.md` - Templates for common decision types
- `references/heuristics.md` - Extracted decision rules that work

## Integration

Connects with reflection skill for task-level learnings and error analyzer for decision-related failures.
