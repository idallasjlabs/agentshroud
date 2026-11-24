---
type: community
members: 12
---

# .test_activity_command_renders_entries

**Members:** 12 nodes

## Members
- [[dot-test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerActivityNotice]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestPendingNoticeIncludesEgressSection]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_capture()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_capture()_1]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_capture()_2]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_send_owner_activity_notice must render tracker entries or honest error.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_send_owner_pending_notice must append Pending Egress Requests when queue non-…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_activity_command_renders_entries
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY__make_sanitizer]]
- 3 edges to [[_COMMUNITY_asyncio_5]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[dot-test_activity_command_renders_entries()]] - degree 6, connects to 2 communities
- [[dot-test_activity_command_reports_tracker_unhealthy()]] - degree 6, connects to 2 communities
- [[TestOwnerActivityNotice]] - degree 5, connects to 2 communities
- [[TestPendingNoticeIncludesEgressSection]] - degree 4, connects to 2 communities
- [[dot-test_pending_includes_egress_entries()]] - degree 4, connects to 2 communities
