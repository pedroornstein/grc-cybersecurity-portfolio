# RouteShield Technologies — Remediation Action Tracker

> **Fictional GRC portfolio case study.** All findings, ownership, remediation actions, dates, and evidence below are simulated. Nothing in this tracker is a representation of actual testing, remediation, or audit assurance.

## Objective and Scope

Translate the [security gap analysis](../05-security-gap-analysis/security-gap-analysis.md) into assigned, trackable actions tied to the [risk register](../02-risk-register/risk-register.md). This demonstrates a typical GRC follow-up process: identify gaps, assign accountability, monitor milestones, validate evidence, and escalate exceptions.

**Baseline:** Day 0 of the illustrative remediation program. Targets below are **relative**, not real-world due dates. All actions initially remain **Planned / Not verified**.

## Action Tracker

| Action ID | Source Gap | Related Risk | Priority | Accountable Owner | Target | Proposed Remediation | Completion Evidence | Status |
|---|---|---|---|---|---|---|---|---|
| ACT-001 | GAP-001 Privileged MFA | R-001 | High | IT Manager | Day 30 | Inventory privileged identities, enforce MFA, review exceptions | Privileged account inventory; configuration export; exception approvals | Planned — not verified |
| ACT-002 | GAP-002 Offboarding/access review | R-005 | High | HR and IT Managers | Day 30 | Approve offboarding workflow and access revocation SLAs; run access review | Approved checklist; sampled termination tickets; signed access-review report | Planned — not verified |
| ACT-003 | GAP-003 Logging/monitoring | R-009 | High | IT Manager | Day 60* | Define critical log sources, centralize collection, enable alerts and test detections | Log source inventory; retention policy; alert test results | Planned — not verified |
| ACT-004 | GAP-004 Backup restore tests | R-010, R-004 | High | IT Manager | Day 60* | Establish RTO/RPO and carry out documented restore test | Approved recovery objectives; restore-test log; results and corrective actions | Planned — not verified |
| ACT-005 | GAP-005 Vulnerability SLAs | R-008 | High | Engineering Manager | Day 60* | Adopt severity-based remediation SLAs and exception workflow | Approved standard; sample vulnerability tickets; aging report | Planned — not verified |
| ACT-006 | GAP-006 Vendor tracking | R-003, R-006 | Moderate | Vendor Risk Owner | Day 90 | Centralize critical vendor inventory, findings, evidence requests, and review dates | Vendor register; evidence request log; follow-up approvals | Planned — not verified |
| ACT-007 | GAP-007 Incident exercises | R-004 | Moderate | IT Manager | Day 90 | Approve incident response plan, perform tabletop, document lessons learned | Approved IR plan; exercise agenda; after-action report; action register | Planned — not verified |

*** Exception required:** High-priority actions ACT-003, ACT-004 and ACT-005 have proposed Day 60 targets rather than the preferred Day 30 target. This is a *proposed, unapproved* schedule extension. The accountable owner must record rationale, interim compensating safeguards, residual risk, a decision-maker, and approval before accepting these deadlines. Until then, the extensions are **pending**, not accepted.

## Milestones and Validation

| Window | Checkpoint | Verification Standard |
|---|---|---|
| Day 0–15 | Establish action owners, work plans, and high-priority risk escalation | Written acknowledgements; tracked dependencies; exception requests |
| Day 16–30 | Review completion of ACT-001 and ACT-002 | Inspect configuration exports and sampled access records; document test result |
| Day 31–60 | Review ACT-003 to ACT-005, subject to formal exception approval | Validate log ingestion and alerts, restored sample, and vulnerability SLA workflow |
| Day 61–90 | Review ACT-006 and ACT-007 | Inspect vendor tracker and tabletop after-action report |
| Quarterly thereafter | Reassess residual risks, overdue actions, and effectiveness | Updated risk register; evidence references; management review minutes |

## Review Rules

1. **Owner accountability:** The action owner implements and supplies evidence. The GRC reviewer tracks and verifies completion independently where practicable.
2. **Status definitions:** `Planned` → `In progress` → `Ready for validation` → `Closed (verified)`; use `Blocked` or `Risk accepted` only with documented justification.
3. **Closure threshold:** No item becomes `Closed (verified)` solely because an owner reports completion. The reviewer checks relevant artifacts against the acceptance criteria and records a review date.
4. **Escalation:** Overdue high-priority actions and unapproved deadline exceptions go to the designated risk owner and management.
5. **Residual risk:** After successful validation, rescore likelihood and impact in the risk register. Never assume a reduction without a defensible assessment.
6. **Evidence handling:** In a real engagement, store evidence in an access-controlled location. This public repository contains **examples only**, not credentials, personal data, vendor reports, or sensitive security configurations.

## Management Status Summary (Illustrative)

- Total proposed actions: **7**
- High priority: **5**; Moderate priority: **2**
- Proposed Day 30: **2**; Day 60: **3**; Day 90: **2**
- Verified closed: **0**
- High-priority deadline exceptions requiring approval: **3**

*This tracker is a case-study deliverable, not a claim that remediation work has been performed at a real company.*
