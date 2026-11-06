# RouteShield Technologies — Cybersecurity Risk Treatment Decision Memo

> **Simulated management decision paper.** Recommendations below are analytical examples, not approvals, completed remediations, or risk acceptances by actual decision makers.

**Audience:** Fictional RouteShield Technology Risk Committee  
**Subject:** Prioritizing privileged access, vulnerability remediation, monitoring, recovery and third-party resilience  
**Source:** [Risk register](../02-risk-register/risk-register.md), [security gap analysis](../05-security-gap-analysis/security-gap-analysis.md), [remediation tracker](../06-remediation-tracker/remediation-tracker.md)

## Executive Decision Requested

Approve **risk-reduction priorities and funded investigation/work planning**, not the unsupported claim that residual risks have already declined. Require accountable owners to provide realistic timelines, compensating safeguards and measurable closure criteria. In the simulated risk register, the strongest inherent exposure is **R-008 (unpatched vulnerability), 20/25**, followed by **R-001 (phishing account compromise), 16/25**.

## Scoring and Important Distinctions

The existing register uses a 1–5 likelihood scale × a 1–5 impact scale (1–25). This is a *qualitative prioritization tool* and not a calibrated financial-loss or actuarial probability estimate.

- **Inherent risk:** Scenario exposure before considering safeguards.
- **Current residual risk:** The exposure after existing safeguards; this must be supported by operational evidence.
- **Target residual risk:** An aspiration if planned treatments work; **not evidence of achieved reduction**.

**Quality caveat:** The original register labels its residual scores without underlying evidence. For this case study, treat all listed residual scores as **scenario estimates pending validation**, not verified assessments.

## Decision Register (Proposed Only)

| Decision ID | Risk | Proposed treatment | Rationale | Accountable owner | Approval gate / verification |
|---|---|---|---|---|---|
| RT-001 | R-008 Critical (20) | **Mitigate** through severity SLAs, tracking and exception process | Highest inherent score; exploitation could affect platform and customer data | Engineering Manager | Approved vulnerability standard; validated ticket samples and management reporting |
| RT-002 | R-001 Critical (16) | **Mitigate** privileged-access and phishing risks | Account compromise is a critical entry path | IT Manager | Verified MFA coverage; documented exceptions; simulations or review results where available |
| RT-003 | R-009 High (12) | **Mitigate** with centralized logging and alert tests | Poor visibility limits incident scoping and response | IT Manager | Log-source reconciliation and detection test |
| RT-004 | R-010 High (15) | **Mitigate** with tested recovery strategy | Backup existence does not prove recoverability | IT + Operations | Restore evidence and approved recovery objectives |
| RT-005 | R-006 High (12) | **Mitigate / transfer selected financial impacts** through vendor SLA and continuity controls | Third-party outage can affect revenue; contractual transfer does not eliminate operational risk | Finance + IT Managers | Contract review and exercised contingency procedure |
| RT-006 | R-003 High (12) | **Mitigate** vendor data risks and track accepted exceptions | Critical provider oversight requires evidence and follow-up | Vendor Risk Owner | Vendor assessment and exception sign-off |

## Recommended Sequencing

**Within 30 days:** Confirm privileged account inventory; implement or validate MFA for admins; establish offboarding and vulnerability exception ownership; request resources for additional remediation.

**Within 60 days (subject to approved extension):** Validate central logging, backup restore capability and severity-based remediation reporting. Require interim protections and documented acceptance of any missed high-priority target.

**Within 90 days:** Formalize critical vendor tracking and complete an incident-response tabletop with a real after-action record if the case study were implemented.

## Risk Acceptance and Exceptions

No high or critical exposure should be silently accepted. Each exception request should specify:
- Risk ID, specific asset and business process
- Decision type (accept, mitigate, avoid or transfer) and why
- Evidence-based assessment of current exposure and duration
- Alternative options and reason for rejection
- Compensating safeguards and interim monitoring
- Accountable business risk owner and authorized approver
- Expiration date, renewal trigger and scheduled reassessment

**In this portfolio no exceptions or residual risk reductions have been actually approved or verified.**

## Sample Decision Record (Unapproved)

| Field | Illustrative entry |
|---|---|
| Request | Extend ACT-003 target from Day 30 to Day 60 |
| Related risk | R-009 |
| Reason | Cross-system log integration dependencies |
| Proposed interim safeguards | Increase manual daily review of critical native alerts and restrict privileged access |
| Evidence still needed | Alert review records, privilege inventory, technical feasibility assessment |
| Approver | **Pending** designated business risk owner |
| Status | **Proposed — not accepted** |
| Expiration | Day 60, subject to explicit approval |

## Questions for Management

1. Which platform services, datasets and customer commitments are most material to business continuity?
2. Can each owner produce credible evidence to establish current control effectiveness?
3. Which treatment options require budget, engineering time or vendor-contract negotiation?
4. Are proposed timelines consistent with the documented risk appetite?
5. Who has authority to accept exposure, and how are exceptions revisited?

## Conclusion

The immediate priority is not to relabel exposure as “low.” It is to assign ownership, deploy defensible safeguards, gather evidence, validate outcomes and **then** rescore residual risk with a documented rationale. The [evidence-testing workbook](../08-audit-evidence/evidence-request-and-testing.md) provides an example mechanism to support this review.
