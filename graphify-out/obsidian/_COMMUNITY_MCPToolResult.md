---
type: community
cohesion: 0.11
members: 27
---

# MCPToolResult

**Cohesion:** 0.11 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-__post_init__()_8]] - code - gateway/proxy/mcp_proxy.py
- [[dot-test_admin_private_data_not_redacted_for_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_admin_private_data_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_params_no_findings()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_result_passes()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_error_result_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_fake_system_prompt_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_gateway_contributor_paths_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_identity_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_low_confidence_not_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_memory_markers_redacted_for_non_owner()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_nested_injection_caught()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_normal_text_not_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_redacted_in_result()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_private_redaction_emits_privacy_event()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_prompt_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_result_audit_logged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_result_processing_time()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_special_token_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tool_call_generates_id_and_timestamp()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-test_tool_result_timestamp_default()]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolCall_1]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[MCPToolResult]] - code - gateway/proxy/mcp_proxy.py
- [[Represents an MCP tool result.]] - rationale - gateway/proxy/mcp_proxy.py
- [[TestDataclasses]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[TestInjectionDetection]] - code - gateway/tests/test_mcp_proxy.py
- [[TestProxyResultProcessing]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPToolResult
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_MCPToolCall]]
- 25 edges to [[_COMMUNITY_StdioConnection]]
- 23 edges to [[_COMMUNITY_MCPPermissionManager]]
- 8 edges to [[_COMMUNITY_PermissionLevel]]
- 6 edges to [[_COMMUNITY_MCPAuditTrail]]
- 6 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 3 edges to [[_COMMUNITY_FakeProcess]]
- 2 edges to [[_COMMUNITY_dot-process_tool_call]]
- 1 edge to [[_COMMUNITY_TestInspectorEdgeCases]]
- 1 edge to [[_COMMUNITY_TestPIIDetection]]
- 1 edge to [[_COMMUNITY_TestExtractEgressTargets]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]

## Top bridge nodes
- [[MCPToolResult]] - degree 77, connects to 11 communities
- [[TestDataclasses]] - degree 17, connects to 5 communities
- [[MCPToolCall_1]] - degree 16, connects to 5 communities
- [[TestProxyResultProcessing]] - degree 23, connects to 4 communities
- [[TestInjectionDetection]] - degree 22, connects to 4 communities
