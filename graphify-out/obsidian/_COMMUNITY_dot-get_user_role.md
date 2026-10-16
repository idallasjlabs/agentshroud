---
type: community
cohesion: 0.20
members: 10
---

# .get_user_role

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-get_user_role()]] - code - gateway/security/rbac_config.py
- [[dot-is_admin_or_higher()]] - code - gateway/security/rbac_config.py
- [[dot-is_collaborator_or_higher()]] - code - gateway/security/rbac_config.py
- [[dot-is_operator_or_higher()]] - code - gateway/security/rbac_config.py
- [[dot-is_owner()_1]] - code - gateway/security/rbac_config.py
- [[Check if user has admin privileges or higher.]] - rationale - gateway/security/rbac_config.py
- [[Check if user has collaborator privileges or higher.]] - rationale - gateway/security/rbac_config.py
- [[Check if user has operator privileges or higher (admin, operator, owner).]] - rationale - gateway/security/rbac_config.py
- [[Check if user is the owner (any platform).]] - rationale - gateway/security/rbac_config.py
- [[Get role for a user ID.]] - rationale - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_user_role
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_Role]]

## Top bridge nodes
- [[dot-get_user_role()]] - degree 6, connects to 2 communities
- [[dot-is_operator_or_higher()]] - degree 4, connects to 1 community
- [[dot-is_admin_or_higher()]] - degree 3, connects to 1 community
- [[dot-is_collaborator_or_higher()]] - degree 3, connects to 1 community
- [[dot-is_owner()_1]] - degree 2, connects to 1 community
