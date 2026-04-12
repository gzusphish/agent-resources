---
skill: insecure-defaults
version: "1.0.0"
---

# Vetting Record: Insecure Defaults

## Source

- **Repository**: trailofbits-skills
- **Repository URL**: https://github.com/trailofbits/skills
- **Path**: `plugins/insecure-defaults/skills/insecure-defaults/`
- **Author**: Trail of Bits
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring security audits

## Rationale

Security audit skill for detecting fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production.

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
| File system access | ✅ CLEAR | Read-only config analysis |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns.

## Installation

```bash
cp -r skills/insecure-defaults/ ~/.claude/skills/           # Claude Code
cp -r skills/insecure-defaults/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-resources/skills/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from trailofbits-skills
- Part of the agent-resources/skills central repository
- Detects hardcoded secrets, weak auth, permissive security configs

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: Low
