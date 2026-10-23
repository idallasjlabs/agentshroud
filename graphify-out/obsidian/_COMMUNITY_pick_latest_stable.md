---
type: community
cohesion: 0.07
members: 40
---

# pick_latest_stable

**Cohesion:** 0.07 - loosely connected
**Members:** 40 nodes

## Members
- [[Add security headers to all responses (defense-in-depth). Also catches Python…]] - rationale - gateway/ingest_api/main.py
- [[ApprovalDecision]] - code - gateway/ingest_api/models.py
- [[CORS middleware that uses config from app_state]] - rationale - gateway/ingest_api/main.py
- [[Catch-all error handler Never leaks stack traces or internal details to client.…]] - rationale - gateway/ingest_api/main.py
- [[Log all incoming requests Never logs request bodies (may contain PII).]] - rationale - gateway/ingest_api/main.py
- [[Reject request bodies larger than 1MB before parsing. Checks Content-Length…]] - rationale - gateway/ingest_api/main.py
- [[Test ApprovalDecision with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test ApprovalRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test FastAPI lifespan initialization]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[User's decision on a pending approval request]] - rationale - gateway/ingest_api/models.py
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
TABLE source_file, type FROM #community/pick_latest_stable
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_voice_stt_model_ab.py]]
- 5 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_ForwardRequest]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (3)]]
- 1 edge to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_create_auth_dependency()]]
- 1 edge to [[_COMMUNITY__make_proxy()]]
- 1 edge to [[_COMMUNITY_ServiceManager]]

## Top bridge nodes
- [[global_exception_handler()]] - degree 8, connects to 3 communities
- [[ApprovalDecision]] - degree 6, connects to 3 communities
- [[test_main_simple.py]] - degree 22, connects to 2 communities
- [[limit_request_body()]] - degree 9, connects to 2 communities
- [[security_headers_middleware()]] - degree 8, connects to 2 communities
