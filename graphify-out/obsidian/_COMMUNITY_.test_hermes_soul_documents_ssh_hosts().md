---
type: community
cohesion: 1.00
members: 2
---

# .test_hermes_soul_documents_ssh_hosts()

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_long_outbound_message_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Blocked outbound messages should be stored in outbound quarantine.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_hermes_soul_documents_ssh_hosts
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_long_outbound_message_quarantined()]] - degree 4, connects to 3 communities