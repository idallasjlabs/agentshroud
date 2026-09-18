---
type: community
cohesion: 0.03
members: 120
---

# TeamsConfig

**Cohesion:** 0.03 - loosely connected
**Members:** 120 nodes

## Members
- [[.coerce_members()]] - code - gateway/security/group_config.py
- [[.get_active_project_for_user()]] - code - gateway/security/group_config.py
- [[.get_all_member_ids()]] - code - gateway/security/group_config.py
- [[.get_group_admin_ids()]] - code - gateway/security/group_config.py
- [[.get_group_safe_response_prefix()]] - code - gateway/security/group_config.py
- [[.get_user_collab_mode()]] - code - gateway/security/group_config.py
- [[.get_user_groups()]] - code - gateway/security/group_config.py
- [[.get_user_projects()]] - code - gateway/security/group_config.py
- [[.is_admin()]] - code - gateway/security/group_config.py
- [[.is_group_admin()_1]] - code - gateway/security/group_config.py
- [[.is_member()]] - code - gateway/security/group_config.py
- [[.matches_topic()]] - code - gateway/security/group_config.py
- [[.model_post_init()_1]] - code - gateway/security/group_config.py
- [[.normalise_topics()]] - code - gateway/security/group_config.py
- [[.test_addtogroup_success()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_already_member()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_apply_persisted_overrides_skips_user_overrides_key()]] - code - gateway/tests/test_group_config.py
- [[.test_collab_outside_scope_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_collab_unavailable_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_contains_allowed_tools()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_contains_group_and_project()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_empty_prefix_string_not_returned()]] - code - gateway/tests/test_group_config.py
- [[.test_empty_teams_parses()]] - code - gateway/tests/test_group_config.py
- [[.test_get_all_member_ids()]] - code - gateway/tests/test_group_config.py
- [[.test_get_user_collab_mode_falls_back_to_group()]] - code - gateway/tests/test_group_config.py
- [[.test_get_user_groups_member()]] - code - gateway/tests/test_group_config.py
- [[.test_get_user_groups_multi_group()]] - code - gateway/tests/test_group_config.py
- [[.test_get_user_groups_non_member()]] - code - gateway/tests/test_group_config.py
- [[.test_get_user_projects_member()]] - code - gateway/tests/test_group_config.py
- [[.test_get_user_projects_non_member()]] - code - gateway/tests/test_group_config.py
- [[.test_group_config_safe_response_prefix_field()]] - code - gateway/tests/test_group_config.py
- [[.test_group_config_safe_response_prefix_set()]] - code - gateway/tests/test_group_config.py
- [[.test_is_group_admin_correct()]] - code - gateway/tests/test_group_config.py
- [[.test_is_group_admin_unknown_group()]] - code - gateway/tests/test_group_config.py
- [[.test_is_group_admin_wrong_user()]] - code - gateway/tests/test_group_config.py
- [[.test_local_only_mode()]] - code - gateway/tests/test_group_config.py
- [[.test_member_sees_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_member_sees_project()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_duplicate_projects()]] - code - gateway/tests/test_group_config.py
- [[.test_no_groups_for_unknown_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_groups_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_permission()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_prefix_by_default()]] - code - gateway/tests/test_group_config.py
- [[.test_no_projects_for_unknown_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_projects_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_not_member()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_parses_groups()]] - code - gateway/tests/test_group_config.py
- [[.test_parses_projects()]] - code - gateway/tests/test_group_config.py
- [[.test_prefix_not_returned_for_non_member()]] - code - gateway/tests/test_group_config.py
- [[.test_prefix_returned_for_member()]] - code - gateway/tests/test_group_config.py
- [[.test_project_scoped_mode()]] - code - gateway/tests/test_group_config.py
- [[.test_rmfromgroup_success()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_setmode_success_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_setmode_success_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_shows_admin()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_shows_projects()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_unknown_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_unknown_user_returns_local_only()]] - code - gateway/tests/test_group_config.py
- [[.test_unknown_user_returns_none()]] - code - gateway/tests/test_group_config.py
- [[.test_user_override_takes_precedence_over_group()]] - code - gateway/tests/test_group_config.py
- [[.validate_mode()]] - code - gateway/security/group_config.py
- [[A project defines a scoped focus area for a team.]] - rationale - gateway/security/group_config.py
- [[A team group with members, admin, projects, and collab mode.]] - rationale - gateway/security/group_config.py
- [[Build the system-prompt injection for project_scoped mode.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format a user's accessible projects for display.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format a user's group memberships for display.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format detailed info for a single group.]] - rationale - gateway/proxy/collaborator_responses.py
- [[GroupConfig]] - code - gateway/security/group_config.py
- [[Merge group_overrides.json additions into the in-memory TeamsConfig.]] - rationale - gateway/security/group_config.py
- [[Per-user collab_mode override persists to group_overrides.json and takes     pr]] - rationale - gateway/tests/test_group_config.py
- [[Per-user override beats group-derived collab_mode.]] - rationale - gateway/tests/test_group_config.py
- [[ProjectConfig]] - code - gateway/security/group_config.py
- [[Return True if any focus_topic appears in the text (case-insensitive).]] - rationale - gateway/security/group_config.py
- [[Return all groups the user belongs to.]] - rationale - gateway/security/group_config.py
- [[Return all projects accessible to the user via group membership.]] - rationale - gateway/security/group_config.py
- [[Return deduplicated list of all user IDs across all groups.]] - rationale - gateway/security/group_config.py
- [[Return mapping of group_id → admin_user_id for all groups that have an admin.]] - rationale - gateway/security/group_config.py
- [[Return the effective collab_mode for a user.          Resolution order]] - rationale - gateway/security/group_config.py
- [[Return the first project accessible to a user (primary project).]] - rationale - gateway/security/group_config.py
- [[Return the safe_response_prefix for the first group that the user belongs to]] - rationale - gateway/security/group_config.py
- [[TeamsConfig_1]] - code - gateway/tests/test_group_config.py
- [[TeamsConfig_2]] - code - gateway/security/group_config.py
- [[TestAdminChecks]] - code - gateway/tests/test_group_config.py
- [[TestBuildProjectContextInjection]] - code - gateway/tests/test_collaborator_responses.py
- [[TestCollabMode]] - code - gateway/tests/test_group_config.py
- [[TestConstantMessages]] - code - gateway/tests/test_collaborator_responses.py
- [[TestErrorFormatters]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupInfo]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatProjectsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestGroupSafeResponsePrefix]] - code - gateway/tests/test_group_config.py
- [[TestMembershipQueries]] - code - gateway/tests/test_group_config.py
- [[TestMutationFormatters]] - code - gateway/tests/test_collaborator_responses.py
- [[TestProjectQueries]] - code - gateway/tests/test_group_config.py
- [[TestTeamsConfigParsing]] - code - gateway/tests/test_group_config.py
- [[TestUserCollabModeOverride]] - code - gateway/tests/test_group_config.py
- [[Top-level teams configuration parsed from agentshroud.yaml `teams` section.]] - rationale - gateway/security/group_config.py
- [[Without a per-user override, group-derived mode is returned.]] - rationale - gateway/tests/test_group_config.py
- [[__user_overrides__ key must not be treated as a group_id.]] - rationale - gateway/tests/test_group_config.py
- [[_apply_persisted_overrides()]] - code - gateway/security/group_config.py
- [[_ipv4_first_getaddrinfo()]] - code - gateway/proxy/telegram_proxy.py
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
- [[teams()]] - code - gateway/tests/test_collaborator_responses.py
- [[teams()_1]] - code - gateway/tests/test_group_config.py
- [[telegram_proxy.py]] - code - gateway/proxy/telegram_proxy.py
- [[test_collaborator_responses.py]] - code - gateway/tests/test_collaborator_responses.py
- [[test_group_config.py]] - code - gateway/tests/test_group_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TeamsConfig
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_RBACConfig]]
- 13 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 11 edges to [[_COMMUNITY_group_config.py]]
- 7 edges to [[_COMMUNITY_rbac_config.py]]
- 7 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 6 edges to [[_COMMUNITY_GroupRoleResolver]]
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_BaseModel]]
- 2 edges to [[_COMMUNITY_gateway.proxy.llm_proxy]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_make_event()]]
- 1 edge to [[_COMMUNITY_RateLimiter]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_load_config()]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_TELEGRAM_API_BASE_URL]]
- 1 edge to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 1 edge to [[_COMMUNITY_TelegramGatewayRelay]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_.scan()]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_GroupRegistry]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_TestGroupMemoryInvisibleFromDM]]
- 1 edge to [[_COMMUNITY_TestGroupMemoryNamespaceIsolation]]
- 1 edge to [[_COMMUNITY_TestGroupRoleResolver]]
- 1 edge to [[_COMMUNITY_TestGroupMemoryWriteACL]]
- 1 edge to [[_COMMUNITY_TestUserMemoryWriteACL]]

## Top bridge nodes
- [[TeamsConfig_2]] - degree 86, connects to 16 communities
- [[telegram_proxy.py]] - degree 36, connects to 16 communities
- [[GroupConfig]] - degree 32, connects to 3 communities
- [[slack_proxy.py]] - degree 4, connects to 3 communities
- [[ProjectConfig]] - degree 18, connects to 2 communities