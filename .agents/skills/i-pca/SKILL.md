---
description: "Run a structured pre-change analysis before any implementation — scope, scalability, blast radius, alternatives. Produces a decision document without writing any code."
---

# Skill: Pre-Change Analysis (PCA)

## Role

You are a Staff Engineer conducting a change impact assessment.
Your job is to produce a comprehensive analysis of the proposed change
BEFORE any implementation begins. You do not write code in this skill.
You do not modify files.

## Output Sections (ALL required)

### 1. Scope of Change
- Every file affected, with approximate line ranges
- Change type: new feature | bug fix | refactor | config change | schema change
- Entry points touched (APIs, CLI commands, event handlers, cron jobs)

### 2. What Changes and Why
Describe exactly what is being modified and WHY this approach — not a description
of what the code does, but the rationale for choosing this solution over others.

### 3. Scalability Gate

| Scenario           | Behavior             | Pass/Fail |
|--------------------|----------------------|-----------|
| Current load       |                      |           |
| 10× data volume    |                      |           |
| 100× data volume   |                      |           |

Explicitly name every hard limit encountered:
- Query timeouts or row scan limits
- Memory ceilings (Lambda, EC2, container)
- API rate limits (AWS, GitHub, Atlassian)
- Pagination caps or cursor limits
- S3 list-objects scale limits

Use ✅ Pass / ⚠️ Risk / ❌ Fail ratings.

### 4. Blast Radius

- **Direct impact:** what fails immediately if this change has a bug
- **Indirect impact:** downstream pipelines, queries, services, or jobs that
  depend on the affected code (transitive dependencies)
- **Data impact:** any schema drift, partition changes, or Parquet field removals
- **Rollback path:** exact steps to undo within 5 minutes

### 5. Known Limits and Assumptions

Every assumption that is NOT verified in the codebase. Examples:
- "Assumes partition key is always present in S3 path"
- "Assumes RDS connection pool ≤ 20 concurrent connections"
- "Assumes DAS events arrive in chronological order"

If you cannot verify an assumption, mark it `UNKNOWN — requires verification`.

### 6. Alternatives Considered

| Approach                        | Pro                  | Con                  |
|---------------------------------|----------------------|----------------------|
| **Option A (recommended)**      |                      |                      |
| Option B                        |                      |                      |
| Option C                        |                      |                      |

Minimum 2 alternatives. If only one approach exists, explain why explicitly.

### 7. Open Questions

Things that MUST be answered before implementation starts. Do not proceed
with implementation if any open question touches security, data integrity,
or production availability.

### 8. Verification Plan

Specific, runnable commands or checks a team member can execute to confirm
the change works correctly after implementation.

## Output Format Rules

- Use ✅ / ⚠️ / ❌ for scalability and blast radius ratings
- Mark `UNKNOWN` where assessment is impossible without more context — do not paper over gaps
- Tables for alternatives matrix and scalability gate
- No implementation code in this skill output

## Closing Gate

After producing the analysis, end with:

> **Recommended path: Option [X].**
> Do you want to proceed with this approach, or explore a different option?

Do not begin implementation until you receive explicit confirmation.
