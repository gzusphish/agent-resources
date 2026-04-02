# Vetting Notes: writing-skills

## Source
- **Repository:** obra/superpowers
- **Path:** `skills/writing-skills/SKILL.md`
- **Author:** Jesse Vincent
- **License:** MIT

## Vetting Date
2026-03-31

## Approved For
- **Panopticon development** (primary use case)
- **General skill authoring** across all projects

## Rationale
TDD approach to skill creation is essential quality control. The RED-GREEN-REFACTOR methodology maps perfectly to documentation. This skill improves the quality of all other skills.

## Dependencies
- Requires `test-driven-development` skill (referenced as background)

## Testing Status
- **Methodology reviewed:** Yes
- **Sample scenarios analyzed:** Yes
- **Platform compatibility:** Verified for Claude Code, Windsurf

## Security Assessment
- **External API calls:** None
- **File system operations:** None (documentation only)
- **Code execution:** None
- **Risk level:** None

## Notes
- Heavy reference to `testing-skills-with-subagents.md` and other support files exist in source
- Consider copying supporting references if intensive skill development is planned
- Token efficiency guidelines are particularly valuable for context management

## Installation
```bash
cp -r writing-skills/ ~/.claude/skills/           # Claude Code
cp -r writing-skills/ .windsurf/skills/          # Windsurf
```
