---
skill: systematic-debugging
version: "1.0.0"
---

# Vetting Record: Systematic Debugging

## Source

- **Repository**: DataStage
- **Created**: 2026-04-03
- **License**: MIT license

## Vetting Date

2026-04-07 (retroactive)

## Approved For

✅ **APPROVED** - All projects requiring debugging

## Rationale

Systematic debugging methodology. ALWAYS find root cause before attempting fixes. Core principle: Symptom fixes are failure. Violating the letter of this process is violating the spirit of debugging.

## Dependencies

- None
- No external API calls

## Testing Status

- [x] Skill validated
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
cp -r skills/systematic-debugging/ ~/.claude/skills/           # Claude Code
cp -r skills/systematic-debugging/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-03 | agent-resources/skills/ | inducted | 1.0.0 | No original VETTING.md |
| 2026-04-07 | agent-resources/skills/ | vetting | 1.0.0 | Retroactive audit |

## Notes

- Inducted 2026-04-03 without security audit (process failure)
- Retroactive audit completed 2026-04-07
- Iron Law: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
- Part of the agent-resources/skills central repository

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-07  
**Risk Level**: None (documentation-only)
