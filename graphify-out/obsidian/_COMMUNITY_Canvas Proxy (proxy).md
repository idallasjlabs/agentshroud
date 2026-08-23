---
type: community
cohesion: 0.22
members: 16
---

# Canvas Proxy (proxy)

**Cohesion:** 0.22 - loosely connected
**Members:** 16 nodes

## Members
- [[ASGI application auth-gated transparent reverse proxy for Canvas.      Handles]] - rationale - gateway/proxy/canvas_proxy.py
- [[Any_12]] - code - gateway/proxy/canvas_proxy.py
- [[Build headers to forward upstream, stripping hop-by-hop and Authorization.]] - rationale - gateway/proxy/canvas_proxy.py
- [[Proxy a WebSocket connection after validating auth.      Auth is extracted from]] - rationale - gateway/proxy/canvas_proxy.py
- [[Proxy an HTTP request after validating Basic Auth.]] - rationale - gateway/proxy/canvas_proxy.py
- [[Return gateway password from secret file or env var.]] - rationale - gateway/proxy/canvas_proxy.py
- [[Validate HTTP Basic Auth credentials against the gateway password.]] - rationale - gateway/proxy/canvas_proxy.py
- [[Validate token query parameter against the gateway password.]] - rationale - gateway/proxy/canvas_proxy.py
- [[_build_proxy_headers()]] - code - gateway/proxy/canvas_proxy.py
- [[_check_basic_auth()]] - code - gateway/proxy/canvas_proxy.py
- [[_check_token_auth()]] - code - gateway/proxy/canvas_proxy.py
- [[_handle_http()]] - code - gateway/proxy/canvas_proxy.py
- [[_handle_websocket()]] - code - gateway/proxy/canvas_proxy.py
- [[_read_gateway_password()]] - code - gateway/proxy/canvas_proxy.py
- [[canvas_proxy.py]] - code - gateway/proxy/canvas_proxy.py
- [[canvas_proxy_app()]] - code - gateway/proxy/canvas_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Canvas_Proxy_proxy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Http Proxy Coverage]]
- 1 edge to [[_COMMUNITY_Dns Canvas Coverage]]

## Top bridge nodes
- [[canvas_proxy_app()]] - degree 8, connects to 3 communities