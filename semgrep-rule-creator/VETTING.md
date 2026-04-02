# Vetting Notes: semgrep-rule-creator

## Source
- **Repository:** trailofbits-skills
- **Path:** `plugins/semgrep-rule-creator/skills/semgrep-rule-creator/`
- **Author:** Trail of Bits
- **License:** MIT

## Vetting Date
2026-03-31

## Purpose
Create and manage Semgrep security scanning rules

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
cp -r semgrep-rule-creator/ ~/.claude/skills/           # Claude Code
cp -r semgrep-rule-creator/ .windsurf/skills/          # Windsurf
```

## Notes
- Inducted from trailofbits-skills
- Part of the agent-skills central repository
