---
type: community
members: 8
---

# scripts/security-scan.sh

**Members:** 8 nodes

## Members
- [[Scenario 00 — Information Disclosure (Phase 0 finding)]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Scenario 01 — Enforce-by-Default]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Scenario 02 — Human-in-the-Loop Bypass]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Scenario 03 — Session Isolation]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Scenario 04 — Separation of Privilege]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Scenario 05 — Credential Isolation]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Scenario 06 — Outbound Information Filter]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[§1 — Re-run of Prior Scenarios]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/security-scansh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Security Docs]]

## Top bridge nodes
- [[§1 — Re-run of Prior Scenarios]] - degree 8, connects to 1 community