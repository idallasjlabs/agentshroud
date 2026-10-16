---
type: community
cohesion: 0.05
members: 88
---

# MCPToolCall

**Cohesion:** 0.05 - loosely connected
**Members:** 88 nodes

## Members
- [[dot-__init__()_145]] - code - gateway/proxy/mcp_inspector.py
- [[dot-__post_init__()_6]] - code - gateway/proxy/mcp_proxy.py
- [[dot-set_event_bus()_2]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_audit_entry_created()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_blocked_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_chain_includes_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_chain_valid_after_calls()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_call_allowed()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_egress_allows_non_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_egress_denied_blocks_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_elevated_agent_can_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_execute_none_content_result_does_not_unbind()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_execute_with_content_still_inspects()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_failed_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_agent()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_server()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_filter_by_tool()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_basic()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_defaults()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_http_transport()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_gateway_data_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_generate_report()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_heavy_url_encoding_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_high()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_none()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_injection_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_inspection_result_threat_level()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_large_base64_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_mixed_allowed_blocked_chain()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_network_request_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_passthrough_allows_everything()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_passthrough_still_audits()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_private_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_private_tool_violation_emits_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_processing_time_recorded()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_rate_limit_enforced()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_read_only_agent_can_read()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_read_only_agent_denied_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_blocked_strict_with_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_not_blocked_default()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_session_store_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_shell_command_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_small_base64_ok()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_stats_blocked_counted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_stats_tracking()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_unknown_server_default_allow()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_workspace_contributor_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[FindingType]] - code - gateway/proxy/mcp_inspector.py
- [[In strict mode, sensitive ops with injection ARE blocked.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPInspector]] - code - gateway/proxy/mcp_inspector.py
- [[MCPProxy_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy.process_tool_call]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy.process_tool_result]] - code - gateway/proxy/mcp_proxy.py
- [[MCPToolCall]] - code - gateway/proxy/mcp_proxy.py
- [[Main MCP proxy that intercepts tool calls and routes through security.      Tran]] - rationale - gateway/proxy/mcp_proxy.py
- [[Mix of allowed, blocked, and result entries all in one chain.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Regression result_inspection was possibly-unbound when the executed tool     re]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Represents an MCP tool_use request.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Sensitive ops are flagged but not blocked in default mode.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[TestAllowDenyList]] - code - gateway/tests/test_mcp_proxy.py
- [[TestAuditQueries]] - code - gateway/tests/test_mcp_proxy.py
- [[TestChainIntegrityMultiple]] - code - gateway/tests/test_mcp_proxy.py
- [[TestConfigParsing]] - code - gateway/tests/test_mcp_proxy.py
- [[TestExecuteResultInspectionBinding]] - code - gateway/tests/test_mcp_proxy.py
- [[TestHashChainIntegration]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPassthroughMode_1]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPrivacyPolicyEvents]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProcessingTime]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyInterception]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyPermissions]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyRateLimiting]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyStats]] - code - gateway/tests/test_mcp_proxy.py
- [[TestSensitiveOps]] - code - gateway/tests/test_mcp_proxy.py
- [[TestSuspiciousEncoding]] - code - gateway/tests/test_mcp_proxy.py
- [[TestThreatLevelCalc]] - code - gateway/tests/test_mcp_proxy.py
- [[Threat level classification.]] - rationale - gateway/proxy/mcp_inspector.py
- [[ThreatLevel_2]] - code - gateway/proxy/mcp_inspector.py
- [[Type of security finding.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Wire optional event bus for privacysecurity telemetry.]] - rationale - gateway/proxy/mcp_proxy.py
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_inspector.py]] - code - gateway/proxy/mcp_inspector.py
- [[passthrough_proxy()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy()_3]] - code - gateway/tests/test_mcp_proxy.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[test_mcp_proxy.py]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPToolCall
SORT file.name ASC
```

## Connections to other communities
- 111 edges to [[_COMMUNITY_MCPPermissionManager]]
- 49 edges to [[_COMMUNITY_StdioConnection]]
- 38 edges to [[_COMMUNITY_MCPToolResult]]
- 34 edges to [[_COMMUNITY_PermissionLevel]]
- 31 edges to [[_COMMUNITY_MCPAuditTrail]]
- 16 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 16 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 9 edges to [[_COMMUNITY_FakeProcess]]
- 9 edges to [[_COMMUNITY_dot-process_tool_call]]
- 7 edges to [[_COMMUNITY_dot-inspect_tool_call]]
- 6 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 6 edges to [[_COMMUNITY_TestPIIDetection]]
- 6 edges to [[_COMMUNITY_TestAuditTrail]]
- 3 edges to [[_COMMUNITY_TestExtractEgressTargets]]
- 3 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_DataLedger]]

## Top bridge nodes
- [[MCPProxy_1]] - degree 89, connects to 15 communities
- [[MCPToolCall]] - degree 100, connects to 12 communities
- [[MCPInspector]] - degree 77, connects to 10 communities
- [[test_mcp_proxy.py]] - degree 46, connects to 7 communities
- [[ThreatLevel_2]] - degree 28, connects to 7 communities
