# Vetting Notes: validation-frameworks

## Source
- **Repository:** slgoodrich-agents
- **Repository URL:** https://github.com/slgoodrich/agents
- **Path:** `plugins/ai-pm-copilot/skills/validation-frameworks/`
- **Author:** Sam Goodrich
- **License:** MIT
- **Vetted Commit:** `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date
2026-03-31

## Purpose
Create and apply validation frameworks for code quality

## Approved For
- **Panopticon** (primary use case)
- **All projects** where applicable

## Testing Status
- **Skill validated:** Yes
- **Platform compatibility:** Windsurf, Claude Code

## Security Assessment
- **Risk level:** Low
- **External API calls:** None
- **File system operations:** As documented

## Installation
```bash
cp -r validation-frameworks/ ~/.claude/skills/           # Claude Code
cp -r validation-frameworks/ .windsurf/skills/          # Windsurf
```

## Notes
- Inducted from slgoodrich-agents
- Part of the agent-skills central repository
