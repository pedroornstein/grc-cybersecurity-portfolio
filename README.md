# GRC and Cybersecurity Portfolio

**Pedro Ornstein** · Governance, risk and compliance · IT audit · Cybersecurity

RouteShield Technologies is a fictional 75-person transportation SaaS company. I built this case study to show how I assess cybersecurity risk, evaluate a third party, prioritize remediation, and design a repeatable control test.

> RouteShield, its vendors and its records are fictional. The framework mappings are illustrative, and the synthetic test provides no assurance about production controls.

## Start here

| Work sample | What to look for |
| --- | --- |
| [Risk register](02-risk-register/risk-register.md) and [decision memo](09-risk-treatment-decisions/risk-treatment-memo.md) | How ten risks are scored, why vulnerability remediation and account compromise lead the proposed priorities, and what evidence management would need before rescoring. |
| [Payment processor assessment](03-vendor-assessment/vendor-assessment.md) | How due diligence findings inform a proposed conditional approval, with evidence and follow-up requirements. |
| [Reproducible offboarding test](11-synthetic-offboarding-test/README.md) | A Python test of 12 fabricated Microsoft 365 records against an illustrative four-hour threshold. Nine meet the threshold, two are late, and one lacks a disablement timestamp. |

## Follow one risk through the case study

[R-005 in the risk register](02-risk-register/risk-register.md) describes the risk of a former employee retaining access. [GAP-002](05-security-gap-analysis/security-gap-analysis.md#gap-002-access-reviews-and-offboarding) documents the lifecycle gap, and [ACT-002](06-remediation-tracker/remediation-tracker.md) assigns a proposed response to HR and IT. The [evidence workbook](08-audit-evidence/evidence-request-and-testing.md) defines PBC-002 and TC-002 for collecting and testing offboarding records. The [Python example](11-synthetic-offboarding-test/README.md) demonstrates the timestamp comparison for one system and identifies records that warrant follow-up.

## Artifact index

| Artifact | What it demonstrates |
| --- | --- |
| [01 · Company Scenario](01-company-scenario/company-profile.md) | Business context, critical assets, data types, risk appetite, and compliance considerations |
| [02 · Risk Register](02-risk-register/risk-register.md) | Ten risk scenarios, inherent and residual scores, risk ownership, and treatments |
| [03 · Vendor Security Assessment](03-vendor-assessment/vendor-assessment.md) | Risk-based due diligence of fictional payment processor BlueHarbor, assessment findings, and conditional approval |
| [04 · Security Control Mapping](04-control-mapping/control-mapping.md) | Connections between risks, NIST CSF 2.0 categories, ISO/IEC 27001:2022 Annex A controls, and example audit evidence |
| [05 · Security Gap Analysis](05-security-gap-analysis/security-gap-analysis.md) | Seven control gaps, responsible owners, expected evidence, and a 30/60/90-day remediation roadmap |
| [06 · Remediation Action Tracker](06-remediation-tracker/remediation-tracker.md) | Seven proposed actions linked to gaps and risk IDs, accountable owners, verification criteria, and exception handling |
| [07 · Incident-Response Tabletop](07-incident-response-tabletop/tabletop-exercise.md) | Simulated ransomware incident, decision timeline, evaluation criteria, and hypothetical after-action findings |
| [08 · Audit Evidence and Control Testing](08-audit-evidence/evidence-request-and-testing.md) | Prepared-by-client requests, control testing plans, sampling guidance, and working-paper template |
| [09 · Risk-Treatment Decisions](09-risk-treatment-decisions/risk-treatment-memo.md) | Decision rationale, treatment sequencing, acceptance gates, and proposed management approvals |
| [10 · Interview Walkthrough](10-interview-walkthrough/interview-guide.md) | Five-minute case-study walkthrough, defensible risk examples, and realistic interview questions |
| [11 · Synthetic Offboarding Test](11-synthetic-offboarding-test/README.md) | Executable Python control-testing sample using fabricated access data, with two late cases and one evidence gap |

## Reproduce the checks

From the repository root, run `python scripts/validate_portfolio.py` with Python 3.10+. See the [QA notes](PORTFOLIO-QA.md) and [GitHub Actions workflow](.github/workflows/portfolio-quality.yml) for coverage and limitations.

[![Portfolio documentation and synthetic test checks](https://github.com/pedroornstein/grc-cybersecurity-portfolio/actions/workflows/portfolio-quality.yml/badge.svg)](https://github.com/pedroornstein/grc-cybersecurity-portfolio/actions/workflows/portfolio-quality.yml)

## Related work

[WordPress security review](https://github.com/pedroornstein/wordpress-site-security-audit) · A retrospective report with a documented review of the evidence needed to verify its claims.
