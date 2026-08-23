---
type: community
cohesion: 0.22
members: 9
---

# Mcp Proxy

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_clean_params_no_findings()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_fake_system_prompt_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_identity_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_low_confidence_not_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_nested_injection_caught()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_normal_text_not_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_prompt_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_special_token_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInjectionDetection]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Mcp_Proxy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Mcp Proxy]]
- 3 edges to [[_COMMUNITY_Mcp Permissions]]
- 1 edge to [[_COMMUNITY_Mcp Audit (proxy)]]
- 1 edge to [[_COMMUNITY_Mcp Permissions (proxy)]]
- 1 edge to [[_COMMUNITY_Mcp Proxy]]

## Top bridge nodes
- [[TestInjectionDetection]] - degree 22, connects to 5 communities