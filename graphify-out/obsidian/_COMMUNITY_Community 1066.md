---
type: community
members: 7
---

# Community 1066

**Members:** 7 nodes

## Members
- [[Hermes API forwarder must include an HTTP-method peek to drop non-HTTP connectio]] - rationale - gateway/tests/test_telegram_executor.py
- [[Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying.]] - rationale - gateway/tests/test_telegram_executor.py
- [[lifespan startup must install ThreadPoolExecutor(max_workers=64).]] - rationale - gateway/tests/test_telegram_executor.py
- [[test_hermes_forwarder_drops_non_http()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_hermes_forwarder_has_http_peek()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_installs_64_worker_executor()]] - code - gateway/tests/test_telegram_executor.py
- [[test_telegram_executor.py]] - code - gateway/tests/test_telegram_executor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1066
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 6]]

## Top bridge nodes
- [[test_telegram_executor.py]] - degree 4, connects to 1 community