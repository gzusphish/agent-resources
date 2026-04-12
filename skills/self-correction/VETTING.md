---
skill: self-correction
version: "1.0.0"
---

# Vetting Record: Self-Correction

## Source

- **Repository**: Panopticon (original work)
- **Author**: Cascade AI Assistant
- **Created**: 2026-04-03
- **License**: MIT license
- **Literature Source**: Lilian Weng "LLM Powered Autonomous Agents" — Planning: Reflection and Refinement component

## Vetting Date

2026-04-03

## Approved For

✅ **APPROVED** - All projects requiring mid-task reflection

## Rationale

Mid-task reflection prevents wasted effort on wrong paths. Literature identifies this as a core agent capability distinct from post-task learning. The 4-question Quick Check provides structure without overhead.

## Provenance

### Borrowed Concepts

**From Lilian Weng "LLM Powered Autonomous Agents":**
- "Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps"
- In-process feedback loop (distinct from post-task reflection)
- Self-criticism as a core agent capability alongside planning

**Implementation Differences from Literature:**
- Made trigger-based rather than continuous (literature implies continuous reflection)
- Added explicit pivot decisions (CONTINUE/ADAPT/ESCALATE/ABANDON)
- Constrained to 30-60 second checkpoint (practical time limit for mid-task use)

## Dependencies

- None (pure reasoning skill)
- No external API calls

## Integration Points

- **Feeds decisions to:** execution flow in planning, debugging, decomposition skills
- **Triggered by:** effort thresholds (3+ calls without value), stuck detection, irreversible actions
- **Complements:** `reflection` (post-task learning), `subgoal-decomposer` (re-decomposition when needed)

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
cp -r skills/self-correction/ ~/.claude/skills/           # Claude Code
cp -r skills/self-correction/ .windsurf/skills/          # Windsurf
cp -r skills/self-correction/ ~/.github/copilot/skills/  # Copilot
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-03 | agent-resources/skills/ | initial | 1.0.0 | Baseline |
| 2026-04-03 | .windsurf/skills/ | install | 1.0.0 | Current |

## Notes

- Version 1.0 uses trigger-based activation (manual and automatic)
- Future enhancement: Automatic trigger detection (effort tracking, progress metrics)
- Future enhancement: Integration with persistent state for checkpoint history

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-03  
**Risk Level**: None (pure reasoning)
