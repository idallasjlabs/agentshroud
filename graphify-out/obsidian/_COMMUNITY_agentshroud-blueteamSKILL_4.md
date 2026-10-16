---
type: community
cohesion: 0.09
members: 26
---

# agentshroud-blueteam/SKILL.md

**Cohesion:** 0.09 - loosely connected
**Members:** 26 nodes

## Members
- [[Alias for Hermes Anthropic SDK's apiv1 preflight path. Some Anthropic SDK…]] - rationale - gateway/ingest_api/main.py
- [[Alias for hermes v0.16.0+'s OpenAI client. Hermes upgraded to v0.16.0 on…]] - rationale - gateway/ingest_api/main.py
- [[CORS middleware that uses config from app_state]] - rationale - gateway/ingest_api/main.py
- [[Log all incoming requests Never logs request bodies (may contain PII).]] - rationale - gateway/ingest_api/main.py
- [[Proxy Google Gemini API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Proxy bot Slack Web API calls through SecurityPipeline. Restricted to the…]] - rationale - gateway/ingest_api/main.py
- [[Proxy native Ollama API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Redirect bare hermes-dashboard to hermes-dashboard so assets resolve.]] - rationale - gateway/ingest_api/main.py
- [[Request_7]] - code
- [[Set a user's role (owner only).]] - rationale - gateway/ingest_api/main.py
- [[Store a report in the gateway-managed multi-bot report store. Body {bot…]] - rationale - gateway/ingest_api/main.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[api_route]] - code
- [[cors_middleware()]] - code - gateway/ingest_api/main.py
- [[create_report()]] - code - gateway/ingest_api/main.py
- [[google_api_proxy]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_root]] - code - gateway/ingest_api/main.py
- [[llm_api_v1_prefix_alias]] - code - gateway/ingest_api/main.py
- [[llm_openai_chat_alias]] - code - gateway/ingest_api/main.py
- [[log_requests()]] - code - gateway/ingest_api/main.py
- [[middleware]] - code
- [[ollama_api_proxy]] - code - gateway/ingest_api/main.py
- [[put]] - code
- [[set_user_role()]] - code - gateway/ingest_api/main.py
- [[slack_api_proxy()]] - code - gateway/ingest_api/main.py
- [[test_log_requests_middleware()]] - code - gateway/tests/test_main_simple.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 7 edges to [[_COMMUNITY_Request]]
- 7 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY_test_main_endpoints.py_1]]
- 2 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 2 edges to [[_COMMUNITY_test_prompt_guard.py_2]]
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 1 edge to [[_COMMUNITY_AuditChain_1]]

## Top bridge nodes
- [[Request_7]] - degree 22, connects to 7 communities
- [[api_route]] - degree 9, connects to 3 communities
- [[google_api_proxy]] - degree 6, connects to 2 communities
- [[log_requests()]] - degree 6, connects to 2 communities
- [[create_report()]] - degree 5, connects to 2 communities
