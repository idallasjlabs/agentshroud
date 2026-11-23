---
type: community
members: 15
---

# ._relay

**Members:** 15 nodes

## Members
- [[dot-_agent_id_for_peer()]] - code - gateway/proxy/http_proxy.py
- [[dot-_clamav_scan_bytes()]] - code - gateway/proxy/http_proxy.py
- [[dot-_handle_client()]] - code - gateway/proxy/http_proxy.py
- [[dot-_process_connect()]] - code - gateway/proxy/http_proxy.py
- [[dot-_relay()]] - code - gateway/proxy/http_proxy.py
- [[dot-_relay_and_scan()]] - code - gateway/proxy/http_proxy.py
- [[Copy bytes from reader to writer until EOF. ``idle_timeout`` (default 120 s)…]] - rationale - gateway/proxy/http_proxy.py
- [[Copy bytes from reader to writer, sampling the first scan_limit bytes for…]] - rationale - gateway/proxy/http_proxy.py
- [[Handle a single incoming client connection.]] - rationale - gateway/proxy/http_proxy.py
- [[Parse CONNECT request, check allowlist, relay or block.]] - rationale - gateway/proxy/http_proxy.py
- [[Resolve source IP to a bot_id; lazily extends registry via DNS. The startup…]] - rationale - gateway/proxy/http_proxy.py
- [[StreamReader_2]] - code
- [[StreamWriter_2]] - code
- [[Write data to a temp file and scan with ClamAV. Runs in a thread executor so it…]] - rationale - gateway/proxy/http_proxy.py
- [[test_relay_copies_bytes_until_eof()]] - code - gateway/tests/test_http_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_relay
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 5 edges to [[_COMMUNITY_test_http_proxy_coverage.py]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]

## Top bridge nodes
- [[dot-_relay()]] - degree 10, connects to 2 communities
- [[dot-_clamav_scan_bytes()]] - degree 4, connects to 2 communities
- [[test_relay_copies_bytes_until_eof()]] - degree 4, connects to 2 communities
- [[dot-_process_connect()]] - degree 8, connects to 1 community
- [[dot-_relay_and_scan()]] - degree 7, connects to 1 community
