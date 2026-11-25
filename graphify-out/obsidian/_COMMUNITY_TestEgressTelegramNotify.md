---
type: community
members: 40
---

# TestEgressTelegramNotify

**Members:** 40 nodes

## Members
- [[dot-notifier()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_answer_callback_error()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_answer_callback_success()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_cleanup_expired_requests()_1]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_get_pending_count()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_allow_always_returns_agent_id()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_approve_1h()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_approve_4h()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_approve_permanent()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_deny()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_deny_returns_agent_id()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_invalid_format()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_missing_agent_id_safe()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_request_not_found()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_handle_callback_returns_agent_id()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_notification_recipients_owner_only_by_default()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_notify_pending_failure()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_notify_pending_success()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[dot-test_risk_emoji_mapping()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[Collaborators are never added to notification_recipients — only owner gets…]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Denial result also includes agent_id so collaborator can be notified.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Missing agent_id in stored request returns empty string, not a crash.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Permanent approval also includes agent_id in result.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test Telegram egress notification system.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test answer_callback handles errors.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test answering callback query.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test callback for non-existent request.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test cleanup removes expired pending requests.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test handling 1-hour time-limited approval callback.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test handling 4-hour time-limited approval callback.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test handling deny callback.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test handling invalid callback data.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test handling permanent (allow_always) approval callback.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test notification handles API failure gracefully.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test risk level emoji display.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[Test successful notification sending.]] - rationale - gateway/tests/test_egress_telegram_notify.py
- [[TestEgressTelegramNotify]] - code - gateway/tests/test_egress_telegram_notify.py
- [[asyncio_45]] - code
- [[fixture_81]] - code
- [[handle_callback must include agent_id so the proxy can notify the originating…]] - rationale - gateway/tests/test_egress_telegram_notify.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressTelegramNotify
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_EgressTelegramNotifier]]
- 1 edge to [[_COMMUNITY_telegram_egress_notify.py]]

## Top bridge nodes
- [[TestEgressTelegramNotify]] - degree 22, connects to 2 communities
- [[dot-notifier()]] - degree 3, connects to 1 community
