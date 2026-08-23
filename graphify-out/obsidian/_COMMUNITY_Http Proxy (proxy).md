---
type: community
cohesion: 0.22
members: 14
---

# Http Proxy (proxy)

**Cohesion:** 0.22 - loosely connected
**Members:** 14 nodes

## Members
- [[._agent_id_for_peer()]] - code - gateway/proxy/http_proxy.py
- [[._clamav_scan_bytes()]] - code - gateway/proxy/http_proxy.py
- [[._handle_client()]] - code - gateway/proxy/http_proxy.py
- [[._process_connect()]] - code - gateway/proxy/http_proxy.py
- [[._relay()]] - code - gateway/proxy/http_proxy.py
- [[._relay_and_scan()]] - code - gateway/proxy/http_proxy.py
- [[Copy bytes from reader to writer until EOF.          ``idle_timeout`` (default 1]] - rationale - gateway/proxy/http_proxy.py
- [[Copy bytes from reader to writer, sampling the first scan_limit bytes         fo]] - rationale - gateway/proxy/http_proxy.py
- [[Handle a single incoming client connection.]] - rationale - gateway/proxy/http_proxy.py
- [[Parse CONNECT request, check allowlist, relay or block.]] - rationale - gateway/proxy/http_proxy.py
- [[Resolve source IP to a bot_id; lazily extends registry via DNS.          The sta]] - rationale - gateway/proxy/http_proxy.py
- [[StreamReader_2]] - code - gateway/proxy/http_proxy.py
- [[StreamWriter_2]] - code - gateway/proxy/http_proxy.py
- [[Write data to a temp file and scan with ClamAV.          Runs in a thread execut]] - rationale - gateway/proxy/http_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Http_Proxy_proxy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Http Proxy Coverage]]
- 4 edges to [[_COMMUNITY_Web Proxy]]
- 1 edge to [[_COMMUNITY_OAuth & Metadata Guard]]

## Top bridge nodes
- [[._clamav_scan_bytes()]] - degree 4, connects to 2 communities
- [[._process_connect()]] - degree 8, connects to 1 community
- [[._relay_and_scan()]] - degree 7, connects to 1 community
- [[StreamReader_2]] - degree 6, connects to 1 community
- [[StreamWriter_2]] - degree 6, connects to 1 community