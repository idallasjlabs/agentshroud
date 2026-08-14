---
type: community
members: 2
---

# examples/docker-compose.minimal.yml

**Members:** 2 nodes

## Members
- [[.test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Startup notice dedupe should still apply when sender forgets system header.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/examples/docker-composeminimalyml
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ESP32 Firmware]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_docsvault]]

## Top bridge nodes
- [[.test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - degree 4, connects to 3 communities