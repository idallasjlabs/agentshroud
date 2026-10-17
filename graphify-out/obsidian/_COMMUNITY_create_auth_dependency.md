---
type: community
members: 71
---

# create_auth_dependency

**Members:** 71 nodes

## Members
- [[dot-__init__()_184]] - code - gateway/ingest_api/auth.py
- [[dot-check()_6]] - code - gateway/ingest_api/auth.py
- [[dot-test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[Args             max_requests Maximum requests allowed in the time window]] - rationale - gateway/ingest_api/auth.py
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/health.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Detailed health check endpoint — authentication required.      Returns full syst]] - rationale - gateway/ingest_api/routes/health.py
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[GatewayConfig_4]] - code - gateway/ingest_api/auth.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Minimal health check endpoint — no authentication required.      Returns only ba]] - rationale - gateway/ingest_api/routes/health.py
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[RateLimiter_1]] - code - gateway/ingest_api/auth.py
- [[Related Notes_60]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Request_6]] - code - gateway/ingest_api/routes/health.py
- [[Simple token-bucket rate limiter      Limits requests per client IP to prevent r]] - rationale - gateway/ingest_api/auth.py
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with missing Authorization header]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with valid token]] - rationale - gateway/tests/test_auth.py
- [[Test enhanced status endpoint with observatory mode and egress info.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test rate limiter allows requests under limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter blocks requests over limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter cleans up old requests]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter tracks clients separately]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiting behavior]] - rationale - gateway/tests/test_security.py
- [[Test status response in monitor mode.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that StatusResponse model accepts new fields.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that new fields are optional (backward compat).]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that token verification uses constant-time comparison]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[TestEnhancedStatus]] - code - gateway/tests/test_enhanced_status.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[Verify token using constant-time comparison      Uses hmac.compare_digest to pre]] - rationale - gateway/ingest_api/auth.py
- [[auth.py_1]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[gatewayREADME]] - document - gateway/README.md
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[ingest_apiauth.py]] - code - gateway/ingest_api/auth.py
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_enhanced_status.py]] - code - gateway/tests/test_enhanced_status.py
- [[test_rate_limiter()]] - code - gateway/tests/test_security.py
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
- 9 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 5 edges to [[_COMMUNITY_AgentTarget (2)]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 3 edges to [[_COMMUNITY_create_auth_dependency (2)]]
- 3 edges to [[_COMMUNITY_create_auth_dependency (3)]]
- 3 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py (3)]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_Error Index.md (4)]]
- 1 edge to [[_COMMUNITY_`SecurityPipeline`]]
- 1 edge to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_Features]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_get_engine]]
- 1 edge to [[_COMMUNITY_main.py_1]]

## Top bridge nodes
- [[gatewayREADME]] - degree 11, connects to 7 communities
- [[RateLimiter_1]] - degree 18, connects to 6 communities
- [[ingest_apiauth.py]] - degree 12, connects to 6 communities
- [[auth.py_1]] - degree 10, connects to 5 communities
- [[create_auth_dependency()]] - degree 18, connects to 3 communities
