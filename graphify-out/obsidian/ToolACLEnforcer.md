---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "Community 134"
location: "206"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_134
---

# ToolACLEnforcer

## Connections
- [[dot-__init__()_1]] - `method` [EXTRACTED]
- [[dot-_can_use_tool_impl()]] - `method` [EXTRACTED]
- [[dot-_get_group_tool_allowlist()]] - `method` [EXTRACTED]
- [[dot-_get_role()]] - `method` [EXTRACTED]
- [[dot-can_use_tool()_1]] - `method` [EXTRACTED]
- [[dot-can_use_tool_from_origin()]] - `method` [EXTRACTED]
- [[dot-can_use_tool_in_group_context()]] - `method` [EXTRACTED]
- [[dot-check_tool_rate_limit()]] - `method` [EXTRACTED]
- [[dot-enforcer()]] - `calls` [EXTRACTED]
- [[dot-get_allowed_tools()]] - `method` [EXTRACTED]
- [[dot-get_denial_counts()]] - `method` [EXTRACTED]
- [[dot-get_denied_tools()]] - `method` [EXTRACTED]
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - `calls` [EXTRACTED]
- [[dot-test_enforce_mode_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_enforcer_without_trust_manager_unchanged()]] - `calls` [EXTRACTED]
- [[dot-test_group_allowlist_grants_extra_tool()]] - `calls` [EXTRACTED]
- [[dot-test_monitor_mode_logs_but_does_not_block_via_trust_gate()]] - `calls` [EXTRACTED]
- [[dot-test_monitor_mode_still_allows_permitted_tools()]] - `calls` [EXTRACTED]
- [[dot-test_no_rbac_allows_read()]] - `calls` [EXTRACTED]
- [[dot-test_no_rbac_defaults_to_viewer()]] - `calls` [EXTRACTED]
- [[dot-test_private_tool_still_blocked_even_when_deny_unknown_false()]] - `calls` [EXTRACTED]
- [[dot-test_project_allowed_tools_grant_access()]] - `calls` [EXTRACTED]
- [[dot-test_tool_acl_can_use_tool_records()]] - `calls` [EXTRACTED]
- [[dot-test_trust_deny_wins_over_acl()]] - `calls` [EXTRACTED]
- [[dot-test_unknown_tool_falls_through_to_acl()]] - `calls` [EXTRACTED]
- [[CVE-2026-35190 — execute_command owner-only fix]] - `cites` [EXTRACTED]
- [[CVE-2026-9367 — command injection bypass via terminal_tool]] - `cites` [EXTRACTED]
- [[Enforces tool-level access control based on user role and group membership.…]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `shares_data_with` [INFERRED]
- [[RateLimitGuard]] - `conceptually_related_to` [INFERRED]
- [[TestDenyUnknownFalse]] - `uses` [INFERRED]
- [[TestEgressWiringEndToEnd]] - `uses` [INFERRED]
- [[TestEnforcementMode]] - `uses` [INFERRED]
- [[TestEnforcementWiring]] - `uses` [INFERRED]
- [[TestGroupRoleProperties]] - `uses` [INFERRED]
- [[TestGroupRoleResolver]] - `uses` [INFERRED]
- [[TestGroupToolAllowlist]] - `uses` [INFERRED]
- [[TestMemberGroupContext]] - `uses` [INFERRED]
- [[TestNoRBACConfig]] - `uses` [INFERRED]
- [[TestOwnerGroupContext]] - `uses` [INFERRED]
- [[TestReadOnlyMemberGroupContext]] - `uses` [INFERRED]
- [[TestToolACLComposition]] - `uses` [INFERRED]
- [[TestToolRateLimiting]] - `uses` [INFERRED]
- [[enforcer()_2]] - `calls` [EXTRACTED]
- [[enforcer()]] - `uses` [INFERRED]
- [[gateway.security.tool_acl]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_group_rbac.py]] - `imports` [EXTRACTED]
- [[test_module_stats.py]] - `imports` [EXTRACTED]
- [[test_progressive_trust_integration.py]] - `imports` [EXTRACTED]
- [[test_tool_acl.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_134