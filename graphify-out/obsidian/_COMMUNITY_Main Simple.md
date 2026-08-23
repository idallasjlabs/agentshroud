---
type: community
cohesion: 0.08
members: 28
---

# Main Simple

**Cohesion:** 0.08 - loosely connected
**Members:** 28 nodes

## Members
- [[Catch-all error handler      Never leaks stack traces or internal details to cli]] - rationale - gateway/ingest_api/main.py
- [[Exception_1]] - code - gateway/ingest_api/main.py
- [[Test ApprovalDecision with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test ApprovalRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test FastAPI lifespan initialization]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[global_exception_handler()]] - code - gateway/ingest_api/main.py
- [[limit_request_body re-injects a fully-read chunked body and calls downstream.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body rejects chunked bodies over 1MB with 413.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body returns a clean 400 when the client drops mid-upload.      Wi]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware adds expected security headers.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware re-raises BaseExceptions that are not groups.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware returns 500 when anyio BaseExceptionGroup is raised.]] - rationale - gateway/tests/test_main_simple.py
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
TABLE source_file, type FROM #community/Main_Simple
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 4 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 4 edges to [[_COMMUNITY_Config Validation & Router]]
- 3 edges to [[_COMMUNITY_Approval Queue]]
- 2 edges to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 2 edges to [[_COMMUNITY_Audit Export]]
- 2 edges to [[_COMMUNITY_Soc Egress Endpoints]]
- 1 edge to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 1 edge to [[_COMMUNITY_Egress Approval (security)]]
- 1 edge to [[_COMMUNITY_Main Endpoints]]

## Top bridge nodes
- [[Exception_1]] - degree 16, connects to 7 communities
- [[test_main_simple.py]] - degree 22, connects to 4 communities
- [[global_exception_handler()]] - degree 8, connects to 2 communities
- [[test_approval_decision_valid()]] - degree 3, connects to 1 community
- [[test_approval_request_valid()]] - degree 3, connects to 1 community