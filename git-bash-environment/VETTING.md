---
skill: git-bash-environment
version: "1.0.0"
---
 
# Vetting Record: Git Bash Environment
 
## Source
 
- **Repository**: Panopticon (original work)
- **Author**: Cascade AI Assistant
- **Created**: 2026-03-31
- **License**: MIT license
 
## Vetting Date
 
2026-03-31
 
## Approved For
 
✅ **APPROVED** - All projects using Git Bash
 
## Rationale
 
Git Bash environment interface and command syntax guide for Windows-based development workflows.
 
## Dependencies
 
- Git Bash environment
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
| File system access | ✅ CLEAR | Documentation only |
| External dependencies | ✅ CLEAR | Git Bash only |
 
**Verdict**: No security concerns. Documentation-only skill.
 
## Installation
 
```bash
cp -r git-bash-environment/ ~/.claude/skills/           # Claude Code
cp -r git-bash-environment/ .windsurf/skills/          # Windsurf
```
 
## Installation Log
 
| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-03-31 | agent-skills-custom/ | initial | 1.0.0 | Baseline |
 
## Notes
 
- Original skill created for Panopticon development
- Part of the agent-skills central repository
 
## Changelog
 
| Date | Change |
|------|--------|
| 2026-04-09 | Added comprehensive "Windsurf on Windows: Command Execution Patterns" section documenting which commands work directly vs. require `bash -c` wrapper. Tested and validated pipelines, redirects, command chaining, quoting, and subshells. Updated all examples to reflect correct usage patterns. |
| 2026-04-06 | Added Git LFS Smudge Failure troubleshooting block (TLS/CA trust failure recovery via sparse-checkout and `GIT_LFS_SKIP_SMUDGE`). Observed during first use of a K-Dense-AI external-untrusted repo with LFS assets on corporate network. |
 
---
 
**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-03-31  
**Risk Level**: None (documentation-only)