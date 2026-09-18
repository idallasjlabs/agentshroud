---
type: community
cohesion: 0.06
members: 79
---

# MCPToolCall

**Cohesion:** 0.06 - loosely connected
**Members:** 79 nodes

## Members
- [[.__post_init__()_8]] - code - gateway/proxy/mcp_proxy.py
- [[.mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.set_event_bus()_1]] - code - gateway/proxy/mcp_proxy.py
- [[.test_audit_entry_created()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_chain_includes_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_chain_valid_after_calls()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_clean_call_allowed()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_allows_non_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_egress_denied_blocks_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_elevated_agent_can_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_execute_none_content_result_does_not_unbind()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_execute_with_content_still_inspects()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_from_dict_basic()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_from_dict_defaults()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_from_dict_http_transport()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_gateway_data_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_heavy_url_encoding_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_highest_threat_high()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_highest_threat_none()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_injection_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_inspection_result_threat_level()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_large_base64_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_mixed_allowed_blocked_chain()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_network_request_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_owner_bypass()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_passthrough_allows_everything()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_passthrough_still_audits()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_pii_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_private_tool_violation_emits_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_processing_time_recorded()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_rate_limit_enforced()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_read_only_agent_can_read()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_read_only_agent_denied_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_sensitive_blocked_strict_with_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_sensitive_not_blocked_default()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_session_store_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_shell_command_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_small_base64_ok()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_stats_blocked_counted()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_stats_tracking()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_unknown_server_default_allow()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_workspace_contributor_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[FindingType]] - code - gateway/proxy/mcp_inspector.py
- [[In strict mode, sensitive ops with injection ARE blocked.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[MCPProxy_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPToolCall_1]] - code - gateway/proxy/mcp_proxy.py
- [[Main MCP proxy that intercepts tool calls and routes through security.      Tran]] - rationale - gateway/proxy/mcp_proxy.py
- [[Mix of allowed, blocked, and result entries all in one chain.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Regression result_inspection was possibly-unbound when the executed tool     re]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Represents an MCP tool_use request.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Sensitive ops are flagged but not blocked in default mode.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Test owner bypass for high-tier tools.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools are allowed without approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestAllowDenyList]] - code - gateway/tests/test_mcp_proxy.py
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
- [[passthrough_proxy()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy()_3]] - code - gateway/tests/test_mcp_proxy.py
- [[test_mcp_proxy.py]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPToolCall
SORT file.name ASC
```

## Connections to other communities
- 75 edges to [[_COMMUNITY_MCPServerConfig]]
- 34 edges to [[_COMMUNITY_PermissionLevel]]
- 31 edges to [[_COMMUNITY_StdioConnection]]
- 28 edges to [[_COMMUNITY_MCPInspector]]
- 27 edges to [[_COMMUNITY_MCPAuditTrail]]
- 27 edges to [[_COMMUNITY_MCPToolResult]]
- 21 edges to [[_COMMUNITY_MCPPermissionManager]]
- 16 edges to [[_COMMUNITY_load_config()]]
- 15 edges to [[_COMMUNITY_ApprovalRequest]]
- 10 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 9 edges to [[_COMMUNITY_.process_tool_call()]]
- 6 edges to [[_COMMUNITY_FakeProcess]]
- 5 edges to [[_COMMUNITY_TestAuditTrail]]
- 5 edges to [[_COMMUNITY_TestInjectionDetection]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[MCPProxy_1]] - degree 89, connects to 17 communities
- [[MCPToolCall_1]] - degree 102, connects to 15 communities
- [[test_mcp_proxy.py]] - degree 46, connects to 9 communities
- [[ThreatLevel_2]] - degree 28, connects to 8 communities
- [[FindingType]] - degree 27, connects to 8 communities