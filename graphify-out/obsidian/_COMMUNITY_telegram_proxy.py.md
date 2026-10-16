---
type: community
cohesion: 0.05
members: 80
---

# telegram_proxy.py

**Cohesion:** 0.05 - loosely connected
**Members:** 80 nodes

## Members
- [[dot-_handle_groupinfo_command()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-coerce_members()]] - code - gateway/security/group_config.py
- [[dot-get_active_project_for_user()]] - code - gateway/security/group_config.py
- [[dot-get_all_member_ids()]] - code - gateway/security/group_config.py
- [[dot-get_group_admin_ids()]] - code - gateway/security/group_config.py
- [[dot-get_group_safe_response_prefix()]] - code - gateway/security/group_config.py
- [[dot-get_user_collab_mode()]] - code - gateway/security/group_config.py
- [[dot-get_user_groups()]] - code - gateway/security/group_config.py
- [[dot-get_user_projects()]] - code - gateway/security/group_config.py
- [[dot-is_admin()]] - code - gateway/security/group_config.py
- [[dot-is_group_admin()_1]] - code - gateway/security/group_config.py
- [[dot-is_member()]] - code - gateway/security/group_config.py
- [[dot-matches_topic()]] - code - gateway/security/group_config.py
- [[dot-model_post_init()_1]] - code - gateway/security/group_config.py
- [[dot-normalise_topics()]] - code - gateway/security/group_config.py
- [[dot-test_addtogroup_success()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_already_member()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_collab_outside_scope_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_collab_unavailable_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_contains_allowed_tools()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_contains_group_and_project()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_member_sees_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_member_sees_project()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_no_groups_for_unknown_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_no_groups_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_no_permission()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_no_projects_for_unknown_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_no_projects_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_not_member()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_rmfromgroup_success()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_setmode_success_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_setmode_success_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_shows_admin()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_shows_projects()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-test_unknown_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[dot-validate_mode()]] - code - gateway/security/group_config.py
- [[A project defines a scoped focus area for a team.]] - rationale - gateway/security/group_config.py
- [[A team group with members, admin, projects, and collab mode.]] - rationale - gateway/security/group_config.py
- [[Build the system-prompt injection for project_scoped mode.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format a user's accessible projects for display.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format a user's group memberships for display.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format detailed info for a single group.]] - rationale - gateway/proxy/collaborator_responses.py
- [[GroupConfig]] - code - gateway/security/group_config.py
- [[Handle groupinfo group_id.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Merge group_overrides.json additions into the in-memory TeamsConfig.]] - rationale - gateway/security/group_config.py
- [[ProjectConfig]] - code - gateway/security/group_config.py
- [[Return True if any focus_topic appears in the text (case-insensitive).]] - rationale - gateway/security/group_config.py
- [[Return all groups the user belongs to.]] - rationale - gateway/security/group_config.py
- [[Return all projects accessible to the user via group membership.]] - rationale - gateway/security/group_config.py
- [[Return deduplicated list of all user IDs across all groups.]] - rationale - gateway/security/group_config.py
- [[Return mapping of group_id → admin_user_id for all groups that have an admin.]] - rationale - gateway/security/group_config.py
- [[Return the effective collab_mode for a user.          Resolution order]] - rationale - gateway/security/group_config.py
- [[Return the first project accessible to a user (primary project).]] - rationale - gateway/security/group_config.py
- [[Return the safe_response_prefix for the first group that the user belongs to]] - rationale - gateway/security/group_config.py
- [[TeamsConfig_2]] - code - gateway/security/group_config.py
- [[TestBuildProjectContextInjection]] - code - gateway/tests/test_collaborator_responses.py
- [[TestConstantMessages]] - code - gateway/tests/test_collaborator_responses.py
- [[TestErrorFormatters]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupInfo]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatProjectsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestMutationFormatters]] - code - gateway/tests/test_collaborator_responses.py
- [[Top-level teams configuration parsed from agentshroud.yaml `teams` section.]] - rationale - gateway/security/group_config.py
- [[_apply_persisted_overrides()]] - code - gateway/security/group_config.py
- [[build_project_context_injection()]] - code - gateway/proxy/collaborator_responses.py
- [[collaborator_responses.py]] - code - gateway/proxy/collaborator_responses.py
- [[format_addtogroup_success()]] - code - gateway/proxy/collaborator_responses.py
- [[format_already_member()]] - code - gateway/proxy/collaborator_responses.py
- [[format_group_info()]] - code - gateway/proxy/collaborator_responses.py
- [[format_groups_list()]] - code - gateway/proxy/collaborator_responses.py
- [[format_no_permission()]] - code - gateway/proxy/collaborator_responses.py
- [[format_not_member()]] - code - gateway/proxy/collaborator_responses.py
- [[format_projects_list()]] - code - gateway/proxy/collaborator_responses.py
- [[format_rmfromgroup_success()]] - code - gateway/proxy/collaborator_responses.py
- [[format_setmode_success()]] - code - gateway/proxy/collaborator_responses.py
- [[format_unknown_group()]] - code - gateway/proxy/collaborator_responses.py
- [[project()]] - code - gateway/tests/test_collaborator_responses.py
- [[slack_proxy.py]] - code - gateway/proxy/slack_proxy.py
- [[teams()_2]] - code - gateway/tests/test_collaborator_responses.py
- [[test_collaborator_responses.py]] - code - gateway/tests/test_collaborator_responses.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_proxypy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_GroupConfig]]
- 15 edges to [[_COMMUNITY_telegram_proxy.py_1]]
- 13 edges to [[_COMMUNITY_RBACConfig]]
- 11 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 11 edges to [[_COMMUNITY_RBACConfig_1]]
- 7 edges to [[_COMMUNITY_DataLedger]]
- 6 edges to [[_COMMUNITY_RBACConfig_2]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig_8]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_GroupRoleResolver]]
- 4 edges to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 3 edges to [[_COMMUNITY__FakeRBAC]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TestSSRFDetection_3]]
- 1 edge to [[_COMMUNITY_diagramsREADME_1]]
- 1 edge to [[_COMMUNITY_hermesSOUL_1]]
- 1 edge to [[_COMMUNITY_ProxyAction_1]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_test_runtime_engines.py_1]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py_3]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_2]]
- 1 edge to [[_COMMUNITY_export_bot]]

## Top bridge nodes
- [[TeamsConfig_2]] - degree 100, connects to 22 communities
- [[GroupConfig]] - degree 32, connects to 4 communities
- [[ProjectConfig]] - degree 18, connects to 2 communities
- [[format_groups_list()]] - degree 8, connects to 2 communities
- [[format_projects_list()]] - degree 7, connects to 2 communities
