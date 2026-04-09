---
skill: senior-data-scientist
version: "1.0.0"
---

# Vetting Record: Senior Data Scientist

## Source

- **Repository**: alirezarezvani-claude-skills
- **Repository URL**: https://github.com/alirezarezvani/claude-skills
- **Path**: `engineering-team/senior-data-scientist/`
- **Author**: Alireza Rezvani
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All data science projects

## Rationale

World-class senior data scientist skill specializing in statistical modeling, experiment design, causal inference, and predictive analytics.

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
| File system access | ✅ CLEAR | Documentation only |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Documentation-only skill.

## Installation

```bash
cp -r senior-data-scientist/ ~/.claude/skills/           # Claude Code
cp -r senior-data-scientist/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from alirezarezvani-claude-skills
- Part of the agent-skills central repository
- Covers A/B testing, cross-validation, SHAP, MLflow

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (documentation-only)
