---
source_file: "gateway/security/mcp_policy.py"
type: "code"
community: "MCPPolicyEngine"
location: "L200"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/MCPPolicyEngine
---

# .from_dict()

## Connections
- [[dot-test_engine_allows_known_server_under_default()]] - `calls` [EXTRACTED]
- [[dot-test_engine_denies_unknown_server_under_default()]] - `calls` [EXTRACTED]
- [[dot-test_engine_requires_approval_for_destructive_tool_on_known_server()]] - `calls` [EXTRACTED]
- [[dot-test_no_mcp_section_still_deny_by_default()]] - `calls` [EXTRACTED]
- [[Any_49]] - `references` [EXTRACTED]
- [[MCPPolicyAction]] - `calls` [EXTRACTED]
- [[MCPPolicyConfig]] - `method` [EXTRACTED]
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - `rationale_for` [EXTRACTED]
- [[_base_config()]] - `calls` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[test_bare_tool_name_risk_tier_applies_across_servers()]] - `calls` [EXTRACTED]
- [[test_default_allow_opt_in_permits_non_allowlisted_safe_tool()]] - `calls` [EXTRACTED]
- [[test_denied_tool_can_be_specified_bare_or_qualified()]] - `calls` [EXTRACTED]
- [[test_denylist_wins_over_allowlist()]] - `calls` [EXTRACTED]
- [[test_enforce_unicode_evasion_still_denied()]] - `calls` [EXTRACTED]
- [[test_invalid_default_action_falls_back_to_deny()]] - `calls` [EXTRACTED]
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - `calls` [EXTRACTED]
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - `calls` [EXTRACTED]
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/MCPPolicyEngine
