---
name: i-test-architect
description: "Playbook for the i-test-architect agent: draft the threat model, review requirements for testability, build the traceability matrix and Given/When/Then criteria, and review schema/API contracts and privacy before implementation starts."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: Test architecture (Plan stage)

The `i-test-architect` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Read the ticket/PRD and design notes; list each requirement with an ID.
2. Draft the threat model (assets, trust boundaries, abuse cases); reuse `/i-sec-defense` for STPA-Sec.
3. Mark each requirement testable or not; write Given/When/Then criteria with `/i-bdd`.
4. Build the traceability matrix (requirement → test → evidence) in `docs/` or the PR.
5. Review schema/API changes for backward compatibility; run the privacy checklist.
6. Hand the criteria to `/i-unit-tdd`. If SQL, pipelines, prompts or OT paths are involved, also invoke `/i-data-ai-ot`.

Output: threat model, traceability matrix, acceptance criteria, open questions.

## Owned testing types

See the `i-test-architect` agent for the ranked checklist.
