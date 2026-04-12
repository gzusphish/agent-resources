---
name: skill-installer
description: "Use when deploying skills from the central agent-resources/skills repository to IDE-specific contexts via symlinks. Handles installation, updates, rollbacks, and IDE-specific path management for Windsurf, Claude Code, GitHub Copilot, and Cursor."
---

# Skill Installer

Deploy skills from central repositories to IDE-specific contexts.

## When To Use

- **Installing skills** from `agent-resources/skills/` to a project via symlinks
- **Updating skills** in IDE contexts when central repository versions change
- **Rolling back** skill installations when issues arise
- **Uninstalling skills** from specific IDE contexts
- **Syncing skills** across multiple IDE contexts (project + global)
- **Resolving conflicts** when skill names collide

## Boundaries

**This skill does NOT:**
- Discover skills from external sources (see `skill-inductor`)
- Vet skills for security/quality (see `skill-vetter`, `skill-auditor`)
- Modify skill content or create new skills (see `skill-creator`, `skill-repurposer`)

**This skill DOES:**
- Create symlinks from `agent-resources/skills/` to IDE contexts (single source of truth)
- Handle IDE-specific directory structures and naming
- Verify installation success and skill functionality
- Manage updates and rollbacks
- Manage logging of skill installation in this environment

## Core Workflow

### 1. Select Source and Target

**Identify source skill:**
```bash
# From unified central repository
ls agent-resources/skills/skill-name/
```

**Identify target IDE context:**
```yaml
ide_context:
  type: [windsurf|claude|copilot|cursor]
  project_path: /path/to/project  # or null for global install
  skill_dir: auto-detected       # see IDE Paths below
```

**IDE-specific paths:**
| IDE | Project Skills | Global Skills |
|-----|----------------|---------------|
| Windsurf | `.windsurf/skills/` | N/A (project-only) |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| GitHub Copilot | `.github/skills/` | N/A (project-only) |
| Cursor | `.cursor/rules/` | `~/.cursor/rules/` |

### 2. Pre-Installation Check

**Verify target environment:**
- [ ] Target directory exists (create if needed)
- [ ] No naming conflict with existing skill
- [ ] Sufficient disk space
- [ ] Write permissions to target directory

**Check for conflicts:**
```bash
# Check if skill already exists
test -d target/.windsurf/skills/skill-name && echo "CONFLICT: Skill exists"

# Check for version differences
# (If exists, this is an UPDATE not an INSTALL)
```

**Decision:**
- Clean install → Proceed to step 3
- Update existing → Use UPDATE workflow (see section below)
- Conflict detected → Resolve before proceeding

### 3. Execute Installation

**Choose deployment method:**

**Method A: Symlink (default, recommended)**
```bash
# Create symlink to central repository (single source of truth)
ln -s /absolute/path/to/agent-resources/skills/skill-name target/.windsurf/skills/skill-name

# Windows Git Bash (use absolute paths with forward slashes)
ln -s "C:/Users/wyatt/git/agent-resources/skills/skill-name" "target/.windsurf/skills/skill-name"
```
- **Pros:** Always current with central repo, single source of truth, no duplication
- **Cons:** Central repo must not move (stable path required)

**Method B: Copy (fallback for special cases)**
```bash
# Simple copy - self-contained, no dependencies
cp -r agent-resources/skills/skill-name/ target/.windsurf/skills/
```
- **Pros:** Self-contained, survives source deletion, easy to modify per-project
- **Cons:** Duplicated storage, manual updates required, drift risk

**Method C: Selective install (subset deployment)**
```bash
# Install only SKILL.md for lightweight usage
mkdir -p target/.windsurf/skills/skill-name/
cp agent-resources/skills/skill-name/SKILL.md target/.windsurf/skills/skill-name/
# Note: May break if skill references external files
```

### 4. Post-Installation Verification

**Structure verification:**
- [ ] SKILL.md exists in target location
- [ ] VETTING.md present (optional but recommended)
- [ ] References directory copied if exists
- [ ] Scripts directory copied if exists

**Parse verification:**
- [ ] SKILL.md frontmatter is valid YAML
- [ ] SKILL.md renders without errors
- [ ] No broken internal references

**Functional verification (if IDE active):**
- [ ] Skill triggers appropriately for description keywords
- [ ] Skill loads without errors in IDE context

### 5. Document Installation

**Update project skill registry (if maintained):**
```markdown
# Project Skills Registry

## Installed Skills

| Skill | Source | Date | Purpose |
|-------|--------|------|---------|
| skill-name | agent-resources/skills/ | YYYY-MM-DD | Brief description |
```

**Update AGENTS.md context (if relevant):**
```markdown
## Available Skills
- `skill-name`: [description from SKILL.md]
```

## Update Workflow

**When central repository skill changes:**

