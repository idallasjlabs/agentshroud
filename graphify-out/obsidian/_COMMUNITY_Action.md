---
type: community
cohesion: 0.26
members: 17
---

# Action

**Cohesion:** 0.26 - loosely connected
**Members:** 17 nodes

## Members
- [[dot-_make_rbac()]] - code - gateway/tests/test_rbac.py
- [[dot-is_member()_1]] - code - gateway/security/rbac_config.py
- [[dot-test_add_remove_member()]] - code - gateway/tests/test_rbac.py
- [[dot-test_auto_groups_created()]] - code - gateway/tests/test_rbac.py
- [[dot-test_cannot_create_reserved_group_id()]] - code - gateway/tests/test_rbac.py
- [[dot-test_cannot_delete_auto_group()]] - code - gateway/tests/test_rbac.py
- [[dot-test_create_custom_group()]] - code - gateway/tests/test_rbac.py
- [[dot-test_delete_custom_group()]] - code - gateway/tests/test_rbac.py
- [[dot-test_everyone_group_contains_all_users()]] - code - gateway/tests/test_rbac.py
- [[dot-test_is_member_unknown_group_returns_false()]] - code - gateway/tests/test_rbac.py
- [[dot-test_slack_group_contains_slack_ids()]] - code - gateway/tests/test_rbac.py
- [[dot-test_telegram_group_contains_numeric_ids()]] - code - gateway/tests/test_rbac.py
- [[GroupRegistry]] - code - gateway/security/rbac_config.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Action
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_MiddlewareManager]]
- 8 edges to [[_COMMUNITY_telegram_proxy.py_1]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_Action_1]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[GroupRegistry]] - degree 34, connects to 7 communities
- [[TestGroupRegistry]] - degree 21, connects to 1 community
- [[dot-_make_rbac()]] - degree 12, connects to 1 community
