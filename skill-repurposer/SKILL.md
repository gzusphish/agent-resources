---
name: skill-repurposer
description: Use when adapting existing or external skills for different contexts, domains, or use cases. Guides analysis, modification, and validation of repurposed skills while maintaining attribution and security standards.
---

# Skill Repurposer

Adapt existing skills for new contexts while preserving quality and attribution.

## When To Use

- **Domain adaptation**: Converting skills from one domain to another (e.g., research → engineering)
- **Scope modification**: Narrowing or broadening skill applicability
- **Integration prep**: Modifying external skills to fit your ecosystem conventions
- **Capability extension**: Adding functionality to existing skills
- **Simplification**: Creating lightweight versions of complex skills

## Core Workflow

### 1. Analyze Source Skill

**Read and understand:**
```bash
# Load original skill
cat agent-skills-custom/skill-name/SKILL.md

# Check structure
ls -la agent-skills-custom/skill-name/
```

**Capture analysis:**
```yaml
source_skill:
  name:
  original_domain: [e.g., "academic research", "data science", "general dev"]
  target_domain: [your intended use case]
  core_workflow: [1-2 sentence summary]
  dependencies: []
  references_count: [number of external files]
  scripts_count: [number of executable components]
  frontmatter_quality: [Good/Medium/Poor]
  modification_type: [adaptation|scope_change|extension|simplification]
```

**Identify repurposing opportunities:**
- Which sections transfer directly?
- Which need domain-specific rewriting?
- What can be simplified vs. what must be preserved?
- Are there hardcoded paths/tools that need abstraction?

### 2. Plan Modifications

**Decision matrix:**

| Component | Action | Rationale |
|-----------|--------|-----------|
| Frontmatter | Keep/Rewrite/Extend | Description must match new use case |
| Core workflow | Adapt/Replace/Preserve | Match target domain conventions |
| Examples | Rewrite | Use target domain language |
| References | Filter/Extend | Remove irrelevant, add domain-specific |
| Scripts | Review/Modify | Check for hardcoded assumptions |

**Modification checklist:**
- [ ] **Name**: Still appropriate? Change if domain-specific
- [ ] **Description**: Rewrite for new triggering conditions
- [ ] **When To Use**: Adapt symptoms/contexts for target domain
- [ ] **Workflow steps**: Modify examples, tools, outputs
- [ ] **Integration points**: Update skill cross-references
- [ ] **Storage paths**: Adjust to your conventions
- [ ] **Tool references**: Update for available tools in target context

### 3. Execute Repurposing

**Create new skill structure:**
```bash
mkdir agent-skills-custom/repurposed-skill-name/
cp agent-skills-custom/source-skill/SKILL.md agent-skills-custom/repurposed-skill-name/
# Copy/modify references and scripts as needed
```

**Modification patterns:**

**Pattern A: Domain Adaptation**
```markdown
# Original: "Use when analyzing survey data"
# Repurposed: "Use when analyzing system performance metrics"

# Keep: Data validation steps, visualization guidance
# Modify: Tool references (pandas → monitoring APIs)
# Add: Domain-specific context (SLIs, SLOs)
```

**Pattern B: Scope Narrowing**
```markdown
# Original: General "data analysis" skill (broad)
# Repurposed: "log analysis" skill (specific)

# Keep: Core analysis methodology
# Remove: Irrelevant analysis types
# Focus: Log-specific patterns, tools, outputs
```

**Pattern C: Integration Prep**
```markdown
# Original: Standalone skill with hardcoded paths
# Repurposed: Skill using your ecosystem conventions

# Modify: ../agent-knowledge/ → your actual knowledge base path
# Modify: Generic tool names → your specific tool names
# Add: Integration with your existing skills
```

### 4. Preserve Attribution

**Required in repurposed VETTING.md:**
```markdown
## Source Attribution
- **Original Skill:** [name]
- **Original Source:** [repo/path]
- **Original Author:** [if known]
- **Original License:** [if applicable]
- **Repurposed By:** [you]
- **Repurposed Date:** [date]
- **Modifications:** [brief description of changes]
- **Rationale:** [why this repurposing was needed]
```

