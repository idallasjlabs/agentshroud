---
name: i-security-scanner
description: "Playbook for the i-security-scanner agent: run Semgrep, gitleaks, Trivy and Checkov through scripts/testing/sec-scan.sh, add SCA and authn/authz checks, and use DAST on staging only. Defers secrets and git safety to i-gg."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: Security scanning (Pre-commit)

The `i-security-scanner` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Run `scripts/testing/sec-scan.sh --json`. Missing scanners are reported as skipped with a warning — install them rather than accept a skipped scan for a release.
2. Secrets and git safety: invoke `/i-gg`; do not duplicate it.
3. SCA: review dependency and license findings; IaC: Checkov results; containers: Trivy image scan.
4. Authn/authz: test least privilege, object-level access and privilege escalation paths.
5. DAST: only against an explicit staging URL.

Output: per-tool results, severity-ranked findings, remediation list.

## Owned testing types

See the `i-security-scanner` agent for the ranked checklist.
