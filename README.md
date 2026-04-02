# Vetted Agent Skills

Central repository for **vetted** agent skills. Skills here have been reviewed and approved for use across projects.

## Workflow

1. **Discover** → Clone/download to `../agent-resources/`
2. **Vet** → Review, test, approve → Copy here
3. **Install** → Copy/symlink to project-specific `.agent/skills/`
4. **Update** → Edit here, re-vet, re-deploy to projects

## Catalog

### Core Skills (General Development)

| Skill | Source | Vetted For | Status |
|-------|--------|------------|--------|
| `writing-skills` | obra/superpowers | Panopticon, general dev | Ready |
| `writing-plans` | obra/superpowers | All projects | Ready |
| `codebase-summary` | strands-agents | GTD, general docs | Ready |
| `pdd` | strands-agents | GTD complex features | Ready |
| `git-workflow` | netresearch | General dev | Ready |

### Self-Inducted Skills (Meta/Process)

| Skill | Source | Vetted For | Status |
|-------|--------|------------|--------|
| `reflection` | Self-inducted | All projects | Ready |
| `prompt-optimizer` | Self-inducted | All projects | Ready |
| `error-pattern-analyzer` | Self-inducted | All projects | Ready |
| `decision-journal` | Self-inducted | All projects | Ready |
| `preference-learner` | Self-inducted | All projects | Ready |

### Specialized Skills

| Skill | Source | Vetted For | Status |
|-------|--------|------------|--------|
| `skill-creator` | microsoft/skills | Panopticon | Ready |
| `skill-vetter` | Panopticon | Panopticon | Ready |
| `skill-security-auditor` | Panopticon | All projects | Ready |
| `autoresearch-agent` | Panopticon | Panopticon | Ready |
| `modern-python` | Panopticon | Python projects | Ready |
| `senior-data-scientist` | Panopticon | Data science | Ready |
| `validation-frameworks` | Panopticon | Code quality | Ready |
| `experiment-designer` | Panopticon | Research tasks | Ready |
| `semgrep-rule-creator` | Panopticon | Security scanning | Ready |
| `knowledge-synthesizer` | Panopticon | Documentation | Ready |
| `workflow-orchestrator` | Panopticon | Task management | Ready |
| `gtd-maintainer` | Panopticon | GTD workflows | Ready |
| `performance-monitor` | Panopticon | Optimization | Ready |
| `privacy-guardian` | Panopticon | Security reviews | Ready |
| `insecure-defaults` | Panopticon | Security audits | Ready |
| `git-worktree-manager` | Panopticon | Git workflows | Ready |
| `git-cleanup` | Panopticon | Git maintenance | Ready |
| `git-bash-environment` | Panopticon | Windows dev | Ready |
| `code-reviewer` | Panopticon | Code review | Ready |
| `task-distributor` | Panopticon | Multi-agent tasks | Ready |

## Installation

```bash
# To GTD project
cp -r writing-plans/ ../gtd/.agent/skills/
cp -r codebase-summary/ ../gtd/.agent/skills/

# To Panopticon
cp -r writing-skills/ ../.panopticon/.windsurf/skills/
cp -r skill-creator/ ../.panopticon/.windsurf/skills/
```

## Vetting Standards

- **Functionality**: Skill actually works as described
- **Security**: No malicious patterns, no external API calls without justification
- **Portability**: Works across Claude Code, Windsurf, Copilot
- **Maintainability**: Clear structure, reasonable scope

See individual `VETTING.md` files in each skill folder for specific notes.
