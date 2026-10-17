---
type: community
members: 39
---

# MCPPolicyEngine (2)

**Members:** 39 nodes

## Members
- [[dot-__init__()_74]] - code - gateway/security/mcp_policy.py
- [[dot-from_dict()_1]] - code - gateway/security/mcp_policy.py
- [[dot-test_configured_servers_are_allowlisted_by_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_engine_allows_known_server_under_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_engine_denies_unknown_server_under_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_engine_requires_approval_for_destructive_tool_on_known_server()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_explicit_policy_section_is_not_overridden()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_mcp_proxy_data_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_mcp_proxy_data_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_missing_section_yields_deny_by_default_policy()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_no_mcp_section_still_deny_by_default()]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[dot-test_proxy_allowed_domains_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_proxy_allowed_domains_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[A config with no mcp_proxy AND no mcp_policy still yields a fail-closed]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[A knownallowlisted server's non-high-risk tool is still ALLOWED — no breakage.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[A stock config (no mcp_policy) must produce a non-empty, deny-by-default policy]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[An operator-authored mcp_policy section must be honoured verbatim.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Declarative MCP security policy.      Loaded from the ``mcp_policy`` section of]] - rationale - gateway/security/mcp_policy.py
- [[Fail-closed intent even on a known server, an obviously destructive         too]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Knownconfigured MCP servers must be carried into the default allowlist]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Load and validate configuration from agentshroud.yaml      Search order     1.]] - rationale - gateway/ingest_api/config.py
- [[MCPPolicyAction]] - code - gateway/security/mcp_policy.py
- [[MCPPolicyConfig]] - code - gateway/security/mcp_policy.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - rationale - gateway/security/mcp_policy.py
- [[Path_16]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[Resolve the Dockerfile for the default bot from gateway config.]] - rationale - gateway/web/api.py
- [[TestDefaultMcpPolicyIsFailClosed]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[TestDefaultPolicyNoMcpServers]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[The synthesised default, fed to the engine, DENIES an unknown server.]] - rationale - gateway/tests/test_mcp_policy_default_failclosed.py
- [[_get_default_bot_dockerfile()]] - code - gateway/web/api.py
- [[_write()_1]] - code - gateway/tests/test_mcp_policy_default_failclosed.py
- [[load_config()]] - code - gateway/ingest_api/config.py
- [[mcp_policy.py]] - code - gateway/security/mcp_policy.py
- [[mcp_proxy_data is an empty dict when section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[mcp_proxy_data is populated from the mcp_proxy YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is empty list when proxy section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is populated from the proxy.allowed_domains YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[test_enforce_real_queue_high_risk_not_downgraded_to_allow (regression guard)]] - code - gateway/tests/test_mcp_policy.py
- [[test_mcp_policy_default_failclosed.py]] - code - gateway/tests/test_mcp_policy_default_failclosed.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPolicyEngine_2
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 9 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 7 edges to [[_COMMUNITY_api.py]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 4 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 3 edges to [[_COMMUNITY_create_auth_dependency]]
- 3 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_ServiceManager]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_ModuleStatsCollector]]
- 1 edge to [[_COMMUNITY_RBACConfig (2)]]
- 1 edge to [[_COMMUNITY__build_image_targets]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine (3)]]
- 1 edge to [[_COMMUNITY_Path (4)]]

## Top bridge nodes
- [[load_config()]] - degree 51, connects to 15 communities
- [[MCPPolicyAction]] - degree 15, connects to 5 communities
- [[mcp_policy.py]] - degree 12, connects to 5 communities
- [[MCPPolicyConfig]] - degree 17, connects to 4 communities
- [[test_mcp_policy_default_failclosed.py]] - degree 9, connects to 2 communities
