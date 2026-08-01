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
| R-006 | A payment processor outage prevents customers from completing transactions. | Payment integrations | 3 | 4 | 12 High | Vendor SLA, service monitoring, manual reconciliation procedures | Mitigate through contingency procedures, alternate payment options, and annual vendor reviews | 6 Moderate | Finance and IT Managers | Open | NIST CSF GV.SC; ISO 27001 Annex A.5.22 and A.5.30 |
| R-007 | A lost or stolen employee laptop exposes company information or login credentials. | Employee devices and company data | 3 | 4 | 12 High | Full-disk encryption, screen locking, MFA | Mitigate through mobile-device management, remote wiping, and device inventory reviews | 4 Low | IT Manager | Open | NIST CSF PR.DS and PR.PS; ISO 27001 Annex A.7.9 and A.8.1 |
| R-008 | An unpatched vulnerability in the customer platform is exploited by an attacker. | Customer platform and source code | 4 | 5 | 20 Critical | Patch management, vulnerability scanning, code reviews | Mitigate through remediation deadlines, penetration testing, and secure-development reviews | 8 Moderate | Engineering Manager | Open | NIST CSF ID.RA and PR.PS; ISO 27001 Annex A.8.8 and A.8.25 |
| R-009 | Insufficient logging and monitoring delays the detection of unauthorized activity. | AWS, Microsoft 365, and customer platform | 3 | 4 | 12 High | Native cloud logs and basic security alerts | Mitigate through centralized logging, alert tuning, retention standards, and detection testing | 6 Moderate | IT Manager | Open | NIST CSF DE.CM and DE.AE; ISO 27001 Annex A.8.15 and A.8.16 |
| R-010 | Backup restoration fails during a major outage or ransomware incident. | Backup systems and customer platform | 3 | 5 | 15 High | Scheduled backups and restricted backup access | Mitigate through restoration testing, immutable backups, and documented recovery objectives | 5 Low | IT Manager | Open | NIST CSF RC.RP and PR.IR; ISO 27001 Annex A.8.13 and A.5.30 |

## Disclaimer

All risks, systems, people, and control information in this register are fictional and were created for educational and professional portfolio purposes.
