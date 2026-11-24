---
type: community
members: 107
---

# MCPPolicyEngine

**Members:** 107 nodes

## Members
- [[dot-__init__()_133]] - code - gateway/security/mcp_policy.py
- [[dot-__init__()_134]] - code - gateway/tests/test_mcp_policy.py
- [[dot-__post_init__()_6]] - code - gateway/security/mcp_policy.py
- [[dot-_decide()]] - code - gateway/security/mcp_policy.py
- [[dot-_tier_for()]] - code - gateway/security/mcp_policy.py
- [[dot-allowed()]] - code - gateway/security/mcp_policy.py
- [[dot-enforce()]] - code - gateway/security/mcp_policy.py
- [[dot-evaluate()]] - code - gateway/security/mcp_policy.py
- [[dot-from_dict()_7]] - code - gateway/security/mcp_policy.py
- [[dot-submit_tool_request()_3]] - code - gateway/tests/test_mcp_policy.py
- [[dot-test_configured_servers_are_allowlisted_by_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_engine_allows_known_server_under_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_engine_denies_unknown_server_under_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_engine_requires_approval_for_destructive_tool_on_known_server()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_explicit_policy_section_is_not_overridden()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_missing_section_yields_deny_by_default_policy()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_no_mcp_section_still_deny_by_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-wait_for_decision()_3]] - code - gateway/tests/test_mcp_policy.py
- [[A REAL EnhancedApprovalQueue + default ToolRiskConfig must NOT let the engine's…]] - rationale - gateway/tests/test_mcp_policy.py
- [[A config with no mcp_proxy AND no mcp_policy still yields a fail-closed default…]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[A destructive tool the operator forgot to classify is still caught as high-risk…]] - rationale - gateway/tests/test_mcp_policy.py
- [[A fullwidthhomoglyph tool name must not evade the denylistkeyword heuristic.…]] - rationale - gateway/tests/test_mcp_policy.py
- [[A knownallowlisted server's non-high-risk tool is still ALLOWED — no breakage.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[A malformed default_action in YAML must not fail open — it becomes deny.]] - rationale - gateway/tests/test_mcp_policy.py
- [[A representative policy two allowlisted servers, one denylisted server, a per-…]] - rationale - gateway/tests/test_mcp_policy.py
- [[A risk tier declared with a bare tool name applies on any allowlisted server…]] - rationale - gateway/tests/test_mcp_policy.py
- [[A server both allowed and denied is denied (deny wins).]] - rationale - gateway/tests/test_mcp_policy.py
- [[A stock config (no mcp_policy) must produce a non-empty, deny-by-default…]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[An empty config denies everything — never a blanket allow.]] - rationale - gateway/tests/test_mcp_policy.py
- [[An operator-authored mcp_policy section must be honoured verbatim.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Any_49]] - code
- [[Decides allow  deny  require-approval for MCP tool calls. Usage engine =…]] - rationale - gateway/security/mcp_policy.py
- [[Declarative MCP security policy. Loaded from the ``mcp_policy`` section of…]] - rationale - gateway/security/mcp_policy.py
- [[End-to-end the engine wired into MCPProxy with a REAL approval queue must…]] - rationale - gateway/tests/test_mcp_policy.py
- [[Enum_33]] - code
- [[Evaluate a single MCP tool call. Pure — no IO, no side effects beyond best-…]] - rationale - gateway/security/mcp_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY. For…]] - rationale - gateway/security/mcp_policy.py
- [[Fail-closed intent even on a known server, an obviously destructive tool must…]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Fail-closed a high-risk tool with no approval queue wired is denied, never…]] - rationale - gateway/tests/test_mcp_policy.py
- [[Fail-closed if the queue returns requires_wait=False for a call the engine…]] - rationale - gateway/tests/test_mcp_policy.py
- [[Knownconfigured MCP servers must be carried into the default allowlist so…]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[LOW finding when owner_bypass is enabled but owner_user_id is left blank, the…]] - rationale - gateway/tests/test_mcp_policy.py
- [[MCP (Model Context Protocol) security policy engine (SCRUM-84). The enforcement…]] - rationale - gateway/security/mcp_policy.py
- [[MCPPolicyAction]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyConfig]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyDecision]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyEngine]] - code - gateway/security/mcp_policy.py
- [[Minimal stand-in for EnhancedApprovalQueue. Records submissions and returns a…]] - rationale - gateway/tests/test_mcp_policy.py
- [[MonkeyPatch]] - code
- [[Normalize a servertool reference for robust, evasion-resistant matching.…]] - rationale - gateway/security/mcp_policy.py
- [[Owner skips the approval gate for high-risk tools, but a denylisted tool is…]] - rationale - gateway/tests/test_mcp_policy.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - rationale - gateway/security/mcp_policy.py
- [[Path_41]] - code
- [[Resolve the risk tier for a tool. Explicit classification (qualified beats…]] - rationale - gateway/security/mcp_policy.py
- [[TDD — WS-E finding RT-11 (HIGH, deploy) MCP policy engine ships DORMANT.…]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[TestDefaultMcpPolicyIsFailClosed]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[TestDefaultPolicyNoMcpServers]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Tests for the MCP (Model Context Protocol) security policy engine (SCRUM-84).…]] - rationale - gateway/tests/test_mcp_policy.py
- [[The engine wired into MCPProxy blocks a denied call before dispatch — the fake…]] - rationale - gateway/tests/test_mcp_policy.py
- [[The result of evaluating a single MCP tool call against the policy.]] - rationale - gateway/security/mcp_policy.py
- [[The synthesised default, fed to the engine, DENIES an unknown server.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[The three terminal policy outcomes for an MCP tool call.]] - rationale - gateway/security/mcp_policy.py
- [[True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on its own —…]] - rationale - gateway/security/mcp_policy.py
- [[When an operator explicitly opts into default-allow, a non-allowlisted server…]] - rationale - gateway/tests/test_mcp_policy.py
- [[_FakeApprovalQueue]] - code - gateway/tests/test_mcp_policy.py
- [[_base_config()]] - code - gateway/tests/test_mcp_policy.py
- [[_boom()_21]] - code - gateway/tests/test_mcp_policy.py
- [[_boom()_22]] - code - gateway/tests/test_mcp_policy.py
- [[_fake_record()]] - code - gateway/tests/test_mcp_policy.py
- [[_norm()]] - code - gateway/security/mcp_policy.py
- [[_run()_8]] - code - gateway/tests/test_mcp_policy.py
- [[_run()_9]] - code - gateway/tests/test_mcp_policy.py
- [[_write()_1]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[engine()]] - code - gateway/tests/test_mcp_policy.py
- [[evaluate() records the decision for the SOC module heat-map.]] - rationale - gateway/tests/test_mcp_policy.py
- [[fixture_92]] - code
- [[mcp_policy.py]] - code - gateway/security/mcp_policy.py
- [[str_18]] - code
- [[test_allowlisted_server_safe_tool_is_allowed()]] - code - gateway/tests/test_mcp_policy.py
- [[test_bare_tool_name_risk_tier_applies_across_servers()]] - code - gateway/tests/test_mcp_policy.py
- [[test_critical_tool_requires_approval()]] - code - gateway/tests/test_mcp_policy.py
- [[test_decision_records_soc_heatmap()]] - code - gateway/tests/test_mcp_policy.py
- [[test_default_allow_opt_in_permits_non_allowlisted_safe_tool()]] - code - gateway/tests/test_mcp_policy.py
- [[test_default_deny_posture_when_no_config()]] - code - gateway/tests/test_mcp_policy.py
- [[test_denied_tool_can_be_specified_bare_or_qualified()]] - code - gateway/tests/test_mcp_policy.py
- [[test_denylist_wins_over_allowlist()]] - code - gateway/tests/test_mcp_policy.py
- [[test_denylisted_server_is_denied_even_if_tool_safe()]] - code - gateway/tests/test_mcp_policy.py
- [[test_denylisted_tool_is_denied()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_allows_allowlisted_safe_tool()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_blocks_unknown_server()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_high_risk_denied_on_rejection()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_high_risk_enqueues_and_allows_on_approval()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_high_risk_queue_no_wait_denies_closed()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_high_risk_without_queue_denies_closed()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_unicode_evasion_still_denied()]] - code - gateway/tests/test_mcp_policy.py
- [[test_high_risk_tool_requires_approval()]] - code - gateway/tests/test_mcp_policy.py
- [[test_invalid_default_action_falls_back_to_deny()]] - code - gateway/tests/test_mcp_policy.py
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_policy.py]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_policy_default_failclosed.py]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[test_mcp_proxy_blocks_policy_denied_call()]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_proxy_real_queue_high_risk_never_executes_without_approval()]] - code - gateway/tests/test_mcp_policy.py
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - code - gateway/tests/test_mcp_policy.py
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - code - gateway/tests/test_mcp_policy.py
- [[test_server_and_tool_matching_is_case_insensitive()]] - code - gateway/tests/test_mcp_policy.py
- [[test_unknown_server_is_denied_by_default()]] - code - gateway/tests/test_mcp_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPolicyEngine
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_lifespan]]
- 8 edges to [[_COMMUNITY_MCPToolCall]]
- 7 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_test_module_stats.py]]

## Top bridge nodes
- [[test_mcp_policy.py]] - degree 46, connects to 4 communities
- [[MCPPolicyEngine]] - degree 46, connects to 3 communities
- [[MCPPolicyConfig]] - degree 23, connects to 3 communities
- [[_run()_9]] - degree 7, connects to 3 communities
- [[mcp_policy.py]] - degree 11, connects to 2 communities
