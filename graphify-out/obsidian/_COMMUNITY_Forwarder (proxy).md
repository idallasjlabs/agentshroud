---
type: community
cohesion: 0.10
members: 26
---

# Forwarder (proxy)

**Cohesion:** 0.10 - loosely connected
**Members:** 26 nodes

## Members
- [[.__init__()_22]] - code - gateway/proxy/forwarder.py
- [[.forward()_1]] - code - gateway/proxy/forwarder.py
- [[.forward()_4]] - code - gateway/tests/test_e2e_proxy.py
- [[.get_stats()_2]] - code - gateway/proxy/forwarder.py
- [[.health_check()_1]] - code - gateway/proxy/forwarder.py
- [[.is_healthy()]] - code - gateway/proxy/forwarder.py
- [[.last_forward_time()]] - code - gateway/proxy/forwarder.py
- [[.set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[Any_13]] - code - gateway/proxy/forwarder.py
- [[Check if the OpenClaw backend is healthy.]] - rationale - gateway/proxy/forwarder.py
- [[Configuration for the HTTP forwarder.]] - rationale - gateway/proxy/forwarder.py
- [[Forward a request to the OpenClaw backend.]] - rationale - gateway/proxy/forwarder.py
- [[ForwardResult]] - code - gateway/proxy/forwarder.py
- [[ForwarderConfig]] - code - gateway/proxy/forwarder.py
- [[Forwards sanitized requests to the OpenClaw backend.      In production, uses ai]] - rationale - gateway/proxy/forwarder.py
- [[HTTPForwarder]] - code - gateway/proxy/forwarder.py
- [[Result of forwarding a request.]] - rationale - gateway/proxy/forwarder.py
- [[Set a mock response handler for testing.]] - rationale - gateway/proxy/forwarder.py
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder mock works correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[forwarder()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[forwarder.py]] - code - gateway/proxy/forwarder.py
- [[healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_forwarder_error_handling()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_forwarder_mock()]] - code - gateway/tests/test_e2e_proxy.py
- [[unhealthy_forwarder()]] - code - gateway/tests/test_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Forwarder_proxy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 7 edges to [[_COMMUNITY_E2e Proxy]]
- 1 edge to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 1 edge to [[_COMMUNITY_Http Proxy Coverage]]
- 1 edge to [[_COMMUNITY_Llm Proxy]]

## Top bridge nodes
- [[HTTPForwarder]] - degree 22, connects to 5 communities
- [[ForwarderConfig]] - degree 11, connects to 2 communities
- [[test_forwarder_error_handling()]] - degree 5, connects to 1 community
- [[healthy_forwarder()]] - degree 3, connects to 1 community
- [[unhealthy_forwarder()]] - degree 3, connects to 1 community