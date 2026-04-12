---
skill: workflow-orchestrator
version: "1.0.0"
---

# Vetting Record: Workflow Orchestrator

## Source

- **Repository**: VoltAgent-awesome-claude-code-subagents
- **Repository URL**: https://github.com/VoltAgent/awesome-claude-code-subagents
- **Path**: `categories/09-meta-orchestration/workflow-orchestrator.md`
- **Author**: VoltAgent
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects with complex workflows

## Rationale

Orchestrate complex multi-step workflows and processes. Design stateful processes, handle errors systematically, manage distributed transactions.

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
cp -r skills/workflow-orchestrator/ ~/.claude/skills/           # Claude Code
cp -r skills/workflow-orchestrator/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-resources/skills/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from VoltAgent-awesome-claude-code-subagents
- Part of the agent-resources/skills central repository
- For workflow modeling, state management, error handling

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (documentation-only)
