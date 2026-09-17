---
type: community
cohesion: 0.67
members: 3
---

# .complete_task()

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[.complete_task()]] - code - gateway/security/a2a_governance.py
- [[.complete_task()_1]] - code - gateway/security/a2a_governance.py
- [[Mark a delegated task as complete (decrements active task counter).]] - rationale - gateway/security/a2a_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/complete_task
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]

## Top bridge nodes
- [[.complete_task()]] - degree 2, connects to 1 community
- [[.complete_task()_1]] - degree 2, connects to 1 community