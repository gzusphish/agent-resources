# Decision Templates

Templates for common decision types.

## Architecture Decision

```markdown
## Decision: [Architecture choice]
**Date**: [YYYY-MM-DD]
**Context**: [System state and requirements]

**Problem**: [What needs solving]

**Options**:
1. [Option A]
   - Pros: [benefits]
   - Cons: [drawbacks]
   - Effort: [estimation]

2. [Option B]
   - Pros: [benefits]
   - Cons: [drawbacks]
   - Effort: [estimation]

3. [Option C]
   - Pros: [benefits]
   - Cons: [drawbacks]
   - Effort: [estimation]

**Decision**: [Chosen option]
**Rationale**: [Why this choice]
**Confidence**: [High/Medium/Low]

**Trade-offs Accepted**:
- [What was given up]
- [Why it was acceptable]

**Reversibility**: [Easy/Moderate/Hard]
**Rollback Plan**: [If decision proves wrong]

**Expected Outcome**: [Success criteria]
**Review Date**: [When to evaluate]
```

## Tool Selection Decision

```markdown
## Decision: Tool Selection - [task]
**Date**: [YYYY-MM-DD]
**Task**: [What needs doing]

**Candidate Tools**:
1. [Tool A]
   - Capabilities: [what it can do]
   - Fit: [how well it matches need]
   - Experience: [past success with tool]

2. [Tool B]
   - Capabilities: [what it can do]
   - Fit: [how well it matches need]
   - Experience: [past success with tool]

**Decision**: [Chosen tool]
**Rationale**: [Specific reasoning]
**Confidence**: [High/Medium/Low]

**Fallback**: [Alternative if primary fails]

**Expected Result**: [What success looks like]
```

## Approach Trade-off Decision

```markdown
## Decision: Approach Trade-off
**Date**: [YYYY-MM-DD]
**Situation**: [Context]

**Trade-off Dimension**: [Speed/Quality/Scope/Resources]

**Extreme Options**:
1. [Fast/More/Less approach]
   - Benefits: [upsides]
   - Risks: [downsides]

2. [Thorough/Less/More approach]
   - Benefits: [upsides]
   - Risks: [downsides]

**Balanced Approach**: [Where on spectrum]
**Justification**: [Why this balance]

**User Alignment**: [Confirmed/Assumed] preferences
```

## Outcome Review Template

```markdown
## Outcome Review: [Decision name]
**Original Date**: [YYYY-MM-DD]
**Review Date**: [YYYY-MM-DD]

**Expected Outcome**:
- [What was predicted]

**Actual Outcome**:
- [What happened]

**Comparison**:
- Alignment: [Better/As Expected/Worse]
- Surprises: [Unexpected elements]
- Missed Factors: [What wasn't anticipated]

**Decision Quality Assessment**:
- Process: [Good/OK/Poor] - reasoning at the time
- Outcome: [Good/OK/Poor] - result achieved
- Luck vs Skill: [mostly luck / mixed / mostly skill]

**Learnings**:
- What to replicate: [successful reasoning]
- What to avoid: [flawed reasoning]
- Calibration update: [confidence adjustments]

**Heuristic Extracted**: [rule for future decisions]
```
