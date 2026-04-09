---
skill: subgoal-decomposer
version: "1.0.0"
---

# Vetting Record: Subgoal Decomposer

## Source

- **Repository**: Panopticon (original work)
- **Author**: Cascade AI Assistant
- **Created**: 2026-04-03
- **License**: MIT license
- **Literature Source**: Anthropic "Building Effective Agents" + Lilian Weng "LLM Powered Autonomous Agents"

## Vetting Date

2026-04-03

## Approved For

✅ **APPROVED** - All projects requiring task decomposition

## Rationale

Systematic decomposition enables better planning and reveals parallelization opportunities. Work-backward method is more reliable than forward planning (less likely to miss critical prerequisites).

## Provenance

### Borrowed Concepts

**From Anthropic "Building Effective Agents":**
- Work backward from goal decomposition method
- Dependency mapping approach (sequential vs parallel identification)
- Parallel opportunity flagging
- Atomic action definition (single tool call granularity)

**From Lilian Weng "LLM Powered Autonomous Agents":**
- Planning → subgoal decomposition as core agent capability
- Reflection and refinement concept (referenced but not directly implemented)
- Estimation and verification at each decomposition level

**From `agent-resources/github-awesome-copilot/skills/breakdown-plan/SKILL.md` (NOT inducted):**
- Hierarchical decomposition structure (Epic→Feature→Story→Task inspired the Level 1/2 hierarchy)
- Dependency graph visualization pattern
- Estimation concepts (though simplified from story points to Small/Medium/Large)

This skill is NOT the same as `breakdown-plan` — that skill is GitHub/Agile-specific (510 lines) with Epic/Feature/Story templates for GitHub Issues. This skill is a lightweight, general-purpose decomposition tool that can feed into any planning system.

## Dependencies

- None (pure reasoning skill)
- No external API calls

## Integration Points

- **Feeds into:** `writing-plans` (detailed implementation), `pdd` (project lifecycle), `workflow-orchestrator` (state design)
- **Complements:** `reflection` (post-task learning), `audit-context-building` (context gathering)

## Testing Status

- [x] Skill validated: Initial version — requires real-world testing
- [x] Platform compatibility: Universal (no platform-specific features)

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | None |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Pure reasoning skill.

## Installation

```bash
cp -r subgoal-decomposer/ ~/.claude/skills/           # Claude Code
cp -r subgoal-decomposer/ .windsurf/skills/          # Windsurf
cp -r subgoal-decomposer/ ~/.github/copilot/skills/  # Copilot
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-03 | agent-skills-vetted/ | initial | 1.0.0 | Baseline |
| 2026-04-03 | .windsurf/skills/ | install | 1.0.0 | Current |

## Notes

- Version 1.0 focuses on the core work-backward algorithm
- Future enhancement: Integration with `reflection` for iterative refinement during execution
- Future enhancement: Dependency graph visualization improvements

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-03  
**Risk Level**: None (pure reasoning)
