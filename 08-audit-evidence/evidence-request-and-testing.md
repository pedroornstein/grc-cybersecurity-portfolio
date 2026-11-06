# RouteShield Technologies — Evidence Request and Control Testing Workbook

> **Portfolio simulation only.** The request lists, testing steps, sample sizes, dispositions, and examples are illustrative. No real evidence has been obtained, no production control has been tested, and no independent assurance conclusion is expressed.

## Engagement Setup

- **Organization:** RouteShield Technologies (fictional)
- **Review scope:** Privileged access, employee offboarding, cloud monitoring, backup recovery, vulnerability remediation, third-party assurance and incident response
- **Illustrative period:** Most recent completed quarter (would be specified for a real engagement)
- **Methodology:** For each control, define objective, population, owner, evidence, sampling criteria, test procedure, exceptions and follow-up
- **Confidentiality:** In real work, evidence should be uploaded to an authorized access-controlled repository and redacted where needed; never publish authentic logs, user records, credentials, vendor SOC 2 reports or sensitive cloud settings here

## Prepared-by-Client Evidence Request List

| Request ID | Related Gap / Risk | Requested artifact | Population / timeframe | Responsible role | Purpose |
|---|---|---|---|---|---|
| PBC-001 | GAP-001 / R-001 | Privileged-account inventory and MFA-enforcement export | All privileged identities, as of a defined date | IT Manager | Verify privileged MFA coverage |
| PBC-002 | GAP-002 / R-005 | Termination register, HR exit notices and deprovisioning timestamps | All departures in review quarter | HR and IT | Test offboarding timeliness |
| PBC-003 | GAP-002 / R-005 | Quarterly access-review sign-offs and exception remediation | In-scope systems, review quarter | IT Manager | Verify review execution and approvals |
| PBC-004 | GAP-003 / R-009 | Log-source inventory, retention standard and sample alert case | Critical environments, review quarter | Security Operations | Check monitoring design and operation |
| PBC-005 | GAP-004 / R-010 | Backup policy, recovery objectives and restore-test record | Critical systems, last completed cycle | IT / Operations | Assess recoverability evidence |
| PBC-006 | GAP-005 / R-008 | Vulnerability scan export, remediation policy and tickets | In-scope assets, review quarter | Engineering Manager | Test severity-based remediation |
| PBC-007 | GAP-006 / R-003 | Critical vendor inventory, due-diligence log and exceptions | Critical vendors, current review period | Vendor Risk Owner | Trace vendor oversight |
| PBC-008 | GAP-007 / R-004 | Incident-response plan, tabletop attendance and after-action report | Most recent exercise if one exists | IT Manager | Check exercise cadence and action tracking |

**Request status:** All eight are **Not requested — simulation**. No request is fulfilled by this workbook.

## Testing Matrix

| Test ID | Control objective | Illustrative test procedure | Example acceptance criteria | Potential exception |
|---|---|---|---|---|
| TC-001 | Privileged access secured with MFA | Reconcile full privileged inventory against effective MFA / conditional-access settings; inspect documented exclusions | Every in-scope privileged account protected, or exceptions approved and compensating safeguards demonstrated | Unprotected emergency/admin account |
| TC-002 | Timely employee deprovisioning | Select departures from HR population; compare exit effective time to identity disablement across in-scope systems | Meets formally approved offboarding SLA; all deviations tracked | Identity disabled after the allowed window |
| TC-003 | Quarterly access review | Inspect review population, reviewer independence, sign-off and remediation of discrepancies | Complete timely review with traceable actions | Unreviewed privileged access |
| TC-004 | Security monitoring | Reconcile expected log sources to actual ingestion; inspect sample detection alert and response timestamps | Log sources present and alert triage documented within approved standard | Missing log source or untriaged alert |
| TC-005 | Backup restoration | Inspect scheduled restore-test evidence for a selected critical system | Evidence shows successful integrity validation against approved RTO/RPO | Only backup-job success, no restore |
| TC-006 | Vulnerability management | Compare sample findings' detection dates, severity, SLAs, tickets and closure/exception approval | Critical/high findings meet approved SLA or valid exceptions | Overdue high-risk finding without approval |
| TC-007 | Vendor assurance | Trace critical vendor classification to due diligence, findings, approvals and reassessment date | Review is documented and approvals/conditions traceable | Critical vendor approved with unresolved unaccepted risk |
| TC-008 | Incident-response readiness | Inspect current plan, exercise attendance, scenarios, after-action review and corrective tracking | Approved plan; evidence of exercise and closed/owned findings | Exercise claimed without supporting documentation |

## Sampling Guidance

Sampling is risk-based and **not a fixed assurance formula**. For a real engagement:
1. Define the full population and verify its completeness before choosing items.
2. Choose a documented approach (for example, full-population inspection for privileged accounts; targeted/risk-based samples plus random items for departures and tickets).
3. Include elevated-risk items, exceptions and boundary dates.
4. Record sample IDs and why each was selected.
5. Escalate population deficiencies; a missing or unreliable population may prevent valid conclusions.

## Working Paper / Test Result Template

| Field | Entry |
|---|---|
| Test ID / control owner | |
| Objective / risk ID / framework reference | |
| Period and system scope | |
| Complete population source and count | |
| Sample methodology and selected IDs | |
| Procedure performed and date | |
| Evidence reference (restricted repository) | |
| Observation / exceptions | |
| Result: Pass / Fail / Inconclusive / Not tested | **Not tested** |
| Reviewer / review date | |
| Remediation action and responsible owner | |

## Example of Proper Evidence Language

**Avoid:** “SOC 2 compliant,” “MFA verified across all accounts,” or “Backups passed” when no evidence was collected.

**Use:** “The scenario proposes privileged MFA as a target control; implementation and operating effectiveness remain unverified.”

## Reporting and Follow-up

Map genuine exceptions to the [remediation action tracker](../06-remediation-tracker/remediation-tracker.md). Any future realistic sample finding must be clearly tagged **fictional**, with assumptions stated. A control should not be marked effective without sufficient, appropriate evidence and a documented test basis.
