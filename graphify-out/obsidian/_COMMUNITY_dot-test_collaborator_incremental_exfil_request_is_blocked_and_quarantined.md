---
type: community
members: 4
---

# .test_collaborator_incremental_exfil_request_is_blocked_and_quarantined

**Members:** 4 nodes

## Members
- [[dot-test_collaborator_incremental_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_memory_access_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Chunked extraction prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Direct memory-content requests should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_incremental_exfil_request_is_blocked_and_quarantined
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY__wrap_response]]

## Top bridge nodes
- [[dot-test_collaborator_incremental_exfil_request_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[dot-test_collaborator_memory_access_request_is_blocked_and_quarantined()]] - degree 7, connects to 2 communities
