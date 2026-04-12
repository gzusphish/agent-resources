---
name: skill-auditor
description: Use when validating skills against project standards, checking skill metadata consistency, identifying missing required files, or performing periodic quality reviews of the skill repository.
---

# Skill Auditor

Validate skills against organizational standards and identify quality issues.

## When To Use

- **Periodic audits** — Quarterly review of all skills for compliance
- **Pre-induction validation** — Final check before adding to repository
- **Repository health checks** — Identify drift, rot, or inconsistency
- **Standard enforcement** — After updating conventions, verify compliance
- **Migration prep** — Before moving skills between repositories
- **Quality baselines** — Establish metrics for skill health

## Core Workflow

### 1. Define Audit Scope

**Target selection:**
```bash
# Single skill
skill-auditor /path/to/skill/

# Entire repository
skill-auditor agent-resources/skills/ --recursive

# Specific category (filter by VETTING.md source_type)
skill-auditor agent-resources/skills/ --filter=source_type=generated
skill-auditor agent-resources/skills/ --filter=source_type=inducted
```

**Audit dimensions (select based on need):**
- [ ] **Structure**: Required files present, correct naming
- [ ] **Metadata**: Frontmatter valid, VETTING.md complete
- [ ] **References**: Linked files exist, no broken paths
- [ ] **Standards**: Follows project conventions, consistent formatting
- [ ] **Security**: Cross-check with skill-vetter results
- [ ] **Integration**: Works with existing skill ecosystem

### 2. Run Structure Audit

**Required files check:**
```yaml
skill_structure:
  required:
    - SKILL.md        # Must exist, valid frontmatter
    - VETTING.md      # Must exist, standardized format
  optional_but_tracked:
    - references/     # If referenced in SKILL.md
    - scripts/        # If referenced in SKILL.md
    - agents/         # If using subagent patterns
    - evaluators/     # If skill-creator methodology used
    - evals/          # If skill-creator methodology used
```

**File naming conventions:**
- [ ] Skill directory: kebab-case (no underscores, no spaces)
- [ ] SKILL.md: exactly `SKILL.md` (not `skill.md`, not `Skill.md`)
- [ ] VETTING.md: exactly `VETTING.md`
- [ ] No orphaned files (not referenced anywhere)

### 3. Run Metadata Audit

**SKILL.md frontmatter validation:**
```yaml
frontmatter_requirements:
  name:
    required: true
    format: kebab-case
    max_length: 50
    pattern: "^[a-z0-9-]+$"  # No underscores, no special chars
  
  description:
    required: true
    format: "Use when..."
    max_length: 500
    must_include: triggering conditions
    must_not_include: workflow summaries  # Per writing-skills CSO
```

**VETTING.md standardization check:**
```yaml
vettingmd_requirements:
  required_sections:
    - Source          # Repository, Author, Created
    - Vetting Date    # ISO format
    - Approved For    # Scope of approval
    - Rationale       # Why this skill was approved
    - Dependencies    # What it relies on
    - Testing Status  # Validation performed
    - Security Assessment  # Risk evaluation
    - Installation    # Copy commands
  
  optional_but_recommended:
    - Notes           # Additional context
    - Limitations     # Known constraints
```

**Common VETTING.md issues:**
- Missing `Source` attribution
- Inconsistent date formats (use ISO 8601: YYYY-MM-DD)
- Missing `Rationale` section
- Generic `Testing Status` without specifics
- Security assessment lacks risk level

### 4. Run Reference Audit

**Validate all internal links:**
```bash
# Check references/ files exist
for ref in $(grep -o 'references/[a-z0-9-]*\.md' SKILL.md); do
  if [ ! -f "$ref" ]; then echo "BROKEN: $ref"; fi
done

# Check scripts/ files exist
for script in $(grep -o 'scripts/[a-z0-9_-]*' SKILL.md); do
  if [ ! -f "$script" ]; then echo "BROKEN: $script"; fi
done
```

**Cross-skill references:**
- [ ] References to other skills use skill name only (not paths)
- [ ] No `@` force-loads unless absolutely necessary
- [ ] Skill dependencies listed in VETTING.md exist in repository

### 5. Run Standards Audit

**Consistency checks:**
```yaml
standards_checks:
  line_length:
    SKILL.md: < 500 lines preferred (per writing-skills)
    VETTING.md: standardized template
  
  description_quality:
    starts_with: "Use when"
    third_person: true
    no_workflow_summary: true  # Critical: per CSO findings
  
  structure:
    has_when_to_use: true
    has_quick_reference: preferred
    has_anti_patterns: preferred
    has_integration_section: preferred
  
  formatting:
    tables_aligned: true
    code_blocks_specified: true
    no_html_except_comments: true  # For Custom Instructions sections
```

