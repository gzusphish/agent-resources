---
name: skill-vetter
description: "Comprehensive security vetting for AI agent skills. Use when: (1) evaluating any skill before installation, (2) auditing skills from external sources, (3) periodic security reviews of installed skills, (4) pre-deployment gate checks. Chains static analysis (skill-security-auditor), dependency scanning (pip-audit, safety), and reputation checks. Produces PASS/WARN/FAIL verdict with detailed findings."
---

# Skill Vetter - Comprehensive Security Audit

**The Panopticon's all-seeing eye for skill evaluation.**

## Quick Start

```bash
# Vett a local skill directory
python .windsurf/skills/skill-vetter/scripts/vett.py /path/to/skill/

# Vett with strict mode (any WARN becomes FAIL)
python .windsurf/skills/skill-vetter/scripts/vett.py /path/to/skill/ --strict

# Vett with JSON output for CI/CD
python .windsurf/skills/skill-vetter/scripts/vett.py /path/to/skill/ --json
```

## What Gets Scanned

| Layer | Tool | Coverage |
|-------|------|----------|
| **Static Analysis** | skill-security-auditor | Code execution, prompt injection, obfuscation, network exfiltration |
| **Dependency Audit** | pip-audit + safety | Known CVEs, typosquatting, vulnerable packages |
| **Reputation Check** | Manual indicators | GitHub stars, contributor history, commit timeline |

## Audit Workflow

### 1. Run the Vetter

Execute comprehensive audit on the skill directory:

```bash
python .windsurf/skills/skill-vetter/scripts/vett.py .windsurf/skills/some-new-skill/
```

### 2. Review the Verdict

**Verdict Hierarchy:**
- **PASS** — All checks passed. Safe to install.
- **WARN** — Medium-risk findings. Review manually.
- **FAIL** — Critical findings or dependency CVEs. Do NOT install.

### 3. Review Findings

Findings include:
- **Category**: CODE-EXEC, PROMPT-INJECTION, DEP-VULN, etc.
- **Severity**: CRITICAL, HIGH, INFO
- **File**: Location of finding
- **Risk**: What could go wrong
- **Fix**: Recommended remediation

## Integration with Panopticon

For centralized skill management:

```bash
# Vett all skills in Panopticon
for skill in .windsurf/skills/*/; do
  python .windsurf/skills/skill-vetter/scripts/vett.py "$skill" --json >> vetting-results.jsonl
done

# Check specific skill before adding
git clone https://github.com/user/suspect-skill /tmp/suspect
python .windsurf/skills/skill-vetter/scripts/vett.py /tmp/suspect --strict
```

## Exit Codes

- **0**: PASS
- **1**: FAIL (do not install)
- **2**: WARN (review manually)

## When to Re-Vett

- Before installing any new skill
- When updating existing skills (new commits)
- Quarterly security reviews
- When skill behavior seems suspicious

---

**Remember**: The Panopticon sees all. Trust but verify.
