---
type: community
members: 3
---

# test_webhook_receiver_passes_agent_id_as_bot_id

**Members:** 3 nodes

## Members
- [[asyncio_39]] - code
- [[process_webhook passes agent_id as bot_id to record_activity.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_webhook_receiver_passes_agent_id_as_bot_id
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_WebhookReceiver]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]

## Top bridge nodes
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - degree 4, connects to 2 communities
