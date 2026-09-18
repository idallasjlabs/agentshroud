---
type: community
cohesion: 0.18
members: 15
---

# TestHandleEvent

**Cohesion:** 0.18 - loosely connected
**Members:** 15 nodes

## Members
- [[.test_event_without_user_ignored()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_message_event_records_activity()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_message_preview_truncated_to_80_chars()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_no_tracker_does_not_raise()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_non_message_event_ignored()]] - code - gateway/tests/test_slack_proxy.py
- [[.test_tracker_error_does_not_propagate()]] - code - gateway/tests/test_slack_proxy.py
- [[SlackAPIProxy]] - code - gateway/tests/test_slack_proxy.py
- [[TestHandleEvent]] - code - gateway/tests/test_slack_proxy.py
- [[Tests for SlackAPIProxy.handle_event() — inbound Socket Mode event processing.]] - rationale - gateway/tests/test_slack_proxy.py
- [[handle_event ignores message events with no user field.]] - rationale - gateway/tests/test_slack_proxy.py
- [[handle_event ignores non-message event types.]] - rationale - gateway/tests/test_slack_proxy.py
- [[handle_event is a no-op and does not raise when tracker is None.]] - rationale - gateway/tests/test_slack_proxy.py
- [[handle_event records inbound activity for message events.]] - rationale - gateway/tests/test_slack_proxy.py
- [[handle_event swallows tracker exceptions (non-fatal).]] - rationale - gateway/tests/test_slack_proxy.py
- [[handle_event truncates message_preview to 80 characters.]] - rationale - gateway/tests/test_slack_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestHandleEvent
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_WebhookReceiver]]
- 2 edges to [[_COMMUNITY_SlackAPIProxy]]
- 2 edges to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[TestHandleEvent]] - degree 10, connects to 3 communities
- [[SlackAPIProxy]] - degree 9, connects to 3 communities