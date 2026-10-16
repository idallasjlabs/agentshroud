---
type: community
cohesion: 0.04
members: 67
---

# Request

**Cohesion:** 0.04 - loosely connected
**Members:** 67 nodes

## Members
- [[Add security headers to all responses (defense-in-depth). Also catches Python…]] - rationale - gateway/ingest_api/main.py
- [[Alias for Hermes Anthropic SDK's apiv1 preflight path. Some Anthropic SDK…]] - rationale - gateway/ingest_api/main.py
- [[Alias for hermes v0.16.0+'s OpenAI client. Hermes upgraded to v0.16.0 on…]] - rationale - gateway/ingest_api/main.py
- [[ApprovalDecision]] - code - gateway/ingest_api/models.py
- [[CORS middleware that uses config from app_state]] - rationale - gateway/ingest_api/main.py
- [[Catch-all error handler Never leaks stack traces or internal details to client.…]] - rationale - gateway/ingest_api/main.py
- [[Log all incoming requests Never logs request bodies (may contain PII).]] - rationale - gateway/ingest_api/main.py
- [[Proxy Anthropic API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Proxy Google Gemini API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Proxy bot Slack Web API calls through SecurityPipeline. Restricted to the…]] - rationale - gateway/ingest_api/main.py
- [[Proxy native Ollama API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Redirect bare hermes-dashboard to hermes-dashboard so assets resolve.]] - rationale - gateway/ingest_api/main.py
- [[Reject request bodies larger than 1MB before parsing. Checks Content-Length…]] - rationale - gateway/ingest_api/main.py
- [[Request_1]] - code
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[Set a user's role (owner only).]] - rationale - gateway/ingest_api/main.py
- [[Test ApprovalDecision with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test ApprovalRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test FastAPI lifespan initialization]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects empty content]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects invalid source]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[User's decision on a pending approval request]] - rationale - gateway/ingest_api/models.py
- [[_body_stream()]] - code - gateway/ingest_api/main.py
- [[api_route]] - code
- [[cors_middleware()]] - code - gateway/ingest_api/main.py
- [[exception_handler]] - code
- [[global_exception_handler()]] - code - gateway/ingest_api/main.py
- [[google_api_proxy()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_proxy()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_root()]] - code - gateway/ingest_api/main.py
- [[limit_request_body re-injects a fully-read chunked body and calls downstream.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body rejects chunked bodies over 1MB with 413.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body returns a clean 400 when the client drops mid-upload.      Wi]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body()]] - code - gateway/ingest_api/main.py
- [[llm_api_proxy()]] - code - gateway/ingest_api/main.py
- [[llm_api_v1_prefix_alias()]] - code - gateway/ingest_api/main.py
- [[llm_openai_chat_alias()]] - code - gateway/ingest_api/main.py
- [[log_requests()]] - code - gateway/ingest_api/main.py
- [[middleware]] - code
- [[ollama_api_proxy()]] - code - gateway/ingest_api/main.py
- [[put]] - code
- [[security_headers_middleware adds expected security headers.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware re-raises BaseExceptions that are not groups.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware returns 500 when anyio BaseExceptionGroup is raised.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware()]] - code - gateway/ingest_api/main.py
- [[set_user_role()]] - code - gateway/ingest_api/main.py
- [[slack_api_proxy()]] - code - gateway/ingest_api/main.py
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
- 21 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 5 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 4 edges to [[_COMMUNITY_ForwardRequest]]
- 2 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_ThreatAssessment]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_ingest_apimodels.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[Request_1]] - degree 22, connects to 3 communities
- [[ApprovalDecision]] - degree 6, connects to 3 communities
- [[test_main_simple.py]] - degree 22, connects to 2 communities
- [[global_exception_handler()]] - degree 8, connects to 2 communities
- [[hermes_dashboard_proxy()]] - degree 7, connects to 2 communities
