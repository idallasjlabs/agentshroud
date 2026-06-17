---
type: community
cohesion: 0.14
members: 26
---

# Module Group 186

**Cohesion:** 0.14 - loosely connected
**Members:** 26 nodes

## Members
- [[._make_rbac()]] - code - gateway/tests/test_rbac.py
- [[.add_member()]] - code - gateway/security/rbac_config.py
- [[.delete_group()]] - code - gateway/security/rbac_config.py
- [[.get_group()]] - code - gateway/security/rbac_config.py
- [[.is_member()_1]] - code - gateway/security/rbac_config.py
- [[.list_groups()]] - code - gateway/security/rbac_config.py
- [[.remove_member()]] - code - gateway/security/rbac_config.py
- [[.test_add_remove_member()]] - code - gateway/tests/test_rbac.py
- [[.test_auto_groups_created()]] - code - gateway/tests/test_rbac.py
- [[.test_cannot_create_reserved_group_id()]] - code - gateway/tests/test_rbac.py
- [[.test_cannot_delete_auto_group()]] - code - gateway/tests/test_rbac.py
- [[.test_create_custom_group()]] - code - gateway/tests/test_rbac.py
- [[.test_delete_custom_group()]] - code - gateway/tests/test_rbac.py
- [[.test_everyone_group_contains_all_users()]] - code - gateway/tests/test_rbac.py
- [[.test_is_member_unknown_group_returns_false()]] - code - gateway/tests/test_rbac.py
- [[.test_slack_group_contains_slack_ids()]] - code - gateway/tests/test_rbac.py
- [[.test_telegram_group_contains_numeric_ids()]] - code - gateway/tests/test_rbac.py
- [[Add a user to a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Delete a custom group. Returns True if deleted, False if not found.]] - rationale - gateway/security/rbac_config.py
- [[GroupRegistry]] - code - gateway/security/rbac_config.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Remove a user from a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[Return group by ID, or None.]] - rationale - gateway/security/rbac_config.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_186
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_RBAC Configuration]]
- 5 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 1 edge to [[_COMMUNITY_Module Group 189]]
- 1 edge to [[_COMMUNITY_Group Config & Teams]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]

## Top bridge nodes
- [[GroupRegistry]] - degree 33, connects to 3 communities
- [[TestGroupRegistry]] - degree 23, connects to 3 communities
- [[.delete_group()]] - degree 4, connects to 2 communities
- [[._make_rbac()]] - degree 12, connects to 1 community
- [[.add_member()]] - degree 3, connects to 1 community