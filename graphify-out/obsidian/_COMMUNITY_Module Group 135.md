---
type: community
cohesion: 0.07
members: 35
---

# Module Group 135

**Cohesion:** 0.07 - loosely connected
**Members:** 35 nodes

## Members
- [[Add security headers to all responses (defense-in-depth).      Also catches Pyth]] - rationale - gateway/ingest_api/main.py
- [[Reject request bodies larger than 1MB before parsing.      Checks Content-Length]] - rationale - gateway/ingest_api/main.py
- [[Test ApprovalDecision with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test ApprovalRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test FastAPI lifespan initialization]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects empty content]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects invalid source]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body re-injects a fully-read chunked body and calls downstream.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body rejects chunked bodies over 1MB with 413.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body returns a clean 400 when the client drops mid-upload.      Wi]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body()]] - code - gateway/ingest_api/main.py
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
TABLE source_file, type FROM #community/Module_Group_135
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 4 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 2 edges to [[_COMMUNITY_Enhanced Approval Queue]]

## Top bridge nodes
- [[test_main_simple.py]] - degree 22, connects to 3 communities
- [[limit_request_body()]] - degree 8, connects to 2 communities
- [[security_headers_middleware()]] - degree 8, connects to 2 communities
- [[test_approval_decision_valid()]] - degree 3, connects to 1 community
- [[test_approval_request_valid()]] - degree 3, connects to 1 community
