---
type: community
members: 97
---

# RBACConfig (2)

**Members:** 97 nodes

## Members
- [[dot-__init__()_137]] - code - gateway/security/tool_acl.py
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
- [[dot-test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_applies_to_any_agent_not_just_openclaw()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_denial_is_counted_for_soc_correlation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_non_owner_over_unverified_origin_is_unchanged()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_allowed_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_claim_over_unverified_origin_is_refused_elevation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_over_verified_origin_keeps_full_authority()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_and_admin_do_not_overlap()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_and_admin_do_not_overlap_with_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_private_tool_still_blocked_even_when_deny_unknown_false()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_tool_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_terminal_tool_not_in_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unknown_origin_defaults_to_unverified()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unverified_origin_still_allows_public_tools()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[A non-owner gains nothing and loses nothing from origin checking.]] - rationale - gateway/tests/test_tool_acl.py
- [[ADMIN_TOOLS]] - code - gateway/security/tool_acl.py
- [[AgentShroud-side mitigation for the 'channel skips the check' CVE class.      Up]] - rationale - gateway/tests/test_tool_acl.py
- [[Authorize a tool call, refusing owner elevation over an unverified origin.]] - rationale - gateway/security/tool_acl.py
- [[COLLABORATOR_ALLOWED_TOOLS]] - code - gateway/security/tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Check whether user_id may invoke the named tool.          Returns             (]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group workspace.]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Enforces tool-level access control based on user role and group membership.]] - rationale - gateway/security/tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[Fail closed an origin nobody vouched for is not trusted.          A caller that]] - rationale - gateway/tests/test_tool_acl.py
- [[PRIVATE_TOOLS]] - code - gateway/security/tool_acl.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the]] - rationale - gateway/security/tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[Refusing ELEVATION is not the same as blanket denial — an unverified         ori]] - rationale - gateway/tests/test_tool_acl.py
- [[Return True if the user is within rate limits for the given tool.          Side-]] - rationale - gateway/security/tool_acl.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOriginAwareAuthorization]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[The control is agent-agnostic by construction it takes an origin and         an]] - rationale - gateway/tests/test_tool_acl.py
- [[The core of the CVE class a side channel claiming to be the owner.          ter]] - rationale - gateway/tests/test_tool_acl.py
- [[The legitimate path must not regress.]] - rationale - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer]] - code - gateway/security/tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[enforcer()_1]] - code - gateway/tests/test_tool_acl.py
- [[rbac()_2]] - code - gateway/tests/test_tool_acl.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig_2
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_MiddlewareManager]]
- 19 edges to [[_COMMUNITY_TrustConfig]]
- 14 edges to [[_COMMUNITY_RBACConfig (2) (2)]]
- 11 edges to [[_COMMUNITY_RBACConfig (3)]]
- 8 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 2 edges to [[_COMMUNITY_RBACConfig (2) (3)]]
- 2 edges to [[_COMMUNITY_RBACConfig (2) (4)]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]

## Top bridge nodes
- [[ToolACLEnforcer]] - degree 77, connects to 8 communities
- [[ToolACLConfig]] - degree 38, connects to 4 communities
- [[test_tool_acl.py]] - degree 23, connects to 3 communities
- [[TestCVE2026_9367TerminalToolDenied]] - degree 14, connects to 2 communities
- [[TestOriginAwareAuthorization]] - degree 14, connects to 2 communities