1. **Detect change:**
   ```bash
   # Compare timestamps or hashes
diff -r agent-resources/skills/skill-name/ target/.windsurf/skills/skill-name/
   ```

2. **Backup current:**
   ```bash
   # Preserve working version
   mv target/.windsurf/skills/skill-name target/.windsurf/skills/skill-name.backup.$(date +%Y%m%d)
   ```

3. **Deploy update:**
   ```bash
   # Remove old symlink, create new one (for symlinks, just verify path)
   rm target/.windsurf/skills/skill-name
   ln -s "~/.git/agent-resources/skills/skill-name" "target/.windsurf/skills/skill-name"
   ```

4. **Verify and commit:**
   - Run parse verification
   - Test basic functionality
   - Remove backup if successful
   - Restore backup if failed

## Rollback Workflow

**When installed skill causes issues:**

```bash
# 1. Identify problematic skill
ls -la target/.windsurf/skills/skill-name/

# 2. Remove problematic installation
rm -rf target/.windsurf/skills/skill-name/

# 3. If backup exists, restore
if [ -d target/.windsurf/skills/skill-name.backup.* ]; then
  mv target/.windsurf/skills/skill-name.backup.* target/.windsurf/skills/skill-name/
fi

# 4. If no backup, reinstall from central repo (previous version)
# (Requires version control in central repo)
git -C ~/.git/agent-resources/ checkout <previous-commit> -- skill-name/
ln -s "~/.git/agent-resources/skills/skill-name" "target/.windsurf/skills/skill-name"
```

## Multi-IDE Deployment

**Deploy to multiple contexts simultaneously:**

```bash
SKILL=skill-name
SOURCE="agent-resources/skills/$SKILL"

# Windsurf (project)
ln -s "$SOURCE" "project/.windsurf/skills/$SKILL"

# Claude Code (project-local)
ln -s "$SOURCE" "project/.claude/skills/$SKILL"

# Claude Code (global)
ln -s "$SOURCE" "~/.claude/skills/$SKILL"

# GitHub Copilot
ln -s "$SOURCE" "project/.github/skills/$SKILL"
```

**IDE-specific considerations:**
- **Windsurf:** Requires IDE restart to pick up new skills
- **Claude Code:** Global skills available immediately; project skills on next context load
- **Copilot:** May require reloading editor window
- **Cursor:** Rules vs skills - different structure, may need adaptation

## Conflict Resolution

**Skill name collision:**

| Scenario | Resolution |
|----------|------------|
| Same skill, same version | Skip, already installed |
| Same skill, newer version | Update workflow |
| Same skill, older version | Replace with newer |
| Different skills, same name | Manual rename required |

**Resolution workflow:**
```bash
# 1. Identify both skills
ls -la agent-resources/skills/skill-a/  # source
ls -la target/.windsurf/skills/skill-a/  # existing

# 2. Compare VETTING.md dates and sources

# 3. If truly different, rename before install
mv agent-resources/skills/skill-a agent-resources/skills/skill-a-alt
ln -s "~/.git/agent-resources/skills/skill-a-alt" "target/.windsurf/skills/skill-a-alt"
```

## Integration with Skill Management Ecosystem

```
skill-inductor (ingest from external → central repo)
    ↓
skill-vetter + skill-auditor (validate)
    ↓
CENTRAL REPO: agent-resources/skills/ (unified custom + vetted)
    ↓
skill-installer (deploy to IDE contexts) ← THIS SKILL
    ↓
IDE: .windsurf/, .claude/, .github/, .cursor/
```

## Quick Reference

**Install single skill (symlink):**
```bash
ln -s "~/.git/agent-resources/skills/skill-name" "project/.windsurf/skills/skill-name"
```

**Install to multiple IDEs:**
```bash
for ide in .windsurf .claude .github; do
  ln -s "~/.git/agent-resources/skills/skill-name" "project/$ide/skills/skill-name"
done
```

**Update skill (symlinks auto-update, just verify):**
```bash
ls -la project/.windsurf/skills/skill-name
# Should show link to agent-resources/skills/skill-name
```

**Rollback skill (remove symlink, reinstall previous version):**
```bash
rm project/.windsurf/skills/skill-name
# Reinstall from git history if needed
cd ~/.git/agent-resources && git checkout <commit> -- skill-name/
ln -s "~/.git/agent-resources/skills/skill-name" "project/.windsurf/skills/skill-name"
```

## Reference Files

- `skill-inductor/SKILL.md` — Ingesting skills from external sources
- `skill-vetter/SKILL.md` — Security validation
- `skill-auditor/SKILL.md` — Quality/consistency validation
- `../agent-resources/skills/` — Unified skill repository (all skills, custom and vetted)

---

**Remember:** Installation is deployment, not creation. The skill was already vetted; now it needs to work in context.
