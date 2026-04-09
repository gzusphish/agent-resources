---
skill: validation-frameworks
version: "1.0.0"
---

# Vetting Record: Validation Frameworks

## Source

- **Repository**: slgoodrich-agents
- **Repository URL**: https://github.com/slgoodrich/agents
- **Path**: `plugins/ai-pm-copilot/skills/validation-frameworks/`
- **Author**: Sam Goodrich
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring validation frameworks

## Rationale

Create and apply validation frameworks for problem and solution validation, assumption testing, and MVP validation experiments.

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
cp -r validation-frameworks/ ~/.claude/skills/           # Claude Code
cp -r validation-frameworks/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from slgoodrich-agents
- Part of the agent-skills central repository
- For problem/solution validation and MVP experiments

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (documentation-only)
