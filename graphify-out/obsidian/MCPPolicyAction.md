---
source_file: "gateway/security/mcp_policy.py"
type: "code"
community: "MCPPolicyEngine"
location: "L51"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCPPolicyEngine
---

# MCPPolicyAction

## Connections
- [[dot-from_dict()_8]] - `calls` [EXTRACTED]
- [[Enum_32]] - `inherits` [EXTRACTED]
- [[TestDefaultMcpPolicyIsFailClosed]] - `uses` [INFERRED]
- [[TestDefaultPolicyNoMcpServers]] - `uses` [INFERRED]
- [[The three terminal policy outcomes for an MCP tool call.]] - `rationale_for` [EXTRACTED]
- [[mcp_policy.py]] - `contains` [EXTRACTED]
- [[str_15]] - `inherits` [EXTRACTED]
- [[test_allowlisted_server_safe_tool_is_allowed()]] - `uses` [INFERRED]
- [[test_bare_tool_name_risk_tier_applies_across_servers()]] - `uses` [INFERRED]
- [[test_critical_tool_requires_approval()]] - `uses` [INFERRED]
- [[test_default_allow_opt_in_permits_non_allowlisted_safe_tool()]] - `uses` [INFERRED]
- [[test_default_deny_posture_when_no_config()]] - `uses` [INFERRED]
- [[test_denied_tool_can_be_specified_bare_or_qualified()]] - `uses` [INFERRED]
- [[test_denylist_wins_over_allowlist()]] - `uses` [INFERRED]
- [[test_denylisted_server_is_denied_even_if_tool_safe()]] - `uses` [INFERRED]
- [[test_denylisted_tool_is_denied()]] - `uses` [INFERRED]
- [[test_enforce_allows_allowlisted_safe_tool()]] - `uses` [INFERRED]
- [[test_enforce_blocks_unknown_server()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_denied_on_rejection()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_enqueues_and_allows_on_approval()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_queue_no_wait_denies_closed()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_without_queue_denies_closed()]] - `uses` [INFERRED]
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow()]] - `uses` [INFERRED]
- [[test_enforce_unicode_evasion_still_denied()]] - `uses` [INFERRED]
- [[test_high_risk_tool_requires_approval()]] - `uses` [INFERRED]
- [[test_invalid_default_action_falls_back_to_deny()]] - `uses` [INFERRED]
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - `uses` [INFERRED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mcp_policy_default_failclosed.py]] - `imports` [EXTRACTED]
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - `uses` [INFERRED]
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - `uses` [INFERRED]
- [[test_server_and_tool_matching_is_case_insensitive()]] - `uses` [INFERRED]
- [[test_unknown_server_is_denied_by_default()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/MCPPolicyEngine
