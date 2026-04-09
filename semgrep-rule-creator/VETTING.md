---
skill: semgrep-rule-creator
version: "1.0.0"
---

# Vetting Record: Semgrep Rule Creator

## Source

- **Repository**: trailofbits-skills
- **Repository URL**: https://github.com/trailofbits/skills
- **Path**: `plugins/semgrep-rule-creator/skills/semgrep-rule-creator/`
- **Author**: Trail of Bits
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring custom static analysis

## Rationale

Create and manage Semgrep security scanning rules for detecting security vulnerabilities, bug patterns, and code patterns.

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
| File system access | ✅ CLEAR | Rule file creation |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns.

## Installation

```bash
cp -r semgrep-rule-creator/ ~/.claude/skills/           # Claude Code
cp -r semgrep-rule-creator/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from trailofbits-skills
- Part of the agent-skills central repository
- For custom static analysis rule creation

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: Low
