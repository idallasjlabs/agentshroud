---
type: community
cohesion: 0.03
members: 80
---

# ingest_api/main.py

**Cohesion:** 0.03 - loosely connected
**Members:** 80 nodes

## Members
- [[dot-__init__()_172]] - code - gateway/security/tool_acl.py
- [[dot-effective_admin()]] - code - gateway/security/tool_acl.py
- [[dot-effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[dot-effective_private()]] - code - gateway/security/tool_acl.py
- [[dot-enforcer()]] - code - gateway/tests/test_tool_acl.py
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
- [[dot-test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
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
- [[dot-test_project_allowed_tools_grant_access()]] - code - gateway/tests/test_tool_acl.py
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
- [[COLLABORATOR_ALLOWED_TOOLS]] - code - gateway/security/tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[Fail closed an origin nobody vouched for is not trusted.          A caller that]] - rationale - gateway/tests/test_tool_acl.py
- [[PRIVATE_TOOLS]] - code - gateway/security/tool_acl.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[Refusing ELEVATION is not the same as blanket denial — an unverified         ori]] - rationale - gateway/tests/test_tool_acl.py
- [[TeamsConfig_2]] - code - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOriginAwareAuthorization]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[The control is agent-agnostic by construction it takes an origin and         an]] - rationale - gateway/tests/test_tool_acl.py
- [[The core of the CVE class a side channel claiming to be the owner.          ter]] - rationale - gateway/tests/test_tool_acl.py
- [[The legitimate path must not regress.]] - rationale - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[_make_rbac()]] - code - gateway/tests/test_tool_acl.py
- [[enforcer()_2]] - code - gateway/tests/test_tool_acl.py
- [[rbac()_4]] - code - gateway/tests/test_tool_acl.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ingest_api/mainpy
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 26 edges to [[_COMMUNITY_socrouter.py]]
- 13 edges to [[_COMMUNITY_colima-health-check.sh]]
- 9 edges to [[_COMMUNITY_test_soc_bots.py]]
- 1 edge to [[_COMMUNITY_record_decision()]]

## Top bridge nodes
- [[test_tool_acl.py]] - degree 23, connects to 4 communities
- [[ToolACLConfig]] - degree 38, connects to 3 communities
- [[TestCVE2026_9367TerminalToolDenied]] - degree 14, connects to 3 communities
- [[TestOriginAwareAuthorization]] - degree 14, connects to 3 communities
- [[TestCollaboratorAccess]] - degree 12, connects to 3 communities
