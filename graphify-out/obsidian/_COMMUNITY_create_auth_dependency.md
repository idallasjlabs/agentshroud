---
type: community
members: 47
---

# create_auth_dependency

**Members:** 47 nodes

## Members
- [[dot-check()_2]] - code - gateway/ingest_api/auth.py
- [[Auth Methods]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/health.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Current Usage]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[GatewayConfig_1]] - code - gateway/ingest_api/auth.py
- [[Key Features_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Purpose_65]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Related Notes_22]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Request_1]] - code - gateway/ingest_api/routes/health.py
- [[Security Note]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with missing Authorization header]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with valid token]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter allows requests under limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter blocks requests over limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter cleans up old requests]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter tracks clients separately]] - rationale - gateway/tests/test_auth.py
- [[Test that token verification uses constant-time comparison]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[Verify token using constant-time comparison      Uses hmac.compare_digest to pre]] - rationale - gateway/ingest_api/auth.py
- [[auth.py]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[python-jose_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[python-jose]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_rate_limiter_allows_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_blocks_excess_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_separate_clients()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_window_cleanup()]] - code - gateway/tests/test_auth.py
- [[test_timing_attack_resistance()]] - code - gateway/tests/test_security.py
- [[test_verify_token_constant_time()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_invalid()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_valid()]] - code - gateway/tests/test_auth.py
- [[verify_token()]] - code - gateway/ingest_api/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/create_auth_dependency
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_telegram_proxy.py]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 3 edges to [[_COMMUNITY_test_security.py]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py (2)]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_create_auth_dependency (3)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_Error Index]]

## Top bridge nodes
- [[create_auth_dependency()]] - degree 18, connects to 5 communities
- [[auth.py]] - degree 10, connects to 5 communities
- [[verify_token()]] - degree 13, connects to 4 communities
- [[get_auth_dependency()]] - degree 8, connects to 2 communities
- [[test_auth.py]] - degree 14, connects to 1 community
