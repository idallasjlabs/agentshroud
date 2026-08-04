---
type: community
cohesion: 0.33
members: 6
---

# Module Group 496

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_extract_user_id_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_user_id_slack_missing_event()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_user_id_telegram_unchanged()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_username_slack()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_extract_username_slack_fallback_to_user_id()]] - code - gateway/tests/test_slack_proxy.py
- [[TestWebhookReceiverSlackExtraction]] - code - gateway/tests/test_slack_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_496
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Slack Proxy]]
- 1 edge to [[_COMMUNITY_Webhook Receiver]]
- 1 edge to [[_COMMUNITY_Slack Proxy Tests]]

## Top bridge nodes
- [[TestWebhookReceiverSlackExtraction]] - degree 8, connects to 3 communities
