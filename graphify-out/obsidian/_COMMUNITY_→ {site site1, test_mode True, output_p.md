---
type: community
cohesion: 0.25
members: 8
---

# → {"site": "site1", "test_mode": True, "output_p

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_deeply_nested_pii()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_empty_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_list_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_no_pii_scan()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_none_values_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_result_none_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_tool_result_string_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInspectorEdgeCases]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_site_site1_test_mode_True_output_p
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 3 edges to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_brand-guidelines]]
- 1 edge to [[_COMMUNITY_TestParanoidConfig]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_AgentShroud v0.9.0 — Human Interface Testing Gui]]

## Top bridge nodes
- [[TestInspectorEdgeCases]] - degree 21, connects to 7 communities