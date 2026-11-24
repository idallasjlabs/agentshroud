---
type: community
members: 21
---

# HTTPForwarder

**Members:** 21 nodes

## Members
- [[dot-__init__()_219]] - code - gateway/proxy/forwarder.py
- [[dot-forward()_1]] - code - gateway/proxy/forwarder.py
- [[dot-get_stats()_18]] - code - gateway/proxy/forwarder.py
- [[dot-health_check()_5]] - code - gateway/proxy/forwarder.py
- [[dot-set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[Any_85]] - code
- [[Check if the OpenClaw backend is healthy.]] - rationale - gateway/proxy/forwarder.py
- [[Configuration for the HTTP forwarder.]] - rationale - gateway/proxy/forwarder.py
- [[Forward a request to the OpenClaw backend.]] - rationale - gateway/proxy/forwarder.py
- [[ForwardResult]] - code - gateway/proxy/forwarder.py
- [[ForwarderConfig]] - code - gateway/proxy/forwarder.py
- [[Forwards sanitized requests to the OpenClaw backend. In production, uses…]] - rationale - gateway/proxy/forwarder.py
- [[HTTPForwarder]] - code - gateway/proxy/forwarder.py
- [[Result of forwarding a request.]] - rationale - gateway/proxy/forwarder.py
- [[Set a mock response handler for testing.]] - rationale - gateway/proxy/forwarder.py
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[fixture_138]] - code
- [[forwarder.py_2]] - code - gateway/proxy/forwarder.py
- [[healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_forwarder_error_handling()]] - code - gateway/tests/test_e2e_proxy.py
- [[unhealthy_forwarder()]] - code - gateway/tests/test_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HTTPForwarder
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 6 edges to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[HTTPForwarder]] - degree 13, connects to 2 communities
- [[ForwarderConfig]] - degree 9, connects to 2 communities
- [[forwarder.py_2]] - degree 5, connects to 2 communities
- [[test_forwarder_error_handling()]] - degree 5, connects to 1 community
- [[healthy_forwarder()]] - degree 4, connects to 1 community
