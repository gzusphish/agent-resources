# Vetting Notes: git-worktree-manager

## Source
- **Repository:** alirezarezvani-claude-skills
- **Repository URL:** https://github.com/alirezarezvani/claude-skills
- **Path:** `engineering/git-worktree-manager/`
- **Author:** Alireza Rezvani
- **License:** MIT
- **Vetted Commit:** `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date
2026-03-31

## Purpose
Manage multiple Git worktrees for parallel development

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
cp -r git-worktree-manager/ ~/.claude/skills/           # Claude Code
cp -r git-worktree-manager/ .windsurf/skills/          # Windsurf
```

## Notes
- Inducted from alirezarezvani-claude-skills
- Part of the agent-skills central repository
