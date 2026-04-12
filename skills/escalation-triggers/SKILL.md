---
name: escalation-triggers
description: Explicit triggers for when to pause execution and engage the user. Complements self-correction with clearer escalation criteria. Use when confidence drops, approaches fail, or user input would decisively resolve ambiguity.
---

# Escalation Triggers

Know when to stop and ask rather than continue guessing.

## When To Escalate

### Immediate Escalation (Stop Now)

| Trigger | Why | What to Ask |
|---------|-----|-------------|
| **3+ failed attempts** on same problem | Pattern indicates missing info | "What's the expected behavior here?" |
| **Irreversible action pending** | No undo available | "About to [action]. Confirm?" |
| **Confidence <50%** on critical decision | Wrong choice has lasting cost | "Between [A] and [B], which fits your intent?" |
| **User signaled confusion** | Feedback loop broken | "I may have misunderstood — what should I prioritize?" |
| **Ambiguous constraints** | Multiple valid interpretations | "You said [X] — did you mean [A] or [B]?" |

### Conditional Escalation (Pause and Offer)

| Trigger | Condition | What to Offer |
|---------|-----------|---------------|
| **Approach failed** | Runner-up exists from multi-approach | "[Approach A] failed — try [Approach B] or discuss?" |
| **Time overrun** | >2x estimate, not complete | "Running long — continue or reassess?" |
| **Unexpected result** | Output doesn't match expectation | "Got [X], expected [Y] — proceed or investigate?" |
| **New requirement discovered** | Wasn't in original scope | "Found [constraint] — include it or stay on track?" |

### Background Escalation (Note and Continue)

| Trigger | Action | Log For Later |
|---------|--------|---------------|
| **Minor uncertainty** | Make best guess, note assumption | "Assumed [X] — verify if incorrect" |
| **Style preference ambiguous** | Apply user patterns if known | "Used [pattern] — override if preferred" |
| **Edge case unclear** | Handle gracefully, flag for review | "May need handling for [edge case]" |

## Escalation Templates

### Quick Check (Preferred)

Keeps momentum while resolving ambiguity:

> **Quick check:** Working on [subgoal]. Two options:
> 1. [Approach A — what you're doing]
> 2. [Approach B — alternative]
> 
> Which direction? (Or say "keep going" to proceed with A)

### Full Escalation (When Stuck)

When genuinely blocked:

> **Need input:** I'm hitting a wall on [subgoal].
> 
> **Tried:**
> - [Attempt 1] → [Result]
> - [Attempt 2] → [Result]
> - [Attempt 3] → [Result]
> 
> **Blocker:** [Specific obstacle]
> 
> **Options:**
> 1. Try [alternative approach]
> 2. Pivot to different subgoal first
> 3. You decide — what should I prioritize?

### Pre-Action Confirmation

Before irreversible steps:

> **Confirm:** About to [specific irreversible action].
> - Impact: [what will happen]
> - Recovery: [hard/easy/impossible]
> 
> Proceed? (Yes / No / Modify to [suggestion])

## Anti-Patterns (Avoid)

**Escalation as abdication:**
- Don't ask user what to do when clear options exist
- Don't escalate for trivial decisions
- Don't use "what should I do?" when you can offer "should I do X or Y?"

**Silent failure:**
- Don't continue when confidence is low
- Don't guess on critical decisions without noting the guess
- Don't ignore user confusion signals

**Over-escalation:**
- Don't pause after every tool call
- Don't escalate for single-step clarifications (ask inline)
- Don't treat style preferences as blockers (apply pattern, note assumption)

## Integration

**With self-correction:**
- Self-correction handles "are we on the right path?"
- Escalation-triggers handles "should we ask the user?"
- Run self-correction first, escalate if ADAPT options exhausted

**With interruptible-execution:**
- Each chunk boundary is a natural escalation check
- Use conditional triggers between chunks
- Use immediate triggers mid-chunk if detected

**With multi-approach:**
- If selected approach fails: offer runner-up (conditional escalation)
- If both fail: full escalation with context

## Platform Variations

**Windsurf:**
- Natural breakpoints between tool call batches
- User can see tool history — reference it in escalations

**Copilot (VS Code):**
- User may be AFK or multitasking — longer escalation messages acceptable
- Explicit "STOP FOR INPUT" headers help

**Claude Code:**
- Supports structured /ask commands
- Can reference conversation history more naturally
