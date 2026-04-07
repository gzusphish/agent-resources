# Vetting Notes: skill-repurposer

## Source
- **Repository:** Panopticon (original work)
- **Author:** Cascade AI Assistant
- **Created:** 2026-04-06

## Vetting Date
2026-04-06

## Approved For
- **Panopticon** (primary use case)
- **All projects** adapting external skills

## Rationale
Enables systematic adaptation of skills across domains without losing quality or attribution. Complements skill-inductor by handling the common case of "this skill is close but not quite right for my context."

## Dependencies
- Uses `skill-inductor` for final induction workflow
- Uses `skill-vetter` for security validation
- References `writing-skills` for documentation quality
- No external API calls

## Testing Status
- **Skill validated:** Yes
- **Platform compatibility:** Verified for Claude Code, Windsurf, Copilot

## Security Assessment
- **External API calls:** None
- **File system operations:** Copy/modify within skill directories (documented)
- **Code execution:** None
- **Risk level:** None

## Notes
- Meta-skill for skill adaptation
- Emphasizes mandatory attribution preservation
- Includes concrete patterns for common repurposing scenarios
- Works as pre-processor to skill-inductor workflow

## Installation
```bash
cp -r skill-repurposer/ ~/.claude/skills/           # Claude Code
cp -r skill-repurposer/ .windsurf/skills/          # Windsurf
cp -r skill-repurposer/ .github/skills/          # GitHub Copilot
```
