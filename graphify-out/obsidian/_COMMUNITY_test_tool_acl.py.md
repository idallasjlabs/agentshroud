---
type: community
members: 54
---

# test_tool_acl.py

**Members:** 54 nodes

## Members
- [[dot-__init__()_182]] - code - gateway/security/tool_acl.py
- [[dot-effective_admin()]] - code - gateway/security/tool_acl.py
- [[dot-effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[dot-effective_private()]] - code - gateway/security/tool_acl.py
- [[dot-enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
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
- [[dot-test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[Policy configuration for tool ACL enforcement. Loaded from agentshroud.yaml…]] - rationale - gateway/security/tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[Tests for gatewaysecuritytool_acl.py — V9-T2 Tool-level access control.]] - rationale - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[_make_rbac()_1]] - code - gateway/tests/test_tool_acl.py
- [[enforcer()_3]] - code - gateway/tests/test_tool_acl.py
- [[fixture_124]] - code
- [[rbac()_6]] - code - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_tool_aclpy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_GroupRoleResolver]]
- 3 edges to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_TestOriginAwareAuthorization]]
- 1 edge to [[_COMMUNITY_TestCVE2026_9367TerminalToolDenied]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[test_tool_acl.py]] - degree 23, connects to 7 communities
- [[_make_rbac()_1]] - degree 7, connects to 2 communities
- [[TestGroupToolAllowlist]] - degree 6, connects to 2 communities
- [[ToolACLConfig]] - degree 18, connects to 1 community
- [[TestToolRateLimiting]] - degree 7, connects to 1 community
