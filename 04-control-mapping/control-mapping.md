# RouteShield Technologies Control Mapping

## Purpose

This document maps RouteShield Technologies’ primary cybersecurity risks and safeguards to the NIST Cybersecurity Framework 2.0 and ISO/IEC 27001:2022 Annex A.

The mapping demonstrates how business risks can be connected to recognized security controls and governance requirements.

## Control-Mapping Approach

Each entry identifies:

- The related risk from the RouteShield risk register
- The recommended security control
- The applicable NIST CSF 2.0 category
- The applicable ISO/IEC 27001:2022 Annex A control
- Suggested implementation evidence

## Risk and Control Mapping

| Risk ID | Risk Scenario | Recommended Control | NIST CSF 2.0 | ISO/IEC 27001:2022 | Example Evidence |
|---|---|---|---|---|---|
| R-001 | Phishing compromises a Microsoft 365 account. | Multifactor authentication, email filtering, and security-awareness training | PR.AA, PR.AT | A.5.17, A.6.3, A.8.5 | MFA configuration, training records, phishing-test results |
| R-002 | An AWS misconfiguration exposes sensitive information. | Cloud-configuration standards, access reviews, and continuous monitoring | GV.SC, PR.PS, DE.CM | A.5.23, A.8.9, A.8.16 | Cloud-security reports, configuration baselines, access-review records |
| R-003 | A payroll or HR vendor experiences a data breach. | Vendor due diligence, contractual security requirements, and annual reassessment | GV.SC | A.5.19, A.5.20, A.5.22 | Vendor assessment, contract clauses, SOC 2 report |
| R-004 | Ransomware disrupts systems and customer services. | Endpoint protection, network segmentation, tested backups, and incident-response exercises | PR.PS, PR.IR, RS.MA, RC.RP | A.5.24, A.5.26, A.8.13, A.8.20 | Backup-test results, incident-response plan, endpoint-security reports |
| R-005 | A terminated employee retains access after departure. | Formal offboarding, immediate account deactivation, and access-right reviews | PR.AA | A.5.16, A.5.18, A.6.5 | Offboarding checklist, deactivation logs, quarterly access reviews |
| R-006 | A payment processor outage prevents transactions. | Vendor service-level agreements, continuity procedures, and alternate payment options | GV.SC, PR.IR, RC.RP | A.5.22, A.5.30 | SLA reports, continuity plan, outage-test documentation |
| R-007 | A lost or stolen laptop exposes company information. | Full-disk encryption, device management, remote wiping, and screen locking | PR.DS, PR.PS | A.7.9, A.8.1, A.8.24 | Encryption report, device inventory, mobile-device-management policy |
| R-008 | An unpatched vulnerability is exploited. | Vulnerability scanning, patch deadlines, secure development, and penetration testing | ID.RA, PR.PS | A.8.8, A.8.25, A.8.28 | Scan reports, patch records, penetration-test report |
| R-009 | Insufficient monitoring delays detection of unauthorized activity. | Centralized logging, alert tuning, retention standards, and detection testing | DE.CM, DE.AE | A.8.15, A.8.16 | Security logs, alert records, monitoring procedures |
| R-010 | Backup restoration fails during a major incident. | Scheduled restoration testing, immutable backups, and documented recovery objectives | PR.IR, RC.RP | A.5.30, A.8.13 | Restoration-test results, backup logs, recovery procedures |

## Control Ownership

| Control Area | Primary Owner |
|---|---|
| Governance and risk management | GRC Analyst |
| Identity and access management | IT Manager |
| Cloud security | Engineering Manager |
| Vendor risk management | GRC Analyst and Business Owner |
| Incident response | IT Manager |
| Business continuity and recovery | IT Manager and Operations Manager |
| Security awareness | Human Resources and GRC |
| Vulnerability management | Engineering Manager |

## Evidence Expectations

RouteShield should retain sufficient evidence to demonstrate that controls are designed, implemented, and reviewed.

Examples include:

- Approved policies and procedures
- System configuration screenshots
- Access-review records
- Security-training completion reports
- Vendor assessments and contracts
- Vulnerability and patch reports
- Incident-response exercise results
- Backup and restoration-test records
- Monitoring alerts and investigation records

## Review Frequency

This control mapping should be reviewed:

- Annually
- After a major security incident
- After significant technology or business changes
- When new critical vendors are introduced
- When relevant frameworks or contractual requirements change

## Disclaimer

This mapping is illustrative and does not represent certification, legal advice, or a complete compliance determination. RouteShield Technologies and all related information are fictional and were created solely for educational and professional portfolio purposes.
