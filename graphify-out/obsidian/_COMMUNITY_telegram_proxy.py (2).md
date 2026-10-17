---
type: community
members: 42
---

# telegram_proxy.py (2)

**Members:** 42 nodes

## Members
- [[dot-_make_rbac()]] - code - gateway/tests/test_rbac.py
- [[dot-add_member()]] - code - gateway/security/rbac_config.py
- [[dot-create_group()]] - code - gateway/security/rbac_config.py
- [[dot-delete_group()]] - code - gateway/security/rbac_config.py
- [[dot-filter()_1]] - code - gateway/ingest_api/lifespan.py
- [[dot-get_group()]] - code - gateway/security/rbac_config.py
- [[dot-init_auto_groups()]] - code - gateway/security/rbac_config.py
- [[dot-is_member()]] - code - gateway/security/rbac_config.py
- [[dot-list_groups()]] - code - gateway/security/rbac_config.py
- [[dot-remove_member()]] - code - gateway/security/rbac_config.py
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
- [[A named group of users.]] - rationale - gateway/security/rbac_config.py
- [[Add a user to a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Create or replace a custom group and persist it.]] - rationale - gateway/security/rbac_config.py
- [[Delete a custom group. Returns True if deleted, False if not found.]] - rationale - gateway/security/rbac_config.py
- [[Derive and reset auto-groups from current RBAC user list, then load custom group]] - rationale - gateway/security/rbac_config.py
- [[Group]] - code - gateway/security/rbac_config.py
- [[GroupRegistry]] - code - gateway/security/rbac_config.py
- [[Install warning filter once for uvicorn logger.]] - rationale - gateway/ingest_api/lifespan.py
- [[LogRecord_2]] - code - gateway/ingest_api/lifespan.py
- [[Manages user groups including auto-groups and custom groups.]] - rationale - gateway/security/rbac_config.py
- [[Read custom groups from disk.]] - rationale - gateway/security/rbac_config.py
- [[Remove a user from a group (auto-groups are updated in-memory only).]] - rationale - gateway/security/rbac_config.py
- [[Return True if user_id is in the group.]] - rationale - gateway/security/rbac_config.py
- [[Return group by ID, or None.]] - rationale - gateway/security/rbac_config.py
- [[Suppress noisy uvicorn warning spam for malformed probe traffic.]] - rationale - gateway/ingest_api/lifespan.py
- [[TestGroupRegistry]] - code - gateway/tests/test_rbac.py
- [[Tests for GroupRegistry auto-groups and custom group management.]] - rationale - gateway/tests/test_rbac.py
- [[Write only custom groups to disk (auto-groups are derived at runtime).]] - rationale - gateway/security/rbac_config.py
- [[_DropInvalidHTTPRequestFilter]] - code - gateway/ingest_api/lifespan.py
- [[_install_uvicorn_warning_filter()]] - code - gateway/ingest_api/lifespan.py
- [[_load_persisted_groups()]] - code - gateway/security/rbac_config.py
- [[_persist_groups()]] - code - gateway/security/rbac_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_proxypy_2
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_MiddlewareManager]]
- 6 edges to [[_COMMUNITY_AlertDispatcher]]
- 4 edges to [[_COMMUNITY_telegram_proxy.py (3)]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_RBACConfig (2)]]
- 2 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_make_event]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[_DropInvalidHTTPRequestFilter]] - degree 15, connects to 10 communities
- [[LogRecord_2]] - degree 10, connects to 8 communities
- [[GroupRegistry]] - degree 34, connects to 6 communities
- [[TestGroupRegistry]] - degree 21, connects to 2 communities
- [[Group]] - degree 9, connects to 2 communities
