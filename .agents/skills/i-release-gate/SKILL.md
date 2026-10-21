---
name: i-release-gate
description: "Playbook for the i-release-gate agent: operational readiness, compliance evidence, RC regression, deploy and rollback verification, SBOM/signature/provenance and license checks, post-deploy smoke and canary analysis via scripts/testing/release-check.sh, sbom-verify.sh and smoke.sh. Replaces the deprecated i-prod-safety."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: Release gate (Release / post-deploy)

The `i-release-gate` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Run `scripts/testing/release-check.sh --json` (clean tree, branch, impact analysis, rollback plan, changelog).
2. Run `scripts/testing/sbom-verify.sh --json` (SBOM validity, signature/provenance when tools are present, license check).
3. Confirm the full RC regression passed (`i-integration-qa`, `i-system-nfr`).
4. Before deploy: backup taken, rollback verified. After deploy: `scripts/testing/smoke.sh` immediately, then canary analysis.
5. Record go/no-go with evidence; exceptions are written down, never hidden.

Output: go/no-go record, smoke and canary results.

## Owned testing types

See the `i-release-gate` agent for the ranked checklist.
