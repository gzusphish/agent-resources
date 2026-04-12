---
skill: skill-repurposer
version: "1.0.0"
---

# Vetting Record: Skill Repurposer

## Source

- **Repository**: Panopticon (original work)
- **Author**: Cascade AI Assistant
- **Created**: 2026-04-06
- **License**: MIT license

## Vetting Date

2026-04-06

## Approved For

✅ **APPROVED** - All projects adapting external skills

## Rationale

Enables systematic adaptation of skills across domains without losing quality or attribution. Complements skill-inductor by handling the common case of "this skill is close but not quite right for my context."

## Dependencies

- Uses `skill-inductor` for final induction workflow
- Uses `skill-vetter` for security validation
- References `writing-skills` for documentation quality
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
| File system access | ✅ CLEAR | Copy/modify within skill directories (documented) |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Documentation-only skill.

## Installation

```bash
cp -r skills/skill-repurposer/ ~/.claude/skills/           # Claude Code
cp -r skills/skill-repurposer/ .windsurf/skills/          # Windsurf
cp -r skills/skill-repurposer/ .github/skills/          # GitHub Copilot
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-06 | agent-resources/skills/ | initial | 1.0.0 | Baseline |

## Notes

- Meta-skill for skill adaptation
- Emphasizes mandatory attribution preservation
- Includes concrete patterns for common repurposing scenarios
- Works as pre-processor to skill-inductor workflow
- Added Pattern/Concept Borrowing section (2026-04-07) for partial adaptation documentation

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-06  
**Risk Level**: None (documentation-only)
