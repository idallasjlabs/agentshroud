---
type: community
cohesion: 0.29
members: 7
---

# Request

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[Catch-all error handler Never leaks stack traces or internal details to client.…]] - rationale - gateway/ingest_api/main.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[exception_handler]] - code
- [[global_exception_handler()]] - code - gateway/ingest_api/main.py
- [[test_global_exception_handler()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler_http_exception()]] - code - gateway/tests/test_main_simple.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Request
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]

## Top bridge nodes
- [[global_exception_handler()]] - degree 8, connects to 4 communities
- [[test_global_exception_handler()]] - degree 3, connects to 1 community
- [[test_global_exception_handler_http_exception()]] - degree 3, connects to 1 community
