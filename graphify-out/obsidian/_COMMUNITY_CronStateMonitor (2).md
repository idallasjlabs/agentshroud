---
type: community
members: 3
---

# CronStateMonitor (2)

**Members:** 3 nodes

## Members
- [[dot-test_proxy_request_suppresses_starting_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_startup_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notice dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CronStateMonitor_2
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__req]]
- 2 edges to [[_COMMUNITY_CronStateMonitor]]
- 2 edges to [[_COMMUNITY_UserSessionManager (2)]]

## Top bridge nodes
- [[dot-test_proxy_request_suppresses_starting_notice_emoji_variants()]] - degree 4, connects to 3 communities
- [[dot-test_proxy_request_suppresses_startup_notice_emoji_variants()]] - degree 4, connects to 3 communities
