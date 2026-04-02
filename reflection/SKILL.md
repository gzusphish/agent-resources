---
name: reflection
description: Conduct structured post-task reflection to identify what worked, what didn't, and how to improve future performance. Use after completing complex multi-step tasks, when user expresses dissatisfaction, or when a task took significantly longer than expected. Captures decision points, tool efficiency, and failure patterns.
---

# Reflection Skill

Structured post-task analysis to extract learnings and identify improvement opportunities.

## When To Use

- After completing complex multi-step tasks (>5 tool calls)
- When user expresses dissatisfaction or corrects your approach
- When a task took significantly longer than expected
- When you encountered repeated obstacles or dead ends
- Periodically for recurring task types

## Core Workflow

### 1. Capture Context

Before reflection begins, gather:
- Task description and goal
- Number of steps/tool calls taken
- Final outcome (success/partial/failure)
- User feedback (explicit or inferred)

### 2. Analyze Decision Points

For each major decision:
- What options were considered?
- Which was chosen and why?
- Was it the right choice in retrospect?
- What would you do differently?

### 3. Evaluate Tool Usage

Review tool sequences for efficiency:
- Redundant reads (checking same file multiple times)
- Unnecessary breadth (searching too broadly)
- Premature actions (editing before understanding)
- Missing shortcuts (could MCP/regex have helped?)

### 4. Identify Failure Patterns

Look for recurring issues:
- Assumptions that proved wrong
- Context that was missed initially
- Paths that led to dead ends
- User corrections that indicate misalignment

### 5. Synthesize Learnings

Output brief reflection summary:
```markdown
## Reflection: [task-type]

**Decision Quality**: [Good/Mixed/Poor]
- Key decisions and their outcomes

**Tool Efficiency**: [Efficient/Okay/Wasteful]
- What worked well: ...
- What to optimize: ...

**Pattern Recognition**: 
- Issue: [description]
- Fix: [specific action for next time]

**User Alignment**: [Aligned/Minor drift/Off target]
- What to clarify upfront next time
```

## Reference Files

- `references/reflection-templates.md` - Templates for common reflection types
- `references/pattern-library.md` - Catalog of observed patterns and fixes
- `scripts/store_reflection.py` - Save reflection to knowledge base

## Integration

Store reflections in `../agent-knowledge/reflections/` for pattern analysis across sessions.
