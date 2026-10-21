---
name: i-data-ai-ot
description: "Playbook for the i-data-ai-ot agent: data reconciliation and SQL fixtures, scan-cost checks, LLM prompt-injection/guardrail/eval tests, and OT telemetry validation via scripts/testing/sql-fixtures.sh, eval-run.sh and telemetry-check.sh. HIL and safety-function tests are human-run."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: Data, AI/LLM and OT/BESS testing (any stage)

The `i-data-ai-ot` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Data: `scripts/testing/sql-fixtures.sh --json` (lint, fixtures, full-scan heuristics); reconcile source vs target counts and checksums; check schema evolution for drift.
2. AI/LLM: `scripts/testing/eval-run.sh --json` on golden sets; test prompt injection, tool-permission guardrails, RAG retrieval, structured-output validation and cost/latency budgets.
3. OT/BESS: `scripts/testing/telemetry-check.sh --spec <spec.json> <files>` for range, timestamp and unit validation; write protocol and segmentation test plans.
4. HIL and safety-function tests: write the procedure and mark it HUMAN-RUN; never report a simulated pass.

Output: reconciliation, eval and telemetry results, human-run test plans.

## Owned testing types

See the `i-data-ai-ot` agent for the ranked checklist.
