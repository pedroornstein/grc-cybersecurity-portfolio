# Synthetic Offboarding Control Test — Reproducible Example

> **Entirely fictional dataset and test.** No employee identity, actual human-resources record, production account, or customer data was used. Running the script constitutes a real computation on **fabricated test data**, not an assurance engagement.

## Control Question

For the fictional RouteShield scenario, do **Microsoft 365 identity disablement timestamps** occur within an **illustrative four-hour maximum** following recorded termination? The four-hour interval is a **case-study assumption**, not a universal regulatory standard or corporate policy.

This test is related to [R-005](../02-risk-register/risk-register.md), [GAP-002](../05-security-gap-analysis/security-gap-analysis.md), and [ACT-002](../06-remediation-tracker/remediation-tracker.md). It demonstrates one technique from the [audit-evidence testing plan](../08-audit-evidence/evidence-request-and-testing.md).

## Evidence, Scope and Script

- `synthetic-offboarding.csv`: twelve deliberately fabricated, unique case IDs; UTC timestamps and a single hypothetical system.
- `analyze_offboarding.py`: standard-library Python script with strict UTC parsing, ID validation, SLA calculation and JSON/text output.
- Scope: **one system and one generated dataset**. It does not reconcile HR population completeness, account inventory, other systems, actual approved SLAs, or identities with multiple accounts.

## Run

From the repository root, with Python 3.10 or later:

```bash
python 11-synthetic-offboarding-test/analyze_offboarding.py
python 11-synthetic-offboarding-test/analyze_offboarding.py --json
```

No installs or internet access required.

## Expected Deterministic Results

| Outcome | Count | Meaning |
| --- | ---: | --- |
| Within illustrative four-hour SLA | 9 | `PASS` |
| Disablement recorded after four hours | 2 | `LATE` — hypothetical exceptions |
| No disablement timestamp supplied | 1 | `MISSING_EVIDENCE` — inconclusive; investigate, do not assume active access |
| **Total** | **12** | Synthetic population only |

Specific follow-ups: inspect `SYN-004` and `SYN-009` for tardy records; seek the source record or authorized alternative evidence for `SYN-006`. Nothing in this fabricated dataset proves real security impact or real employee access.

## Procedure and Judgment

1. Define control objective, eligible population, observation period, scope and approved timeliness criterion.
2. Confirm source-population completeness and integrity **before** using production records for conclusions.
3. Compare termination and disablement timestamps in a common UTC format.
4. Recalculate elapsed time and separate failures from evidence gaps.
5. Document exceptions with responsible owners, impact, reviewer, follow-up due date and approval.
6. Retest corrective actions before any closure or residual-risk adjustment.

## Critical Limitations

- Synthetic data was **designed** to have nine passes, two late cases and one missing timestamp; it is not a random sample and estimates no real-world failure rate.
- A negative elapsed time is rejected as invalid data; identical timestamps count as meeting the limit.
- The script tests the timestamps it receives. A missing timestamp is **not** proof the identity was never disabled.
- In a real assessment, source-system time accuracy, timezone, population reconciliation, other SaaS applications, service accounts, privileged identities and rehires would require additional procedures.
- The sample outcome is **not** a control effectiveness opinion, an audit conclusion, or completed real-world remediation.

**Interview talking point:** "I designed and ran a repeatable test against intentionally synthetic identity-offboarding records, explained the observed exceptions, and separated missing evidence from confirmed SLA misses."
