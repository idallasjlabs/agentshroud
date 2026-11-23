---
type: community
members: 81
---

# test_mcp_proxy.py

**Members:** 81 nodes

## Members
- [[dot-__init__()_87]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-test_clean_params_no_findings()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_detected()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_deeply_nested_pii()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_empty_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_fake_system_prompt_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_heavy_url_encoding_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_high()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_none()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_identity_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_inspection_result_threat_level()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_large_base64_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_list_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_low_confidence_not_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_nested_injection_caught()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_network_request_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_no_pii_scan()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_none_values_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_normal_text_not_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_prompt_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_blocked_strict_with_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_not_blocked_default()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_shell_command_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_small_base64_ok()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_special_token_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tool_result_none_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tool_result_string_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[AgentShroud Proxy — security pipeline for all OpenClaw traffic.]] - rationale - gateway/proxy/__init__.py
- [[Any_31]] - code
- [[Comprehensive tests for MCP Proxy Layer.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Enum_25]] - code
- [[FindingType]] - code - gateway/proxy/mcp_inspector.py
- [[In strict mode, sensitive ops with injection ARE blocked.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCP Inspector — tool call inspection for injection, PII, and sensitive ops.…]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPInspector]] - code - gateway/proxy/mcp_inspector.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Sensitive ops are flagged but not blocked in default mode.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[TestInjectionDetection]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInspectorEdgeCases]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPIIDetection_1]] - code - gateway/tests/test_mcp_proxy.py
- [[TestSensitiveOps]] - code - gateway/tests/test_mcp_proxy.py
- [[TestSuspiciousEncoding]] - code - gateway/tests/test_mcp_proxy.py
- [[TestThreatLevelCalc]] - code - gateway/tests/test_mcp_proxy.py
- [[Threat level classification.]] - rationale - gateway/proxy/mcp_inspector.py
- [[ThreatLevel_1]] - code - gateway/proxy/mcp_inspector.py
- [[Type of security finding.]] - rationale - gateway/proxy/mcp_inspector.py
- [[audit()]] - code - gateway/tests/test_mcp_proxy.py
- [[config()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[fixture_52]] - code
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[mcp_inspector.py_2]] - code - gateway/proxy/mcp_inspector.py
- [[passthrough_proxy()]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[proxy__init__.py]] - code - gateway/proxy/__init__.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[test_mcp_proxy.py]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_mcp_proxypy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_MCPToolCall]]
- 12 edges to [[_COMMUNITY_PermissionLevel]]
- 11 edges to [[_COMMUNITY_MCPProxy]]
- 8 edges to [[_COMMUNITY_MCPAuditTrail]]
- 6 edges to [[_COMMUNITY_MCPPermissionManager]]
- 6 edges to [[_COMMUNITY_mcp_proxy.py]]
- 3 edges to [[_COMMUNITY_MCPServerConfig]]
- 3 edges to [[_COMMUNITY_test_mcp_proxy_coverage.py]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_TestAuditQueries]]

## Top bridge nodes
- [[test_mcp_proxy.py]] - degree 47, connects to 9 communities
- [[proxy__init__.py]] - degree 24, connects to 7 communities
- [[MCPInspector]] - degree 22, connects to 4 communities
- [[config()_1]] - degree 7, connects to 3 communities
- [[proxy()_1]] - degree 6, connects to 3 communities
