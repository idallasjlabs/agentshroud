---
type: community
cohesion: 0.22
members: 9
---

# HIGH — Should Fix Before Release

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[C4 Root Endpoint `` Exposes System Metrics Without Authentication]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[C5 `status` Endpoint Exposes Security Posture Without Authentication]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[CRITICAL — Must Fix Before Release]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[H4 Docker Network `agentshroud-isolated` Not Actually Isolated]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[H5 `dashboardws-token` Returns Master Auth Token to Browser]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[H6 Session Manager Path Traversal via Crafted User ID]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[H7 Error Messages Disclose Internal Details]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[HIGH — Should Fix Before Release]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md
- [[New Findings]] - document - docs/planning/v0.8/blue-team-assessment-v0.8.0-final.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HIGH__Should_Fix_Before_Release
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AgentShroud v0.8.0 — Blue Team Security Assessme]]
- 1 edge to [[_COMMUNITY_LOW — Informational]]
- 1 edge to [[_COMMUNITY_MEDIUM — Fix Soon]]

## Top bridge nodes
- [[New Findings]] - degree 5, connects to 3 communities