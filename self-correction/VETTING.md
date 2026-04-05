# Vetting Notes: self-correction

## Source
- **Repository:** Created based on research synthesis
- **Author:** Cascade AI Assistant
- **Created:** 2026-04-03
- **Literature Source:** Lilian Weng "LLM Powered Autonomous Agents" — Planning: Reflection and Refinement component

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

## Vetting Date
2026-04-03

## Approved For
- **Mid-task checkpointing** — stuck detection, course correction
- **Pre-irreversible-action verification** — safety guardrail
- **Integration with execution skills** — writing-plans, subgoal-decomposer, systematic-debugging

## Rationale
Mid-task reflection prevents wasted effort on wrong paths. Literature identifies this as a core agent capability distinct from post-task learning. The 4-question Quick Check provides structure without overhead.

## Dependencies
- None (pure reasoning skill)

## Integration Points
- **Feeds decisions to:** execution flow in planning, debugging, decomposition skills
- **Triggered by:** effort thresholds (3+ calls without value), stuck detection, irreversible actions
- **Complements:** `reflection` (post-task learning), `subgoal-decomposer` (re-decomposition when needed)

## Testing Status
- **Skill validated:** Initial version — requires real-world testing
- **Platform compatibility:** Universal (no platform-specific features)

## Security Assessment
- **External API calls:** None
- **File system operations:** None
- **Code execution:** None
- **Risk level:** None

## Notes
- Version 1.0 uses trigger-based activation (manual and automatic)
- Future enhancement: Consider automatic trigger detection (effort tracking, progress metrics)
- Future enhancement: Integration with persistent state to track checkpoint history

## Installation
```bash
cp -r self-correction/ ~/.claude/skills/           # Claude Code
cp -r self-correction/ .windsurf/skills/          # Windsurf
cp -r self-correction/ ~/.github/copilot/skills/  # Copilot (if supported)
```

## Installation Log

| Date | Location | Version | Status |
|------|----------|---------|--------|
| 2026-04-03 | `.windsurf/skills/` | 1.0 | Current |

**Check for drift:** Compare installed copy against `agent-skills-vetted/self-correction/` before use.
