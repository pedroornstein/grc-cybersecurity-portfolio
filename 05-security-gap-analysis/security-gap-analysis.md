# RouteShield Technologies Security Gap Analysis

## Purpose

This security gap analysis compares RouteShield Technologies' current cybersecurity practices with its target control environment.

The analysis identifies control weaknesses, assigns remediation priorities, and defines evidence that should be collected to demonstrate improvement.

## Scope

The review covers:

- Identity and access management
- Logging and monitoring
- Vulnerability management
- Backup and recovery
- Incident response
- Third-party risk management
- Security governance

## Severity Ratings

- **Critical:** Immediate action required
- **High:** Remediate within 30 days
- **Moderate:** Remediate within 31-90 days
- **Low:** Address through ongoing improvement

## Gap Summary

| Gap ID | Security Gap | Severity | Owner | Target |
|---|---|---|---|---|
| GAP-001 | Multifactor authentication is not consistently enforced for privileged access. | High | IT Manager | 30 days |
| GAP-002 | User-access reviews and offboarding activities rely heavily on manual processes. | High | HR and IT Managers | 30 days |
| GAP-003 | Security logs are not fully centralized or consistently monitored. | High | IT Manager | 60 days |
| GAP-004 | Backup-restoration testing is not performed on a documented schedule. | High | IT Manager | 60 days |
| GAP-005 | Vulnerability-remediation deadlines are not formally defined by severity. | High | Engineering Manager | 60 days |
| GAP-006 | Third-party security evidence and remediation items are not centrally tracked. | Moderate | Vendor Risk Owner | 90 days |
| GAP-007 | Incident-response exercises are not conducted on a recurring schedule. | Moderate | IT Manager | 90 days |

## Detailed Findings

### GAP-001: Privileged Multifactor Authentication

**Current state:** Multifactor authentication is available but is not confirmed for every administrative and privileged account.

**Target state:** Multifactor authentication is required for all privileged accounts, remote access, and sensitive cloud services.

**Recommended actions:**

1. Inventory all privileged accounts.
2. Enforce multifactor authentication.
3. Remove unnecessary administrative privileges.
4. Review privileged access quarterly.

**Expected evidence:**

- Privileged-account inventory
- Multifactor-authentication configuration screenshots
- Quarterly access-review records

**Framework alignment:**

- NIST Cybersecurity Framework 2.0 access-control practices
- ISO/IEC 27001:2022 identity and access-management controls

### GAP-002: Access Reviews and Offboarding

**Current state:** Account termination and access reviews depend on manual communication between Human Resources and Information Technology.

**Target state:** Access is removed promptly when employment ends, and user access is formally reviewed every quarter.

**Recommended actions:**

1. Create a documented offboarding checklist.
2. Define account-deactivation deadlines.
3. Maintain a centralized account inventory.
4. Perform quarterly access reviews.

**Expected evidence:**

- Completed offboarding checklists
- Account-deactivation records
- Quarterly access-review reports

**Framework alignment:**

- NIST Cybersecurity Framework 2.0 identity-management practices
- ISO/IEC 27001:2022 access-rights controls

### GAP-003: Centralized Logging and Monitoring

**Current state:** AWS, Microsoft 365, and application logs are stored separately, limiting centralized detection and investigation.

**Target state:** Security-relevant logs are centralized, retained, reviewed, and connected to actionable alerts.

**Recommended actions:**

1. Define logging and retention requirements.
2. Centralize critical cloud and application logs.
3. Configure alerts for suspicious activity.
4. Test alert effectiveness quarterly.

**Expected evidence:**

- Logging standard
- Log-source inventory
- Alert configuration records
- Detection-testing results

**Framework alignment:**

- NIST Cybersecurity Framework 2.0 detection and continuous-monitoring practices
- ISO/IEC 27001:2022 logging and monitoring controls

### GAP-004: Backup Restoration Testing

