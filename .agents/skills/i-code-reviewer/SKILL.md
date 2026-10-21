---
name: i-code-reviewer
description: "Playbook for the i-code-reviewer agent: mandatory system-wide change impact analysis via scripts/testing/impact-map.sh, then peer review with lint, complexity and production-safety checks. Replaces the deprecated i-cr."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: Code review and impact analysis (Pre-commit)

The `i-code-reviewer` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Run `scripts/testing/impact-map.sh --base main --json` and, for the write-up, `scripts/testing/impact-map.sh --base main` (markdown). Paste it as section 10 of `.impact-analysis/<branch>.md` ("Change Impact Analysis (i-code-reviewer)").
2. For each changed file list consumers, jobs, tables, queries and schedules affected; flag SQL/pipeline/prompt/OT paths for `/i-data-ai-ot`.
3. Review the diff as the reviewer, not the author: correctness, readability, the 400-line rule, lint and complexity.
4. Production safety: blast radius, rollback path, test isolation, Athena cost guards (LIMIT / partition WHERE), IAM least privilege.
5. Report findings by severity with concrete fixes.

Output: impact analysis section, review findings, rollback path.

## Owned testing types

See the `i-code-reviewer` agent for the ranked checklist.
