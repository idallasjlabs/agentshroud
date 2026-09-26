---
type: community
cohesion: 0.20
members: 10
---

# switch_model.sh

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_critical_tool_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[.test_owner_bypass()]] - code - gateway/tests/test_enhanced_approval.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test MCP proxy integration with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test owner bypass for high-tier tools.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that critical tools are identified as requiring approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools are allowed without approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestMCPProxyIntegration]] - code - gateway/tests/test_enhanced_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/switch_modelsh
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 5 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]

## Top bridge nodes
- [[TestMCPProxyIntegration]] - degree 14, connects to 2 communities
- [[.mcp_proxy_with_approval()]] - degree 3, connects to 1 community
- [[.test_low_risk_tool_allowed()]] - degree 3, connects to 1 community
- [[.test_owner_bypass()]] - degree 3, connects to 1 community