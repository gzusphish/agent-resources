---
skill: skill-security-auditor
version: "1.0.0"
---

# Vetting Record: Skill Security Auditor

## Source

- **Repository**: alirezarezvani-claude-skills
- **Repository URL**: https://github.com/alirezarezvani/claude-skills
- **Path**: `engineering/skill-security-auditor/`
- **Author**: Alireza Rezvani
- **License**: MIT
- **Vetted Commit**: `89500d759d43b13ee292a04a88834f57d0e07b98`

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects requiring security audits

## Rationale

Static analysis security audit for AI skills. Detects code execution, prompt injection, obfuscation, network exfiltration patterns. Essential pre-induction security gate.

## Dependencies

- Python
- No external API calls

## Testing Status

- [x] Skill validated
- [x] Platform compatibility: Windsurf, Claude Code

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | Read-only skill analysis |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Read-only tool.

## Installation

```bash
cp -r skill-security-auditor/ ~/.claude/skills/           # Claude Code
cp -r skill-security-auditor/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-vetted/ | inducted | 1.0.0 | Baseline |

## Notes

- Inducted from alirezarezvani-claude-skills
- Part of the agent-skills central repository
- Critical security gate for skill induction
- Run before any skill installation

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (read-only)
