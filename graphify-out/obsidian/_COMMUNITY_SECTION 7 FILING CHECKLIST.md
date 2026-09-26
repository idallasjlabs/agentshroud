---
type: community
cohesion: 0.50
members: 4
---

# SECTION 7: FILING CHECKLIST

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_collaborator_incremental_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_memory_access_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Chunked extraction prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Direct memory-content requests should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SECTION_7_FILING_CHECKLIST
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[.test_collaborator_incremental_exfil_request_is_blocked_and_quarantined()]] - degree 8, connects to 2 communities
- [[.test_collaborator_memory_access_request_is_blocked_and_quarantined()]] - degree 7, connects to 2 communities