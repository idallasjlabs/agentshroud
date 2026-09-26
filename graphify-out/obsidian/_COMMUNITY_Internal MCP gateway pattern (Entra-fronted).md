---
type: community
cohesion: 1.00
members: 2
---

# Internal MCP gateway pattern (Entra-fronted)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_pii_redacted_on_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Phone numbers in outbound messages must be redacted by PII sanitizer.          R]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Internal_MCP_gateway_pattern_Entra-fronted
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_pii_redacted_on_outbound()]] - degree 4, connects to 3 communities