#!/usr/bin/env python3
"""Dependency-free validation of this *fictional* GRC portfolio's internal consistency.

Does not validate live systems, vendor evidence, compliance, or ISO control meaning.
"""
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
NIST_CSF_20_CATEGORIES = {
    "GV.OC", "GV.RM", "GV.RR", "GV.PO", "GV.OV", "GV.SC",
    "ID.AM", "ID.RA", "ID.IM",
    "PR.AA", "PR.AT", "PR.DS", "PR.PS", "PR.IR",
    "DE.CM", "DE.AE",
    "RS.MA", "RS.AN", "RS.CO", "RS.MI",
    "RC.RP", "RC.CO",
}
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
RISK = re.compile(r"^\|\s*(R-\d{3})\s*\|", re.MULTILINE)
GAP = re.compile(r"^\|\s*(GAP-\d{3})\s*\|", re.MULTILINE)
ACTION = re.compile(r"^\|\s*(ACT-\d{3})\s*\|", re.MULTILINE)
FINDING = re.compile(r"^\|\s*(F-\d{3})\s*\|", re.MULTILINE)


def check(condition, message, errors):
    if not condition:
        errors.append(message)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def main():
    errors = []
    docs = sorted(ROOT.rglob("*.md"))
    check(bool(docs), "No Markdown files found", errors)

    # Local Markdown links only: URLs outside this repository are not checked here.
    for source in docs:
        for match in LINK.finditer(source.read_text(encoding="utf-8")):
            dest = match.group(1).split()[0].strip("<>")
            if dest.startswith(("https://", "http://", "mailto:", "#")):
                continue
            dest = unquote(dest.split("#", 1)[0].split("?", 1)[0])
            if not dest:
                continue
            target = (source.parent / dest).resolve()
            check(target.is_relative_to(ROOT), f"{source.relative_to(ROOT)}: path leaves repository: {dest}", errors)
            if target.is_relative_to(ROOT):
                check(target.exists(), f"{source.relative_to(ROOT)}: missing linked target: {dest}", errors)

    register = read("02-risk-register/risk-register.md")
    risk_rows = [line for line in register.splitlines() if re.match(r"^\|\s*R-\d{3}\s*\|", line)]
    risks = set()
    for line in risk_rows:
        cells = [v.strip() for v in line.split("|")[1:-1]]
        try:
            risk_id, likelihood, impact = cells[0], int(cells[3]), int(cells[4])
            score = int(cells[5].split()[0])
            check(1 <= likelihood <= 5 and 1 <= impact <= 5,
                  f"{risk_id}: likelihood or impact outside 1-5", errors)
            check(likelihood * impact == score,
                  f"{risk_id}: expected {likelihood * impact}, found {score}", errors)
            check(risk_id not in risks, f"Duplicate risk ID: {risk_id}", errors)
            risks.add(risk_id)
        except (ValueError, IndexError) as exc:
            errors.append(f"Malformed risk-register row: {exc} | {line[:100]}")
    check(len(risks) == 10, f"Expected 10 distinct risk records, found {len(risks)}", errors)

    gap_text = read("05-security-gap-analysis/security-gap-analysis.md")
    action_text = read("06-remediation-tracker/remediation-tracker.md")
    vendor_text = read("03-vendor-assessment/vendor-assessment.md")
    gaps = set(GAP.findall(gap_text))
    actions = set(ACTION.findall(action_text))
    findings = set(FINDING.findall(vendor_text))
    check(len(gaps) == 7, f"Expected 7 GAP records, found {len(gaps)}", errors)
    check(len(actions) == 7, f"Expected 7 ACT records, found {len(actions)}", errors)
    check(len(findings) == 3, f"Expected 3 vendor findings, found {len(findings)}", errors)

    for line in action_text.splitlines():
        if not re.match(r"^\|\s*ACT-\d{3}\s*\|", line):
            continue
        for risk_ref in re.findall(r"\bR-\d{3}\b", line):
            check(risk_ref in risks, f"Unknown remediation risk: {risk_ref}", errors)
        gap_refs = re.findall(r"\bGAP-\d{3}\b", line)
        check(bool(gap_refs), f"Action missing GAP reference: {line[:80]}", errors)
        for gap_ref in gap_refs:
            check(gap_ref in gaps, f"Unknown remediation GAP: {gap_ref}", errors)

    mapping = read("04-control-mapping/control-mapping.md")
    mapping_risks = set(RISK.findall(mapping))
    check(mapping_risks == risks, f"Risk mapping does not cover all register IDs: {sorted(risks ^ mapping_risks)}", errors)
    mapped_categories = set(re.findall(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}\b", mapping))
    check(mapped_categories.issubset(NIST_CSF_20_CATEGORIES),
          f"Unknown NIST CSF categories: {sorted(mapped_categories - NIST_CSF_20_CATEGORIES)}", errors)

    for relative in [
        "01-company-scenario/company-profile.md",
        "02-risk-register/risk-register.md",
        "03-vendor-assessment/vendor-assessment.md",
        "04-control-mapping/control-mapping.md",
        "05-security-gap-analysis/security-gap-analysis.md",
        "06-remediation-tracker/remediation-tracker.md",
        "07-incident-response-tabletop/tabletop-exercise.md",
        "08-audit-evidence/evidence-request-and-testing.md",
        "09-risk-treatment-decisions/risk-treatment-memo.md",
        "10-interview-walkthrough/interview-guide.md",
        "11-synthetic-offboarding-test/README.md",
    ]:
        c = read(relative).lower()
        check(any(term in c for term in ("fictional", "simulation", "simulated", "synthetic")),
              f"Missing simulation disclosure: {relative}", errors)

    analyzer = ROOT / "11-synthetic-offboarding-test/analyze_offboarding.py"
    p = subprocess.run([sys.executable, str(analyzer), "--json"],
                       capture_output=True, text=True, check=False)
    if p.returncode:
        errors.append(f"Synthetic analyzer failed: {p.stderr.strip()[:500]}")
    else:
        try:
            report = json.loads(p.stdout)
            expected = {"total": 12, "pass": 9, "late": 2, "missing_evidence": 1}
            for field, value in expected.items():
                check(report.get(field) == value,
                      f"Synthetic analyzer {field}: expected {value}, got {report.get(field)}", errors)
        except json.JSONDecodeError as exc:
            errors.append(f"Synthetic analyzer returned invalid JSON: {exc}")

    if errors:
        print("PORTFOLIO QUALITY CHECK FAILED")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("PORTFOLIO QUALITY CHECK PASSED")
    print(f"  Markdown documents: {len(docs)}; local links: resolved")
    print(f"  Risk calculations: {len(risks)} validated")
    print(f"  GAP records: {len(gaps)}; ACT records: {len(actions)}; vendor findings: {len(findings)}")
    print(f"  NIST CSF 2.0 category identifiers: {len(mapped_categories)} recognized")
    print("  Synthetic control analysis: 12 rows; 9 pass, 2 late, 1 missing evidence")
    print("  NOTE: No real-world controls, ISO compliance or evidence were audited.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
