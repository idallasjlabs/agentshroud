---
type: community
cohesion: 0.22
members: 14
---

# ._process_connect()

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
- [[StreamReader_3]] - code - gateway/proxy/http_proxy.py
- [[StreamWriter_2]] - code - gateway/proxy/http_proxy.py
- [[Write data to a temp file and scan with ClamAV.          Runs in a thread execut]] - rationale - gateway/proxy/http_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_process_connect
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 2 edges to [[_COMMUNITY_WebProxyConfig]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]

## Top bridge nodes
- [[StreamReader_3]] - degree 6, connects to 2 communities
- [[StreamWriter_2]] - degree 6, connects to 2 communities
- [[._clamav_scan_bytes()]] - degree 4, connects to 2 communities
- [[._process_connect()]] - degree 8, connects to 1 community
- [[._relay_and_scan()]] - degree 7, connects to 1 community