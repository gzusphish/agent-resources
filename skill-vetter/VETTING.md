---
skill: skill-vetter
version: "1.0.0"
---

# Vetting Record: Skill Vetter

## Source

- **Repository**: Panopticon (original work)
- **Repository URL**: https://gitlab.com/agora.panopticon/bespoke-agent-resources.git (agent-skills-custom/skill-vetter/)
- **Author**: Cascade AI Assistant
- **Created**: 2026-03-31
- **License**: MIT license
- **Vetted Commit**: current

## Vetting Date

2026-03-31

## Approved For

✅ **APPROVED** - All projects managing skill security

## Rationale

Provides comprehensive security auditing for agent skills before installation. Chains static analysis, dependency scanning, and reputation checks to produce PASS/WARN/FAIL verdicts. Essential gate for preventing malicious or vulnerable skills from entering the ecosystem.

## Dependencies

- References `skill-security-auditor` for static analysis patterns
- No external API calls

## Testing Status

- [x] Skill validated
- [x] Platform compatibility: Verified for Claude Code, Windsurf, Copilot

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | Read-only analysis of skill files |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Read-only skill.

## Installation

```bash
cp -r skill-vetter/ ~/.claude/skills/           # Claude Code
cp -r skill-vetter/ .windsurf/skills/          # Windsurf
cp -r skill-vetter/ .github/skills/          # GitHub Copilot
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-custom/ | initial | 1.0.0 | Baseline |
| 2026-04-07 | .windsurf/skills/ | install | 1.0.0 | Central repo copy |

## Notes

- Original skill created for Panopticon development
- Part of the agent-skills central repository
- Serves as canonical security vetting reference
- Scripts directory required for vett.py execution

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (read-only)