**Required in repurposed SKILL.md:**
- Add to Notes section: "Adapted from [original] for [new context]"
- Keep original license headers if present
- Credit original patterns/concepts

### 5. Validate Repurposed Skill

**Functionality test:**
- [ ] SKILL.md parses correctly (no YAML/frontmatter errors)
- [ ] Description accurately describes new triggering conditions
- [ ] Workflow steps make sense in new domain
- [ ] Examples use target domain language/concepts
- [ ] Cross-references point to existing skills in your ecosystem

**Security review:**
- [ ] No new external API calls added without justification
- [ ] Scripts reviewed for hardcoded credentials/paths
- [ ] File operations limited to appropriate scope
- [ ] Run `skill-vetter` on repurposed skill

**Integration test:**
- [ ] Skill triggers appropriately for new use case
- [ ] References resolve correctly
- [ ] Works with your existing skill ecosystem

### 6. Document and Induct

**Complete induction workflow:**
```
1. Finalize SKILL.md with proper attribution
2. Create VETTING.md (mark as "Repurposed from X")
3. Run full vetting via skill-inductor
4. Add to skill catalog with "repurposed" tag
5. Deploy to target projects
```

## Repurposing Patterns

### Research → Engineering

**Original:** `literature-review` (academic paper analysis)
**Repurposed:** `technical-paper-review` (engineering docs, RFCs)

**Modifications:**
- Replace: Academic databases → Internal docs, RFCs, specs
- Replace: Citation analysis → Version/dependency tracking
- Keep: Structured analysis methodology
- Add: Implementation feasibility assessment

### Data Science → DevOps

**Original:** `exploratory-data-analysis` (statistical analysis)
**Repurposed:** `system-health-analysis` (metrics investigation)

**Modifications:**
- Replace: pandas/ggplot → monitoring APIs/dashboards
- Replace: Statistical tests → SLO violation detection
- Keep: Hypothesis generation, structured investigation
- Add: Alert correlation, incident timeline analysis

### General → Domain-Specific

**Original:** `codebase-summary` (general code analysis)
**Repurposed:** `security-audit-summary` (security-focused analysis)

**Modifications:**
- Narrow: Focus on security-relevant files/patterns
- Add: Vulnerability scanning integration
- Add: Threat model documentation
- Keep: Documentation structure and workflow

## Anti-Patterns to Avoid

| Don't | Why |
|-------|-----|
| Strip attribution | Violates license, loses provenance |
| Remove security checks | Repurposed skills need same vetting |
| Hardcode new paths | Makes skill non-portable |
| Over-modify | Breaks working patterns unnecessarily |
| Skip testing | Repurposed skills must re-verify |
| Ignore license terms | Some skills prohibit modification |

## Quick Reference

**Repurposing checklist:**
```
1. Analyze source skill structure and dependencies
2. Identify transferable vs. domain-specific components
3. Plan modifications (use decision matrix)
4. Create new skill with proper attribution
5. Adapt examples, tools, references for target domain
6. Run security vetting on repurposed skill
7. Test integration with existing skills
8. Complete induction workflow
```

**Attribution template:**
```markdown
## Source
- **Original Skill:** [name] from [repo]
- **Original Author:** [name]
- **License:** [license]
- **Repurposed By:** [you]
- **Date:** [date]
- **Changes:** [brief description]
- **Rationale:** [why repurposed]
```

## Integration with skill-inductor

After repurposing, treat as new skill:
```
skill-repurposer → [creates repurposed skill]
    ↓
skill-inductor → [full vetting and induction]
    ↓
deploy to projects
```

## Reference Files

- `skill-inductor/SKILL.md` — Complete induction workflow
- `skill-vetter/SKILL.md` — Security validation
- `writing-skills/SKILL.md` — Quality documentation patterns

---

**Remember:** Repurposing extends the utility of existing work. Attribute generously, verify thoroughly.
