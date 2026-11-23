---
type: community
members: 12
---

# _FakeWSConnect

**Members:** 12 nodes

## Members
- [[dot-__aenter__()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-__aexit__()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-__init__()_29]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[Async context manager mimicking websockets.connect().]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[WebSocket relay for Slack Socket Mode inbound traffic. Bot connects here…]] - rationale - gateway/ingest_api/main.py
- [[_FakeWSConnect]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[_bot_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_upstream_to_bot()]] - code - gateway/ingest_api/main.py
- [[fake_connect()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[slack_ws_relay()]] - code - gateway/ingest_api/main.py
- [[upstream()]] - code - gateway/tests/test_hermes_dashboard_bridge.py
- [[websocket_1]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeWSConnect
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY__run_asgi]]
- 2 edges to [[_COMMUNITY_hermes_dashboard_ws_proxy]]
- 1 edge to [[_COMMUNITY_test_dns_canvas_coverage.py]]
- 1 edge to [[_COMMUNITY_TestRewriteRequestHeaders]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[_FakeWSConnect]] - degree 8, connects to 2 communities
- [[upstream()]] - degree 4, connects to 2 communities
- [[slack_ws_relay()]] - degree 6, connects to 1 community
- [[fake_connect()]] - degree 3, connects to 1 community
- [[websocket_1]] - degree 2, connects to 1 community
