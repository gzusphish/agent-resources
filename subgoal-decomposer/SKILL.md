---
name: subgoal-decomposer
description: Break complex tasks into hierarchical subgoals with dependency mapping. Use when facing complex tasks where the path forward is unclear, before committing to a specific implementation approach, or when you need to identify parallelizable work streams.
---

# Subgoal Decomposer

Transform complex, ambiguous tasks into structured, actionable subgoals using systematic decomposition.

## When To Use

- Task complexity is high (>3 distinct conceptual components)
- Uncertainty about where to start or what steps are needed
- Need to identify parallel work streams
- Planning before execution (precedes writing-plans, pdd, or similar)
- Stuck or overwhelmed by task scope

## Core Algorithm: Work Backward from Goal

### Step 1: Define the End State

Write a single sentence describing the completed task:
```
End State: [Concrete, verifiable outcome]
```

### Step 2: Ask "What Must Be True Just Before?"

Identify immediate prerequisites:
- What conditions must exist immediately before the end state is achieved?
- What outputs must be ready?
- What decisions must be made?

List 2-5 immediate prerequisites. For each, write:
```
Subgoal N: [Prerequisite condition/output]
├── Verifiable: [How you know it's done]
├── Estimate: [Small/Medium/Large effort]
└── Blockers: [What it depends on]
```

### Step 3: Recurse Until Current State

For each subgoal identified in Step 2, repeat Step 2:
- What must be true just before this subgoal is achieved?
- Continue until reaching the current state (nothing more to decompose)

Stop when a subgoal is:
- A single atomic action (one tool call, one file read, one edit)
- Fully understood (no unknowns about how to do it)
- Less than 10 minutes of work

### Step 4: Map Dependencies

Create dependency graph:
```
Independent (can run in parallel):
- Subgoal A
- Subgoal B

Sequential (must run in order):
- Subgoal C → Subgoal D → End State

Merge points:
- Subgoal A AND Subgoal B both required for Subgoal E
```

### Step 5: Flag Parallel Opportunities

For each independent subgoal, mark parallelization potential:
```
[PARALLEL] Subgoal X: [description]
[PARALLEL] Subgoal Y: [description]
[SEQUENTIAL] Subgoal Z: [description] (depends on X and Y)
```

## Output Format

```markdown
## Decomposition: [Task Name]

### End State
[Verifiable completion criteria]

### Subgoal Hierarchy

#### Level 1: Major Milestones
1. [Subgoal 1] - [Estimate] - [PARALLEL/SEQUENTIAL]
   - Verifiable: [criteria]
   - Depends on: [none/listed subgoals]

2. [Subgoal 2] - [Estimate] - [PARALLEL/SEQUENTIAL]
   - Verifiable: [criteria]
   - Depends on: [none/listed subgoals]

#### Level 2: Decomposition
[For each Level 1 subgoal that isn't atomic:]

**Subgoal N Breakdown:**
- 2.1 [Atomic action] - [~X min]
- 2.2 [Atomic action] - [~Y min]
- 2.3 [Atomic action] - [~Z min]

### Dependency Graph

```text
[Current State]
    │
    ├──→ [Subgoal 1.1] ──→ [Subgoal 1.2] ──┐
    │                                        │
    ├──→ [Subgoal 2.1] ──→ [Subgoal 2.2] ────┼──→ [End State]
    │                                        │
    └──→ [Subgoal 3.1] ──────────────────────┘
```

### Execution Strategy

**Phase 1 (Parallel):**
- [ ] Subgoal 1.1
- [ ] Subgoal 2.1
- [ ] Subgoal 3.1

**Phase 2 (Sequential/Parallel as noted):**
- [ ] Subgoal 1.2 (after 1.1)
- [ ] Subgoal 2.2 (after 2.1)

**Phase 3 (Merge):**
- [ ] Final integration (after 1.2, 2.2, 3.1)

### Risk Flags

- [ ] Subgoal with unclear approach: [which one]
- [ ] External dependency: [what and who]
- [ ] Estimation uncertainty: [which subgoals]
```

## Integration with Other Skills

After decomposition:

**For implementation:**
- Use `writing-plans` to convert subgoals into detailed implementation steps
- Use `pdd` for full project lifecycle management

**For execution:**
- Reference subgoal hierarchy as roadmap
- Update status as subgoals complete
- **When a subgoal proves more complex than estimated (> 20 min for "Small" subgoal):**
  - Run `self-correction` checkpoint
  - If ADOPT or ESCALATE: Re-decompose the oversized subgoal
  - Update dependency graph if parallel opportunities emerge

## Anti-Patterns (Avoid)

**Over-decomposition:**
- Don't break single actions into multiple subgoals
- Don't create dependencies where none exist
- Stop at "can execute now" granularity

**Under-decomposition:**
- Don't leave "figure out X" as a subgoal (decompose the figuring-out)
- Don't assume understanding — decompose until confident

**Premature sequencing:**
- Mark everything sequential by default (assumes no parallel work)
- Ignore opportunities for parallel exploration
