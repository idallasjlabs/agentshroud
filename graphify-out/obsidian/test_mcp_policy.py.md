---
source_file: "gateway/tests/test_mcp_policy.py"
type: "code"
community: "Community 33"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_33
---

# test_mcp_policy.py

## Connections
- [[ApprovalQueueConfig_2]] - `imports` [EXTRACTED]
- [[ApprovalStore_1]] - `imports` [EXTRACTED]
- [[EnhancedApprovalQueue]] - `imports` [EXTRACTED]
- [[MCPPolicyAction]] - `imports` [EXTRACTED]
- [[MCPPolicyConfig]] - `imports` [EXTRACTED]
- [[MCPPolicyDecision]] - `imports` [EXTRACTED]
- [[MCPPolicyEngine]] - `imports` [EXTRACTED]
- [[MCPProxy]] - `imports` [EXTRACTED]
- [[MCPToolCall]] - `imports` [EXTRACTED]
- [[MCPToolResult]] - `imports` [EXTRACTED]
- [[RBACConfig_1]] - `imports` [EXTRACTED]
- [[ToolRiskConfig_1]] - `imports` [EXTRACTED]
- [[_FakeApprovalQueue]] - `contains` [EXTRACTED]
- [[_base_config()_1]] - `contains` [EXTRACTED]
- [[_real_queue()]] - `contains` [EXTRACTED]
- [[engine()_1]] - `contains` [EXTRACTED]
- [[mcp_policy.py]] - `references` [EXTRACTED]
- [[test_allowlisted_server_safe_tool_is_allowed()]] - `contains` [EXTRACTED]
- [[test_bare_tool_name_risk_tier_applies_across_servers()]] - `contains` [EXTRACTED]
- [[test_critical_tool_requires_approval()]] - `contains` [EXTRACTED]
- [[test_decision_records_soc_heatmap()]] - `contains` [EXTRACTED]
- [[test_default_allow_opt_in_permits_non_allowlisted_safe_tool()]] - `contains` [EXTRACTED]
- [[test_default_deny_posture_when_no_config()]] - `contains` [EXTRACTED]
- [[test_denied_tool_can_be_specified_bare_or_qualified()]] - `contains` [EXTRACTED]
- [[test_denylist_wins_over_allowlist()]] - `contains` [EXTRACTED]
- [[test_denylisted_server_is_denied_even_if_tool_safe()]] - `contains` [EXTRACTED]
- [[test_denylisted_tool_is_denied()]] - `contains` [EXTRACTED]
- [[test_enforce_allows_allowlisted_safe_tool()]] - `contains` [EXTRACTED]
- [[test_enforce_blocks_unknown_server()]] - `contains` [EXTRACTED]
- [[test_enforce_high_risk_denied_on_rejection()]] - `contains` [EXTRACTED]
- [[test_enforce_high_risk_enqueues_and_allows_on_approval()]] - `contains` [EXTRACTED]
- [[test_enforce_high_risk_queue_no_wait_denies_closed()]] - `contains` [EXTRACTED]
- [[test_enforce_high_risk_without_queue_denies_closed()]] - `contains` [EXTRACTED]
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow (regression guard)]] - `references` [EXTRACTED]
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow()]] - `contains` [EXTRACTED]
- [[test_enforce_unicode_evasion_still_denied()]] - `contains` [EXTRACTED]
- [[test_high_risk_tool_requires_approval()]] - `contains` [EXTRACTED]
- [[test_invalid_default_action_falls_back_to_deny()]] - `contains` [EXTRACTED]
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - `contains` [EXTRACTED]
- [[test_mcp_proxy_allows_policy_permitted_call()]] - `contains` [EXTRACTED]
- [[test_mcp_proxy_blocks_policy_denied_call()]] - `contains` [EXTRACTED]
- [[test_mcp_proxy_real_queue_high_risk_never_executes_without_approval()]] - `contains` [EXTRACTED]
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - `contains` [EXTRACTED]
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - `contains` [EXTRACTED]
- [[test_server_and_tool_matching_is_case_insensitive()]] - `contains` [EXTRACTED]
- [[test_unknown_server_is_denied_by_default()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_33