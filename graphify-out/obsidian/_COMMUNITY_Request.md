---
type: community
members: 35
---

# Request

**Members:** 35 nodes

## Members
- [[Alias for Hermes Anthropic SDK's apiv1 preflight path. Some Anthropic SDK…]] - rationale - gateway/ingest_api/main.py
- [[Alias for hermes v0.16.0+'s OpenAI client. Hermes upgraded to v0.16.0 on…]] - rationale - gateway/ingest_api/main.py
- [[CORS middleware that uses config from app_state]] - rationale - gateway/ingest_api/main.py
- [[Catch-all error handler Never leaks stack traces or internal details to client.…]] - rationale - gateway/ingest_api/main.py
- [[Log all incoming requests Never logs request bodies (may contain PII).]] - rationale - gateway/ingest_api/main.py
- [[Proxy Anthropic API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Proxy Google Gemini API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Proxy bot Slack Web API calls through SecurityPipeline. Restricted to the…]] - rationale - gateway/ingest_api/main.py
- [[Proxy native Ollama API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Redirect bare hermes-dashboard to hermes-dashboard so assets resolve.]] - rationale - gateway/ingest_api/main.py
- [[Request_4]] - code
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[Set a user's role (owner only).]] - rationale - gateway/ingest_api/main.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[api_route]] - code
- [[cors_middleware()]] - code - gateway/ingest_api/main.py
- [[exception_handler]] - code
- [[global_exception_handler()]] - code - gateway/ingest_api/main.py
- [[google_api_proxy]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_proxy()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_root]] - code - gateway/ingest_api/main.py
- [[llm_api_proxy()]] - code - gateway/ingest_api/main.py
- [[llm_api_v1_prefix_alias]] - code - gateway/ingest_api/main.py
- [[llm_openai_chat_alias]] - code - gateway/ingest_api/main.py
- [[log_requests()]] - code - gateway/ingest_api/main.py
- [[middleware]] - code
- [[ollama_api_proxy]] - code - gateway/ingest_api/main.py
- [[put]] - code
- [[set_user_role()]] - code - gateway/ingest_api/main.py
- [[slack_api_proxy()]] - code - gateway/ingest_api/main.py
- [[test_global_exception_handler()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler_http_exception()]] - code - gateway/tests/test_main_simple.py
- [[test_log_requests_middleware()]] - code - gateway/tests/test_main_simple.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Request
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_ingest_apimain.py]]
- 9 edges to [[_COMMUNITY_Request (2)]]
- 4 edges to [[_COMMUNITY_test_main_endpoints.py (2)]]
- 4 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 3 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 2 edges to [[_COMMUNITY_cmd_start]]
- 2 edges to [[_COMMUNITY_test_prompt_guard.py (2)]]
- 1 edge to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy()]]
- 1 edge to [[_COMMUNITY_ConsentFramework (2)]]

## Top bridge nodes
- [[llm_api_proxy()]] - degree 13, connects to 6 communities
- [[Request_4]] - degree 22, connects to 5 communities
- [[hermes_dashboard_proxy()]] - degree 12, connects to 5 communities
- [[global_exception_handler()]] - degree 8, connects to 3 communities
- [[log_requests()]] - degree 6, connects to 2 communities
