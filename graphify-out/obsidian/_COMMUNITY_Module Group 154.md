---
type: community
cohesion: 0.08
members: 31
---

# Module Group 154

**Cohesion:** 0.08 - loosely connected
**Members:** 31 nodes

## Members
- [[.__ge__()]] - code - gateway/proxy/mcp_config.py
- [[.__gt__()]] - code - gateway/proxy/mcp_config.py
- [[.__le__()]] - code - gateway/proxy/mcp_config.py
- [[.__lt__()]] - code - gateway/proxy/mcp_config.py
- [[.infer_permission_level()]] - code - gateway/proxy/mcp_permissions.py
- [[.level_value()]] - code - gateway/proxy/mcp_config.py
- [[.record_private_data_redaction()]] - code - gateway/proxy/mcp_permissions.py
- [[.test_clean_params_no_findings()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_deeply_nested_pii()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_empty_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_fake_system_prompt_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_identity_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_list_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_low_confidence_not_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_nested_injection_caught()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_no_pii_scan()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_none_values_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_normal_text_not_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_prompt_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_special_token_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_result_none_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_result_string_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[Audit signal when admin-private data is redacted from tool results.]] - rationale - gateway/proxy/mcp_permissions.py
- [[Infer the permission level needed for a tool based on its name.          Checks]] - rationale - gateway/proxy/mcp_permissions.py
- [[MCPServerConfig_1]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel_1]] - code - gateway/proxy/mcp_permissions.py
- [[PermissionLevel]] - code - gateway/proxy/mcp_config.py
- [[PrivateRedactionEvent]] - code - gateway/proxy/mcp_permissions.py
- [[Record admin-private data redaction event for compliance audit.]] - rationale - gateway/proxy/mcp_permissions.py
- [[TestInjectionDetection]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInspectorEdgeCases]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_154
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_MCP Config & Proxy]]
- 16 edges to [[_COMMUNITY_MCP Inspector & Audit]]
- 16 edges to [[_COMMUNITY_Module Group 78]]
- 15 edges to [[_COMMUNITY_MCP Permissions Manager]]
- 5 edges to [[_COMMUNITY_Module Group 124]]
- 4 edges to [[_COMMUNITY_Module Group 266]]
- 3 edges to [[_COMMUNITY_Module Group 139]]
- 3 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 1 edge to [[_COMMUNITY_Module Group 387]]
- 1 edge to [[_COMMUNITY_Module Group 442]]
- 1 edge to [[_COMMUNITY_Module Group 468]]

## Top bridge nodes
- [[PermissionLevel]] - degree 70, connects to 11 communities
- [[TestInjectionDetection]] - degree 22, connects to 6 communities
- [[TestInspectorEdgeCases]] - degree 21, connects to 6 communities
- [[PrivateRedactionEvent]] - degree 7, connects to 3 communities
- [[MCPServerConfig_1]] - degree 5, connects to 2 communities
