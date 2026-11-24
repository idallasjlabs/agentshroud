---
type: community
members: 6
---

# .get_user_role

**Members:** 6 nodes

## Members
- [[dot-get_user_role()_2]] - code - gateway/security/rbac_config.py
- [[dot-is_admin_or_higher()]] - code - gateway/security/rbac_config.py
- [[dot-is_collaborator_or_higher()]] - code - gateway/security/rbac_config.py
- [[Check if user has admin privileges or higher.]] - rationale - gateway/security/rbac_config.py
- [[Check if user has collaborator privileges or higher.]] - rationale - gateway/security/rbac_config.py
- [[Get role for a user ID.]] - rationale - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_user_role
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[dot-get_user_role()_2]] - degree 5, connects to 1 community
- [[dot-is_admin_or_higher()]] - degree 3, connects to 1 community
- [[dot-is_collaborator_or_higher()]] - degree 3, connects to 1 community
