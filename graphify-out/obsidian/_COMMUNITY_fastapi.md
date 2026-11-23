---
type: community
members: 94
---

# fastapi.md

**Members:** 94 nodes

## Members
- [[dot-__init__()_189]] - code - gateway/ingest_api/auth.py
- [[dot-__init__()_190]] - code - gateway/proxy/telegram_proxy.py
- [[dot-check()_5]] - code - gateway/ingest_api/auth.py
- [[dot-test_collaborator_rate_limit_retry_after_seconds_uses_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Args max_requests Maximum requests allowed in the time window window_seconds…]] - rationale - gateway/ingest_api/auth.py
- [[Auth dependency that uses the app state config._3]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired_4]] - code
- [[Check if client is within rate limit Args client_id Usually client IP address…]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable This is a synchronous wrapper that…]] - rationale - gateway/ingest_api/auth.py
- [[Detailed health check endpoint — authentication required. Returns full system…]] - rationale - gateway/ingest_api/routes/health.py
- [[Factory that returns authentication dependency for FastAPI This allows us to…]] - rationale - gateway/ingest_api/auth.py
- [[FastAPI_4]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[Health check endpoint for the AgentShroud Gateway]] - rationale - gateway/ingest_api/routes/health.py
- [[Key FastAPI Features Used]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[Main Endpoints Integration Tests - P1 Middleware Wiring Tests for main.py…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Minimal health check endpoint — no authentication required. Returns only basic…]] - rationale - gateway/ingest_api/routes/health.py
- [[Purpose_173]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[RateLimiter_1]] - code - gateway/ingest_api/auth.py
- [[Read persisted paused-collaborator IDs from disk. Owner-initiated manual pause…]] - rationale - gateway/security/rbac_config.py
- [[Related Notes_70]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[Request_9]] - code
- [[Security and edge case tests for AgentShroud Gateway]] - rationale - gateway/tests/test_security.py
- [[Simple token-bucket rate limiter Limits requests per client IP to prevent…]] - rationale - gateway/ingest_api/auth.py
- [[Test PII detection with special characters nearby]] - rationale - gateway/tests/test_security.py
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with invalid token]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with missing Authorization header]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with valid token]] - rationale - gateway/tests/test_auth.py
- [[Test content with Unicode characters]] - rationale - gateway/tests/test_security.py
- [[Test content with multiple instances of same PII type]] - rationale - gateway/tests/test_security.py
- [[Test handling of extremely long content (10MB)]] - rationale - gateway/tests/test_security.py
- [[Test handling of malformed metadata]] - rationale - gateway/tests/test_security.py
- [[Test handling of null bytes (potential injection attack)]] - rationale - gateway/tests/test_security.py
- [[Test handling of very large content (1MB+)]] - rationale - gateway/tests/test_security.py
- [[Test overlapping or nested PII patterns]] - rationale - gateway/tests/test_security.py
- [[Test rate limiter allows requests under limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter blocks requests over limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter cleans up old requests]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter tracks clients separately]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiting behavior]] - rationale - gateway/tests/test_security.py
- [[Test that SQL injection is prevented]] - rationale - gateway/tests/test_security.py
- [[Test that XSS payloads are safely stored]] - rationale - gateway/tests/test_security.py
- [[Test that common false positives are handled]] - rationale - gateway/tests/test_security.py
- [[Test that token verification uses constant-time comparison]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with invalid token]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[Tests for authentication and rate limiting]] - rationale - gateway/tests/test_auth.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[Verify token using constant-time comparison Uses hmac.compare_digest to prevent…]] - rationale - gateway/ingest_api/auth.py
- [[Where Used_5]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[asyncio_74]] - code
- [[asyncio_75]] - code
- [[auth_check()]] - code - gateway/ingest_api/auth.py
- [[auth_dep()_4]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[dependency()]] - code - gateway/ingest_api/auth.py
- [[fastapi_3]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[get_8]] - code
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()_1]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[ingest_apiauth.py]] - code - gateway/ingest_api/auth.py
- [[load_paused_collaborator_ids()]] - code - gateway/security/rbac_config.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_extremely_long_content()]] - code - gateway/tests/test_security.py
- [[test_false_positive_patterns()]] - code - gateway/tests/test_security.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py
- [[test_malformed_json_metadata()]] - code - gateway/tests/test_security.py
- [[test_multiple_same_type_pii()]] - code - gateway/tests/test_security.py
- [[test_nested_pii_patterns()]] - code - gateway/tests/test_security.py
- [[test_null_bytes_in_content()]] - code - gateway/tests/test_security.py
- [[test_rate_limiter()]] - code - gateway/tests/test_security.py
- [[test_rate_limiter_allows_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_blocks_excess_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_separate_clients()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_window_cleanup()]] - code - gateway/tests/test_auth.py
- [[test_security.py]] - code - gateway/tests/test_security.py
- [[test_special_characters_in_pii()]] - code - gateway/tests/test_security.py
- [[test_sql_injection_attempt()]] - code - gateway/tests/test_security.py
- [[test_timing_attack_resistance()]] - code - gateway/tests/test_security.py
- [[test_unicode_content()]] - code - gateway/tests/test_security.py
- [[test_verify_token_constant_time()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_invalid()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_valid()]] - code - gateway/tests/test_auth.py
- [[test_very_large_content()]] - code - gateway/tests/test_security.py
- [[test_xss_attempt()]] - code - gateway/tests/test_security.py
- [[verify_token()]] - code - gateway/ingest_api/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/fastapimd
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_ingest_apimain.py]]
- 9 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 9 edges to [[_COMMUNITY_TestConfigValidation]]
- 8 edges to [[_COMMUNITY_app]]
- 5 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 4 edges to [[_COMMUNITY_hermes_dashboard_ws_proxy]]
- 4 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message]]
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_FakeRBAC]]
- 2 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py]]
- 2 edges to [[_COMMUNITY_test_web_api_coverage.py]]
- 2 edges to [[_COMMUNITY_socmodels.py]]
- 2 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 1 edge to [[_COMMUNITY_TestScanParameterAllowlists]]
- 1 edge to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 1 edge to [[_COMMUNITY_dot-test_mcp_proxy_endpoint]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_rate_limit_resets_after_window]]
- 1 edge to [[_COMMUNITY_fake_urlopen]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_rate_limit_notice_includes_retry_window]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY_ContributorManager]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_test_skill_guard.py]]
- 1 edge to [[_COMMUNITY_EdgeOAuthService]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_test_edge_fuzz.py]]
- 1 edge to [[_COMMUNITY_DraftEntry]]
- 1 edge to [[_COMMUNITY_dot-from_source]]
- 1 edge to [[_COMMUNITY_TestVersionRoutes]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_installer.py]]

## Top bridge nodes
- [[fastapi_3]] - degree 32, connects to 22 communities
- [[test_main_endpoints.py]] - degree 25, connects to 10 communities
- [[RateLimiter_1]] - degree 25, connects to 8 communities
- [[create_auth_dependency()]] - degree 19, connects to 4 communities
- [[ingest_apiauth.py]] - degree 15, connects to 4 communities
