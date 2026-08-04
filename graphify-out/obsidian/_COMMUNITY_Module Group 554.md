---
type: community
cohesion: 0.50
members: 4
---

# Module Group 554

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.__post_init__()_4]] - code - gateway/security/rbac_config.py
- [[Initialize user roles based on configuration.]] - rationale - gateway/security/rbac_config.py
- [[Read dynamically approved collaborator IDs from disk.]] - rationale - gateway/security/rbac_config.py
- [[load_persisted_collaborators()]] - code - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_554
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_RBAC Configuration]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_SOC Router & Correlation]]

## Top bridge nodes
- [[load_persisted_collaborators()]] - degree 4, connects to 2 communities
- [[.__post_init__()_4]] - degree 3, connects to 1 community
