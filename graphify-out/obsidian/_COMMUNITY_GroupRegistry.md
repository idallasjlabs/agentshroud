---
type: community
cohesion: 0.21
members: 20
---

# GroupRegistry

**Cohesion:** 0.21 - loosely connected
**Members:** 20 nodes

## Members
- [[._make_rbac()]] - code - gateway/tests/test_rbac.py
- [[.filter()_1]] - code - gateway/ingest_api/lifespan.py
- [[.is_member()_1]] - code - gateway/security/rbac_config.py
- [[.list_groups()]] - code - gateway/security/rbac_config.py
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
- [[LogRecord_2]] - code - gateway/ingest_api/lifespan.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GroupRegistry
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_ingest_apimain.py]]
- 8 edges to [[_COMMUNITY_rbac_config.py]]
- 5 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_AlertTelegramRelay]]
- 1 edge to [[_COMMUNITY_make_event()]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPersistence]]

## Top bridge nodes
- [[LogRecord_2]] - degree 10, connects to 6 communities
- [[GroupRegistry]] - degree 34, connects to 5 communities
- [[TestGroupRegistry]] - degree 21, connects to 3 communities
- [[._make_rbac()]] - degree 12, connects to 1 community
- [[.filter()_1]] - degree 2, connects to 1 community