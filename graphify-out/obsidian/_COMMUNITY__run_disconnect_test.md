---
type: community
members: 6
---

# _run_disconnect_test

**Members:** 6 nodes

## Members
- [[ConnectionClosedError (WS code 1006 — ungraceful ESP disconnect, e.g. device…]] - rationale - gateway/tests/test_voice_gateway.py
- [[ConnectionClosedOK (WS code 10001001 — clean websockets-library close path)…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Directly invoke ``voice_endpoint`` with a mocked WebSocket whose second…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_run_disconnect_test()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_error_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_ok_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_run_disconnect_test
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[_run_disconnect_test()]] - degree 5, connects to 2 communities
- [[test_ws_connectionclosed_error_logs_info_no_traceback()]] - degree 3, connects to 1 community
- [[test_ws_connectionclosed_ok_logs_info_no_traceback()]] - degree 3, connects to 1 community
