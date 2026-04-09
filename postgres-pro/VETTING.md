---
skill: postgres-pro
version: "1.0.0"
---

# Vetting Record: PostgreSQL Pro

## Source

- **Repository**: DataStage
- **Created**: 2026-04-03
- **License**: MIT license

## Vetting Date

2026-04-07 (retroactive)

## Approved For

✅ **APPROVED** - All projects using PostgreSQL

## Rationale

Senior PostgreSQL expertise for query optimization, configuration tuning, replication setup, backup strategies, and mastering advanced PostgreSQL features for enterprise deployments.

## Dependencies

- PostgreSQL
- No external API calls

## Testing Status

- [x] Skill validated
- [x] Platform compatibility: Verified for Claude Code, Windsurf

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No code execution |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system access | ✅ CLEAR | Database operations documented |
| External dependencies | ✅ CLEAR | PostgreSQL only |

**Verdict**: No security concerns.

## Installation

```bash
cp -r postgres-pro/ ~/.claude/skills/           # Claude Code
cp -r postgres-pro/ .windsurf/skills/          # Windsurf
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-03 | agent-skills-vetted/ | inducted | 1.0.0 | No original VETTING.md |
| 2026-04-07 | agent-skills-vetted/ | vetting | 1.0.0 | Retroactive audit |

## Notes

- Inducted 2026-04-03 without security audit (process failure)
- Retroactive audit completed 2026-04-07
- Performance targets: Query < 50ms, Replication lag < 500ms, RPO < 5 min
- Part of the agent-skills central repository

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-07  
**Risk Level**: Low
