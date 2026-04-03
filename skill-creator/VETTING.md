# Vetting Notes: skill-creator

## Source
- **Repository:** anthropic-skills
- **Repository URL:** https://github.com/anthropics/skills
- **Path:** `skills/skill-creator/`
- **Author:** Anthropic
- **License:** MIT
- **Vetted Commit:** `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date
2026-03-31

## Purpose
Create effective AI skills with proper structure and metadata

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
cp -r skill-creator/ ~/.claude/skills/           # Claude Code
cp -r skill-creator/ .windsurf/skills/          # Windsurf
```

## Notes
- Inducted from anthropic-skills
- Part of the agent-skills central repository
