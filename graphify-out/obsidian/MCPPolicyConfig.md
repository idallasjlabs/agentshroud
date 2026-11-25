---
source_file: "gateway/security/mcp_policy.py"
type: "code"
community: "MCPPolicyEngine"
location: "L113"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCPPolicyEngine
---

# MCPPolicyConfig

## Connections
- [[dot-__init__()_129]] - `calls` [EXTRACTED]
- [[dot-__post_init__()_6]] - `method` [EXTRACTED]
- [[dot-from_dict()_8]] - `method` [EXTRACTED]
- [[Declarative MCP security policy. Loaded from the ``mcp_policy`` section of…]] - `rationale_for` [EXTRACTED]
- [[RBACConfig]] - `uses` [INFERRED]
- [[TestDefaultMcpPolicyIsFailClosed]] - `uses` [INFERRED]
- [[TestDefaultPolicyNoMcpServers]] - `uses` [INFERRED]
- [[_base_config()]] - `uses` [INFERRED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[mcp_policy.py]] - `contains` [EXTRACTED]
- [[test_bare_tool_name_risk_tier_applies_across_servers()]] - `uses` [INFERRED]
- [[test_default_allow_opt_in_permits_non_allowlisted_safe_tool()]] - `uses` [INFERRED]
- [[test_default_deny_posture_when_no_config()]] - `calls` [EXTRACTED]
- [[test_denied_tool_can_be_specified_bare_or_qualified()]] - `uses` [INFERRED]
- [[test_denylist_wins_over_allowlist()]] - `uses` [INFERRED]
- [[test_enforce_unicode_evasion_still_denied()]] - `uses` [INFERRED]
- [[test_invalid_default_action_falls_back_to_deny()]] - `uses` [INFERRED]
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - `uses` [INFERRED]
- [[test_mcp_policy.py]] - `imports` [EXTRACTED]
- [[test_mcp_policy_default_failclosed.py]] - `imports` [EXTRACTED]
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - `uses` [INFERRED]
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/MCPPolicyEngine
