---
type: community
cohesion: 0.50
members: 4
---

# ApprovalQueueConfig (2) (2)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-test_non_owner_activity_is_tracked_for_unknown_user()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown non-owner users should still be tracked at gateway level.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[__init__()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[record_activity()]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_2_2
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 1 edge to [[_COMMUNITY_TestInboundPipelineOnGetUpdates]]
- 1 edge to [[_COMMUNITY_asyncio]]

## Top bridge nodes
- [[dot-test_non_owner_activity_is_tracked_for_unknown_user()]] - degree 9, connects to 3 communities
