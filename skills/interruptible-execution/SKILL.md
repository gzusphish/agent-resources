---
name: interruptible-execution
description: Structure long-running tasks into user-visible chunks with natural pause points. Use when a task will take >5 tool calls, spans multiple files, or has irreversible steps. Keeps the user in the loop and enables mid-course corrections.
---

# Interruptible Execution

Break long work into chunks where the user can intercept before wasted effort.

## When To Use

**Automatic triggers:**
- [ ] Task estimated >10 minutes
- [ ] Will touch >3 files
- [ ] Contains irreversible steps (delete, force push, major refactor)
- [ ] Previous attempt went off track

**Manual triggers:**
- [ ] User said "keep me posted" or similar
- [ ] Uncertainty about approach mid-execution
- [ ] Complex task with unclear subtask boundaries

## Core Algorithm

### Step 1: Chunk the Work

Before starting, identify 2-4 natural breakpoints:

```
Chunk 1: [What] → [Expected outcome] → ~[N] tool calls
Chunk 2: [What] → [Expected outcome] → ~[N] tool calls
Chunk 3: [What] → [Expected outcome] → ~[N] tool calls
```

**Good chunk boundaries:**
- After reading/analyzing (before modifying)
- After each file change
- Before irreversible actions
- When switching subgoals

### Step 2: Pre-Chunk Checkpoint

Before each chunk, state:

> **Next:** [One sentence describing upcoming work]
> **ETA:** [~N tool calls / ~X minutes]
> **Risk:** [None / Low / Medium — why]
> 
> *Interrupt if this looks wrong. Proceeding...*

Then pause briefly (literally stop output, let user read).

### Step 3: Execute Chunk

Work the chunk. Every 3-5 tool calls:

> **Progress:** [Completed X/Y, currently doing Z]
> **On track:** [Yes / No — if no, escalate immediately]

**If you detect going in circles:**
- Stop immediately
- State: "Detected repetition — possible misdirection"
- Offer: continue / reassess / escalate

### Step 4: Post-Chunk Summary

After each chunk:

```
✓ [Chunk name] complete
- Result: [what was accomplished]
- Next chunk: [what's coming]
- Blockers: [none / what they are]
```

**Before continuing to next chunk, offer:**
> "Continue to Chunk N? Or pause to discuss?"

### Step 5: Completion

Final summary:

```
## Completed: [Task]
- Chunks executed: [N]
- Total tool calls: [N]
- Deviations from plan: [none / what and why]
- Final state: [brief description]
```

## Anti-Patterns (Avoid)

**Wall of text:**
- Don't dump 20+ lines of progress updates between chunks
- Keep progress updates to 2-3 lines

**False granularity:**
- Don't create chunks for single tool calls
- Don't split atomic operations

**Ignoring the pause:**
- The pre-chunk statement is a yield point — give the user a moment
- Don't stream through it

## Integration

**With subgoal-decomposer:**
- Each subgoal = potential chunk
- Use decomposition's dependency graph to order chunks

**With self-correction:**
- If chunk takes >2x estimated time: run self-correction
- If chunk produces unexpected result: pause, don't auto-continue

**With multi-approach:**
- If mid-chunk you realize wrong approach was selected: stop, offer runner-up

## Platform Variations

**Windsurf:**
- Tool calls are visible in sidebar — user can see progress
- Brief progress updates sufficient

**Copilot (VS Code):**
- Output streams inline — user may scroll past checkpoints
- Use explicit headers to make checkpoints visible
- Consider shorter chunks (more frequent yields)

**Claude Code:**
- Supports explicit /checkpoint commands
- User can interrupt with Ctrl+C — handle gracefully if interrupted
