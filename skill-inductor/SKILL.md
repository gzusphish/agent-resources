---
name: skill-inductor
description: Use when discovering new skills, evaluating external skills for adoption, or integrating approved skills into projects. Guides the complete skill induction workflow from discovery through vetting to installation.
---

# Skill Inductor

Complete workflow for bringing new skills into your agent ecosystem.

## When To Use

- **Discovering skills** from external repositories, documentation, or community sources
- **Evaluating skills** before adoption — security, quality, fit assessment
- **Integrating skills** into specific projects after vetting
- **Updating existing skills** when new versions become available
- **Auditing installed skills** for security or relevance

## Core Workflow

### 1. Discover

Find candidate skills and capture initial metadata.

**Sources to check:**
- `../agent-resources/` — cloned external skill repositories
- Community sources: GitHub, agent skill registries, documentation
- Self-identified needs from task friction

**Capture for each candidate:**
```yaml
skill_candidate:
  name: 
  source_repo: 
  source_path:
  discovered_date:
  trigger_reason: [what problem does this solve?]
  initial_assessment: [quick scan of quality/scope]
```

**Store in:** `../agent-resources/skill-candidates.md`

### 2. Vet (Security & Quality Gate)

**REQUIRED:** Run security audit before any installation.

```bash
# Comprehensive vetting
python agent-skills/skill-vetter/scripts/vett.py /path/to/skill/ --strict

# JSON output for tracking
python agent-skills/skill-vetter/scripts/vett.py /path/to/skill/ --json >> vetting-log.jsonl
```

**Manual review checklist:**
- [ ] **Functionality**: Skill does what it claims
- [ ] **Security**: No malicious patterns, justified API calls only
- [ ] **Portability**: Works across Claude Code, Windsurf, Copilot
- [ ] **Maintainability**: Clear structure, reasonable scope (<150 lines for SKILL.md)
- [ ] **Dependencies**: Documented, minimal, justified

**Create VETTING.md:**
Use standardized format (see `agent-skills/skill-vetter/VETTING.md` template):
- Source attribution (repo, author, license)
- Vetting date
- Approval scope
- Rationale for adoption
- Security assessment
- Installation commands

**Verdict:**
- **PASS** → Proceed to Install
- **WARN** → Document risks, conditional approval
- **FAIL** → Do not install, document why

### 3. Install

Copy approved skill to central repository.

```bash
# To agent-skills-custom (central repository)
cp -r /path/to/vetted/skill/ agent-skills-custom/

# Create VETTING.md if not present (use skill-vetter template)
# Update README catalog (see Integration below)
```

**Post-install verification:**
- [ ] SKILL.md loads without parsing errors
- [ ] References exist (check all linked files)
- [ ] Scripts are executable (if applicable)
- [ ] Integration test: skill triggers appropriately

### 4. Deploy to Projects

Distribute to specific project skill directories.

```bash
# Example: Deploy to Panopticon
cp -r agent-skills-custom/skill-name/ .panopticon/.windsurf/skills/

# Example: Deploy to GTD project
cp -r agent-skills-custom/skill-name/ gtd/.github/skills/
cp -r agent-skills-custom/skill-name/ gtd/.windsurf/skills/
```

**Update project context:**
- Add to project's skill index if maintained
- Document in project-specific AGENTS.md if relevant

### 5. Monitor & Update

**Periodic review triggers:**
- Quarterly: Re-vet all installed skills
- On update: New commits to source repo
- On drift: Skill behavior seems off
- On deploy to Panopticon: Review dependencies and security

**Update workflow:**
1. Check source for updates
2. Re-run vetting (especially `--strict` mode)
3. Review diff before replacing
4. Re-deploy to all projects using the skill

## Integration with Existing Skills

| Phase | Helper Skill | Usage |
|-------|--------------|-------|
| **Vet** | `skill-vetter` | Security audit, dependency scanning |
| **Vet** | `skill-security-auditor` | Static analysis for malicious patterns |
| **Create** | `skill-creator` | If modifying/improving before induction |
| **Create** | `writing-skills` | TDD approach to skill documentation |
| **Document** | `codebase-summary` | Generate skill documentation from analysis |

## Quality Gates

**Before vetting approval:**
- MUST have SKILL.md with proper frontmatter
- MUST have verifiable source (git repo preferred)
- MUST pass `skill-vetter` with no FAIL items

**Before installation:**
- MUST have VETTING.md in standardized format
- MUST have README catalog entry (if central repo)
- MUST have tested integration

**Before deployment:**
- MUST verify target project skill directory structure
- MUST confirm no naming conflicts
- SHOULD announce to project context

## Anti-Patterns to Avoid

| Don't | Why |
|-------|-----|
| Install without vetting | Security risk, quality unknown |
| Skip VETTING.md creation | Loses audit trail, unclear approval status |
| Batch-install multiple skills | Harder to isolate issues, rollback complications |
| Install from unverified sources | Malicious code risk |
| Keep stale skills without review | Bitrot, security vulnerabilities |

## Quick Reference

**New skill from external source:**
```
1. Clone to ../agent-resources/
2. Run skill-vetter --strict
3. Create VETTING.md
4. Copy to agent-skills-custom/
5. Update README catalog
6. Deploy to target projects
```

**Self-inducted skill:**
```
1. Use skill-creator or writing-skills methodology
2. Self-vet with skill-vetter
3. Create VETTING.md (self-attested)
4. Follow standard install/deploy
```

**Skill update:**
```
1. Check source for changes
2. Re-run full vetting
3. Review diff
4. Replace in agent-skills-custom/
5. Re-deploy to all projects
```

## Reference Files

- `skill-vetter/SKILL.md` — Security audit procedures
- `skill-vetter/VETTING.md` — Template for vetting documentation
- `writing-skills/SKILL.md` — TDD approach to skill creation
- `../agent-resources/README.md` — External skill staging area

## Storage Conventions

| Location | Purpose |
|----------|---------|
| `../agent-resources/` | Staging area for unvetted external skills |
| `agent-skills-vetted/` | Central vetted skill repository |
| `<project>/.windsurf/skills/` | Windsurf project skills |
| `<project>/.agent/skills/` | Generic project skills |
| `~/.claude/skills/` | Claude Code global skills |

---

**Remember:** Trust but verify. Every inducted skill becomes part of your agent's decision-making apparatus.
