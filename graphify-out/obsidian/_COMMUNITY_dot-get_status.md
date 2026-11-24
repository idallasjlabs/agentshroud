---
type: community
members: 4
---

# .get_status

**Members:** 4 nodes

## Members
- [[dot-all_statuses()]] - code - gateway/security/progressive_lockdown.py
- [[dot-get_status()_1]] - code - gateway/security/progressive_lockdown.py
- [[Return current lockdown state for a principal (for collabs or owner…]] - rationale - gateway/security/progressive_lockdown.py
- [[Return lockdown status for all tracked principals.]] - rationale - gateway/security/progressive_lockdown.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_status
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_LockdownLevel]]

## Top bridge nodes
- [[dot-get_status()_1]] - degree 4, connects to 2 communities
- [[dot-all_statuses()]] - degree 3, connects to 1 community
