---
name: skill-inductor
description: "Use when discovering new skills from external sources, evaluating external skills for adoption, or ingesting approved skills into the unified agent-skills/ repository. Guides the ingestion workflow from discovery through vetting. Does NOT handle IDE installation - use skill-installer for that."
---

# Skill Inductor

Ingest skills from external sources into central repositories.

## Scope Clarification

**This skill handles:**
- Discovering skills from **external** sources (GitHub, documentation, community)
- Vetting skills for security and quality
- Placing vetted skills into `agent-skills/` (unified repository)
- Managing the skill catalog and metadata

**This skill does NOT handle:**
- Installing skills to IDE contexts (see `skill-installer`)
- Deploying skills to project directories (see `skill-installer`)
- Managing IDE-specific paths or configurations

The workflow boundary: **External sources → Central repositories** (not to IDE contexts)

## When To Use

- **Discovering skills** from external repositories, documentation, or community sources
- **Evaluating skills** before adoption — security, quality, fit assessment
- **Ingesting approved skills** into `agent-skills/` (unified repository)
- **Updating existing skills** in central repositories when new versions become available
- **Auditing skills** in central repositories for security or relevance

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
Use standardized format (see `skill-vetter/VETTING.md` as canonical template):
- Source attribution (repo, author, license)
- Repository URL (for vetted external skills)
- Vetted Commit hash (pins exact state)
- Vetting date
- Approval scope
- Rationale for adoption
- Dependencies
- Security assessment
- Testing status
- Installation commands
- Installation Log (for tracking drift)

**Custom/original skills:** Use `skill-vetter/VETTING.md` structure but omit Repository URL and Vetted Commit fields.

**Verdict:**
- **PASS** → Proceed to Install
- **WARN** → Document risks, conditional approval
- **FAIL** → Do not install, document why

### 3. Ingest

Copy approved skill to central repository (NOT to IDE contexts).

```bash
# Copy to unified agent-skills/ repository
cp -r /path/to/vetted/skill/ agent-skills/

# Create VETTING.md if not present (use skill-vetter template)
# Note: VETTING.md source_type field differentiates custom vs vetted
# Update README catalog
```

**Post-ingest verification:**
- [ ] SKILL.md loads without parsing errors
- [ ] References exist (check all linked files)
- [ ] Scripts are executable (if applicable)
- [ ] VETTING.md present with standardized format
- [ ] Catalog entry created/updated

**This is NOT installation.** The skill is now in central storage, ready for `skill-installer` to deploy to IDE contexts.

### 4. Handoff to Installation

Once skill is ingested to central repository, deployment to IDE contexts is handled by `skill-installer`.

**Next step (if needed):**
```bash
# Deploy to specific IDE context
# See skill-installer/SKILL.md for:
# - IDE-specific paths (.windsurf/, .claude/, .github/)
# - Copy vs symlink decisions
# - Multi-IDE deployment
# - Update and rollback workflows
```

**When to handoff:**
- User wants skill available in a specific project → `skill-installer`
- User wants skill in global IDE context → `skill-installer`
- Updating skill in IDE contexts → `skill-installer`
- Rolling back IDE installation → `skill-installer`

**What stays in central repo only:**
- Skills being cataloged but not yet deployed
- Skills vetted for specific use cases only
- Skills awaiting further modification (skill-repurposer)

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

## Integration with Skill Management Ecosystem

```
External Sources (GitHub, docs, community)
    ↓
skill-inductor (THIS SKILL: discover → vet → ingest to central repo)
    ↓
CENTRAL REPO: agent-skills/ (unified)
    ↓
skill-installer (deploy to IDE contexts: .windsurf/, .claude/, etc.)
    ↓
IDE contexts and projects
```

**Helper skills by phase:**

| Phase | Helper Skill | Usage |
|-------|--------------|-------|
| **Discover/Vet** | `skill-vetter` | Security audit, dependency scanning |
| **Discover/Vet** | `skill-security-auditor` | Static analysis |
| **Create** | `skill-creator` | If modifying before ingestion |
| **Create** | `skill-repurposer` | If adapting external skill |
| **Create** | `writing-skills` | TDD approach to skill documentation |
| **Validate** | `skill-auditor` | Quality/consistency before ingestion |
| **Deploy** | `skill-installer` | Installation to IDE contexts (NOT this skill) |

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
4. Copy to agent-skills/
5. Update README catalog
6. STOP - Ingestion complete

If deployment to IDE needed:
7. Use skill-installer to deploy to .windsurf/, .claude/, etc.
```

**Self-inducted skill:**
```
1. Use skill-creator or writing-skills methodology
2. Self-vet with skill-vetter
3. Create VETTING.md (self-attested)
4. Copy to agent-skills-custom/
5. STOP - Ingestion complete

If deployment to IDE needed:
6. Use skill-installer to deploy
```

**Skill update:**
```
1. Check source for changes
2. Re-run full vetting
3. Review diff
4. Replace in agent-skills/
5. Re-deploy to all projects
```

## Reference Files

- `skill-installer/SKILL.md` — Deploy skills to IDE contexts
- `skill-vetter/SKILL.md` — Security audit procedures
- `skill-vetter/VETTING.md` — Template for vetting documentation
- `skill-auditor/SKILL.md` — Quality validation before ingestion
- `writing-skills/SKILL.md` — TDD approach to skill creation
- `skill-repurposer/SKILL.md` — Adapting external skills
- `../agent-resources/README.md` — External skill staging area

## Storage Conventions

| Location | Purpose |
|----------|---------|
| `../agent-resources/` | Staging area for unvetted external skills |
| `agent-skills/` | Unified repository (all skills, differentiated by VETTING.md source_type) |
| `skill-installer` | Deploys from central repos to IDE contexts |

---

**Remember:** Trust but verify. Every inducted skill becomes part of your agent's decision-making apparatus.
