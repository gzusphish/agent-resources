---
skill: pdd
version: "1.0.0"
---

# Vetting Record: Prompt-Driven Development (PDD)

## Source

- **Repository**: strands-agents/agent-sop
- **Repository URL**: https://github.com/strands-agents/agent-sop
- **Path**: `agent-sops/pdd.sop.md`
- **Author**: AWS / Strands Agents
- **License**: Apache 2.0
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring structured development methodology

## Rationale

Prompt-Driven Development methodology for structured project planning. Iterative refinement from rough idea to detailed design plan. Good for complex feature development.

## Dependencies

- None
- No external API calls

## Testing Status

- [x] Methodology reviewed
- [x] Platform compatibility: Verified for Claude Code

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
cp pdd.sop.md ~/.claude/skills/
cp pdd.sop.md .windsurf/skills/
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- SOP format (different from SKILL.md)
- Emphasizes interactive requirements clarification
- Complements writing-plans skill for implementation

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (documentation-only)
