---
skill: exploratory-data-analysis
version: "1.0.0"
---

# Vetting Record: Exploratory Data Analysis

## Source

- **Repository**: k-dense-ai-claude-scientific-skills (K-Dense Inc.)
- **Author**: K-Dense Inc.
- **Created**: 2025 (estimated from content)
- **License**: MIT license

## Vetting Date

2026-04-07

## Approved For

⚠️ **CONDITIONAL USE** - Internal scientific analysis workflows only

## Rationale

This skill provides comprehensive exploratory data analysis capabilities across 200+ scientific file formats. The value proposition is high for bioinformatics, chemistry, and microscopy workflows. However, security findings require mitigation before broader deployment.

## Security Assessment

**Status**: ⚠️ **ACCEPTABLE WITH RISKS**

### Findings Summary

| Severity | Count | Finding | Risk Level |
|----------|-------|---------|------------|
| 🔴 CRITICAL | 0 | - | - |
| 🟡 HIGH | 2 | DEPS-RUNTIME | Low (false positive) |
| ⚪ INFO | 0 | - | - |

### Detailed Analysis

**Issue DEPS-RUNTIME-1** (Line 374):
- **Pattern**: `results['error'] = f"Required library not installed (try: pip install biopython): {e}"`
- **Auditor Flag**: Runtime package installation risk
- **Actual Assessment**: **FALSE POSITIVE** - This is a string error message returned to users, not executed code. The script catches ImportError and returns guidance text. No actual pip execution occurs.

**Issue DEPS-RUNTIME-2** (Line 414):
- **Pattern**: `results['error'] = f"Required library not installed (try: pip install pillow): {e}"`
- **Auditor Flag**: Runtime package installation risk  
- **Actual Assessment**: **FALSE POSITIVE** - Same as above; static error message only.

### Real Security Considerations

1. **Script Execution Risk**: The `eda_analyzer.py` script processes user-provided file paths. Malicious paths (e.g., containing shell metacharacters) could theoretically cause issues if not properly sanitized.

2. **Dependency Chain**: The skill recommends installing biopython, pillow, numpy, pandas, and other scientific libraries. These are legitimate packages but add supply chain risk.

3. **File System Access**: Script reads arbitrary user-provided files. No sandboxing is implemented.

### Risk Mitigation Applied

- [x] Code review confirms no actual runtime pip execution
- [x] No network calls detected in script analysis
- [x] No eval/exec/__import__ patterns found
- [ ] File path sanitization not verified (user responsibility)

## Dependencies

**Python Libraries Referenced**:
- `biopython` - Sequence analysis (FASTA/FASTQ)
- `pillow` (PIL) - Image analysis
- `numpy` - Array processing
- `pandas` - Tabular data analysis
- `pysam` - SAM/BAM genomics files
- `pyBigWig` - Genomics annotation files
- `nd2reader`, `aicsimageio`, `pydicom` - Microscopy formats
- `nmrglue`, `pymzml`, `pyteomics` - Spectroscopy/proteomics

**Installation Required**: Yes - users must install dependencies manually per error messages

## Testing Status

- [x] Static analysis completed (skill-security-auditor)
- [x] Code review performed for pip execution patterns
- [ ] Dynamic testing with sample data files pending
- [ ] Integration testing with actual scientific datasets pending

## Security Assessment Summary

| Criterion | Result | Notes |
|-----------|--------|-------|
| Code injection risk | ✅ CLEAR | No eval/exec patterns |
| Network exfiltration | ✅ CLEAR | No network calls |
| Credential harvesting | ✅ CLEAR | No credential access |
| Privilege escalation | ✅ CLEAR | No sudo/system calls |
| File system abuse | ⚠️ NOTE | Reads user paths; use with trusted files |
| Dependency risk | ⚠️ NOTE | False positive on pip install messages |
| Obfuscation | ✅ CLEAR | No encoded payloads |

**Verdict**: Acceptable for use with scientific data files from trusted sources. The "pip install" auditor warnings are false positives - the code only returns these as error messages, never executes them.

## Installation

```bash
# Copy to vetted skills
cp -r agent-external/k-dense-ai-claude-scientific-skills/scientific-skills/exploratory-data-analysis agent-skills-vetted/

# Install dependencies as needed
pip install biopython pillow numpy pandas
```

## Installation Log

| Date | Location | Method | Version | Drift Check |
|------|----------|--------|---------|-------------|
| 2026-04-07 | agent-skills-vetted/ | copy from agent-external | 1.0.0 | No original VETTING.md to compare |

## Notes

- This skill was part of the K-Dense scientific skills batch induction
- Original induction on 2026-04-07 did NOT include proper security audit (process failure)
- Retrospective audit completed same day identified false-positive pip install warnings
- Users must manually install scientific libraries; skill provides guidance via error messages only
- Consider creating a `requirements.txt` for this skill to standardize dependency management

## Limitations

1. Requires manual dependency installation
2. No automated sandboxing for file processing
3. Large reference files (10,000+ words each) may strain context window
4. Limited to read-only analysis; does not modify data files

## Anti-Patterns Detected

| Pattern | Location | Severity | Action Taken |
|---------|----------|----------|--------------|
| Missing VETTING.md | skill root | High | Created this file |
| Inline pip suggestions | eda_analyzer.py:374,414 | Low | False positive; documented |

---

**Auditor**: Cascade AI Assistant  
**Audit Date**: 2026-04-07  
**Risk Level**: Low-Medium (acceptable for trusted scientific workflows)
