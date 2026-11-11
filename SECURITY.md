# Security Policy

## Scope

This is a **public educational portfolio**, not a production service. RouteShield Technologies, its users, and its control-testing data are fictional. The code currently consists of a synthetic offboarding CSV analyzer and documentation validator; no live service or authentication endpoint is provided by this repository.

## Reporting a suspected vulnerability

**Do not publish working credentials, personal data, or exploit details in a public GitHub issue.** Contact the repository owner privately through GitHub profile contact information or a private vulnerability-reporting feature, if enabled. Do not assume a private reporting feature is enabled.

Include:
- Affected file and commit, with a concise description
- Minimal safe reproduction using synthetic data only
- Expected versus observed behavior and potential impact
- Suggested fix, if known

Do not run scans against external websites, real organizations, or systems based on fictional case studies without explicit authorization.

## Current safeguards and limitations

- GitHub Actions uses `permissions: contents: read` and runs the local validator and unit tests.
- The included `.gitignore` blocks many **new accidental local-file additions**, but is **not a secret-scanning control** and does not remove anything already committed.
- All example control evidence is synthetic or illustrative; passing CI does **not** establish live security, SOC 2 or ISO certification, or real-world control effectiveness.
- GitHub account MFA, branch rules, security alerts, secret scanning, and private vulnerability reporting must be checked directly in repository/account settings; their status is **not attested by this document**.
- Before publishing any future materials, manually review for secrets, personal information, proprietary records, and unauthorized target details.

## Remediation practice

Prefer focused pull requests with a documented security rationale, tests where applicable, and review of the resulting CI status before merging.
