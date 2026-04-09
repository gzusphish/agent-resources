# Vetting Notes: prompt-optimizer

## Source
- **Repository:** Panopticon (original work)
- **Author:** Cascade AI Assistant
- **Created:** 2026-04-01

## Vetting Date
2026-04-01

## Approved For
- **All projects** - prompt improvement and optimization

## Rationale
Systematic prompt optimization improves tool and LLM outputs. Patterns derived from actual usage failures.

## Dependencies
- None

## Testing Status
- **Skill validated:** Yes
- **Platform compatibility:** Verified for Claude Code, Windsurf, Copilot

## Security Assessment
- **External API calls:** None
- **File system operations:** None (documentation only)
- **Code execution:** None
- **Risk level:** None

## Notes
- Pattern library established with common failure modes
- Iterative improvement expected as new patterns emerge
- Focuses on specificity, context provision, and output format guidance

## Installation
```bash
cp -r prompt-optimizer/ ~/.claude/skills/           # Claude Code
cp -r prompt-optimizer/ .windsurf/skills/          # Windsurf
```
