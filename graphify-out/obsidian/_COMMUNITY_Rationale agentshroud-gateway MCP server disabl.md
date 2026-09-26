---
type: community
cohesion: 1.00
members: 2
---

# Rationale: agentshroud-gateway MCP server disabl

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_ssn_redacted_on_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[SSN in outbound messages must be redacted.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Rationale_agentshroud-gateway_MCP_server_disabl
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_ssn_redacted_on_outbound()]] - degree 4, connects to 3 communities