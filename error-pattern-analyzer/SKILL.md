---
name: error-pattern-analyzer
description: Track, categorize, and analyze recurring errors to identify systemic issues. Use when errors occur, when investigating failure trends, or when preparing for similar tasks where past errors might repeat. Builds personal error taxonomy and prevention strategies.
---

# Error Pattern Analyzer

Track and learn from mistakes to prevent recurrence.

## When To Use

- Any error occurs (tool failure, wrong assumption, etc.)
- Preparing for tasks similar to past failures
- Investigating why a pattern keeps failing
- Periodic review of error trends

## Core Workflow

### 1. Capture Error Context

When an error occurs, record:
```yaml
error:
  type: [tool_failure | assumption_wrong | logic_error | context_miss]
  tool: [tool_name if applicable]
  task_context: [what you were trying to do]
  trigger: [what action caused it]
  symptom: [error message or unexpected result]
  root_cause: [why it actually failed]
```

### 2. Categorize Error Type

**Tool failures**: API errors, timeouts, permission issues
**Assumption errors**: Wrong file structure, missing dependencies
**Logic errors**: Wrong approach, flawed reasoning
**Context misses**: Missed requirements, wrong scope
**Communication errors**: Misunderstood user intent

### 3. Check for Patterns

Query existing errors for similarities:
- Same tool failing?
- Same type of assumption wrong?
- Same task context recurring?
- Time correlation (certain times of day)?

### 4. Generate Prevention Strategy

For identified patterns:
```markdown
## Pattern: [name]
- **Trigger**: [when this occurs]
- **Current failure mode**: [what happens]
- **Prevention checklist**:
  - [ ] Step to verify before proceeding
  - [ ] Alternative approach if check fails
- **Detection**: Early warning signs
```

### 5. Update Working Patterns

Apply prevention strategies to current workflow:
- Add verification steps before error-prone actions
- Use alternative approaches for known failure modes
- Add guardrails in relevant skills

## Reference Files

- `references/error-taxonomy.md` - Categorized error types and examples
- `references/prevention-patterns.md` - Checklists and guardrails

## Integration

Errors feed into reflection skill for holistic improvement.
