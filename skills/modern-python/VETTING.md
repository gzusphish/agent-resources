---
skill: modern-python
version: "1.0.0"
---

# Vetting Record: Modern Python

## Source

- **Repository**: trailofbits-skills
- **Repository URL**: https://github.com/trailofbits/skills
- **Path**: `plugins/modern-python/skills/modern-python/`
- **Author**: Trail of Bits
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All Python projects

## Rationale

Modern Python development patterns and best practices. Configures projects with modern tooling (uv, ruff, ty). Based on trailofbits/cookiecutter-python.

## Dependencies

- Python
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
| File system access | ✅ CLEAR | File operations documented |
| External dependencies | ✅ CLEAR | Python only |

**Verdict**: No security concerns.

## Installation

```bash
cp -r skills/modern-python/ ~/.claude/skills/           # Claude Code
cp -r skills/modern-python/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-resources/skills/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from trailofbits-skills
- Part of the agent-resources/skills central repository
- Modern tooling: uv, ruff, ty

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: Low