**Current state:** Backups are scheduled, but restoration testing is not consistently documented.

**Target state:** Critical systems have tested backups, documented recovery objectives, and verified restoration procedures.

**Recommended actions:**

1. Define recovery-time and recovery-point objectives.
2. Test restoration procedures quarterly.
3. Maintain protected or immutable backup copies.
4. Document test results and corrective actions.

**Expected evidence:**

- Backup policy
- Restoration-test reports
- Recovery objectives
- Corrective-action records

**Framework alignment:**

- NIST Cybersecurity Framework 2.0 recovery-planning practices
- ISO/IEC 27001:2022 backup and continuity controls

### GAP-005: Vulnerability Remediation

**Current state:** Vulnerabilities may be identified, but formal remediation deadlines are not assigned according to severity.

**Target state:** Vulnerabilities are prioritized, assigned, tracked, and remediated within documented service-level targets.

**Recommended actions:**

1. Establish severity-based remediation deadlines.
2. Assign vulnerability owners.
3. Track exceptions and risk acceptances.
4. Report overdue findings to management.

**Expected evidence:**

- Vulnerability-management standard
- Scan reports
- Remediation tickets
- Risk-acceptance records

**Framework alignment:**

- NIST Cybersecurity Framework 2.0 risk-assessment and platform-security practices
- ISO/IEC 27001:2022 vulnerability-management controls

### GAP-006: Third-Party Risk Tracking

**Current state:** Vendor assessments are performed, but evidence requests, findings, and remediation dates are not centrally tracked.

**Target state:** Critical vendors are assessed before approval and monitored throughout the relationship.

**Recommended actions:**

1. Maintain a centralized vendor inventory.
2. Track security evidence and findings.
3. Define reassessment frequencies.
4. Monitor remediation deadlines and material vendor changes.

**Expected evidence:**

- Vendor inventory
- Completed assessments
- SOC 2 or equivalent reports
- Vendor-remediation tracker

**Framework alignment:**

- NIST Cybersecurity Framework 2.0 supply-chain risk-management practices
- ISO/IEC 27001:2022 supplier-relationship controls

### GAP-007: Incident-Response Testing

**Current state:** Incident-response responsibilities exist informally, but recurring exercises are not documented.

**Target state:** RouteShield maintains an approved incident-response plan and tests it at least annually.

**Recommended actions:**

1. Document incident roles and escalation procedures.
2. Define internal and external notification requirements.
3. Conduct an annual tabletop exercise.
4. Track lessons learned and corrective actions.

**Expected evidence:**

- Incident-response plan
- Contact and escalation list
- Tabletop-exercise report
- Corrective-action tracker

**Framework alignment:**

- NIST Cybersecurity Framework 2.0 incident-management practices
- ISO/IEC 27001:2022 incident-management controls

## Prioritized Remediation Roadmap

### First 30 Days

- Enforce privileged multifactor authentication.
- Complete the privileged-account inventory.
- Implement the formal offboarding checklist.
- Begin quarterly access reviews.

### Days 31-60

- Centralize critical security logs.
- Define logging-retention requirements.
- Test backup restoration.
- Establish vulnerability-remediation deadlines.

### Days 61-90

- Centralize vendor-risk tracking.
- Complete outstanding vendor evidence requests.
- Finalize the incident-response plan.
- Conduct a tabletop exercise.

### Ongoing

- Review risks quarterly.
- Track remediation evidence.
- Report overdue actions to management.
- Reassess controls after major business or technology changes.

## Overall Conclusion

RouteShield Technologies has established foundational cybersecurity practices, but several controls require greater consistency, documentation, and evidence.

The highest priorities are privileged-access protection, reliable offboarding, centralized monitoring, tested recovery procedures, and formal vulnerability-remediation timelines.

## Disclaimer

This security gap analysis, organization, findings, and remediation activities are fictional and were created solely for educational and professional portfolio purposes.
