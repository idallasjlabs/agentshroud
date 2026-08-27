---
type: community
members: 111
---

# Community 34

**Members:** 111 nodes

## Members
- [[.__init__()_94]] - code - gateway/security/mcp_policy.py
- [[.__init__()_172]] - code - gateway/tests/test_mcp_policy.py
- [[.__post_init__()_5]] - code - gateway/security/mcp_policy.py
- [[._decide()_1]] - code - gateway/security/mcp_policy.py
- [[._tier_for()_1]] - code - gateway/security/mcp_policy.py
- [[.allowed()_1]] - code - gateway/security/mcp_policy.py
- [[.enforce()_1]] - code - gateway/security/mcp_policy.py
- [[.evaluate()_1]] - code - gateway/security/mcp_policy.py
- [[.from_dict()_7]] - code - gateway/security/mcp_policy.py
- [[.submit_tool_request()_3]] - code - gateway/tests/test_mcp_policy.py
- [[.test_configured_servers_are_allowlisted_by_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[.test_engine_allows_known_server_under_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[.test_engine_denies_unknown_server_under_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[.test_engine_requires_approval_for_destructive_tool_on_known_server()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[.test_explicit_policy_section_is_not_overridden()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[.test_mcp_proxy_data_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_mcp_proxy_data_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_missing_section_yields_deny_by_default_policy()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[.test_no_mcp_section_still_deny_by_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[.test_proxy_allowed_domains_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_proxy_allowed_domains_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.wait_for_decision()_3]] - code - gateway/tests/test_mcp_policy.py
- [[A REAL EnhancedApprovalQueue + default ToolRiskConfig must NOT let the     engin]] - rationale - gateway/tests/test_mcp_policy.py
- [[A config with no mcp_proxy AND no mcp_policy still yields a fail-closed]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[A destructive tool the operator forgot to classify is still caught as     high-r]] - rationale - gateway/tests/test_mcp_policy.py
- [[A fullwidthhomoglyph tool name must not evade the denylistkeyword     heuristi]] - rationale - gateway/tests/test_mcp_policy.py
- [[A knownallowlisted server's non-high-risk tool is still ALLOWED — no breakage.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[A malformed default_action in YAML must not fail open — it becomes deny.]] - rationale - gateway/tests/test_mcp_policy.py
- [[A policy-permitted call passes the policy gate (inspectionpermission     layers]] - rationale - gateway/tests/test_mcp_policy.py
- [[A representative policy two allowlisted servers, one denylisted server,     a p]] - rationale - gateway/tests/test_mcp_policy.py
- [[A risk tier declared with a bare tool name applies on any allowlisted     server]] - rationale - gateway/tests/test_mcp_policy.py
- [[A server both allowed and denied is denied (deny wins).]] - rationale - gateway/tests/test_mcp_policy.py
- [[A stock config (no mcp_policy) must produce a non-empty, deny-by-default policy]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[An empty config denies everything — never a blanket allow.]] - rationale - gateway/tests/test_mcp_policy.py
- [[An operator-authored mcp_policy section must be honoured verbatim.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Any_47]] - code - gateway/security/mcp_policy.py
- [[Decides allow  deny  require-approval for MCP tool calls.      Usage]] - rationale - gateway/security/mcp_policy.py
- [[Declarative MCP security policy.      Loaded from the ``mcp_policy`` section of]] - rationale - gateway/security/mcp_policy.py
- [[End-to-end the engine wired into MCPProxy with a REAL approval queue     must n]] - rationale - gateway/tests/test_mcp_policy.py
- [[Evaluate a single MCP tool call. Pure — no IO, no side effects         beyond b]] - rationale - gateway/security/mcp_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY.          For REQUIRE]] - rationale - gateway/security/mcp_policy.py
- [[Fail-closed intent even on a known server, an obviously destructive         too]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Fail-closed a high-risk tool with no approval queue wired is denied,     never]] - rationale - gateway/tests/test_mcp_policy.py
- [[Fail-closed if the queue returns requires_wait=False for a call the     engine]] - rationale - gateway/tests/test_mcp_policy.py
- [[Knownconfigured MCP servers must be carried into the default allowlist]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[LOW finding when owner_bypass is enabled but owner_user_id is left     blank, t]] - rationale - gateway/tests/test_mcp_policy.py
- [[Load and validate configuration from agentshroud.yaml      Search order     1.]] - rationale - gateway/ingest_api/config.py
- [[MCPPolicyAction]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyConfig]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyConfig_1]] - code - gateway/tests/test_mcp_policy.py
- [[MCPPolicyDecision]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyEngine]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyEngine_1]] - code - gateway/tests/test_mcp_policy.py
- [[Minimal stand-in for EnhancedApprovalQueue.      Records submissions and returns]] - rationale - gateway/tests/test_mcp_policy.py
- [[MonkeyPatch]] - code - gateway/tests/test_mcp_policy.py
- [[Normalize a servertool reference for robust, evasion-resistant matching.      A]] - rationale - gateway/security/mcp_policy.py
- [[Owner skips the approval gate for high-risk tools, but a denylisted     tool is]] - rationale - gateway/tests/test_mcp_policy.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML)._1]] - rationale - gateway/security/mcp_policy.py
- [[Path_32]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Resolve the risk tier for a tool.          Explicit classification (qualified be]] - rationale - gateway/security/mcp_policy.py
- [[TestDefaultMcpPolicyIsFailClosed]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[TestDefaultPolicyNoMcpServers]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[The engine wired into MCPProxy blocks a denied call before dispatch —     the fa]] - rationale - gateway/tests/test_mcp_policy.py
- [[The result of evaluating a single MCP tool call against the policy.]] - rationale - gateway/security/mcp_policy.py
- [[The synthesised default, fed to the engine, DENIES an unknown server.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[The three terminal policy outcomes for an MCP tool call.]] - rationale - gateway/security/mcp_policy.py
- [[True only for a terminal ALLOW.          REQUIRE_APPROVAL is not allowed on it]] - rationale - gateway/security/mcp_policy.py
- [[When an operator explicitly opts into default-allow, a non-allowlisted     serve]] - rationale - gateway/tests/test_mcp_policy.py
- [[_FakeApprovalQueue]] - code - gateway/tests/test_mcp_policy.py
- [[_base_config()_1]] - code - gateway/tests/test_mcp_policy.py
- [[_norm()_1]] - code - gateway/security/mcp_policy.py
- [[_write()_1]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[engine()_1]] - code - gateway/tests/test_mcp_policy.py
- [[evaluate() records the decision for the SOC module heat-map.]] - rationale - gateway/tests/test_mcp_policy.py
- [[load_config()]] - code - gateway/ingest_api/config.py
- [[mcp_policy.py]] - code - gateway/security/mcp_policy.py
- [[mcp_proxy_data is an empty dict when section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[mcp_proxy_data is populated from the mcp_proxy YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is empty list when proxy section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is populated from the proxy.allowed_domains YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
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
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow (regression guard)]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow()]] - code - gateway/tests/test_mcp_policy.py
- [[test_enforce_unicode_evasion_still_denied()]] - code - gateway/tests/test_mcp_policy.py
- [[test_high_risk_tool_requires_approval()]] - code - gateway/tests/test_mcp_policy.py
- [[test_invalid_default_action_falls_back_to_deny()]] - code - gateway/tests/test_mcp_policy.py
- [[test_keyword_heuristic_auto_classifies_unlisted_destructive_tool()]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_policy.py]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_policy_default_failclosed.py]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[test_mcp_proxy_allows_policy_permitted_call()]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_proxy_blocks_policy_denied_call()]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_proxy_real_queue_high_risk_never_executes_without_approval()]] - code - gateway/tests/test_mcp_policy.py
- [[test_owner_bypass_defaults_to_rbac_owner_identity()]] - code - gateway/tests/test_mcp_policy.py
- [[test_owner_bypasses_approval_but_not_hard_deny()]] - code - gateway/tests/test_mcp_policy.py
- [[test_server_and_tool_matching_is_case_insensitive()]] - code - gateway/tests/test_mcp_policy.py
- [[test_unknown_server_is_denied_by_default()]] - code - gateway/tests/test_mcp_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_34
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Community 24]]
- 16 edges to [[_COMMUNITY_Community 36]]
- 14 edges to [[_COMMUNITY_Community 15]]
- 9 edges to [[_COMMUNITY_Community 1325]]
- 9 edges to [[_COMMUNITY_Community 1]]
- 6 edges to [[_COMMUNITY_Community 6]]
- 6 edges to [[_COMMUNITY_Community 45]]
- 6 edges to [[_COMMUNITY_Community 283]]
- 5 edges to [[_COMMUNITY_Community 273]]
- 3 edges to [[_COMMUNITY_Community 78]]
- 3 edges to [[_COMMUNITY_Community 1001]]
- 2 edges to [[_COMMUNITY_Community 19]]
- 2 edges to [[_COMMUNITY_Community 27]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 12]]
- 1 edge to [[_COMMUNITY_Community 81]]
- 1 edge to [[_COMMUNITY_Community 779]]
- 1 edge to [[_COMMUNITY_Community 482]]
- 1 edge to [[_COMMUNITY_Community 31]]
- 1 edge to [[_COMMUNITY_Community 75]]
- 1 edge to [[_COMMUNITY_Community 69]]

## Top bridge nodes
- [[load_config()]] - degree 51, connects to 13 communities
- [[test_mcp_policy.py]] - degree 46, connects to 4 communities
- [[MCPPolicyEngine_1]] - degree 39, connects to 4 communities
- [[_FakeApprovalQueue]] - degree 20, connects to 4 communities
- [[MCPPolicyConfig_1]] - degree 14, connects to 4 communities