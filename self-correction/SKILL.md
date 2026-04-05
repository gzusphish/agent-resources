---
name: self-correction
description: Mid-task course correction and approach pivoting. Use when stuck, going in circles, about to take irreversible action, or after multiple failed attempts. Quick checkpoint to verify progress and decide whether to continue, adapt, escalate, or abandon current approach.
---

# Self-Correction

Quick mid-task checkpoint to detect wrong paths early and pivot before wasting effort.

## When To Use (Trigger Points)

**Automatic triggers — run checkpoint immediately:**
- [ ] After 3+ consecutive tool calls without delivering user value
- [ ] Stuck on same problem for > 2 attempts (same error, same dead end)
- [ ] About to take irreversible action (delete file, major refactor, force push)
- [ ] User expresses confusion or dissatisfaction with approach
- [ ] Task time elapsed > 2x initial estimate with no clear progress

**Manual triggers:**
- [ ] Gut feeling that something is off
- [ ] Complexity suddenly spiked unexpectedly

## Quick Check (30-60 seconds)

Answer these 4 questions honestly:

### 1. Current Subgoal
```
What specific subgoal are we working on right now?
→ [one sentence description]
```

If you can't articulate it clearly → **ESCALATE** (ask user for clarification)

### 2. Progress Assessment
```
Are we demonstrably closer to completing this subgoal than 3 tool calls ago?
→ YES / NO / UNCLEAR
```

- **YES**: Continue current approach
- **NO**: Consider **ADAPT** or **ABANDON**
- **UNCLEAR**: Need better verification → **ADAPT** (add intermediate verification)

### 3. Path Quality
```
Is there a simpler approach we're ignoring because we're already committed?
→ List 2 alternative approaches:
  1. [alternative]
  2. [alternative]
```

If alternatives are clearly better → **ADAPT** (switch approach)

### 4. User Alignment Check
```
Would the user agree this is the right priority right now?
→ YES / NO / UNCLEAR
```

- **NO** or **UNCLEAR** → **ESCALATE** (brief check-in with user)

## Pivot Decision

Based on Quick Check answers, choose:

| Decision | Condition | Action |
|----------|-----------|--------|
| **CONTINUE** | Clear progress, aligned with user, no better alternatives | Proceed with current approach |
| **ADAPT** | Stuck but goal is right — need different method | Switch to alternative approach, try simpler path |
| **ESCALATE** | Unclear subgoal, user alignment uncertain, or need input | Brief user check-in: "Quick question — should I..." |
| **ABANDON** | Wrong subgoal, dead end confirmed, or approach fundamentally flawed | Back up to previous checkpoint or re-decompose with `subgoal-decomposer` |

## Escalation Templates

**Quick check-in (preferred — keeps momentum):**
> "Quick check: I'm working on [subgoal]. Two options:
> 1. [approach A — what you're doing]
> 2. [approach B — alternative]
> Which direction?"

**Full escalation (when truly stuck):**
> "I'm hitting a wall on [subgoal]. After [N] attempts:
> - Tried: [what you did]
> - Result: [what happened]
> - Blocker: [specific obstacle]
> 
> Options:
> 1. Try [alternative approach]
> 2. Pivot to different subgoal first
> 3. You decide — what should I prioritize?"

## Integration With Other Skills

### In writing-plans execution
Between tasks, ask:
- "Did the last task complete as expected?"
- "Does the next task still make sense given what we learned?"

### In subgoal-decomposer
When a subgoal proves harder than estimated (> 20 min for "Small" subgoal):
- Run self-correction checkpoint
- Re-decompose the oversized subgoal
- Update dependency graph if parallel opportunities emerge

### In systematic-debugging
When diagnosis stalls (no new hypotheses after 3 investigations):
- **ADAPT**: Try different debugging angle (symptoms → root cause vs. recent changes → cause)
- **ESCALATE**: Ask user for observed behavior vs. expected

## Anti-Patterns

**Checkpoint abuse:**
- Don't run checkpoint after every tool call — only at triggers
- Don't escalate for trivial decisions the agent should handle

**Commitment bias:**
- Don't CONTINUE just because of sunk cost
- Don't ADAPT to a slightly different version of the same failing approach

**Escalation as abdication:**
- Don't ask user what to do when you have clear options and context
- Do escalate when genuinely uncertain or when user preference is the deciding factor
