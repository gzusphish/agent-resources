---
skill: conversation-manager
version: 1.0.1
---

# Vetting Record: Conversation Manager

## Source

- **Repository**: Panopticon Skill Manager (original work)
- **Author**: Cascade AI Assistant
- **Created**: 2026-04-07
- **License**: MIT license

## Vetting Date

2026-04-07

## Approved For

✅ **APPROVED** - All projects with conversation history management

## Rationale

Addresses context overflow problem in long-running conversations. Two-stage loading (filter → recover) enables working with conversation histories of arbitrary length without hitting context limits. Complements existing conversation infrastructure (TEMPLATE.md, GENERATION_PROMPT.md).

## Dependencies

- Relies on conversation files following standardized format (YAML frontmatter, exchange IDs)
- Integrates with `conversation-manager` skill ecosystem
- No external API calls

## Testing Status

- [x] Skill validated
- [x] Platform compatibility: Verified for Claude Code, Windsurf, Copilot

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | Read-only access to conversation files |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Read-only skill.

## Installation

```bash
cp -r skills/conversation-manager/ ~/.claude/skills/           # Claude Code
cp -r skills/conversation-manager/ .windsurf/skills/          # Windsurf
cp -r skills/conversation-manager/ .github/skills/          # GitHub Copilot
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-07 | final/skills/ | initial | 1.0.0 | Baseline |

## Notes

- Implements two-stage loading: preliminary filter → targeted recovery
- Designed for conversations with 10-100+ exchanges
- Prevents context overflow by loading 5-15 relevant exchanges instead of entire history
- Requires conversation files to have exchange IDs (exchange-NNN format)
- Includes 3 implementation patterns for common use cases

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-07  
**Risk Level**: None (read-only)
