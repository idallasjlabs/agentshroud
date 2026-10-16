---
type: community
cohesion: 0.05
members: 84
---

# MCPPermissionManager

**Cohesion:** 0.05 - loosely connected
**Members:** 84 nodes

## Members
- [[dot-__post_init__()_8]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_emit_privacy_event()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_extract_egress_targets()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_sanitize_admin_private_data()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-check_approval_required()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-process_tool_result()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-set_event_bus()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_audit_entry_created()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_chain_includes_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_chain_valid_after_calls()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_call_allowed()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_egress_allows_non_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_egress_denied_blocks_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_elevated_agent_can_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_execute_none_content_result_does_not_unbind()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_execute_with_content_still_inspects()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_basic()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_defaults()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_http_transport()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_gateway_data_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_heavy_url_encoding_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_high()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_none()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_injection_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_inspection_result_threat_level()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_large_base64_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_mixed_allowed_blocked_chain()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_passthrough_allows_everything()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_passthrough_still_audits()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_private_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_private_tool_violation_emits_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_processing_time_recorded()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_rate_limit_enforced()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_read_only_agent_can_read()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_read_only_agent_denied_execute()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_result_processing_time()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_session_store_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_small_base64_ok()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_stats_blocked_counted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_stats_tracking()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_unknown_server_default_allow()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_workspace_contributor_parameter_violation_blocks_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Best-effort privacy event emission.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Check if a tool call requires approval and wait for it if needed.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Extract outbound URL-like targets from nested MCP tool parameters.]] - rationale - gateway/proxy/mcp_proxy.py
- [[FindingType]] - code - gateway/proxy/mcp_inspector.py
- [[MCPProxy_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPToolCall_1]] - code - gateway/proxy/mcp_proxy.py
- [[Main MCP proxy that intercepts tool calls and routes through security.      Tran]] - rationale - gateway/proxy/mcp_proxy.py
- [[Mix of allowed, blocked, and result entries all in one chain.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Process a tool result coming back (for cases where execution happens externally)]] - rationale - gateway/proxy/mcp_proxy.py
- [[Process an MCP tool call through the security pipeline.          Args]] - rationale - gateway/proxy/mcp_proxy.py
- [[Redact admin-private data from tool results for non-owner agents.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Regression result_inspection was possibly-unbound when the executed tool     re]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Represents an MCP tool_use request.]] - rationale - gateway/proxy/mcp_proxy.py
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
- [[TestSuspiciousEncoding]] - code - gateway/tests/test_mcp_proxy.py
- [[TestThreatLevelCalc]] - code - gateway/tests/test_mcp_proxy.py
- [[Threat level classification.]] - rationale - gateway/proxy/mcp_inspector.py
- [[ThreatLevel_2]] - code - gateway/proxy/mcp_inspector.py
- [[Type of security finding.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Wire optional event bus for privacysecurity telemetry.]] - rationale - gateway/proxy/mcp_proxy.py
- [[audit()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[passthrough_proxy()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy()_4]] - code - gateway/tests/test_mcp_proxy.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[test_mcp_proxy.py]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 49 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 48 edges to [[_COMMUNITY_MCPInspector]]
- 33 edges to [[_COMMUNITY_MCPPermissionManager_4]]
- 30 edges to [[_COMMUNITY_PermissionLevel]]
- 27 edges to [[_COMMUNITY_MCPAuditTrail]]
- 20 edges to [[_COMMUNITY_MCPPermissionManager_2]]
- 20 edges to [[_COMMUNITY_StdioConnection]]
- 18 edges to [[_COMMUNITY_StdioConnection_1]]
- 16 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 15 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 5 edges to [[_COMMUNITY_MCPToolResult]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager_5]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager_6]]
- 5 edges to [[_COMMUNITY_MCPPermissionManager_7]]
- 5 edges to [[_COMMUNITY_TestAuditTrail]]
- 2 edges to [[_COMMUNITY_Athena — Knowledge Distiller_4]]
- 2 edges to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]

## Top bridge nodes
- [[MCPProxy_1]] - degree 89, connects to 19 communities
- [[MCPToolCall_1]] - degree 100, connects to 15 communities
- [[test_mcp_proxy.py]] - degree 46, connects to 11 communities
- [[ThreatLevel_2]] - degree 28, connects to 10 communities
- [[FindingType]] - degree 27, connects to 9 communities
