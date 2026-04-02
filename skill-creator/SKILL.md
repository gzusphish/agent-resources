---
name: skill-creator
description: "Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit or optimize an existing skill, run evals to test a skill, or benchmark skill performance."
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

## The Core Loop

1. **Capture intent** — Understand what the skill should do
2. **Draft the skill** — Write SKILL.md with progressive disclosure
3. **Test manually** — Run 2-3 realistic prompts through the skill
4. **Evaluate with user** — Review outputs together
5. **Iterate** — Refine based on feedback
6. **Finalize** — Polish description and package

Flexibility: Skip steps if the user says "just vibe with me."

---

## Creating a Skill

### 1. Capture Intent

Extract from conversation or interview the user:

1. What should this skill enable?
2. When should it trigger? (user phrases/contexts)
3. Expected output format?
4. Need test cases? (Yes for verifiable outputs like file transforms; no for subjective tasks like writing style)

### 2. Interview and Research

Ask about edge cases, input/output formats, examples, success criteria, dependencies.

Research inline — check existing skills for patterns, search docs if MCPs available.

### 3. Write SKILL.md

Required frontmatter:
```yaml
---
name: skill-name
description: "When to trigger, what it does. Be specific and 'pushy' — the skill only triggers if the description matches."
---
```

**Progressive disclosure structure:**
```
skill-name/
├── SKILL.md          # Core workflow (~100 lines)
├── references/       # Detailed patterns (loaded on demand)
└── scripts/          # Executable helpers
```

Keep SKILL.md under 150 lines. Move detailed patterns to `references/`.

**Writing principles:**
- Explain *why*, not just *what*
- Use examples for complex formats
- No rigid MUST/NEVER — explain reasoning
- Imperative form preferred

### 4. Test Cases

Draft 2-3 realistic prompts. Save to `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

---

## Testing in Windsurf

Since Windsurf doesn't support subagents, test sequentially:

### Step 1: Manual Test Run

For each test case:
1. Read the skill's SKILL.md
2. Follow its instructions to complete the task
3. Save outputs to `<skill-name>-workspace/iteration-1/eval-<id>/outputs/`

### Step 2: User Review

Present results in conversation:
- Show the prompt and output
- For files (.docx, .csv, etc.), save to disk and provide paths
- Ask: "How does this look? Anything you'd change?"

### Step 3: Capture Feedback

Document user feedback in `feedback.md`:
```markdown
## Iteration 1

### Eval 1: [descriptive name]
- **Prompt**: ...
- **Issue**: ...
- **Fix**: ...
```

---

## Improving the Skill

Based on feedback:

1. **Generalize** — Don't overfit to test cases; aim for reusable patterns
2. **Keep lean** — Remove instructions that waste tokens without adding value
3. **Explain why** — Theory of mind beats rigid rules
4. **Bundle repeated work** — If tests all need similar scripts, add to `scripts/`

### Iteration Loop

1. Apply improvements to skill
2. Rerun all test cases (sequential, not parallel)
3. Present results to user for review
4. Capture new feedback
5. Repeat until satisfied

Stop when:
- User says they're happy
- Feedback is minimal/none
- No meaningful progress between iterations

---

## Reference Files

- `references/schemas.md` — JSON structures for evals, grading, etc.
- `agents/grader.md` — How to grade assertions (if running quantitative evals)
- `agents/analyzer.md` — How to analyze benchmark results

---

**Core loop in brief:** Draft → Test → Review → Improve → Repeat → Package.
