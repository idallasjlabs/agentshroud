---
name: i-unit-tdd
description: "Playbook for the i-unit-tdd agent: red-green-refactor TDD with type checks, coverage, property-based, mutation, component and snapshot tests. Run through scripts/testing/run-unit.sh. Replaces the deprecated i-tdd."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: Unit-level TDD (Implement stage)

The `i-unit-tdd` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Take the acceptance criteria and write the failing test first; run it and show it fail.
2. Implement the minimum code to pass; refactor with tests green.
3. Run the gate: `scripts/testing/run-unit.sh --json` (set `I_UNIT_CMD` to override detection; `I_GATE=block` to fail the stage).
4. Check types and coverage (≥80% on new/modified code); add property-based tests for invariants and mutation tests for critical logic.
5. Review snapshot/golden diffs by hand before accepting a new baseline.

Output: failing-then-passing test evidence, coverage and mutation summary, run-unit.sh JSON.

## Owned testing types

See the `i-unit-tdd` agent for the ranked checklist.
