# Prompt Patterns

Catalog of effective prompt patterns and their applications.

## Pattern: Context Sandwich

**Structure**:
```
Given [background context],
I need to [task description],
formatted as [output format].
```

**When to use**: Complex tasks where context matters
**Example**:
```
Given a TypeScript Express application using dependency injection,
I need to find all route handlers that don't have authentication middleware.
Return the results as file paths with line numbers.
```

## Pattern: Specificity Ladder

**Approach**: Start broad, narrow based on results
**When to use**: When unsure of exact scope

**Progression**:
1. Broad: "Find auth issues"
2. Narrow: "Find auth issues in API routes"
3. Precise: "Find missing auth checks in /api/* routes"

## Pattern: Constraint Explicitness

**Structure**: Include/exclude lists
```
Include: [file patterns, date ranges, specific terms]
Exclude: [noise patterns, out-of-scope areas]
Focus on: [priority aspects]
```

## Pattern: Example-Driven

**When to use**: Complex formats or ambiguous tasks
**Structure**: Provide input/output pairs

```
Example 1:
Input: [sample input]
Expected: [desired output]

Example 2:
Input: [edge case]
Expected: [desired output]

Now process: [actual input]
```

## Pattern: Negative Examples

**When to use**: Preventing common misinterpretations
**Structure**: Show what NOT to do/include

```
Include: [what you want]
Do NOT include: [common mistakes]
Exclude: [false positives]
```

## Pattern: Chain of Verification

**When to use**: Tasks requiring multiple checks
**Structure**: Step-by-step with verification

```
Step 1: [action] → verify: [success criteria]
Step 2: [action] → verify: [success criteria]
Final check: [completion criteria]
```

## Common Failures & Fixes

| Failure Mode | Fix Pattern |
|-------------|-------------|
| Too many results | Add filters, date ranges, file patterns |
| Wrong format | Explicit format specification with example |
| Missed edge cases | Include examples of edge cases |
| Misinterpretation | Negative examples + explicit intent |
| Incomplete output | Explicit completeness criteria |
| Ambiguous scope | Constraint lists (include/exclude) |

## Pattern Selection Guide

**Information retrieval** → Context Sandwich + Specificity Ladder  
**Format transformation** → Example-Driven + Explicit format  
**Quality checking** → Chain of Verification + Negative examples  
**Complex analysis** → Context Sandwich + Example-Driven  
**Scope definition** → Constraint Explicitness
