# Interview Walkthrough — RouteShield GRC Case Study

> **Fictional portfolio exercise.** RouteShield Technologies, BlueHarbor Payment Services, and all associated risk assessments, evidence requests and tabletop materials are simulated. These documents demonstrate analytical skills, not prior employment, verified control operation or an actual audit.

## 30-second introduction

"I built an end-to-end GRC case study for RouteShield, a fictional 75-person transportation SaaS company. I started with business context and ten cyber risks, then documented vendor assurance, NIST CSF 2.0 / ISO 27001 control mapping, seven control gaps, remediation actions, a mock incident-response tabletop, and audit-evidence testing procedures. The goal was to show how I would connect risk, control ownership, evidence and management decisions."

## Five-minute walkthrough

**Minute 1 — Business context and risk prioritization.** Explain the fictitious company, AWS / Microsoft 365 environment, customer platform and third-party payment processor. Show the [risk register](../02-risk-register/risk-register.md); describe the 1–5 likelihood × impact method. The highest inherent score is **R-008 (unpatched platform vulnerability, 20/25)**. These are qualitative scenario assumptions, not empirical probabilities.

**Minute 2 — Third-party assessment.** Open the [BlueHarbor assessment](../03-vendor-assessment/vendor-assessment.md). Explain business criticality, data sensitivity, conditional approval and three hypothetical follow-up findings. Stress that all SOC 2/evidence descriptions are fictional and do not represent a real report.

**Minute 3 — Control mapping and gaps.** Show [control mapping](../04-control-mapping/control-mapping.md) and [gap analysis](../05-security-gap-analysis/security-gap-analysis.md). Discuss privileged MFA, offboarding, logging, restore testing and vulnerability remediation. Framework references guide the control design; a mapping does not prove implementation or compliance.

**Minute 4 — Audit test design and remediation.** In the [evidence request workbook](../08-audit-evidence/evidence-request-and-testing.md), explain how to validate the population first, pick samples with documented rationale, inspect appropriate artifacts, and distinguish Pass, Fail, Inconclusive and Not Tested. Use the [action tracker](../06-remediation-tracker/remediation-tracker.md) to show owners, acceptance criteria and how overdue high-severity items are escalated.

**Minute 5 — Incident response and management decisions.** Use the [tabletop plan](../07-incident-response-tabletop/tabletop-exercise.md) to explain containment, evidence preservation, cross-functional response, recovery validation and cautious communications. End with the [risk-treatment memo](../09-risk-treatment-decisions/risk-treatment-memo.md): recommend prioritized action, but do **not** claim residual risk decreased before validation.

## Three defensible examples to discuss

### 1. R-008 — Vulnerability management
- **Problem:** A critical inherent risk score of 20/25 for an exploitable platform vulnerability.
- **Approach:** Define severity-based SLAs, track remediation tickets, establish approval for exceptions, and inspect samples against approved target dates.
- **Success criteria:** Policy approved, population complete, findings traceable to closure or accepted exceptions.
- **Unknown:** Actual operating effectiveness; no real vulnerability scans or sample tickets have been reviewed.

### 2. R-005 — Employee offboarding
- **Problem:** Retained access after employee departure.
- **Approach:** Reconcile HR terminations against identity disablement timestamps across in-scope systems.
- **Success criteria:** Evidence demonstrates prompt removal within an approved SLA, with remediation of exceptions.
- **Unknown:** No real HR records or account deactivation data exist in the simulated project.

### 3. R-006 — Payment processor continuity
- **Problem:** Business interruption from an external processor outage.
- **Approach:** Assess contractual SLAs, business continuity, vendor concentration, alternatives and monitoring. Obtain assurances from an authorized vendor owner.
- **Success criteria:** Conditional approval has tracked follow-ups and functioning continuity evidence.
- **Unknown:** No genuine BlueHarbor assurance documents exist.

## Tough interview questions and suggested answer directions

**"Was this a real client engagement?"**  
"No. RouteShield and BlueHarbor are fictional, and the artifacts are explicitly marked as simulations. They are designed to demonstrate how I structure GRC work, not to imply prior audit engagements."

**"Why can't you say your controls are effective?"**  
"A recommendation or framework reference is not operating-effectiveness evidence. I would request a complete population, inspect samples and exceptions, document scope and determine whether the control actually worked."

**"How did you decide the risk scores?"**  
"They are illustrative relative assessments using likelihood × impact. In a real environment I'd first agree on risk scales with the business, document assumptions and validate the ratings with relevant owners."

**"What would you improve first?"**  
"I'd verify privileged access and prioritize vulnerability remediation while preserving business service. I'd also define a measurable testing and exception process, rather than claiming risks were reduced on paper."

**"What is the difference between inherent and residual risk?"**  
"Inherent risk is assessed before considering safeguards; current residual risk requires credible evidence about safeguards that already exist and operate. Target residual risk is a proposal, not an achieved outcome."

**"What is SOC 2?"**  
"An attestation framework for relevant trust services criteria. A report's scope, opinion, exceptions, period, complementary user-entity controls and subservice providers must be assessed before relying on it."

## Resume and LinkedIn project wording

**GRC Cybersecurity Portfolio — Independent Simulated Case Study**  
"Developed an end-to-end cybersecurity GRC case study for a fictional transportation SaaS organization, including a ten-risk register, supplier assessment, NIST CSF 2.0 / ISO 27001 control alignment, remediation tracking and evidence-based audit testing plans."

Avoid: claiming a completed audit, implemented controls, achieved risk reductions, client engagement, certification or production incident response.

## Accuracy and Integrity Checklist

- [ ] Every case-study artifact states its fictional scope
- [ ] Risk / gap / action IDs cross-reference correctly
- [ ] NIST CSF category references match the official NIST CSF 2.0 Core
- [ ] ISO controls use the correct 2022 Annex A identifiers and are verified with an authorized copy
- [ ] All external links work and local Markdown links resolve
- [ ] No internal data, credentials or real customer information are exposed
- [ ] Profile, resume and LinkedIn distinguish completed credentials from studies in progress
- [ ] Interview responses avoid claiming real-world control validation

## Reference

[NIST Cybersecurity Framework 2.0 — NIST CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) (official framework reference).
