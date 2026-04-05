# Vetting Notes: subgoal-decomposer

## Source
- **Repository:** Created based on research synthesis
- **Author:** Cascade AI Assistant
- **Created:** 2026-04-03
- **Literature Source:** Anthropic "Building Effective Agents" + Lilian Weng "LLM Powered Autonomous Agents"

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

## Vetting Date
2026-04-03

## Approved For
- **All projects** - general task decomposition before planning
- **Pre-planning phase** - before writing-plans, pdd, or similar skills
- **Complex task analysis** - when task structure is unclear

## Rationale
Systematic decomposition enables better planning and reveals parallelization opportunities. Work-backward method is more reliable than forward planning (less likely to miss critical prerequisites).

## Dependencies
- None (pure reasoning skill)

## Integration Points
- **Feeds into:** `writing-plans` (detailed implementation), `pdd` (project lifecycle), `workflow-orchestrator` (state design)
- **Complements:** `reflection` (post-task learning), `audit-context-building` (context gathering)

## Testing Status
- **Skill validated:** Initial version — requires real-world testing
- **Platform compatibility:** Universal (no platform-specific features)

## Security Assessment
- **External API calls:** None
- **File system operations:** None
- **Code execution:** None
- **Risk level:** None

## Notes
- Version 1.0 focuses on the core work-backward algorithm
- Future enhancement: Integration with `reflection` for iterative refinement during execution
- Future enhancement: Dependency graph visualization improvements

## Installation
```bash
cp -r subgoal-decomposer/ ~/.claude/skills/           # Claude Code
cp -r subgoal-decomposer/ .windsurf/skills/          # Windsurf
cp -r subgoal-decomposer/ ~/.github/copilot/skills/  # Copilot (if supported)
```

## Installation Log

| Date | Location | Version | Status |
|------|----------|---------|--------|
| 2026-04-03 | `.windsurf/skills/` | 1.0 | Current |

**Check for drift:** Compare installed copy against `agent-skills-vetted/subgoal-decomposer/` before use.
