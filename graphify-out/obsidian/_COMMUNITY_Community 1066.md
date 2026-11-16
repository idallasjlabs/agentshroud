---
type: community
members: 17
---

# Community 1066

**Members:** 17 nodes

## Members
- [[._make_rbac()]] - code - gateway/tests/test_rbac.py
- [[.is_member()_1]] - code - gateway/security/rbac_config.py
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
- [[GroupRegistry]] - code - gateway/security/rbac_config.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1066
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 6]]
- 8 edges to [[_COMMUNITY_Community 223]]
- 5 edges to [[_COMMUNITY_Community 151]]
- 3 edges to [[_COMMUNITY_Community 194]]
- 3 edges to [[_COMMUNITY_Community 235]]
- 1 edge to [[_COMMUNITY_Community 1]]

## Top bridge nodes
- [[GroupRegistry]] - degree 34, connects to 5 communities
- [[TestGroupRegistry]] - degree 21, connects to 3 communities
- [[._make_rbac()]] - degree 12, connects to 1 community