---
name: conversation-manager
description: Use when loading conversation history for context recovery, preparing context for new conversations, or managing selective loading of prior exchanges to avoid context overflow. Also use when the user asks to summarize, document, or archive the current conversation. Implements two-stage loading with preliminary filtering followed by targeted exchange recovery.
trust: Core
version: 1.0.3
---

# Conversation Manager

Intelligent conversation history loading with two-stage filtering to prevent context overflow.

## When To Use

- **Starting a new conversation** that builds on prior work — need relevant context without overload
- **Resuming long-term work** — recover context from days/weeks ago selectively
- **Cross-project context** — find relevant exchanges across multiple conversation files
- **Context overflow mitigation** — limit loaded exchanges to most relevant subset
- **Multi-hop reasoning** — follow a chain of decisions through multiple conversations
- **Summarizing a conversation** — when the user asks you to document the current conversation, store it as a new file in the resolved scriptorium folder (see "Scriptorium Location") following this skill's format with YAML frontmatter, exchange IDs, and structured sections

## Scriptorium Location

When writing or reading archived conversation summaries, resolve the scriptorium folder in this order:

1. Prefer a central scriptorium at `.panopticon/scriptorium/` if it exists and is accessible in the current environment.
2. Otherwise use a workspace-local scriptorium at `scriptorium/` (create it if missing).

## Archiving the Current Conversation

Use this skill in **archiving mode** when the user asks you to summarize/document the current conversation as a reusable context file.

**Steps:**
- Resolve the scriptorium folder using "Scriptorium Location"
- Create a new conversation file in that scriptorium folder using the timestamp of the first exchange for the filename
- Follow `conversation-manager/references/TEMPLATE.md` for the canonical structure
- Follow `conversation-manager/references/GENERATION_PROMPT.md` for generation rules (what to include/omit, refresh rules)
- Include `exchange-000` as the first exchange (final state summary) and mark it `always`

## Core Concept: Two-Stage Loading

```
Stage 1: Preliminary Chat (Quick Filter)
    ↓
Analyze current request + conversation metadata (frontmatter only)
    ↓
Identify relevant conversation files and exchange IDs
    ↓
Output: Target list [file:exchange-ids]

Stage 2: Main Chat (Targeted Recovery)
    ↓
Load only identified exchanges from Stage 1
    ↓
Proceed with full context
```

This prevents loading 28 exchanges when only 3-5 are relevant to the current task.

## Stage 1: Preliminary Filtering

**Input:** Current user request + available conversation files (metadata only)

**Process:**
```yaml
filtering_steps:
  1_file_selection:
    - Read YAML frontmatter of all conversation files
    - Match topics/keywords to current request
    - Score relevance (High/Medium/Low)
    - Select High + conditional Medium matches
  
  2_exchange_identification:
    - Read Exchange ID headers from selected files
    - Match relevance tags to request
    - Note Load Priority (always first, then conditional)
    - Build target list: [file: [exchange-ids]]
  
  3_context_budget:
    - Limit to ~10-15 exchanges maximum
    - Prioritize: always > conditional > optional
    - Include final state summaries as "exchange-000"
```

**Output format for Stage 2:**
```markdown
## Context Recovery Plan

**Current Request Topic:** [extracted topic]

**Selected Conversations:**
1. `references/20260329.0143-central-workspace-assembly.md`
   - exchange-000 (final state summary)
   - exchange-001 (skill discovery)
   - exchange-005 (security infrastructure)
   - exchange-007 (skill-vetter creation)

2. `references/20260407.2048-conversation-history-management.md`
   - exchange-001 (concept proposal)

**Total Exchanges to Load:** 5
**Estimated Context Tokens:** ~2000
**Confidence:** High
```

## Stage 2: Targeted Recovery

**Input:** Recovery plan from Stage 1

**Process:**
```bash
# Load each targeted file, then extract only the specified exchanges
# (e.g., by locating the "**Exchange ID:** exchange-NNN" markers for each selected ID)
```

**Verification:**
- [ ] All identified exchanges loaded successfully
- [ ] No unrelated exchanges accidentally included
- [ ] Key decisions and outcomes captured
- [ ] Context sufficient for current request

## Implementation Patterns

### Pattern A: Single File, Selective Exchanges

