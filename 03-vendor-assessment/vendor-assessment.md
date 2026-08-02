# RouteShield Technologies Vendor Security Assessment

## Assessment Overview

This assessment evaluates a fictional payment-processing vendor used by RouteShield Technologies.

- **Vendor:** BlueHarbor Payment Services
- **Service:** Third-party payment processing
- **Business owner:** Finance Manager
- **Technical owner:** IT Manager
- **Assessment type:** Initial vendor security review
- **Vendor criticality:** High
- **Assessment status:** Conditionally approved

## Vendor Relationship

BlueHarbor Payment Services processes customer payment transactions for RouteShield’s transportation SaaS platform.

The vendor:

- Connects to RouteShield through an application programming interface
- Processes payment-related information
- Supports customer transactions
- Stores limited customer and transaction information
- Does not receive RouteShield employee credentials
- Could affect revenue and customer service if unavailable

## Data Classification

| Data Type | Vendor Access | Classification |
|---|---|---|
| Customer names | Limited | Confidential |
| Customer contact information | Limited | Confidential |
| Payment-related information | Yes | Restricted |
| Transaction records | Yes | Confidential |
| Employee records | No | Not applicable |
| RouteShield login credentials | No | Not applicable |

## Security Assessment

| ID | Security Domain | Assessment Question | Vendor Response / Evidence | Rating |
|---|---|---|---|---|
| VA-001 | Governance | Does the vendor maintain documented information-security policies? | Vendor reports annual policy review and executive approval. | Satisfactory |
| VA-002 | Independent Assurance | Does the vendor maintain a current SOC 2 Type II report or equivalent assurance? | SOC 2 Type II report provided for review. | Satisfactory |
| VA-003 | Access Control | Is multifactor authentication required for administrative and privileged access? | MFA is required for administrative accounts. | Satisfactory |
| VA-004 | Encryption | Is sensitive information encrypted in transit and at rest? | TLS is used in transit, and stored sensitive data is encrypted. | Satisfactory |
| VA-005 | Vulnerability Management | Are vulnerability scans and penetration tests performed regularly? | Quarterly scanning and annual penetration testing reported. | Satisfactory |
| VA-006 | Incident Response | Does the vendor maintain and test an incident-response plan? | Documented plan exists, but evidence of the most recent exercise was not provided. | Needs Improvement |
| VA-007 | Breach Notification | Is RouteShield notified promptly after a confirmed security incident? | Contract requires notification within 72 hours. | Satisfactory |
| VA-008 | Business Continuity | Are continuity and disaster-recovery procedures documented and tested? | Procedures exist; summary results from the latest recovery test were provided. | Satisfactory |
| VA-009 | Backup and Recovery | Are backups protected and restoration procedures tested? | Encrypted backups and annual restoration testing reported. | Satisfactory |
| VA-010 | Subprocessors | Does the vendor identify and assess subcontractors that process RouteShield information? | Vendor maintains a subprocessor list, but advance change notification is limited. | Needs Improvement |
| VA-011 | Data Retention | Are customer and transaction records deleted according to defined retention requirements? | Retention schedule exists, but deletion evidence was not provided. | Needs Improvement |
| VA-012 | Termination | Can RouteShield data be returned or securely deleted when the contract ends? | Contract supports data return and deletion upon termination. | Satisfactory |

## Identified Findings

| Finding ID | Finding | Risk Level | Recommended Action | Owner | Target |
|---|---|---|---|---|---|
| F-001 | Evidence of the vendor’s most recent incident-response exercise was not provided. | Moderate | Obtain an executive summary or attestation from the latest exercise. | IT Manager | Before annual reassessment |
| F-002 | RouteShield may not receive adequate advance notice of new subprocessors. | Moderate | Add contractual notification and objection requirements. | Legal and IT Managers | Contract renewal |
| F-003 | Evidence confirming secure deletion according to the retention schedule was not provided. | Moderate | Request deletion procedures and supporting evidence. | IT Manager | Within 90 days |

## Overall Risk Evaluation

- **Inherent vendor risk:** High
- **Control effectiveness:** Generally effective
- **Residual vendor risk:** Moderate
- **Decision:** Conditionally approve
- **Review frequency:** Annually and after significant service or security changes

## Approval Conditions

BlueHarbor Payment Services may remain approved provided that RouteShield:

1. Tracks the three identified findings.
2. Reviews the vendor’s SOC 2 report annually.
3. Confirms incident and breach-notification requirements contractually.
4. Reviews material subprocessor changes.
5. Reassesses the vendor after a major incident or significant service change.

## Framework Alignment

This assessment supports:

- NIST Cybersecurity Framework 2.0 supply-chain risk management
- ISO/IEC 27001:2022 supplier-relationship controls
- SOC 2 security and availability considerations
- RouteShield’s contractual and risk-management requirements

## Disclaimer

The vendor, responses, evidence, findings, and assessment conclusions are fictional and were created solely for educational and professional portfolio purposes.
