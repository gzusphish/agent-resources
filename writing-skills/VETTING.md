---
skill: writing-skills
version: "1.0.0"
---

# Vetting Record: Writing Skills

## Source

- **Repository**: obra/superpowers
- **Repository URL**: https://github.com/obra/superpowers
- **Path**: `skills/writing-skills/SKILL.md`
- **Author**: Jesse Vincent
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects creating AI skills

## Rationale

TDD approach to skill creation is essential quality control. The RED-GREEN-REFACTOR methodology maps perfectly to documentation. This skill improves the quality of all other skills.

## Dependencies

- Requires `test-driven-development` skill (referenced as background)
- No external API calls

## Testing Status

- [x] Methodology reviewed
- [x] Sample scenarios analyzed
- [x] Platform compatibility: Verified for Claude Code, Windsurf

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | Documentation only |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Documentation-only skill.

## Installation

```bash
cp -r writing-skills/ ~/.claude/skills/           # Claude Code
cp -r writing-skills/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- Heavy reference to `testing-skills-with-subagents.md` in source
- Consider copying supporting references for intensive skill development
- Token efficiency guidelines valuable for context management

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (documentation-only)