```
User: "Update the skill-vetter to handle Python 3.12"

Stage 1 Analysis:
- Topic: skill-vetter, Python, security-vetting
- File match: 20260329.0143-central-workspace-assembly.md (keywords: skill-vetter)
- Exchange match: exchange-007 (skill-vetter creation)

Stage 2 Loading:
- Load: exchange-000 (final state), exchange-007
- Skip: 26 other unrelated exchanges
```

### Pattern B: Cross-File Context Chain

```
User: "Why did we choose Ollama over other local model options?"

Stage 1 Analysis:
- Topic: local-models, ollama, model-comparison
- File matches: 
  - references/20260329.0143-central-workspace-assembly.md (exchange-010: local models)
  - references/20260407.2048-conversation-history-management.md (none)
- Exchange match: exchange-010

Stage 2 Loading:
- Load: exchange-010 (full local models discussion)
- Result: Full context on decision rationale
```

### Pattern C: Multi-Hop Decision Chain

```
User: "Should we switch from copy to symlink for skill installation?"

Stage 1 Analysis:
- Topic: skill-installation, symlink, tech-debt
- File matches:
  - 20260329.0143-central-workspace-assembly.md (exchange-005: security infrastructure, copy operations)
  - Current TO-DO.md mentions symlink in tech debt
- Decision: Load exchange-005 for security context, note current open question

Stage 2 Loading:
- Load: exchange-000 (current skills state), exchange-005
- Augment: Read current TO-DO.md tech debt section
```

## Conversation File Schema

**Required for two-stage loading:**

```yaml
# Frontmatter (Stage 1 uses this)
---
topics: [searchable, list]
keywords: [for, matching]
exchanges: N  # Total count
load_priority: always|conditional|optional
summary: "For quick assessment"
---

# Exchange Headers (Stage 2 uses this)
## Exchange N: Title
**Exchange ID:** exchange-NNN  # REQUIRED
**Relevance Tags:** [tag1, tag2]  # For filtering
**Load Priority:** always|conditional|optional
```

## Loading Strategies by Use Case

| Use Case | Strategy | Typical Load |
|----------|----------|--------------|
| **Quick reference** | Final state only | 1 exchange |
| **Specific decision** | Decision exchange + context | 2-3 exchanges |
| **Feature continuation** | All exchanges tagged with feature | 5-10 exchanges |
| **Architecture review** | Multiple files, key decisions | 10-15 exchanges |
| **Full recovery** | All exchanges (rarely needed) | All |

## Anti-Patterns to Avoid

| Pattern | Problem | Solution |
|---------|---------|----------|
| **Load entire files** | Context overflow | Use Stage 1 filtering |
| **Ignore frontmatter** | Miss relevant files | Always scan YAML first |
| **Skip exchange IDs** | Can't target specific content | Add IDs when creating files |
| **Load chronologically** | Old context may be stale | Load by relevance, not time |
| **No verification** | Missing key context | Check loaded exchanges cover the need |
| **Missing history** | The conversation history is empty | Check the timestamp of the first exchange in the conversation |

## Quick Reference

**Preliminary chat prompt:**
```
I need to recover context for: [current request]

Available conversation files: [list]

For each file, read only the YAML frontmatter.
Identify which files and exchanges are relevant.
Output a recovery plan with specific exchange IDs.
```

**Main chat prompt:**
```
Load the following exchanges for context:
- file: [path], exchanges: [exchange-001, exchange-005]

After loading, confirm:
1. Are the loaded exchanges sufficient?
2. Is there any missing context needed?
3. Can we proceed with the current request?
```

**Creating exchange IDs:**
```yaml
## Exchange N: Title
**Exchange ID:** exchange-NNN  # Sequential numbering
**Relevance Tags:** [topic1, topic2]  # From standard tag set
**Load Priority:** conditional  # always|conditional|optional
```

## Reference Files

- `conversation-manager/references/GENERATION_PROMPT.md` — Instructions for archiving/summarizing a conversation
- `conversation-manager/references/TEMPLATE.md` — Standardized conversation format
- `references/20260329.0143-central-workspace-assembly.md` — Example with exchange IDs

---

**Remember:** Context is expensive. Load only what you need, verify what you loaded, and proceed efficiently.
