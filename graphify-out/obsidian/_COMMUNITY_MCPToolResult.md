---
type: community
members: 9
---

# MCPToolResult

**Members:** 9 nodes

## Members
- [[dot-test_clean_params_no_findings()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_fake_system_prompt_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_identity_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_low_confidence_not_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_nested_injection_caught()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_normal_text_not_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_prompt_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_special_token_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInjectionDetection]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPToolResult
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_MCPPermissionManager]]
- 3 edges to [[_COMMUNITY_StdioConnection]]
- 2 edges to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (2)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager (3)]]

## Top bridge nodes
- [[TestInjectionDetection]] - degree 22, connects to 7 communities
