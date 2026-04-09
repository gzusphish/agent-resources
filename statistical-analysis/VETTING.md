---
skill: statistical-analysis
version: "1.0.0"
---

# Vetting Record: Statistical Analysis

## Source

- **Repository**: k-dense-ai-claude-scientific-skills (K-Dense Inc.)
- **Author**: K-Dense Inc.
- **Created**: 2025 (estimated from content)
- **License**: MIT license

## Vetting Date

2026-04-07

## Approved For

✅ **APPROVED** - Academic statistical analysis and reporting workflows

## Rationale

Statistical test selection, assumption checking, and APA-format reporting framework. Provides guidance for t-tests, ANOVA, regression, correlation, and Bayesian analyses. Complements programmatic statistical libraries.

## Security Assessment

**Status**: ✅ **CLEAR**

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No eval/exec |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| File system abuse | ✅ CLEAR | Read-only guidance |
| External dependencies | ✅ CLEAR | None required |

**Verdict**: No security concerns. Analytical guidance skill.

## Dependencies

None - conversational guidance skill only.

**Note**: For actual statistical implementation, users should use statsmodels, scipy, or R. This skill provides test selection guidance and interpretation frameworks.

## Testing Status

- [x] Static analysis completed (skill-security-auditor)
- [x] No malicious patterns detected
- [x] One script file audited (clean - statistical guidance only)

## Installation

```bash
cp -r agent-resources/k-dense-ai-claude-scientific-skills/scientific-skills/statistical-analysis agent-skills-vetted/
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-07 | agent-skills-vetted/ | copy from agent-resources | 1.0.0 | No original VETTING.md |

## Notes

- Statistical test selection and interpretation framework
- APA-format reporting guidance
- Complements programmatic stats libraries (statsmodels, scipy)
- One script present (statistical reference material, clean)
- Originally inducted without security audit (process failure now corrected)

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-07  
**Risk Level**: None (guidance only)
