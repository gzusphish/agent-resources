# Vetting Notes: insecure-defaults

## Source
- **Repository:** trailofbits-skills
- **Path:** `plugins/insecure-defaults/skills/insecure-defaults/`
- **Author:** Trail of Bits
- **License:** MIT

## Vetting Date
2026-03-31

## Purpose
Security audit skill for detecting insecure default configurations

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
cp -r insecure-defaults/ ~/.claude/skills/           # Claude Code
cp -r insecure-defaults/ .windsurf/skills/          # Windsurf
```

## Notes
- Inducted from trailofbits-skills
- Part of the agent-skills central repository
