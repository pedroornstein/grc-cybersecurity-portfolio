# RouteShield Technologies — Ransomware Tabletop Exercise

> **Simulated scenario and illustrative facilitator materials.** No live incident occurred and no actual exercise was conducted. All personnel, decisions, timings and outcomes below are fictional. This is a planning and analysis artifact, not proof of incident-response testing.

## Exercise Charter

- **Scenario:** Ransomware alert and suspected customer-data exposure affecting the dispatch SaaS platform
- **Exercise type:** Discussion-based tabletop (proposed)
- **Participants (roles, not real people):** Incident Commander (IT Manager), Engineering Lead, GRC Analyst, Legal/Privacy Counsel, Operations Lead, Communications Lead, Finance Lead, Vendor Manager
- **Purpose:** Evaluate coordination, evidence preservation, containment, continuity, customer communications and recovery priorities
- **Related risks:** [R-004](../02-risk-register/risk-register.md) (ransomware), R-009 (logging), R-010 (restore failure), R-002 (cloud exposure)
- **Related gaps:** GAP-003, GAP-004, GAP-007 from the [gap analysis](../05-security-gap-analysis/security-gap-analysis.md)

## Background and Assumptions

RouteShield has 75 employees, uses AWS and Microsoft 365, and relies on a web dispatch platform. The scenario assumes potentially affected cloud workloads, possible lateral movement and uncertain data access. No real customer information, credentials or network details are included. RTO/RPO figures must be approved by business owners before any real deployment; they are **not assumed here**.

## Inject Timeline and Decision Log (Illustrative)

| Inject | New information | Expected decision / discussion | Owner | Evidence to preserve |
|---|---|---|---|---|
| T+00 | Security alert indicates unusual file modifications and a suspected ransomware note on a nonproduction-connected workload | Declare severity and incident command; confirm scope; avoid premature attribution | Incident Commander | Detection alert, first-seen timestamp, incident ticket |
| T+15 | Platform response times increase; dispatch customers report intermittent failures | Identify critical services; consider isolating affected workload while preserving dispatch continuity | Engineering + Operations | Service metrics, affected assets list, decision record |
| T+30 | AWS audit trail indicates unusual authentication from a privileged identity | Revoke sessions, rotate exposed credentials using approved procedure, preserve logs; determine whether privilege misuse is confirmed | IT + Cloud Lead | Cloud audit records, access changes, chain-of-custody notes |
| T+60 | Logs are incomplete; there is no conclusive evidence on data exfiltration | State uncertainty explicitly; commission a scoped forensic investigation; start legal/privacy assessment without claiming a breach | Security + Legal | Evidence gaps, investigative questions, counsel decision log |
| T+90 | Primary restoration approach fails a validation check | Activate alternate recovery strategy and test system/data integrity before reconnecting | Recovery Lead | Backup inventory, restore test output, validation findings |
| T+120 | A major customer requests an explanation and timeline | Issue only approved, factual communications; distinguish observed disruption from unconfirmed access to personal information | Communications + Legal | Approved holding statement, approval record |
| T+180 | Contained workload appears stable but investigation remains open | Agree measurable exit criteria, monitoring period and a staged recovery approval | Incident Commander | Recovery checklist, monitoring plan, sign-offs |

## Decision Principles

1. **Protect people and essential service:** Coordinate containment and continuity decisions, recording business impacts.
2. **Preserve evidence:** Capture authorized logs and forensic artifacts before destructive rebuilding where practical; record collection times and access.
3. **Don't infer exfiltration from encryption alone:** The privacy team evaluates facts, jurisdiction and contractual obligations; no blanket notification deadline is assumed.
4. **Avoid ransom-payment assumptions:** Refer any extortion decision to executive, legal, sanctions and law-enforcement review; do not promise decryption, non-disclosure or recovery.
5. **Restore safely:** Validate backups for integrity and malicious persistence; use authorized recovery procedures and explicit go/no-go decisions.
6. **Keep one decision log:** Record the question, options, rationale, owner, time and approver.

## Facilitator Discussion Questions

- Which signal confirms an incident versus a false positive, and who can declare severity?
- What isolation action could protect systems without unintentionally disrupting dispatch?
- Which logging gaps could prevent determination of scope and affected identities?
- Which records must be preserved, who can access them, and how is evidence custody documented?
- What would constitute sufficient assurance to resume customer-facing services?
- Who determines whether any regulatory or contractual notification applies?
- What needs to change in detection rules, backups, vendor obligations and tabletop cadence?

## Proposed Exercise Evaluation Criteria

| Control objective | Example observable success criterion | Evidence expected |
|---|---|---|
| Command and escalation | Incident commander identified; severity and roles recorded | Incident ticket, escalation matrix |
| Identity containment | Privileged identities enumerated and containment steps approved | Access/identity review record |
| Detection and scope | Critical cloud/application log sources identified with gaps called out | Log-source inventory, event timeline |
| Business continuity | Dispatch impact assessed, recovery priorities approved | BIA/RTO/RPO sign-off, continuity decision |
| Backup integrity | Restoration verified before production restart | Restore test record and validation report |
| Communications | Claims are factual and approved by Legal/Privacy | Approval log, draft customer statement |
| Follow-up | Corrective actions assigned, due dates and validation defined | Updated remediation tracker |

## Illustrative After-Action Review — Hypothetical Findings Only

These are **hypothetical facilitator observations**, not actual exercise outcomes.

| Hypothetical observation | Why it matters | Proposed corrective action | Related tracker |
|---|---|---|---|
| Log sources are fragmented across AWS, Microsoft 365 and application workloads | Slows incident scoping | Centralize critical logs, define retention and test alerts | ACT-003 |
| Restore procedures lack repeatable validation evidence | Increases recovery uncertainty | Quarterly documented restore tests and RTO/RPO approval | ACT-004 |
| Notification decision owners are not formally documented | Risks inconsistent communications | Approve incident escalation and Legal/Privacy review matrix | ACT-007 |
| Privileged-session containment is not standardized | Increases exposure time | Inventory privilege and document session-revocation playbook | ACT-001 |

## Reusable Decision Record Template

| Field | Entry |
|---|---|
| Incident ID | `SIM-IR-001` (illustrative) |
| Time / time zone | To be recorded during a real exercise |
| Facts known / confidence | |
| Open questions | |
| Options considered | |
| Decision and rationale | |
| Owner / approver | |
| Impact on services or evidence | |
| Follow-up and due date | |

## Closure and Next Steps

This document is **ready to facilitate a tabletop**, not evidence that one was run. A credible real exercise would require participant attendance, completed decision records, observed performance, a signed after-action report and verified corrective actions. Update [ACT-007](../06-remediation-tracker/remediation-tracker.md) only after those artifacts exist.
