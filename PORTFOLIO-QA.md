# Portfolio Quality Assurance Review

**Review date:** November 6, 2026  
**Scope:** Public RouteShield GRC case-study Markdown files and cross-references.  
**Review type:** Documentation consistency check, not a cybersecurity audit or certification.

## Checks Completed

| Check | Method | Result |
|---|---|---|
| Risk-score arithmetic | Recalculated the ten inherent scores as likelihood × impact from the risk-register table | **10/10 consistent** |
| Internal Markdown links | Resolved internal Markdown links across repository documentation using a repeatable Python validator | **0 broken local Markdown links** |
| NIST CSF 2.0 category identifiers | Compared category codes used in the mapping against the official NIST CSF 2.0 Core category set | **No unknown category IDs** |
| Vendor assessment assurance wording | Confirmed that purported SOC 2 evidence, controls and approvals are labeled as fictional and unverified | **Caveats added** |
| Risk scoring context | Clarified that existing controls and residual scores are illustrative rather than independently validated | **Caveats added** |
| Remediation traceability | Mapped seven GAP IDs to seven ACT IDs, and linked payment-vendor sample findings to ACT-006 | **Documented linkage** |
| Reproducible synthetic offboarding test | Executed a Python analyzer on twelve deliberately fictional Microsoft 365 offboarding records | **9 pass / 2 late / 1 missing evidence** |
| Automated continuous checks | GitHub Actions runs the standard-library validator on each push and pull request | **Configured; initial workflow run passed** |

## Material Changes From Review

1. Replaced the vendor statement of general control effectiveness with **Not tested** and made conditional approval explicitly **proposed**.
2. Clarified that controls in the risk register are scenario assumptions. Existing MFA may be partial even when privileged-account MFA remains a gap.
3. Updated NIST CSF category alignment for cloud-configuration exposure and backup recovery (including **PR.DS**, whose subcategory PR.DS-11 addresses backup protection, maintenance and testing).
4. Added malware protection (**ISO A.8.7**) to the ransomware control selection.
5. Cross-referenced hypothetical vendor findings F-001 to F-003 from the third-party assessment within the remediation tracker.
6. Repaired a Markdown footnote in the remediation tracker.
7. Added [repeatable synthetic offboarding analysis](11-synthetic-offboarding-test/README.md) and an automatic [documentation quality workflow](.github/workflows/portfolio-quality.yml).

## Limitations and Outstanding Review Items

- **ISO/IEC 27001:2022:** Control numbers and thematic fit are illustrative; no authoritative licensed text or certified crosswalk has been supplied for an exhaustive line-by-line mapping audit. A qualified reviewer should validate context and any applicable Annex A wording.
- **SOC 2:** No genuine vendor SOC 2 report or independent attestation was examined.
- **Evidence:** No **real** logs, configuration exports, HR data, vulnerability findings, tickets, backup-restore results or authorization records were tested. The scripted example uses **fabricated records only**.
- **Residual risk:** The risk-register estimates have no empirically verified current-state likelihood/impact rationale; they are not audited measurements.
- **Security claims:** Code and document review is not a penetration test, legal conclusion, or assurance opinion.
- **Employment claims:** Portfolio work should be presented as an independently constructed case study rather than professional client experience.

## Reproduction

Run `python scripts/validate_portfolio.py` locally (Python 3.10+) or inspect the repository's [GitHub Actions checks](https://github.com/pedroornstein/grc-cybersecurity-portfolio/actions/workflows/portfolio-quality.yml). The checks cover current Markdown links, ten risk-score calculations, R/GAP/ACT/F relationships, category identifier recognition, simulation labels, and synthetic dataset expected results.

For a manual review:
1. Inspect the [risk register](02-risk-register/risk-register.md) and verify that the inherent score equals likelihood × impact for each row.
2. Open the [portfolio index](README.md) and navigate all eleven linked artifacts.
3. Compare the category codes in the [control map](04-control-mapping/control-mapping.md) to [NIST CSF 2.0, Appendix A](https://doi.org/10.6028/NIST.CSWP.29).
4. Verify that the [vendor assessment](03-vendor-assessment/vendor-assessment.md) discloses the simulation and unverified evidence.
5. Follow GAP, ACT, R and F identifiers across the risk register, gap analysis, remediation tracker and vendor assessment.

**This file documents checks of portfolio text, fabricated test data, and internal consistency. It does not claim validation of fictional organizational controls.**
