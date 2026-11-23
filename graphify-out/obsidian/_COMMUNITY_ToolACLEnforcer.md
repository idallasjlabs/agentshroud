---
type: community
members: 28
---

# ToolACLEnforcer

**Members:** 28 nodes

## Members
- [[dot-_can_use_tool_impl()]] - code - gateway/security/tool_acl.py
- [[dot-_get_group_tool_allowlist()]] - code - gateway/security/tool_acl.py
- [[dot-_get_role()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool()_1]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_from_origin()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_in_group_context()]] - code - gateway/security/tool_acl.py
- [[dot-check_tool_rate_limit()]] - code - gateway/security/tool_acl.py
- [[dot-get_allowed_tools()]] - code - gateway/security/tool_acl.py
- [[dot-get_denial_counts()]] - code - gateway/security/tool_acl.py
- [[dot-get_denied_tools()]] - code - gateway/security/tool_acl.py
- [[dot-test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_no_rbac_allows_read()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_trust_deny_wins_over_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unknown_tool_falls_through_to_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Authorize a tool call, refusing owner elevation over an unverified origin. WHY…]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke the named tool. Returns (allowed bool,…]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group…]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Enforces tool-level access control based on user role and group membership.…]] - rationale - gateway/security/tool_acl.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80), then…]] - rationale - gateway/security/tool_acl.py
- [[Return True if the user is within rate limits for the given tool. Side-effect…]] - rationale - gateway/security/tool_acl.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py
- [[TestNoRBACConfig]] - code - gateway/tests/test_tool_acl.py
- [[TestToolACLComposition]] - code - gateway/tests/test_progressive_trust_integration.py
- [[ToolACLEnforcer]] - code - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolACLEnforcer
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_lifespan.py]]
- 13 edges to [[_COMMUNITY_test_tool_acl.py]]
- 5 edges to [[_COMMUNITY_test_module_stats.py]]
- 2 edges to [[_COMMUNITY_test_group_rbac.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_GroupRole]]
- 1 edge to [[_COMMUNITY_TestToolRateLimiting]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[ToolACLEnforcer]] - degree 44, connects to 9 communities
- [[TestToolACLComposition]] - degree 7, connects to 1 community
- [[dot-can_use_tool()_1]] - degree 6, connects to 1 community
- [[TestNoRBACConfig]] - degree 5, connects to 1 community
- [[dot-can_use_tool_from_origin()]] - degree 4, connects to 1 community
