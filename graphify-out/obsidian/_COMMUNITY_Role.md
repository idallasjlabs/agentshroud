---
type: community
cohesion: 0.03
members: 103
---

# Role

**Cohesion:** 0.03 - loosely connected
**Members:** 103 nodes

## Members
- [[dot-__init__()_197]] - code - gateway/security/tool_acl.py
- [[dot-_can_use_tool_impl()]] - code - gateway/security/tool_acl.py
- [[dot-_get_group_tool_allowlist()]] - code - gateway/security/tool_acl.py
- [[dot-_get_role()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool()_1]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_from_origin()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_in_group_context()]] - code - gateway/security/tool_acl.py
- [[dot-check_tool_rate_limit()]] - code - gateway/security/tool_acl.py
- [[dot-effective_admin()]] - code - gateway/security/tool_acl.py
- [[dot-effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[dot-effective_private()]] - code - gateway/security/tool_acl.py
- [[dot-enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-get_allowed_tools()]] - code - gateway/security/tool_acl.py
- [[dot-get_denial_counts()]] - code - gateway/security/tool_acl.py
- [[dot-get_denied_tools()]] - code - gateway/security/tool_acl.py
- [[dot-get_users_by_role()]] - code - gateway/security/rbac_config.py
- [[dot-set_user_role()_1]] - code - gateway/security/rbac_config.py
- [[dot-test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_allowed_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_and_admin_do_not_overlap()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_and_admin_do_not_overlap_with_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_tool_still_blocked_even_when_deny_unknown_false()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_project_allowed_tools_grant_access()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_tool_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_tool_not_in_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[ADMIN_TOOLS]] - code - gateway/security/tool_acl.py
- [[Authorize a tool call, refusing owner elevation over an unverified origin.]] - rationale - gateway/security/tool_acl.py
- [[COLLABORATOR_ALLOWED_TOOLS]] - code - gateway/security/tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Check whether user_id may invoke the named tool.          Returns             (]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group workspace.]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Enforces tool-level access control based on user role and group membership.]] - rationale - gateway/security/tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[GHSA-58qx-6m8p-wh2j — Slack group DMs skip sender allowlists]] - document - gateway/security/tool_acl.py
- [[GHSA-7cp7-87pj-p32v — skill dispatch skips owner-only policy]] - document - gateway/security/tool_acl.py
- [[GHSA-hpg5-cq3m-phqp — agent cron tool reaches operator command jobs]] - document - gateway/security/tool_acl.py
- [[GHSA-rrxp-5mx8-mvhh — inbound voice calls inherit owner tool authorization]] - document - gateway/security/tool_acl.py
- [[GHSA-wwcw-jfpp-gpxw — native tools ignore per-chat policy]] - document - gateway/security/tool_acl.py
- [[Get all users with a specific role.]] - rationale - gateway/security/rbac_config.py
- [[Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)]] - rationale - gateway/security/tool_acl.py
- [[PRIVATE_TOOLS]] - code - gateway/security/tool_acl.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the_1]] - rationale - gateway/security/tool_acl.py
- [[RBACConfig_4]] - code - gateway/security/rbac.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[Return True if the user is within rate limits for the given tool.          Side-]] - rationale - gateway/security/tool_acl.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py
- [[Role_96]] - code - gateway/security/rbac_config.py
- [[SCLCaller_2]] - code - gateway/tests/test_soc_bots.py
- [[Set role for a user ID (owner-only operation).]] - rationale - gateway/security/rbac_config.py
- [[TeamsConfig_2]] - code - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorActivityBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer]] - code - gateway/security/tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[User roles in AgentShroud RBAC system.      Hierarchy (highest to lowest)]] - rationale - gateway/security/rbac_config.py
- [[_make_rbac()_1]] - code - gateway/tests/test_tool_acl.py
- [[can_use_tool_from_origin]] - code - gateway/security/tool_acl.py
- [[enforcer()_3]] - code - gateway/tests/test_tool_acl.py
- [[rbac()_6]] - code - gateway/tests/test_tool_acl.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Role
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_RBACConfig]]
- 20 edges to [[_COMMUNITY_GroupRoleResolver]]
- 19 edges to [[_COMMUNITY_TrustConfig]]
- 19 edges to [[_COMMUNITY_Action]]
- 17 edges to [[_COMMUNITY_test_soc_bots.py]]
- 10 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 6 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 6 edges to [[_COMMUNITY_TestFromAuditChainEntry]]
- 5 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 5 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 4 edges to [[_COMMUNITY_Enum]]
- 4 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 4 edges to [[_COMMUNITY__FakeRBAC]]
- 4 edges to [[_COMMUNITY_TestOriginAwareAuthorization]]
- 3 edges to [[_COMMUNITY_A2AMethod]]
- 3 edges to [[_COMMUNITY_TestMiddlewareSessionEnforcement]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_TestGroupRoleResolver]]
- 1 edge to [[_COMMUNITY_dot-get_user_role]]
- 1 edge to [[_COMMUNITY_rbac_config.py]]
- 1 edge to [[_COMMUNITY_WebhookReceiver]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPersistence]]
- 1 edge to [[_COMMUNITY_TestUserSessionManager]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_test_e2e.py]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy._process]]

## Top bridge nodes
- [[Role_96]] - degree 107, connects to 21 communities
- [[ToolACLEnforcer]] - degree 78, connects to 9 communities
- [[ToolACLConfig]] - degree 38, connects to 4 communities
- [[test_tool_acl.py]] - degree 23, connects to 2 communities
- [[can_use_tool_from_origin]] - degree 5, connects to 2 communities
