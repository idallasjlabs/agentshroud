---
type: community
cohesion: 1.00
members: 2
---

# activate-lockdown.sh

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[When pipeline is set, process_outbound must be called on outbound messages.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/activate-lockdownsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_outbound_pipeline_called_when_available()]] - degree 4, connects to 3 communities