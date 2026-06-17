---
type: community
cohesion: 0.05
members: 65
---

# Group Config & Teams

**Cohesion:** 0.05 - loosely connected
**Members:** 65 nodes

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
- [[.is_group_admin()]] - code - gateway/security/group_config.py
- [[.is_member()]] - code - gateway/security/group_config.py
- [[.model_post_init()_1]] - code - gateway/security/group_config.py
- [[.test_apply_persisted_overrides_skips_user_overrides_key()]] - code - gateway/tests/test_group_config.py
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
- [[.test_no_duplicate_projects()]] - code - gateway/tests/test_group_config.py
- [[.test_no_prefix_by_default()]] - code - gateway/tests/test_group_config.py
- [[.test_parses_groups()]] - code - gateway/tests/test_group_config.py
- [[.test_parses_projects()]] - code - gateway/tests/test_group_config.py
- [[.test_prefix_not_returned_for_non_member()]] - code - gateway/tests/test_group_config.py
- [[.test_prefix_returned_for_member()]] - code - gateway/tests/test_group_config.py
- [[.test_project_scoped_mode()]] - code - gateway/tests/test_group_config.py
- [[.test_unknown_user_returns_local_only()]] - code - gateway/tests/test_group_config.py
- [[.test_unknown_user_returns_none()]] - code - gateway/tests/test_group_config.py
- [[.test_user_override_takes_precedence_over_group()]] - code - gateway/tests/test_group_config.py
- [[A team group with members, admin, projects, and collab mode.]] - rationale - gateway/security/group_config.py
- [[GroupConfig]] - code - gateway/security/group_config.py
- [[Merge group_overrides.json additions into the in-memory TeamsConfig.]] - rationale - gateway/security/group_config.py
- [[Per-user collab_mode override persists to group_overrides.json and takes     pr]] - rationale - gateway/tests/test_group_config.py
- [[Per-user override beats group-derived collab_mode.]] - rationale - gateway/tests/test_group_config.py
- [[Return all groups the user belongs to.]] - rationale - gateway/security/group_config.py
- [[Return all projects accessible to the user via group membership.]] - rationale - gateway/security/group_config.py
- [[Return deduplicated list of all user IDs across all groups.]] - rationale - gateway/security/group_config.py
- [[Return mapping of group_id → admin_user_id for all groups that have an admin.]] - rationale - gateway/security/group_config.py
- [[Return the effective collab_mode for a user.          Resolution order]] - rationale - gateway/security/group_config.py
- [[Return the first project accessible to a user (primary project).]] - rationale - gateway/security/group_config.py
- [[Return the safe_response_prefix for the first group that the user belongs to]] - rationale - gateway/security/group_config.py
- [[TeamsConfig_1]] - code - gateway/tests/test_group_config.py
- [[TeamsConfig]] - code - gateway/security/group_config.py
- [[TestAdminChecks]] - code - gateway/tests/test_group_config.py
- [[TestCollabMode]] - code - gateway/tests/test_group_config.py
- [[TestGroupSafeResponsePrefix]] - code - gateway/tests/test_group_config.py
- [[TestMembershipQueries]] - code - gateway/tests/test_group_config.py
- [[TestProjectQueries]] - code - gateway/tests/test_group_config.py
- [[TestTeamsConfigParsing]] - code - gateway/tests/test_group_config.py
- [[TestUserCollabModeOverride]] - code - gateway/tests/test_group_config.py
- [[Top-level teams configuration parsed from agentshroud.yaml `teams` section.]] - rationale - gateway/security/group_config.py
- [[Without a per-user override, group-derived mode is returned.]] - rationale - gateway/tests/test_group_config.py
- [[__user_overrides__ key must not be treated as a group_id.]] - rationale - gateway/tests/test_group_config.py
- [[_apply_persisted_overrides()]] - code - gateway/security/group_config.py
- [[teams()_1]] - code - gateway/tests/test_group_config.py
- [[test_group_config.py]] - code - gateway/tests/test_group_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Group_Config__Teams
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_Collaborator Responses]]
- 14 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 7 edges to [[_COMMUNITY_Privacy Policy]]
- 7 edges to [[_COMMUNITY_Module Group 75]]
- 6 edges to [[_COMMUNITY_Module Group 208]]
- 4 edges to [[_COMMUNITY_RBAC Configuration]]
- 2 edges to [[_COMMUNITY_Module Group 83]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 1 edge to [[_COMMUNITY_Module Group 189]]
- 1 edge to [[_COMMUNITY_Module Group 186]]

## Top bridge nodes
- [[TeamsConfig]] - degree 67, connects to 9 communities
- [[GroupConfig]] - degree 32, connects to 5 communities
- [[test_group_config.py]] - degree 12, connects to 2 communities
- [[TestUserCollabModeOverride]] - degree 10, connects to 2 communities
- [[TestGroupSafeResponsePrefix]] - degree 11, connects to 1 community