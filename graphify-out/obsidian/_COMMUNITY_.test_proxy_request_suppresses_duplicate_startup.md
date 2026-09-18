---
type: community
cohesion: 1.00
members: 2
---

# .test_proxy_request_suppresses_duplicate_startup

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Startup notice dedupe should still apply when sender forgets system header.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_proxy_request_suppresses_duplicate_startup
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[.test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - degree 4, connects to 1 community