**Project-specific conventions:**
- Storage path is `agent-resources/skills/` (unified repository)
- VETTING.md uses full standardized format (not brief self-inducted version)
- GitHub Copilot support: include `.github/skills/` in installation
- Skill names are kebab-case, descriptive, action-oriented

### 6. Generate Audit Report

**Output format:**
```markdown
# Skill Audit Report: [scope]
**Date:** YYYY-MM-DD
**Auditor:** [name/tool]
**Scope:** [target skills]

## Summary
- **Total Skills:** N
- **Passed:** N (X%)
- **Warnings:** N
- **Failed:** N

## Findings by Category

### Structure Issues
| Skill | Issue | Severity | Fix |
|-------|-------|----------|-----|
| skill-name | Missing VETTING.md | High | Create from template |
| skill-name | Orphaned file: refs/old.md | Low | Remove or reference |

### Metadata Issues
| Skill | Issue | Severity | Fix |
|-------|-------|----------|-----|
| skill-name | Description too long (650 chars) | Medium | Trim to <500 |
| skill-name | Missing Rationale in VETTING.md | Medium | Add required section |

### Reference Issues
| Skill | Issue | Severity | Fix |
|-------|-------|----------|-----|
| skill-name | Broken ref: scripts/missing.py | High | Create file or remove ref |

### Standards Issues
| Skill | Issue | Severity | Fix |
|-------|-------|----------|-----|
| skill-name | SKILL.md > 600 lines | Low | Consider splitting refs |

## Action Items
- [ ] Fix high severity issues
- [ ] Address medium severity in next iteration
- [ ] Schedule follow-up audit in 3 months
```

## Integration with Skill Lifecycle

**Pre-induction gate:**
```
skill-creator / skill-repurposer
    ↓
skill-vetter (security)
    ↓
skill-auditor (quality) ← validates against project standards
    ↓
skill-inductor (install)
```

**Periodic maintenance:**
```
skill-auditor agent-resources/skills/ --recursive
    ↓
Generate report with drift metrics
    ↓
Prioritize fixes by severity
    ↓
Update skills or standards as needed
```

## Audit Checklist Templates

**Quick audit** (5 min per skill):
- [ ] SKILL.md exists with valid frontmatter
- [ ] VETTING.md exists with all required sections
- [ ] No obviously broken references
- [ ] Description follows "Use when" format

**Full audit** (15 min per skill):
- [ ] All required files present
- [ ] Frontmatter validates against schema
- [ ] VETTING.md follows standardized format exactly
- [ ] All referenced files exist
- [ ] All referenced skills exist in repository
- [ ] Line counts reasonable
- [ ] No deprecated patterns (old date formats, etc.)
- [ ] Integration section mentions related skills
- [ ] Installation commands match current conventions

## Standards Evolution

**Version tracking:**
```yaml
audit_standards_version: "2026-04-06"
key_conventions:
  vettingmd_format: "full_standardized"  # not brief
  description_format: "use_when_only"    # no workflow summaries
  storage_path: "agent-resources/skills/"   # unified repository
  date_format: "ISO_8601"                # YYYY-MM-DD
  skill_name_format: "kebab_case"        # lowercase-with-hyphens
```

**When standards change:**
1. Update skill-auditor with new rules
2. Run audit against all skills
3. Batch-fix high-severity issues
4. Schedule medium/low fixes over time
5. Document migration in standards changelog

## Anti-Patterns to Detect

| Pattern | Issue | Detection |
|---------|-------|-----------|
| **Brief VETTING.md** | Self-inducted format in custom repo | Check for missing Source/Rationale sections |
| **Missing Installation Log** | Cannot track drift between repo and installed versions | No Installation Log table in VETTING.md |
| **Workflow in description** | CSO violation | Regex: description contains workflow words |
| **Orphan references** | Dead code | File in references/ not linked in SKILL.md |
| **Missing integration** | Siloed skill | No cross-references to related skills |
| **Stale dates** | Unmaintained | Vetting date > 1 year old |

## Reference Files

- `skill-vetter/SKILL.md` — Security audit baseline
- `skill-inductor/SKILL.md` — Installation requirements
- `writing-skills/SKILL.md` — Documentation quality standards
- `skill-repurposer/SKILL.md` — Attribution requirements

---

**Remember:** Standards exist to reduce friction. Audit to maintain consistency, not to create bureaucracy.
