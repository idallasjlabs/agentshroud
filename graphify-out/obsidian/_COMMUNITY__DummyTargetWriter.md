---
type: community
cohesion: 0.18
members: 13
---

# _DummyTargetWriter

**Cohesion:** 0.18 - loosely connected
**Members:** 13 nodes

## Members
- [[.__init__()_181]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.__init__()_182]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.close()_20]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.close()_21]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.drain()_3]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.readline()_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.write()_3]] - code - gateway/tests/test_http_proxy_coverage.py
- [[First readline returns the request line; the next stalls.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[_CloseRaisesTargetWriter]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_DummyTargetWriter_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_HeaderTimeoutReader]] - code - gateway/tests/test_http_proxy_coverage.py
- [[start() binds a real loopback server; a client gets a parsed response;     stop(]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[test_start_serves_and_stop_closes_loopback()]] - code - gateway/tests/test_http_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_DummyTargetWriter
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 3 edges to [[_COMMUNITY_WebProxyConfig]]
- 3 edges to [[_COMMUNITY_WebProxy]]

## Top bridge nodes
- [[_DummyTargetWriter_1]] - degree 9, connects to 3 communities
- [[_HeaderTimeoutReader]] - degree 8, connects to 3 communities
- [[_CloseRaisesTargetWriter]] - degree 6, connects to 3 communities
- [[test_start_serves_and_stop_closes_loopback()]] - degree 8, connects to 1 community