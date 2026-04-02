# Vetting Notes: reflection

## Source
- **Repository:** Panopticon (original work)
- **Author:** Cascade AI Assistant
- **Created:** 2026-04-01

## Vetting Date
2026-04-01

## Approved For
- **All projects** - post-task analysis and improvement

## Rationale
Structured post-task reflection enables continuous improvement. Captures decision quality, tool efficiency, and failure patterns for future sessions.

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
- Initial version focused on post-task reflection
- Integration with knowledge base for pattern learning TBD
- Works best when applied consistently after complex tasks

## Installation
```bash
cp -r reflection/ ~/.claude/skills/           # Claude Code
cp -r reflection/ .windsurf/skills/          # Windsurf
```
