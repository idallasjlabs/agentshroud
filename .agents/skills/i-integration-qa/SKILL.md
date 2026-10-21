---
name: i-integration-qa
description: "Playbook for the i-integration-qa agent: integration, regression, smoke, migration apply+rollback, contract/API, ETL, VCR replay and flaky-test detection through scripts/testing/run-integration.sh and smoke.sh. Replaces the integration half of the deprecated i-qa."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: Integration and regression QA (PR/CI)

The `i-integration-qa` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Run `scripts/testing/run-integration.sh --json` (`I_INTEGRATION_CMD` overrides detection).
2. Run `scripts/testing/smoke.sh --json` (`I_SMOKE_CMD` or `I_SMOKE_URLS`).
3. Migrations: apply, verify, then roll back and verify again; attach both outputs.
4. Re-run failures once to classify flaky vs real; quarantine flaky tests with a ticket.
5. Retest each defect fix and record the result.

Output: integration/regression report, migration evidence, flaky list.

## Owned testing types

See the `i-integration-qa` agent for the ranked checklist.
