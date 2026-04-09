---
skill: autoresearch-agent
version: "1.0.0"
---

# Vetting Record: Autoresearch Agent

## Source

- **Repository**: alirezarezvani-claude-skills
- **Repository URL**: https://github.com/alirezarezvani/claude-skills
- **Path**: `engineering/autoresearch-agent/`
- **Author**: Alireza Rezvani
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring autonomous research

## Rationale

Autonomous research agent for gathering and synthesizing information from multiple sources. Implements experimental optimization loop (edit → evaluate → commit/reset → repeat).

## Dependencies

- Git repository for experimental tracking
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
| File system access | ✅ CLEAR | Git operations only (documented) |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns.

## Installation

```bash
cp -r autoresearch-agent/ ~/.claude/skills/           # Claude Code
cp -r autoresearch-agent/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from alirezarezvani-claude-skills
- Part of the agent-skills central repository
- Requires git repository for experiment tracking

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: Low
