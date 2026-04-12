---
skill: skill-creator
version: "1.0.0"
---

# Vetting Record: Skill Creator

## Source

- **Repository**: anthropic-skills
- **Repository URL**: https://github.com/anthropics/skills
- **Path**: `skills/skill-creator/`
- **Author**: Anthropic
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects creating AI skills

## Rationale

Create effective AI skills with proper structure and metadata. Official Anthropic skill for skill development.

## Dependencies

- None
- No external API calls

## Testing Status

- [x] Skill validated
- [x] Platform compatibility: Windsurf, Claude Code

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | Skill file creation |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns.

## Installation

```bash
cp -r skills/skill-creator/ ~/.claude/skills/           # Claude Code
cp -r skills/skill-creator/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-resources/skills/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from anthropic-skills
- Part of the agent-resources/skills central repository
- Official Anthropic skill creation methodology

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: Low
