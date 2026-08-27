---
type: community
members: 63
---

# Community 83

**Members:** 63 nodes

## Members
- [[.test_chat_allows_valid_token()]] - code - chatbot/test_main.py
- [[.test_chat_allows_when_no_token_configured()]] - code - chatbot/test_main.py
- [[.test_chat_requires_auth_when_token_set()]] - code - chatbot/test_main.py
- [[.test_chat_success_returns_parsed_response()]] - code - chatbot/test_main.py
- [[.test_get_auth_token_falls_back_to_env_when_no_secret_file()]] - code - chatbot/test_main.py
- [[.test_get_auth_token_reads_secret_file_over_env()]] - code - chatbot/test_main.py
- [[.test_health_degraded_without_client()]] - code - chatbot/test_main.py
- [[.test_health_healthy_with_client()]] - code - chatbot/test_main.py
- [[.test_internal_error_not_leaked()]] - code - chatbot/test_main.py
- [[.test_lifespan_logs_when_auth_token_configured()]] - code - chatbot/test_main.py
- [[.test_lifespan_reads_api_key_from_secret_file()]] - code - chatbot/test_main.py
- [[.test_lifespan_with_api_key_initializes_async_client()]] - code - chatbot/test_main.py
- [[.test_lifespan_without_api_key_leaves_client_none()]] - code - chatbot/test_main.py
- [[.test_openai_auth_error_returns_503()]] - code - chatbot/test_main.py
- [[.test_openai_rate_limit_error_returns_429()]] - code - chatbot/test_main.py
- [[.test_rate_limit_enforced()]] - code - chatbot/test_main.py
- [[.test_uses_async_openai_client()]] - code - chatbot/test_main.py
- [[A successful OpenAI completion returns 200 with the parsed fields         via th]] - rationale - chatbot/test_main.py
- [[ChatRequest]] - code - chatbot/main.py
- [[ChatResponse]] - code - chatbot/main.py
- [[Exceeding the rate limit returns 429.]] - rationale - chatbot/test_main.py
- [[FastAPI]] - code - chatbot/main.py
- [[FastAPI lifespan - initialize OpenAI client and persona once.]] - rationale - chatbot/main.py
- [[HTTPAuthorizationCredentials]] - code - chatbot/main.py
- [[Health check endpoint for Docker.      Reports degraded status when the OpenAI c]] - rationale - chatbot/main.py
- [[Health endpoint reports degraded when OpenAI client is not available.]] - rationale - chatbot/test_main.py
- [[Health endpoint reports healthy when OpenAI client is available.]] - rationale - chatbot/test_main.py
- [[Import chatbot.main with a fresh module state (no real OpenAI).]] - rationale - chatbot/test_main.py
- [[Isaiah Chat Service - Phase 3 MVP Minimal chat service with Isaiah's personality]] - rationale - chatbot/main.py
- [[Load Isaiah's persona from IDENTITY, SOUL, and USER files.]] - rationale - chatbot/main.py
- [[OpenAI AuthenticationError returns 503 without leaking the key.]] - rationale - chatbot/test_main.py
- [[OpenAI exceptions should not leak internal details to the client.]] - rationale - chatbot/test_main.py
- [[OpenAI's own RateLimitError is translated to a 429 for the caller.]] - rationale - chatbot/test_main.py
- [[Process chat message with Isaiah's personality.]] - rationale - chatbot/main.py
- [[Raise 429 if the client has exceeded the rate limit.]] - rationale - chatbot/main.py
- [[Read the expected auth token from env or secrets.]] - rationale - chatbot/main.py
- [[Request]] - code - chatbot/main.py
- [[Require valid Bearer token for chat endpoints.      When CHATBOT_AUTH_TOKEN is n]] - rationale - chatbot/main.py
- [[TestAsyncClient]] - code - chatbot/test_main.py
- [[TestAuth]] - code - chatbot/test_main.py
- [[TestAuthTokenSource]] - code - chatbot/test_main.py
- [[TestErrorSanitization]] - code - chatbot/test_main.py
- [[TestHealthCheck]] - code - chatbot/test_main.py
- [[TestLifespan]] - code - chatbot/test_main.py
- [[TestRateLimit]] - code - chatbot/test_main.py
- [[Tests for chatbotmain.py.  Covers the four SCRUM-109 fixes 1. Auth enforcement]] - rationale - chatbot/test_main.py
- [[Verify the module uses AsyncOpenAI, not sync OpenAI.]] - rationale - chatbot/test_main.py
- [[When CHATBOT_AUTH_TOKEN is not set, chat is open (backward compat).]] - rationale - chatbot/test_main.py
- [[When CHATBOT_AUTH_TOKEN is set and correct token given, request proceeds.]] - rationale - chatbot/test_main.py
- [[When CHATBOT_AUTH_TOKEN is set, chat without a token returns 401.]] - rationale - chatbot/test_main.py
- [[When the Docker secret file exists, it wins over the env var.]] - rationale - chatbot/test_main.py
- [[When the Docker secret file for the OpenAI key exists, it wins         over the]] - rationale - chatbot/test_main.py
- [[_check_rate_limit()]] - code - chatbot/main.py
- [[_get_auth_token()]] - code - chatbot/main.py
- [[app()]] - code - chatbot/test_main.py
- [[chat()]] - code - chatbot/main.py
- [[client()]] - code - chatbot/test_main.py
- [[health_check()]] - code - chatbot/main.py
- [[lifespan()]] - code - chatbot/main.py
- [[load_persona_files()]] - code - chatbot/main.py
- [[main.py]] - code - chatbot/main.py
- [[require_auth()]] - code - chatbot/main.py
- [[test_main.py]] - code - chatbot/test_main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_83
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 109]]
- 2 edges to [[_COMMUNITY_Community 18]]

## Top bridge nodes
- [[ChatRequest]] - degree 3, connects to 1 community
- [[ChatResponse]] - degree 3, connects to 1 community
- [[.test_internal_error_not_leaked()]] - degree 3, connects to 1 community
- [[.test_openai_auth_error_returns_503()]] - degree 3, connects to 1 community
- [[.test_chat_success_returns_parsed_response()]] - degree 3, connects to 1 community