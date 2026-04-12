#!/usr/bin/env python3
"""
Skill Vetter - Comprehensive security audit for AI agent skills.
Chains: skill-security-auditor + pip-audit + safety
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict


@dataclass
class VettingReport:
    skill_name: str
    skill_path: str
    verdict: str
    findings: List[Dict]
    dependency_issues: List[Dict]
    summary: Dict


def run_security_audit(skill_path: str) -> Dict:
    """Run skill-security-auditor."""
    auditor_path = ".windsurf/skills/skill-security-auditor/scripts/skill_security_auditor.py"
    
    try:
        result = subprocess.run(
            [sys.executable, auditor_path, skill_path, "--json"],
            capture_output=True,
            text=True,
            timeout=60
        )
        return json.loads(result.stdout) if result.stdout else {"verdict": "ERROR", "findings": []}
    except Exception as e:
        return {"verdict": "ERROR", "findings": [], "error": str(e)}


def run_pip_audit(skill_path: str) -> List[Dict]:
    """Run pip-audit on requirements.txt if present."""
    req_file = Path(skill_path) / "requirements.txt"
    if not req_file.exists():
        return []
    
    try:
        result = subprocess.run(
            ["pip-audit", "--requirement", str(req_file), "--format", "json"],
            capture_output=True,
            text=True,
            timeout=120
        )
        if result.stdout:
            data = json.loads(result.stdout)
            return data.get("dependencies", [])
        return []
    except Exception as e:
        return [{"error": str(e)}]


def run_safety_check(skill_path: str) -> List[Dict]:
    """Run safety check on requirements.txt if present."""
    req_file = Path(skill_path) / "requirements.txt"
    if not req_file.exists():
        return []
    
    try:
        result = subprocess.run(
            ["safety", "check", "-r", str(req_file), "--json"],
            capture_output=True,
            text=True,
            timeout=120
        )
        if result.stdout:
            data = json.loads(result.stdout)
            return data.get("vulnerabilities", [])
        return []
    except Exception as e:
        return [{"error": str(e)}]


def calculate_verdict(security_report: Dict, dep_issues: List[Dict], strict: bool) -> str:
    """Calculate overall verdict."""
    security_verdict = security_report.get("verdict", "PASS")
    
    critical_deps = len([d for d in dep_issues if d.get("severity") in ["CRITICAL", "HIGH"]])
    
    if security_verdict == "FAIL" or critical_deps > 0:
        return "FAIL"
    elif security_verdict == "WARN" or len(dep_issues) > 0:
        return "FAIL" if strict else "WARN"
    else:
        return "PASS"


def vett_skill(skill_path: str, strict: bool = False) -> VettingReport:
    """Run complete vetting pipeline."""
    skill_name = Path(skill_path).name
    
    # Run all audits
    security = run_security_audit(skill_path)
    pip_issues = run_pip_audit(skill_path)
    safety_issues = run_safety_check(skill_path)
    
    # Combine dependency issues
    all_dep_issues = []
    for issue in pip_issues:
        if "vulns" in issue:
            for vuln in issue["vulns"]:
                all_dep_issues.append({
                    "package": issue.get("name"),
                    "version": issue.get("version"),
                    "vulnerability_id": vuln.get("id"),
                    "severity": vuln.get("severity"),
                    "source": "pip-audit"
                })
    
    for issue in safety_issues:
        all_dep_issues.append({
            "package": issue.get("package_name"),
            "vulnerability": issue.get("vulnerability_id"),
            "severity": issue.get("severity"),
            "source": "safety"
        })
    
    # Calculate verdict
    verdict = calculate_verdict(security, all_dep_issues, strict)
    
    # Build findings list
    findings = security.get("findings", [])
    
    summary = {
        "security_critical": len([f for f in findings if f.get("severity") == 2]),
        "security_high": len([f for f in findings if f.get("severity") == 1]),
        "dependency_issues": len(all_dep_issues),
        "total_files": security.get("stats", {}).get("files_scanned", 0)
    }
    
    return VettingReport(
        skill_name=skill_name,
        skill_path=skill_path,
        verdict=verdict,
        findings=findings,
        dependency_issues=all_dep_issues,
        summary=summary
    )


def main():
    parser = argparse.ArgumentParser(description="Comprehensive skill vetting")
    parser.add_argument("skill_path", help="Path to skill directory")
    parser.add_argument("--strict", action="store_true", help="Treat WARN as FAIL")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.skill_path):
        print(f"Error: Path not found: {args.skill_path}", file=sys.stderr)
        sys.exit(1)
    
    report = vett_skill(args.skill_path, strict=args.strict)
    
    if args.json:
        print(json.dumps(asdict(report), indent=2))
    else:
        print(f"\n{'='*70}")
        print(f"  SKILL VETTING REPORT - PANOPTICON")
        print(f"{'='*70}")
        print(f"  Skill: {report.skill_name}")
        print(f"  Verdict: {report.verdict}")
        print(f"{'='*70}")
        print(f"  Security Critical: {report.summary['security_critical']}")
        print(f"  Security High: {report.summary['security_high']}")
        print(f"  Dependency Issues: {report.summary['dependency_issues']}")
        print(f"{'='*70}\n")
        
        if report.findings:
            print("Security Findings:")
            for f in report.findings[:5]:  # Show first 5
                sev = "CRIT" if f.get("severity") == 2 else "HIGH" if f.get("severity") == 1 else "INFO"
                print(f"  [{sev}] {f.get('category')}: {f.get('risk')}")
            if len(report.findings) > 5:
                print(f"  ... and {len(report.findings) - 5} more")
        
        if report.dependency_issues:
            print("\nDependency Issues:")
            for d in report.dependency_issues[:3]:
                print(f"  {d.get('package', 'unknown')}: {d.get('vulnerability_id', 'N/A')}")
    
    # Exit codes
    if report.verdict == "PASS":
        sys.exit(0)
    elif report.verdict == "WARN":
        sys.exit(2)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
