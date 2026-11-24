---
type: community
members: 55
---

# telegram_proxy.py

**Members:** 55 nodes

## Members
- [[dot-__init__()_49]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_apply_persisted_overrides_skips_user_overrides_key()]] - code - gateway/tests/test_group_config.py
- [[dot-test_get_all_member_ids()]] - code - gateway/tests/test_group_config.py
- [[dot-test_get_user_collab_mode_falls_back_to_group()]] - code - gateway/tests/test_group_config.py
- [[dot-test_get_user_groups_member()]] - code - gateway/tests/test_group_config.py
- [[dot-test_get_user_groups_multi_group()]] - code - gateway/tests/test_group_config.py
- [[dot-test_get_user_groups_non_member()]] - code - gateway/tests/test_group_config.py
- [[dot-test_get_user_projects_member()]] - code - gateway/tests/test_group_config.py
- [[dot-test_get_user_projects_non_member()]] - code - gateway/tests/test_group_config.py
- [[dot-test_is_group_admin_correct()]] - code - gateway/tests/test_group_config.py
- [[dot-test_is_group_admin_unknown_group()]] - code - gateway/tests/test_group_config.py
- [[dot-test_is_group_admin_wrong_user()]] - code - gateway/tests/test_group_config.py
- [[dot-test_local_only_mode()]] - code - gateway/tests/test_group_config.py
- [[dot-test_no_duplicate_projects()]] - code - gateway/tests/test_group_config.py
- [[dot-test_persist_user_collab_mode()]] - code - gateway/tests/test_group_config.py
- [[dot-test_persist_user_collab_mode_update()]] - code - gateway/tests/test_group_config.py
- [[dot-test_project_scoped_mode()]] - code - gateway/tests/test_group_config.py
- [[dot-test_unknown_user_returns_local_only()]] - code - gateway/tests/test_group_config.py
- [[dot-test_user_override_takes_precedence_over_group()]] - code - gateway/tests/test_group_config.py
- [[Calling persist_user_collab_mode twice updates the stored value.]] - rationale - gateway/tests/test_group_config.py
- [[Group and Project configuration models for v0.9.0 Team Collaboration. Defines…]] - rationale - gateway/security/group_config.py
- [[Per-user collab_mode override persists to group_overrides.json and takes…]] - rationale - gateway/tests/test_group_config.py
- [[Per-user override beats group-derived collab_mode.]] - rationale - gateway/tests/test_group_config.py
- [[Persist a per-user collab mode override set via the SOC dashboard. Stored under…]] - rationale - gateway/security/group_config.py
- [[Persist a runtime collab mode change for a group.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group creation so it survives container restarts.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group deletion so it survives container restarts.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group membership addition.]] - rationale - gateway/security/group_config.py
- [[Persist a runtime group membership removal.]] - rationale - gateway/security/group_config.py
- [[Read persisted paused-collaborator IDs from disk. Owner-initiated manual pause…]] - rationale - gateway/security/rbac_config.py
- [[Telegram API Reverse Proxy — intercepts all bot ↔ Telegram traffic. The gateway…]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestAdminChecks]] - code - gateway/tests/test_group_config.py
- [[TestCollabMode]] - code - gateway/tests/test_group_config.py
- [[TestMembershipQueries]] - code - gateway/tests/test_group_config.py
- [[TestProjectQueries]] - code - gateway/tests/test_group_config.py
- [[TestUserCollabModeOverride]] - code - gateway/tests/test_group_config.py
- [[Tests for group_config.py — V9-4A TeamsConfig, GroupConfig, ProjectConfig.]] - rationale - gateway/tests/test_group_config.py
- [[Without a per-user override, group-derived mode is returned.]] - rationale - gateway/tests/test_group_config.py
- [[__user_overrides__ key must not be treated as a group_id.]] - rationale - gateway/tests/test_group_config.py
- [[_ipv4_first_getaddrinfo()]] - code - gateway/proxy/telegram_proxy.py
- [[_load_overrides()]] - code - gateway/security/group_config.py
- [[_save_overrides()]] - code - gateway/security/group_config.py
- [[fixture_32]] - code
- [[group_config.py]] - code - gateway/security/group_config.py
- [[load_paused_collaborator_ids()]] - code - gateway/security/rbac_config.py
- [[persist_group_collab_mode()]] - code - gateway/security/group_config.py
- [[persist_group_create()]] - code - gateway/security/group_config.py
- [[persist_group_delete()]] - code - gateway/security/group_config.py
- [[persist_group_member_add()]] - code - gateway/security/group_config.py
- [[persist_group_member_remove()]] - code - gateway/security/group_config.py
- [[persist_user_collab_mode writes under __user_overrides__ key.]] - rationale - gateway/tests/test_group_config.py
- [[persist_user_collab_mode()]] - code - gateway/security/group_config.py
- [[teams()_2]] - code - gateway/tests/test_group_config.py
- [[telegram_proxy.py_2]] - code - gateway/proxy/telegram_proxy.py
- [[test_group_config.py]] - code - gateway/tests/test_group_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_proxypy
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_socrouter.py]]
- 15 edges to [[_COMMUNITY_test_collaborator_responses.py]]
- 7 edges to [[_COMMUNITY_TeamsConfig]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_GroupWorkspaceManager]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 2 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_normalize_input]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_DelegationPrivilege]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_read_secret]]
- 1 edge to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 1 edge to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_test_progressive_lockdown.py]]
- 1 edge to [[_COMMUNITY_test_telegram_pipeline.py]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_GatewayConfig]]
- 1 edge to [[_COMMUNITY_test_group_isolation.py]]
- 1 edge to [[_COMMUNITY_GroupRoleResolver]]
- 1 edge to [[_COMMUNITY_test_shared_memory.py]]
- 1 edge to [[_COMMUNITY_test_tool_acl.py]]

## Top bridge nodes
- [[telegram_proxy.py_2]] - degree 39, connects to 17 communities
- [[group_config.py]] - degree 27, connects to 11 communities
- [[dot-__init__()_49]] - degree 5, connects to 4 communities
- [[test_group_config.py]] - degree 13, connects to 2 communities
- [[persist_group_collab_mode()]] - degree 8, connects to 2 communities
