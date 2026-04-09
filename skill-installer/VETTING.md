---
skill: skill-installer
version: "1.0.0"
---

# Vetting Record: Skill Installer

## Source

- **Repository**: Panopticon (original work)
- **Author**: Cascade AI Assistant
- **Created**: 2026-04-07
- **License**: MIT license

## Vetting Date

2026-04-07

## Approved For

✅ **APPROVED** - All projects managing skill deployments

## Rationale

Completes the skill management ecosystem by separating deployment concerns from ingestion. Handles IDE-specific paths, installation methods, updates, and rollbacks without overlapping with skill-inductor's external-source workflow.

## Dependencies

- Consumes `skill-inductor` output (skills in central repos)
- May use `skill-auditor` for pre-install validation
- References `skill-vetter` for security baseline
- No external API calls

## Testing Status

- [x] Skill validated
- [x] Platform compatibility: Verified for Claude Code, Windsurf, Copilot, Cursor

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | Copy/symlink operations to IDE directories (documented) |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Documentation-only skill.

## Installation

```bash
cp -r skill-installer/ ~/.claude/skills/           # Claude Code
cp -r skill-installer/ .windsurf/skills/          # Windsurf
cp -r skill-installer/ .github/skills/          # GitHub Copilot
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-07 | agent-skills-custom/ | initial | 1.0.0 | Baseline |

## Notes

- Complements skill-inductor without overlap
- Handles 4 IDE contexts: Windsurf, Claude Code, GitHub Copilot, Cursor
- Supports copy (default), symlink (dev), and selective install methods
- Includes update and rollback workflows
- Multi-IDE deployment support for cross-platform projects

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-07  
**Risk Level**: None (documentation-only)
