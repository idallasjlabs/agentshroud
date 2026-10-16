---
type: community
cohesion: 0.05
members: 74
---

# telegram_proxy.py

**Cohesion:** 0.05 - loosely connected
**Members:** 74 nodes

## Members
- [[dot-_handle_addtogroup_command()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_groupinfo_command()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_groups_command()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_projects_command()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_rmfromgroup_command()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_setmode_command()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_mirror_to_owner_if_collaborator()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_send_owner_admin_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-get_active_project_for_user()]] - code - gateway/security/group_config.py
- [[dot-get_user_projects()]] - code - gateway/security/group_config.py
- [[dot-matches_topic()]] - code - gateway/security/group_config.py
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
- [[A project defines a scoped focus area for a team.]] - rationale - gateway/security/group_config.py
- [[Build the system-prompt injection for project_scoped mode.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format a user's accessible projects for display.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format a user's group memberships for display.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Format detailed info for a single group.]] - rationale - gateway/proxy/collaborator_responses.py
- [[Handle addtogroup user_id group_id (owner only).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle groupinfo group_id.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle groups — list groups this user belongs to.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle projects — list accessible projects.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle rmfromgroup user_id group_id (owner or group admin).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Handle setmode group_iduser_id local_onlyproject_scopedfull_access (owne]] - rationale - gateway/proxy/telegram_proxy.py
- [[ProjectConfig]] - code - gateway/security/group_config.py
- [[Return True if any focus_topic appears in the text (case-insensitive).]] - rationale - gateway/security/group_config.py
- [[Return all projects accessible to the user via group membership.]] - rationale - gateway/security/group_config.py
- [[Return the first project accessible to a user (primary project).]] - rationale - gateway/security/group_config.py
- [[Send a rate-limited activity mirror to the owner chat for collaborator messages.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic owner admin notice without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestBuildProjectContextInjection]] - code - gateway/tests/test_collaborator_responses.py
- [[TestConstantMessages]] - code - gateway/tests/test_collaborator_responses.py
- [[TestErrorFormatters]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupInfo]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatProjectsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestMutationFormatters]] - code - gateway/tests/test_collaborator_responses.py
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
- [[teams()_3]] - code - gateway/tests/test_collaborator_responses.py
- [[telegram_proxy.py_2]] - code - gateway/proxy/telegram_proxy.py
- [[test_collaborator_responses.py]] - code - gateway/tests/test_collaborator_responses.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/telegram_proxypy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_TelegramAPIProxy_1]]
- 15 edges to [[_COMMUNITY_RBACConfig]]
- 11 edges to [[_COMMUNITY_GroupConfig]]
- 8 edges to [[_COMMUNITY_group_config.py]]
- 5 edges to [[_COMMUNITY_rbac_config.py]]
- 1 edge to [[_COMMUNITY_TELEGRAM_API_BASE_URL]]
- 1 edge to [[_COMMUNITY_dot-analyze_message]]
- 1 edge to [[_COMMUNITY_RateLimiter]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_dot-_proxy_request_impl]]
- 1 edge to [[_COMMUNITY_dot-_active_send_token]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_DOCKER-VPN-NETWORKING]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_egress_retry.py]]
- 1 edge to [[_COMMUNITY_TelegramGatewayRelay]]

## Top bridge nodes
- [[telegram_proxy.py_2]] - degree 34, connects to 16 communities
- [[collaborator_responses.py]] - degree 16, connects to 3 communities
- [[test_collaborator_responses.py]] - degree 23, connects to 2 communities
- [[ProjectConfig]] - degree 18, connects to 2 communities
- [[dot-_send_owner_admin_notice()]] - degree 12, connects to 2 communities
