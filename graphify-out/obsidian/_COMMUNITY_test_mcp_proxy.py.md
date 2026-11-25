---
type: community
members: 107
---

# test_mcp_proxy.py

**Members:** 107 nodes

## Members
- [[dot-__init__()_51]] - code - gateway/proxy/mcp_inspector.py
- [[dot-__init__()_52]] - code - gateway/proxy/mcp_permissions.py
- [[dot-__init__()_53]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_load_privacy_policy()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_recompile_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-from_dict()_6]] - code - gateway/proxy/mcp_config.py
- [[dot-get_privacy_policy_status()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_access_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_data_patterns()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_events()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-get_private_redaction_summary()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-set_event_bus()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-set_trust_level()]] - code - gateway/proxy/mcp_permissions.py
- [[dot-shutdown()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_disabled_server_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_egress_denied_blocks_url_tool_call()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_basic()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_defaults()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_from_dict_http_transport()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_heavy_url_encoding_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_high()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_none()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_inspection_result_threat_level()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_large_base64_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_passthrough_process_tool_result()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_small_base64_ok()]] - code - gateway/tests/test_mcp_proxy.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[AgentShroud Proxy — security pipeline for all OpenClaw traffic.]] - rationale - gateway/proxy/__init__.py
- [[Aggregate recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Aggregate recent private-tool violations for SOC reporting.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Any_21]] - code
- [[Any_22]] - code
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Clean shutdown — close all connections.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Compile private data patterns once for efficient repeated use.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Comprehensive tests for MCP Proxy Layer.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Configuration for a specific MCP tool.]] - rationale - gateway/proxy/mcp_config.py
- [[Coverage tests for gatewayproxymcp_proxy.py. Targets the branches not…]] - rationale - gateway/tests/test_mcp_proxy_coverage.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Enum_14]] - code
- [[Enum_15]] - code
- [[FindingType]] - code - gateway/proxy/mcp_inspector.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Load optional admin-private tool patterns from policy file.]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCP Inspector — tool call inspection for injection, PII, and sensitive ops.…]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPInspector]] - code - gateway/proxy/mcp_inspector.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_permissions.py
- [[MCPProxy]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPToolConfig]] - code - gateway/proxy/mcp_config.py
- [[MCPTransport]] - code - gateway/proxy/mcp_config.py
- [[Main MCP proxy that intercepts tool calls and routes through security.…]] - rationale - gateway/proxy/mcp_proxy.py
- [[Manages permissions for MCP tool calls. Default-allow philosophy tools work…]] - rationale - gateway/proxy/mcp_permissions.py
- [[Parse config from a dictionary (e.g. loaded from YAML).]] - rationale - gateway/proxy/mcp_config.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Return configured admin-private data redaction patterns.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return privacy policy file load status for dashboardaudit APIs.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent blocked private-tool attempts for auditing.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return recent private-data redaction events.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Set trust level for an agent.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestAllowDenyList]] - code - gateway/tests/test_mcp_proxy.py
- [[TestConfigParsing]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPassthrough]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestSuspiciousEncoding]] - code - gateway/tests/test_mcp_proxy.py
- [[TestThreatLevelCalc]] - code - gateway/tests/test_mcp_proxy.py
- [[Threat level classification.]] - rationale - gateway/proxy/mcp_inspector.py
- [[ThreatLevel]] - code - gateway/proxy/mcp_inspector.py
- [[Top-level MCP proxy configuration.]] - rationale - gateway/proxy/mcp_config.py
- [[Type of security finding.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Wire optional event bus for privacysecurity telemetry.]] - rationale - gateway/proxy/mcp_proxy.py
- [[audit()]] - code - gateway/tests/test_mcp_proxy.py
- [[check_async()_31]] - code - gateway/tests/test_mcp_proxy.py
- [[config()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[fixture_46]] - code
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[make_config()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[mcp_audit.py_2]] - code - gateway/proxy/mcp_audit.py
- [[mcp_config.py_2]] - code - gateway/proxy/mcp_config.py
- [[mcp_inspector.py_2]] - code - gateway/proxy/mcp_inspector.py
- [[mcp_permissions.py_2]] - code - gateway/proxy/mcp_permissions.py
- [[mcp_proxy.py_2]] - code - gateway/proxy/mcp_proxy.py
- [[passthrough_proxy()]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy()]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy__init__.py]] - code - gateway/proxy/__init__.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[test_mcp_proxy.py]] - code - gateway/tests/test_mcp_proxy.py
- [[test_mcp_proxy_coverage.py]] - code - gateway/tests/test_mcp_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_mcp_proxypy
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_MCPToolCall]]
- 28 edges to [[_COMMUNITY_MCPServerConfig]]
- 19 edges to [[_COMMUNITY_PermissionLevel]]
- 16 edges to [[_COMMUNITY_make_proxy]]
- 13 edges to [[_COMMUNITY_MCPAuditTrail]]
- 12 edges to [[_COMMUNITY_PermissionCheck]]
- 8 edges to [[_COMMUNITY_ProxyResult]]
- 6 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 4 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 3 edges to [[_COMMUNITY_TestToolPermission]]
- 3 edges to [[_COMMUNITY_TestPIIDetection]]
- 3 edges to [[_COMMUNITY_lifespan]]
- 3 edges to [[_COMMUNITY_TestInjectionDetection]]
- 3 edges to [[_COMMUNITY_dot-_extract_egress_targets]]
- 2 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 2 edges to [[_COMMUNITY_TestSensitiveOps]]
- 2 edges to [[_COMMUNITY_TestMCPProxyIntegration]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_TestAuditQueries]]

## Top bridge nodes
- [[MCPProxy]] - degree 44, connects to 12 communities
- [[test_mcp_proxy.py]] - degree 47, connects to 10 communities
- [[mcp_proxy.py_2]] - degree 30, connects to 8 communities
- [[MCPPermissionManager]] - degree 41, connects to 7 communities
- [[test_mcp_proxy_coverage.py]] - degree 38, connects to 6 communities
