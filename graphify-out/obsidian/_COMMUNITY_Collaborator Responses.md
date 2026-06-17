---
type: community
cohesion: 0.05
members: 68
---

# Collaborator Responses

**Cohesion:** 0.05 - loosely connected
**Members:** 68 nodes

## Members
- [[._handle_addtogroup_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_groupinfo_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_groups_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_projects_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_rmfromgroup_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_setmode_command()]] - code - gateway/proxy/telegram_proxy.py
- [[._mirror_to_owner_if_collaborator()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_admin_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[.matches_topic()]] - code - gateway/security/group_config.py
- [[.normalise_topics()]] - code - gateway/security/group_config.py
- [[.test_addtogroup_success()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_already_member()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_collab_outside_scope_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_collab_unavailable_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_contains_allowed_tools()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_contains_group_and_project()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_member_sees_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_member_sees_project()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_groups_for_unknown_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_groups_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_permission()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_projects_for_unknown_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_no_projects_not_empty()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_not_member()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_rmfromgroup_success()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_setmode_success_group()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_setmode_success_user()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_shows_admin()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_shows_projects()]] - code - gateway/tests/test_collaborator_responses.py
- [[.test_unknown_group()]] - code - gateway/tests/test_collaborator_responses.py
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
- [[Send a rate-limited activity mirror to the owner chat for collaborator messages.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic owner admin notice without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestBuildProjectContextInjection]] - code - gateway/tests/test_collaborator_responses.py
- [[TestConstantMessages]] - code - gateway/tests/test_collaborator_responses.py
- [[TestErrorFormatters]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupInfo]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatGroupsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestFormatProjectsList]] - code - gateway/tests/test_collaborator_responses.py
- [[TestMutationFormatters]] - code - gateway/tests/test_collaborator_responses.py
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
- [[test_collaborator_responses.py]] - code - gateway/tests/test_collaborator_responses.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Collaborator_Responses
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_Group Config & Teams]]
- 17 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 13 edges to [[_COMMUNITY_Module Group 208]]
- 2 edges to [[_COMMUNITY_Module Group 160]]
- 1 edge to [[_COMMUNITY_Module Group 83]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Slack Proxy]]
- 1 edge to [[_COMMUNITY_Module Group 87]]

## Top bridge nodes
- [[ProjectConfig]] - degree 27, connects to 3 communities
- [[._send_owner_admin_notice()]] - degree 12, connects to 3 communities
- [[slack_proxy.py]] - degree 4, connects to 3 communities
- [[collaborator_responses.py]] - degree 16, connects to 2 communities
- [[._handle_addtogroup_command()]] - degree 7, connects to 2 communities