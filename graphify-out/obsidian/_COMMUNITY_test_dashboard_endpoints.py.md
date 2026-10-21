---
type: community
members: 2
---

# test_dashboard_endpoints.py

**Members:** 2 nodes

## Members
- [[process_webhook passes agent_id as bot_id to record_activity.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_dashboard_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py (2)]]

## Top bridge nodes
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - degree 3, connects to 2 communities
