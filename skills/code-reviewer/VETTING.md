---
skill: code-reviewer
version: "1.0.0"
---

# Vetting Record: Code Reviewer

## Source

- **Repository**: alirezarezvani-claude-skills
- **Repository URL**: https://github.com/alirezarezvani/claude-skills
- **Path**: `engineering-team/code-reviewer/`
- **Author**: Alireza Rezvani
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring code review

## Rationale

Systematic code review with security, performance, and maintainability checks. Supports TypeScript, JavaScript, Python, Go, Swift, Kotlin.

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
| File system access | ✅ CLEAR | Read-only code analysis |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns.

## Installation

```bash
cp -r skills/code-reviewer/ ~/.claude/skills/           # Claude Code
cp -r skills/code-reviewer/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-resources/skills/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from alirezarezvani-claude-skills
- Part of the agent-resources/skills central repository
- Multi-language support (TypeScript, JavaScript, Python, Go, Swift, Kotlin)

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: Low
