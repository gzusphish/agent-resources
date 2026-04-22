# Prompt: Generate/Refresh Conversation History

Use this prompt at the end of a conversation to create or update a conversation history file.

---

## Instructions

Summarize this conversation into a structured markdown file optimized for agent context recovery.

**CRITICAL:** Use the timestamp of the first exchange in the conversation, NOT the current date when generating the summary.

**Output location:** Resolved scriptorium folder

Resolve the scriptorium folder in this order:
- Prefer `.panopticon/scriptorium/` if it exists and is accessible
- Otherwise use `scriptorium/` in the current workspace (create it if missing)

**Filename:** `YYYYMMDD.HHMM-[descriptive-name].md`

- `YYYYMMDD.HHMM` = Timestamp of the FIRST exchange in the conversation
- NOT the current date when creating this file
- Example: If first exchange happened March 29, 2026 at 01:43 → filename is `20260329.0143-*.md` even if generating on April 7

---

## Required Structure

Follow `conversation-manager/references/TEMPLATE.md` for the canonical structure.

Additional structural requirements:
- Include `exchange-000` as the first exchange and mark it `always`
- Use sequential IDs for the remaining exchanges (`exchange-001`, `exchange-002`, ...)
- Include the summary sections from the template (Key Decisions, Deliverables Created, Statistics, Key Learnings, Related Conversations)

### Special Exchange: exchange-000 (Final State Summary)

Create `exchange-000` as the first exchange.

Include:
- Current state snapshot (what exists now)
- Open tasks / next steps
- Key decisions (brief)
- Any important constraints (paths, environment assumptions)

---

## Content Guidelines

### Do Include

- ✅ Direct user quotes (exact or nearly exact)
- ✅ Concrete file paths and locations
- ✅ Specific skill names and tool references
- ✅ Decisions made and their rationale
- ✅ Quantified outcomes (counts, metrics)
- ✅ Tags for filtering (e.g., "skill-management", "security", "refactoring")
- ✅ Specific skill names and tool references
- ✅ Decisions made and their rationale
- ✅ Quantified outcomes (counts, metrics)
- ✅ Tags for filtering (e.g., "skill-management", "security", "refactoring")

### Do Not Include

- ❌ Raw API call logs or technical minutia
- ❌ Full code blocks (reference paths instead)
- ❌ Transient errors that were resolved
- ❌ Obvious pleasantries ("Good idea!", "You're welcome")
- ❌ Information already in standard documentation

### Exchange Priority Guidelines

- **always** — Critical context for understanding this conversation
- **conditional** — Relevant if working on specific sub-topic
- **optional** — Background, exploratory, or superseded content

---

## Two-Stage Loading Pattern

For long conversations, enable selective loading:

```markdown
**Usage Notes for Agents:**
- Load this file when working on: [topic tags]
- Quick context: Read frontmatter + Key Decisions only
- Full context: Load exchanges: [exchange-ids]
- Deep context: Load all exchanges
```

---

## Refreshing Existing Files

When updating an existing conversation file:

1. **Preserve structure** — Maintain existing exchange IDs
2. **Add new exchanges** — Append with new IDs
3. **Update metadata** — Refresh statistics, duration
4. **Mark amendments** — If modifying past exchanges:

   ```markdown
   **Note:** Exchange updated on [date] - [reason]
   ```

5. **Update related conversations** — Link to newer follow-ups

---

## Example Output

See: `references/20260329.0143-central-workspace-assembly.md` (good example, though lacks YAML frontmatter)

See: `references/20260407.2048-conversation-history-management.md` (complete example with all sections)

---

## Quick Checklist

- [ ] YAML frontmatter complete with topics/keywords
- [ ] Each exchange has unique ID
- [ ] User quotes are direct or clearly summarized
- [ ] File paths are absolute or clearly relative
- [ ] Key Decisions table captures rationale
- [ ] Statistics are quantified (not vague)
- [ ] Key Learnings are actionable insights
- [ ] Usage Notes guide selective loading

---

**Remember:** The goal is enabling future agents (or yourself) to quickly recover relevant context without reading entire conversations. Structure for scanability, tag for filterability, summarize for comprehension.
