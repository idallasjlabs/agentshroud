---
type: community
members: 22
---

# canvas_proxy.py

**Members:** 22 nodes

## Members
- [[ASGI application auth-gated transparent reverse proxy for Canvas. Handles…]] - rationale - gateway/proxy/canvas_proxy.py
- [[Any_69]] - code
- [[Build headers to forward upstream, stripping hop-by-hop and Authorization.]] - rationale - gateway/proxy/canvas_proxy.py
- [[Canvas Reverse Proxy with HTTP Basic Auth Gate (CVE-2026-34871 fix). Intercepts…]] - rationale - gateway/proxy/canvas_proxy.py
- [[Canvas reverse-proxy upstream wiring regression tests. The v1.1.0 container…]] - rationale - gateway/tests/test_canvas_proxy.py
- [[Proxy a WebSocket connection after validating auth. Auth is extracted from the…]] - rationale - gateway/proxy/canvas_proxy.py
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
- [[client_to_upstream()]] - code - gateway/proxy/canvas_proxy.py
- [[test_canvas_proxy.py]] - code - gateway/tests/test_canvas_proxy.py
- [[test_default_upstream_is_current_container_name()]] - code - gateway/tests/test_canvas_proxy.py
- [[test_env_override_takes_precedence()]] - code - gateway/tests/test_canvas_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/canvas_proxypy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_GatewayEmailService]]
- 1 edge to [[_COMMUNITY__run_asgi]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_test_dns_canvas_coverage.py]]

## Top bridge nodes
- [[canvas_proxy.py]] - degree 11, connects to 2 communities
- [[canvas_proxy_app()]] - degree 7, connects to 2 communities
- [[_handle_websocket()]] - degree 9, connects to 1 community
