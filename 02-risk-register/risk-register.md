# RouteShield Technologies Risk Register

## Purpose

This risk register identifies, evaluates, and tracks cybersecurity and operational risks affecting RouteShield Technologies.

## Scoring Method

- Likelihood: 1–5
- Impact: 1–5
- Inherent Risk Score: Likelihood × Impact
- Low: 1–5
- Moderate: 6–10
- High: 11–15
- Critical: 16–25

## Risk Register

| ID | Risk Scenario | Asset / Process | Likelihood | Impact | Inherent Score | Existing Controls | Treatment | Residual Score | Owner | Status | Framework References |
|---|---|---|---:|---:|---:|---|---|---:|---|---|---|
| R-001 | A phishing attack compromises an employee Microsoft 365 account and exposes company information. | Microsoft 365 accounts | 4 | 4 | 16 Critical | MFA, email filtering, security awareness training | Mitigate through stronger phishing simulations and conditional-access policies | 8 Moderate | IT Manager | Open | NIST CSF PR.AA; ISO 27001 Annex A.5.17 |
| R-002 | An AWS cloud misconfiguration exposes customer or driver information to unauthorized users. | AWS infrastructure and databases | 3 | 5 | 15 High | Access controls, encryption, logging | Mitigate through configuration reviews and automated cloud-security monitoring | 6 Moderate | Cloud Administrator | Open | NIST CSF PR.PS; ISO 27001 Annex A.8.9 |
| R-003 | A third-party payroll or HR provider experiences a breach involving employee records. | HR and payroll data | 3 | 4 | 12 High | Vendor contracts and limited data sharing | Mitigate through vendor assessments, breach-notification requirements, and annual reviews | 6 Moderate | HR Manager | Open | NIST CSF GV.SC; ISO 27001 Annex A.5.19 |
| R-004 | Ransomware disrupts RouteShield systems and prevents customers from using the platform. | Customer platform and backups | 3 | 5 | 15 High | Endpoint protection, backups, access controls | Mitigate through backup testing, network segmentation, and incident-response exercises | 6 Moderate | IT Manager | Open | NIST CSF PR.IR; ISO 27001 Annex A.8.13 |
| R-005 | A terminated employee retains access to company systems after leaving RouteShield. | Employee accounts and company data | 3 | 4 | 12 High | Offboarding checklist and account inventory | Mitigate through automated account deactivation and quarterly access reviews | 4 Low | HR and IT Managers | Open | NIST CSF PR.AA; ISO 27001 Annex A.5.18 |

## Disclaimer

All risks, systems, people, and control information in this register are fictional and were created for educational and professional portfolio purposes.
