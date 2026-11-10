---
type: community
members: 56
---

# Community 194

**Members:** 56 nodes

## Members
- [[.__init__()_121]] - code - gateway/security/tool_acl.py
- [[.effective_admin()]] - code - gateway/security/tool_acl.py
- [[.effective_collaborator_allowed()]] - code - gateway/security/tool_acl.py
- [[.effective_private()]] - code - gateway/security/tool_acl.py
- [[.test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_can_use_unknown_tool_when_not_denied()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[.test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[.test_group_allowlist_grants_extra_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[.test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_allowed_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_and_admin_do_not_overlap_with_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_private_tool_still_blocked_even_when_deny_unknown_false()]] - code - gateway/tests/test_tool_acl.py
- [[.test_project_allowed_tools_grant_access()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_in_private_tools()]] - code - gateway/tests/test_tool_acl.py
- [[.test_terminal_tool_not_in_collab_allowed()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_viewer_denied_terminal_tool()]] - code - gateway/tests/test_tool_acl.py
- [[ADMIN_TOOLS]] - code - gateway/security/tool_acl.py
- [[COLLABORATOR_ALLOWED_TOOLS]] - code - gateway/security/tool_acl.py
- [[PRIVATE_TOOLS]] - code - gateway/security/tool_acl.py
- [[Policy configuration for tool ACL enforcement.      Loaded from agentshroud.yaml]] - rationale - gateway/security/tool_acl.py
- [[RBACConfig_4]] - code - gateway/tests/test_tool_acl.py
- [[TeamsConfig_2]] - code - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCVE2026_9367TerminalToolDenied]] - code - gateway/tests/test_tool_acl.py
- [[TestClassificationSets]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestDenyUnknownFalse]] - code - gateway/tests/test_tool_acl.py
- [[TestGroupToolAllowlist]] - code - gateway/tests/test_tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestViewerAccess]] - code - gateway/tests/test_tool_acl.py
- [[ToolACLConfig]] - code - gateway/security/tool_acl.py
- [[_make_rbac()_1]] - code - gateway/tests/test_tool_acl.py
- [[enforcer()_3]] - code - gateway/tests/test_tool_acl.py
- [[rbac()_6]] - code - gateway/tests/test_tool_acl.py
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - rationale - gateway/tests/test_tool_acl.py
- [[test_tool_acl.py]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_194
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Community 6]]
- 24 edges to [[_COMMUNITY_Community 11]]
- 12 edges to [[_COMMUNITY_Community 196]]
- 7 edges to [[_COMMUNITY_Community 33]]
- 2 edges to [[_COMMUNITY_Community 986]]
- 2 edges to [[_COMMUNITY_Community 1424]]
- 1 edge to [[_COMMUNITY_Community 884]]
- 1 edge to [[_COMMUNITY_Community 1284]]
- 1 edge to [[_COMMUNITY_Community 1070]]
- 1 edge to [[_COMMUNITY_Community 300]]

## Top bridge nodes
- [[ToolACLConfig]] - degree 38, connects to 8 communities
- [[test_tool_acl.py]] - degree 23, connects to 6 communities
- [[TestCVE2026_9367TerminalToolDenied]] - degree 14, connects to 3 communities
- [[TestCollaboratorAccess]] - degree 12, connects to 3 communities
- [[TestOwnerAccess]] - degree 10, connects to 3 communities