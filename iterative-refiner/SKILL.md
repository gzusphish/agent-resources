---
name: iterative-refiner
description: Iterative quality refinement for substantial outputs. Use when writing plans, documentation, complex code, or any deliverable where "good enough" isn't acceptable. Self-evaluates against explicit criteria and regenerates to improve low scores.
---

# Iterative Refiner

Quality enforcement through structured self-evaluation and targeted regeneration.

## When To Use

**Automatic triggers:**
- [ ] Writing a plan >10 steps or spanning multiple phases
- [ ] Creating documentation >500 words
- [ ] Generating complex code with multiple interacting components
- [ ] Previous output was rejected or received criticism

**Manual triggers:**
- [ ] User signals something is "weak" or "needs work"
- [ ] Gut feeling that output is mediocre
- [ ] High-stakes deliverable (user-facing, architectural decision)

**Skip when:**
- Output is trivial (<5 lines, simple answer)
- User explicitly wants "rough draft" or "quick take"
- Time pressure exceeds quality needs

## Core Algorithm

### Step 1: Define Quality Criteria (30 seconds)

Choose 3-5 criteria relevant to the output type:

**For plans:**
- Clarity: Each step is unambiguous and actionable
- Completeness: No gaps between current state and goal
- Feasibility: Each step is achievable with available tools/context
- Sequencing: Dependencies correctly ordered
- Conciseness: No redundancy, no filler

**For documentation:**
- Accuracy: Technical details are correct
- Completeness: Covers all necessary topics, no omitted edge cases
- Clarity: Can be understood by intended audience
- Structure: Logical flow, good scannable format
- Utility: Reader can act on this information

**For code:**
- Correctness: Handles stated requirements and edge cases
- Readability: Clear naming, appropriate abstraction
- Maintainability: Easy to modify, well-structured
- Efficiency: No obvious performance pitfalls
- Testability: Can be verified

### Step 2: Generate Initial Draft

Produce the output normally.

### Step 3: Self-Evaluate (60 seconds)

Score 1-5 for each criterion:

```
| Criterion | Score | Evidence |
|-----------|-------|----------|
| [Name 1]  | 1-5   | [specific line/section demonstrating quality] |
| [Name 2]  | 1-5   | |
| [Name 3]  | 1-5   | |
| [Name 4]  | 1-5   | |
| [Name 5]  | 1-5   | |

**Total:** [sum] / [max] = [percentage]
**Weaknesses:** [criteria scoring ≤3]
```

**Scoring rubric:**
- 5 = Excellent, exceeds expectations
- 4 = Good, meets expectations
- 3 = Acceptable, minor issues
- 2 = Problematic, needs work
- 1 = Unacceptable, major issues

### Step 4: Decide Refinement

```
If all scores ≥4: → Deliver as-is
If any score ≤2 AND time budget > 2 min: → Regenerate
If total < 70%: → Regenerate
Otherwise: → Deliver with quality note
```

### Step 5: Regenerate (if needed)

Focus specifically on low-scoring criteria:

```
Regeneration focus: [weakness 1], [weakness 2]
Constraints: Maintain strengths from previous draft
```

Produce new version, return to Step 3 (max 2 refinement cycles).

### Step 6: Deliver

**If refined:**
> "[Output] — Refined 1 cycle to strengthen [aspects improved]. Final quality: [total]/[max]."

**If not refined:**
> "[Output] — Quality check passed ([total]/[max])."

## Anti-Patterns (Avoid)

**Over-refinement:**
- Don't chase perfect scores (diminishing returns)
- Cap at 2 refinement cycles
- Don't refine trivial outputs

**Criteria mismatch:**
- Don't use code criteria for documentation
- Don't include irrelevant criteria just to have 5

**Ignoring time budget:**
- If user is waiting, deliver current version with honesty: "Quality: X/15 — could use another pass on [aspect] if time permits"

## Integration

**With writing-plans:**
- Run after plan generation, before delivery
- Quality threshold: 80% (12/15) minimum

**With writing-skills:**
- Use for complex skill content (>100 lines)
- Quick version: 3 criteria, 1 refinement max

**With multi-approach:**
- If selected approach scores low on feasibility, try runner-up approach instead of refining

**With self-correction:**
- If refinement cycles exceed 2, treat as "stuck" — run self-correction checkpoint
