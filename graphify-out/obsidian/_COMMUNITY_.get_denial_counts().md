---
type: community
cohesion: 0.67
members: 3
---

# .get_denial_counts()

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[.get_denial_counts()]] - code - gateway/security/tool_acl.py
- [[.get_denial_counts()_1]] - code - gateway/security/tool_acl.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_denial_counts
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[.get_denial_counts()]] - degree 2, connects to 1 community
- [[.get_denial_counts()_1]] - degree 2, connects to 1 community