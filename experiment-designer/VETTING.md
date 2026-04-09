---
skill: experiment-designer
version: "1.0.0"
---

# Vetting Record: Experiment Designer

## Source

- **Repository**: alirezarezvani-claude-skills
- **Repository URL**: https://github.com/alirezarezvani/claude-skills
- **Path**: `product-team/experiment-designer/`
- **Author**: Alireza Rezvani
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring experiment design

## Rationale

Structured approach to designing and documenting experiments with clear hypotheses, sample size estimation, and statistical rigor.

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
cp -r experiment-designer/ ~/.claude/skills/           # Claude Code
cp -r experiment-designer/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from alirezarezvani-claude-skills
- Part of the agent-skills central repository
- Covers A/B testing, sample sizing, statistical methods

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (documentation-only)
