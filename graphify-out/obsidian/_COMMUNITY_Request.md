---
type: community
cohesion: 0.06
members: 44
---

# Request

**Cohesion:** 0.06 - loosely connected
**Members:** 44 nodes

## Members
- [[Add security headers to all responses (defense-in-depth). Also catches Python…]] - rationale - gateway/ingest_api/main.py
- [[CORS middleware that uses config from app_state]] - rationale - gateway/ingest_api/main.py
- [[Catch-all error handler Never leaks stack traces or internal details to client.…]] - rationale - gateway/ingest_api/main.py
- [[Log all incoming requests Never logs request bodies (may contain PII).]] - rationale - gateway/ingest_api/main.py
- [[Reject request bodies larger than 1MB before parsing. Checks Content-Length…]] - rationale - gateway/ingest_api/main.py
- [[Test ApprovalDecision with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test ApprovalRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test FastAPI lifespan initialization]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects empty content]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects invalid source]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[_body_stream()]] - code - gateway/ingest_api/main.py
- [[cors_middleware()]] - code - gateway/ingest_api/main.py
- [[exception_handler]] - code
- [[global_exception_handler()]] - code - gateway/ingest_api/main.py
- [[limit_request_body re-injects a fully-read chunked body and calls downstream.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body rejects chunked bodies over 1MB with 413.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body returns a clean 400 when the client drops mid-upload.      Wi]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body()]] - code - gateway/ingest_api/main.py
- [[log_requests()]] - code - gateway/ingest_api/main.py
- [[middleware]] - code
- [[security_headers_middleware adds expected security headers.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware re-raises BaseExceptions that are not groups.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware returns 500 when anyio BaseExceptionGroup is raised.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware()]] - code - gateway/ingest_api/main.py
- [[test_approval_decision_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_approval_request_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_empty_content()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_invalid_source()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler_http_exception()]] - code - gateway/tests/test_main_simple.py
- [[test_lifespan_initialization()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_chunked_body_over_limit_rejected()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_chunked_body_within_limit_passes_through()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_client_disconnect_returns_clean_response()]] - code - gateway/tests/test_main_simple.py
- [[test_log_requests_middleware()]] - code - gateway/tests/test_main_simple.py
- [[test_main_simple.py]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_catches_exception_group()]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_normal_response()]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_reraises_non_group()]] - code - gateway/tests/test_main_simple.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Request
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 5 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 4 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_DataLedger]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[test_main_simple.py]] - degree 22, connects to 3 communities
- [[global_exception_handler()]] - degree 8, connects to 3 communities
- [[limit_request_body()]] - degree 9, connects to 2 communities
- [[security_headers_middleware()]] - degree 8, connects to 2 communities
- [[log_requests()]] - degree 6, connects to 2 communities
