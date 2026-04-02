---
name: preference-learner
description: Systematically capture and apply user preferences to reduce friction and improve alignment. Use when user corrects suggestions, rejects approaches, expresses strong preferences, or when working with a user over multiple sessions. Builds lightweight preference profile for personalized assistance.
---

# Preference Learner

Capture and apply user preferences for personalized assistance.

## When To Use

- User explicitly states a preference
- User corrects or overrides your suggestion
- User rejects an approach multiple times
- Starting work with a returning user
- When you sense misalignment in style/approach

## Core Workflow

### 1. Detect Preference Signals

Watch for:
- **Explicit**: "I prefer...", "Always do...", "Never..."
- **Implicit**: Rejecting suggestions, requesting alternatives
- **Pattern**: Repeated corrections in same direction
- **Tone**: Frustration at certain approaches

### 2. Categorize Preferences

Organize by domain:
```yaml
code_style:
  - [specific preference]
  
communication:
  - [verbosity, formality, etc.]
  
tool_usage:
  - [which tools to prefer/avoid]
  
workflow:
  - [order of operations, checkpoints]
  
output_format:
  - [file structure, documentation style]
```

### 3. Capture Preference

Record in structured format:
```markdown
## Preference: [category]
**Signal**: [what the user did/said]
**Preference**: [what they want]
**Confidence**: [High/Medium/Low] 
**Source**: [explicit statement / inferred from pattern]
**Date**: [when observed]

**Apply When**: [situations where this applies]
**Exceptions**: [if any]
```

### 4. Apply Proactively

Before suggesting:
- Check preference profile for relevant entries
- Default to preferred approaches
- Note when preferences conflict (ask for clarification)

### 5. Verify and Refine

Periodically:
- Confirm preferences still hold (styles evolve)
- Remove outdated preferences
- Check for contradictions in profile

## Reference Files

- `references/preference-categories.md` - Standard preference taxonomy
- `templates/user-profile.md` - User preference template

## Storage

Store in `../agent-knowledge/preferences/[user-id].md` or inline in conversation context if ephemeral.

## Integration

Works with reflection skill (preferences often surface during reflection) and decision journal (preferences influence decisions).
