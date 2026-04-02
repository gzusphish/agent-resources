---
name: prompt-optimizer
description: Analyze and improve prompt formulations for better tool/LLM results. Use when tool calls return unexpected results, when queries fail to find relevant information, or when refining recurring prompt patterns. Focuses on specificity, context provision, and output format guidance.
---

# Prompt Optimizer

Systematic prompt improvement for better tool and LLM outputs.

## When To Use

- Tool call returns unexpected or poor results
- Search/query fails to find relevant information
- LLM response doesn't match intended goal
- Refining recurring prompt patterns
- User indicates your request was unclear

## Core Workflow

### 1. Diagnose Prompt Issues

Analyze what went wrong:
- Too vague? (broad queries, missing constraints)
- Too specific? (over-constrained, missing edge cases)
- Missing context? (assumed knowledge not provided)
- Wrong format? (expected JSON, got text, etc.)
- Ambiguous intent? (multiple valid interpretations)

### 2. Apply Optimization Patterns

**Specificity ladder**: Start broad, narrow based on results
- Bad: "Find authentication bugs"
- Better: "Find SQL injection in Python auth handlers"
- Best: "Find SQL injection in Python auth handlers using string concatenation"

**Context sandwich**: Background + Task + Format
```
Given [background context],
extract [specific information],
formatted as [structure]
```

**Constraint clarity**: Use explicit constraints
- Include: patterns, file types, date ranges
- Exclude: obvious noise, out-of-scope areas

**Example-driven**: Provide input/output examples for complex tasks

### 3. Test Iteration

For critical prompts:
1. Draft optimized version
2. Test with actual tool/LLM
3. Compare results to baseline
4. Refine if needed

### 4. Document Learnings

When a pattern proves effective, document in `references/prompt-patterns.md`:
- Original prompt (why it failed)
- Optimized version (what changed)
- When to apply this pattern

## Reference Files

- `references/prompt-patterns.md` - Catalog of effective prompt patterns
- `references/common-failures.md` - Typical prompt issues and fixes

## Quick Reference

| Issue | Fix |
|-------|-----|
| Too many results | Add filters, date ranges, file patterns |
| Wrong result type | Explicit output format specification |
| Missed edge cases | Include examples of what to catch |
| Misinterpretation | Clarify intent, add negative examples |
| Incomplete output | Explicit completeness criteria |
