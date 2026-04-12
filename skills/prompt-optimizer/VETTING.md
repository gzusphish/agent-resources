---
skill: prompt-optimizer
version: "1.0.0"
---

# Vetting Record: Prompt Optimizer

## Source

- **Repository**: Panopticon (original work)
- **Author**: Cascade AI Assistant
- **Created**: 2026-04-01
- **License**: MIT license

## Vetting Date

2026-04-01

## Approved For

✅ **APPROVED** - All projects requiring prompt improvement

## Rationale

Systematic prompt optimization improves tool and LLM outputs. Patterns derived from actual usage failures.

## Dependencies

- None
- No external API calls

## Testing Status

- [x] Skill validated
- [x] Platform compatibility: Verified for Claude Code, Windsurf, Copilot

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
cp -r skills/prompt-optimizer/ ~/.claude/skills/           # Claude Code
cp -r skills/prompt-optimizer/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-01 | agent-resources/skills/ | initial | 1.0.0 | Baseline |

## Notes

- Pattern library established with common failure modes
- Iterative improvement expected as new patterns emerge
- Focuses on specificity, context provision, and output format guidance

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-01  
**Risk Level**: None (documentation-only)
