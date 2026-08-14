---
source_file: "gateway/tests/test_mcp_policy.py"
type: "code"
community: "Egress Domain Allowlist"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Domain_Allowlist
---

# MCPPolicyEngine

## Connections
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[ApprovalStore_1]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[MCPPolicyAction]] - `uses` [INFERRED]
- [[MCPPolicyConfig]] - `uses` [INFERRED]
- [[MCPPolicyDecision]] - `uses` [INFERRED]
- [[MCPPolicyEngine]] - `uses` [INFERRED]
- [[MCPProxy]] - `uses` [INFERRED]
- [[MCPToolCall]] - `uses` [INFERRED]
- [[MCPToolResult]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[ToolRiskConfig_1]] - `uses` [INFERRED]
- [[engine()_1]] - `references` [EXTRACTED]
- [[test_allowlisted_server_safe_tool_is_allowed()]] - `references` [EXTRACTED]
- [[test_bare_tool_name_risk_tier_applies_across_servers()]] - `calls` [EXTRACTED]
- [[test_critical_tool_requires_approval()]] - `references` [EXTRACTED]
- [[test_decision_records_soc_heatmap()]] - `calls` [EXTRACTED]
- [[test_default_allow_opt_in_permits_non_allowlisted_safe_tool()]] - `calls` [EXTRACTED]
- [[test_default_deny_posture_when_no_config()]] - `calls` [EXTRACTED]
- [[test_denied_tool_can_be_specified_bare_or_qualified()]] - `calls` [EXTRACTED]
- [[test_denylist_wins_over_allowlist()]] - `calls` [EXTRACTED]
- [[test_denylisted_server_is_denied_even_if_tool_safe()]] - `references` [EXTRACTED]
- [[test_denylisted_tool_is_denied()]] - `references` [EXTRACTED]
- [[test_enforce_allows_allowlisted_safe_tool()]] - `calls` [EXTRACTED]
- [[test_enforce_blocks_unknown_server()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_denied_on_rejection()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_enqueues_and_allows_on_approval()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_queue_no_wait_denies_closed()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_without_queue_denies_closed()]] - `calls` [EXTRACTED]
- [[test_enforce_unicode_evasion_still_denied()]] - `calls` [EXTRACTED]
- [[test_high_risk_tool_requires_approval()]] - `references` [EXTRACTED]
- [[test_invalid_default_action_falls_back_to_deny()]] - `calls` [EXTRACTED]
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - `calls` [EXTRACTED]
- [[test_mcp_proxy_allows_policy_permitted_call()]] - `calls` [EXTRACTED]
- [[test_mcp_proxy_blocks_policy_denied_call()]] - `calls` [EXTRACTED]
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - `calls` [EXTRACTED]
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - `calls` [EXTRACTED]
- [[test_server_and_tool_matching_is_case_insensitive()]] - `references` [EXTRACTED]
- [[test_unknown_server_is_denied_by_default()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Domain_Allowlist