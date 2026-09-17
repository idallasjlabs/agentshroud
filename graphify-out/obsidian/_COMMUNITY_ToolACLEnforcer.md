---
type: community
cohesion: 0.09
members: 46
---

# ToolACLEnforcer

**Cohesion:** 0.09 - loosely connected
**Members:** 46 nodes

## Members
- [[.__init__()_206]] - code - gateway/security/tool_acl.py
- [[.check_tool_rate_limit()_1]] - code - gateway/security/tool_acl.py
- [[.effective_admin()_1]] - code - gateway/security/tool_acl.py
- [[.effective_collaborator_allowed()_1]] - code - gateway/security/tool_acl.py
- [[.effective_private()_1]] - code - gateway/security/tool_acl.py
- [[.enforcer()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_blocked_from_private_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_admin_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_collaborator_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_denied_tools_contains_private()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_group_allowlist_grants_extra_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_no_rbac_allows_read()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_no_rbac_defaults_to_viewer()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_admin_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_any_unknown_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_private_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_denied_tools_is_empty()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap_with_collab_allowed()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_project_allowed_tools_grant_access()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_admin_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_private_tool()_1]] - code - gateway/tests/test_tool_acl.py
- [[ADMIN_TOOLS]] - code - gateway/security/tool_acl.py
- [[COLLABORATOR_ALLOWED_TOOLS]] - code - gateway/security/tool_acl.py
- [[LLMProxy._enforce_tool_acl]] - code - gateway/proxy/llm_proxy.py
- [[PRIVATE_TOOLS]] - code - gateway/security/tool_acl.py
- [[Return True if the user is within rate limits for the given tool.          Side-]] - rationale - gateway/security/tool_acl.py
- [[TeamsConfig]] - code
- [[TestAdminAccess_1]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets_1]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse_1]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist_1]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig_1]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess_1]] - code - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting_1]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess_1]] - code - gateway/tests/test_tool_acl.py
- [[ToolACLConfig_1]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer_1]] - code - gateway/security/tool_acl.py
- [[_make_rbac()_2]] - code - gateway/tests/test_tool_acl.py
- [[can_use_tool_from_origin]] - code - gateway/security/tool_acl.py
- [[enforcer()_4]] - code - gateway/tests/test_tool_acl.py
- [[rbac()_7]] - code - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py_1]] - code - gateway/tests/test_tool_acl.py
- [[tool_acl.py]] - code - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolACLEnforcer
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 8 edges to [[_COMMUNITY_._can_use_tool_impl()]]
- 3 edges to [[_COMMUNITY_TestCollaboratorAccess]]
- 3 edges to [[_COMMUNITY_TestCVE2026_9367TerminalToolDenied]]
- 3 edges to [[_COMMUNITY_TestOriginAwareAuthorization]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_.get_denial_counts()]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_.test_under_threshold_passes()]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages]]
- 1 edge to [[_COMMUNITY_sunday-upgrade]]

## Top bridge nodes
- [[ToolACLEnforcer_1]] - degree 42, connects to 8 communities
- [[ToolACLConfig_1]] - degree 27, connects to 4 communities
- [[test_tool_acl.py_1]] - degree 21, connects to 4 communities
- [[TestToolRateLimiting_1]] - degree 8, connects to 2 communities
- [[tool_acl.py]] - degree 5, connects to 2 communities