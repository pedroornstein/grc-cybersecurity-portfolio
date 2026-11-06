# GRC Cybersecurity Portfolio

[![Portfolio documentation QA](https://github.com/pedroornstein/grc-cybersecurity-portfolio/actions/workflows/portfolio-quality.yml/badge.svg)](https://github.com/pedroornstein/grc-cybersecurity-portfolio/actions/workflows/portfolio-quality.yml)

*This status checks documentation consistency and a synthetic-data test—not actual organizational controls.*

A hands-on Governance, Risk, and Compliance (GRC) case study focused on cybersecurity risk assessment, third-party risk management, security control mapping, and remediation planning.

> **Simulation notice:** RouteShield Technologies, BlueHarbor Payment Services, all personnel, evidence, risks, and assessment conclusions in this repository are fictional. The artifacts are portfolio examples, not records from a real engagement, independent audit, or certification.

## Case Study: RouteShield Technologies

RouteShield is a fictional 75-employee U.S. transportation SaaS company providing dispatch, scheduling, customer management, and payment integrations. Its sample technology environment includes AWS, Microsoft 365, employee endpoints, and external vendors.

**Portfolio objective:** Show how a GRC analyst translates business context into documented risks, control recommendations, vendor assessments, and prioritized remediation actions.

## Explore the Projects

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

## How the Artifacts Connect

1. Start with the [company scenario](01-company-scenario/company-profile.md) to understand the business and assets.
2. Evaluate the most relevant threats in the [risk register](02-risk-register/risk-register.md).
3. Examine a critical service provider through the [vendor assessment](03-vendor-assessment/vendor-assessment.md).
4. Link safeguards to recognized frameworks in the [control mapping](04-control-mapping/control-mapping.md).
5. Prioritize identified deficiencies in the [security gap analysis](05-security-gap-analysis/security-gap-analysis.md).
6. Track actions, evidence expectations, and exceptions with the [remediation action tracker](06-remediation-tracker/remediation-tracker.md).
7. Walk through an incident decision process with the [simulated tabletop exercise](07-incident-response-tabletop/tabletop-exercise.md).
8. Plan evidence collection and test procedures in the [audit-evidence workbook](08-audit-evidence/evidence-request-and-testing.md).
9. Consider management tradeoffs with the [risk-treatment decision memo](09-risk-treatment-decisions/risk-treatment-memo.md).
10. Practice presenting the work with the [interview walkthrough](10-interview-walkthrough/interview-guide.md).
11. Reproduce a hypothetical access-control audit test with the [synthetic offboarding analysis](11-synthetic-offboarding-test/README.md).

## Reproducible Checks

Run `python scripts/validate_portfolio.py` locally using Python 3.10+, or review the [GitHub Actions quality workflow](.github/workflows/portfolio-quality.yml). Checks validate **portfolio consistency and synthetic computations only**; they do not establish live security, vendor assurance, ISO certification, or SOC 2 compliance.

## Quality Assurance and Limitations

See the **[portfolio quality-assurance review](PORTFOLIO-QA.md)** for risk-score and internal-link checks, control-mapping corrections, and remaining verification limitations. These checks assess documentation consistency, not real-world control effectiveness.

## Frameworks and Practices

- **NIST Cybersecurity Framework 2.0** — cybersecurity governance and risk management
- **ISO/IEC 27001:2022 Annex A** — illustrative security-control alignment
- **SOC 2** — illustrative assurance considerations for security and availability
- **Third-party risk management** — vendor due diligence, evidence requests, and remediation tracking

Control mappings are illustrative, not exhaustive. NIST CSF 2.0 category IDs should be checked against the [official NIST CSF 2.0 Core](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf); ISO/IEC 27001:2022 Annex A alignment is not independently certified. No actual SOC 2 report, ISO certification, or validated technical evidence is included.

## Skills Demonstrated

Cybersecurity risk identification and scoring · Risk treatment planning · Third-party security assessment · Control mapping · Gap analysis · Remediation prioritization · Remediation tracking · Reproducible synthetic control testing · Incident-response tabletop design · Audit testing methodology · Risk-treatment recommendations · Documentation for audit readiness

## Author

**Pedro Ornstein**  
Cybersecurity / Governance, Risk & Compliance portfolio

*This repository is an educational demonstration of analytical work, not a claim of prior professional engagement with the fictional organizations.*
