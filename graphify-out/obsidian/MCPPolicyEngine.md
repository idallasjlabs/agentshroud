---
source_file: "gateway/security/mcp_policy.py"
type: "code"
community: "Egress Domain Allowlist"
location: "L241"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Domain_Allowlist
---

# MCPPolicyEngine

## Connections
- [[.__init__()_91]] - `method` [EXTRACTED]
- [[._decide()_1]] - `method` [EXTRACTED]
- [[._tier_for()_1]] - `method` [EXTRACTED]
- [[.enforce()_1]] - `method` [EXTRACTED]
- [[.evaluate()_1]] - `method` [EXTRACTED]
- [[.test_engine_allows_known_server_under_default()]] - `calls` [EXTRACTED]
- [[.test_engine_denies_unknown_server_under_default()]] - `calls` [EXTRACTED]
- [[.test_engine_requires_approval_for_destructive_tool_on_known_server()]] - `calls` [EXTRACTED]
- [[.test_no_mcp_section_still_deny_by_default()]] - `calls` [EXTRACTED]
- [[Decides allow  deny  require-approval for MCP tool calls.      Usage]] - `rationale_for` [EXTRACTED]
- [[GroupRoleResolver]] - `semantically_similar_to` [INFERRED]
- [[MCPPolicyConfig_1]] - `uses` [INFERRED]
- [[MCPPolicyEngine_1]] - `uses` [INFERRED]
- [[MonkeyPatch]] - `uses` [INFERRED]
- [[Path_32]] - `uses` [INFERRED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[TestDefaultMcpPolicyIsFailClosed]] - `uses` [INFERRED]
- [[TestDefaultPolicyNoMcpServers]] - `uses` [INFERRED]
- [[_FakeApprovalQueue]] - `uses` [INFERRED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[mcp_policy.py]] - `contains` [EXTRACTED]
- [[rbac_config.py]] - `calls` [EXTRACTED]
- [[test_bare_tool_name_risk_tier_applies_across_servers()]] - `calls` [EXTRACTED]
- [[test_decision_records_soc_heatmap()]] - `calls` [EXTRACTED]
- [[test_default_allow_opt_in_permits_non_allowlisted_safe_tool()]] - `calls` [EXTRACTED]
- [[test_default_deny_posture_when_no_config()]] - `calls` [EXTRACTED]
- [[test_denied_tool_can_be_specified_bare_or_qualified()]] - `calls` [EXTRACTED]
- [[test_denylist_wins_over_allowlist()]] - `calls` [EXTRACTED]
- [[test_enforce_allows_allowlisted_safe_tool()]] - `calls` [EXTRACTED]
- [[test_enforce_blocks_unknown_server()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_denied_on_rejection()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_enqueues_and_allows_on_approval()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_queue_no_wait_denies_closed()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_without_queue_denies_closed()]] - `calls` [EXTRACTED]
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow()]] - `calls` [EXTRACTED]
- [[test_enforce_unicode_evasion_still_denied()]] - `calls` [EXTRACTED]
- [[test_invalid_default_action_falls_back_to_deny()]] - `calls` [EXTRACTED]
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - `calls` [EXTRACTED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mcp_policy_default_failclosed.py]] - `imports` [EXTRACTED]
- [[test_mcp_proxy_allows_policy_permitted_call()]] - `calls` [EXTRACTED]
- [[test_mcp_proxy_blocks_policy_denied_call()]] - `calls` [EXTRACTED]
- [[test_mcp_proxy_real_queue_high_risk_never_executes_without_approval()]] - `calls` [EXTRACTED]
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - `calls` [EXTRACTED]
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Domain_Allowlist