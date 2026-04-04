---
name: multi-approach
description: Generate and evaluate multiple approaches to a complex decision before committing. Use when facing ambiguous architecture choices, algorithm selection, design tradeoffs, or whenever a wrong early decision will have cascading costs.
---

# Multi-Approach

Structured multi-option analysis for decisions where early commitment has lasting impact.

## When To Use

**Trigger when one of these conditions is met:**
- Architecture or design decision with >2 reasonable alternatives
- Algorithm or data structure choice affecting multiple components
- Unclear which tradeoff (speed vs simplicity vs flexibility) to prioritize
- Previous attempt failed, need fresh angles
- "There are multiple ways to do this" crosses your mind

**Skip when:**
- Only one viable approach exists
- Decision is easily reversible
- Context clearly dictates the answer
- Time pressure demands immediate action

## Core Algorithm

### Step 1: Define the Decision

```
Decision: [One sentence framing the choice]
Context: [Key constraints, goals, non-negotiables]
Time budget: [How much time to spend deciding]
```

### Step 2: Generate 2-3 Distinct Approaches

For each approach:

```
Approach N: [Short name]
Description: [2-3 sentences on mechanics]
Pros:
- [benefit 1]
- [benefit 2]
Cons:
- [cost 1]
- [cost 2]
```

**Generate diversity:**
- One simple/direct approach
- One robust/flexible approach
- One hybrid or unconventional approach (if viable)

### Step 3: Score Against Criteria

Score 1-3 for each approach on:

```
| Approach | Simplicity | Maintainability | Fit Constraints | Speed to Implement |
|----------|-----------:|----------------:|----------------:|-------------------:|
| A        |     [1-3]  |        [1-3]    |       [1-3]     |         [1-3]      |
| B        |     [1-3]  |        [1-3]    |       [1-3]     |         [1-3]      |
| C        |     [1-3]  |        [1-3]    |       [1-3]     |         [1-3]      |
```

Add tiebreaker criterion if scores are close:
- **Reversibility**: Easy to change later?
- **Confidence**: How well do you understand this approach?
- **User alignment**: Fits what user typically prefers?

### Step 4: Decide

```
Selected: [Approach X]
Reasoning: [One sentence why it wins]
Runner-up: [Approach Y] - keep in reserve if X stalls
```

**Decision rules:**
- Total score wins unless tiebreaker flips it
- If approaches within 1 point: pick simpler one
- If user preference is known and relevant: apply as override

### Step 5: Commit and Proceed

Briefly state the choice to user (optional, depending on context):

> "Going with [Approach X] because [reason]. Alternative was [Approach Y] but [tradeoff decided against]."

Then proceed without second-guessing.

## Output Format

```markdown
## Decision: [Brief description]

### Context
- Constraints: [list]
- Goals: [list]
- Time budget: [X minutes]

### Approaches

**Approach A: [Name]**
Description: [mechanics]
Pros:
- 
- 
Cons:
- 
- 

**Approach B: [Name]**
...

### Scoring

| Approach | Simplicity | Maintainability | Fit Constraints | Speed | Total |
|----------|-----------:|----------------:|----------------:|------:|------:|
| A        |            |                 |                 |       |       |
| B        |            |                 |                 |       |       |

Tiebreaker: [criterion and result]

### Decision

**Selected:** [Approach X]
**Rationale:** [one sentence]
**Fallback:** [Approach Y if X fails]
```

## Anti-Patterns (Avoid)

**Analysis paralysis:**
- Don't generate >3 approaches
- Don't score on >5 criteria
- Timebox: 2 minutes for simple decisions, 5 for complex

**False diversity:**
- Don't present variations of the same approach as different
- Don't include obviously wrong approaches to pad the list

**Commitment without commitment:**
- Don't run multi-approach then ignore the result
- Don't keep re-running for the same decision

## Integration

**With subgoal-decomposer:**
- Use multi-approach when a subgoal has multiple viable implementation paths
- Decision output becomes part of subgoal's "approach" field

**With self-correction:**
- If selected approach fails after 2+ attempts, fallback approach becomes the ADAPT option
- Track which approach was selected for future pattern learning

**With writing-plans:**
- Use for "how should I structure this" decisions before writing the plan
- Quick version: 2 approaches, 2 criteria, 30 seconds
