---
type: community
cohesion: 0.04
members: 65
---

# Auth

**Cohesion:** 0.04 - loosely connected
**Members:** 65 nodes

## Members
- [[.check()]] - code - gateway/ingest_api/auth.py
- [[.test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[.test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[.test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[Auth Methods]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Auth dependency that uses the app state config._3]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired_4]] - code - gateway/ingest_api/routes/health.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Current Usage]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Detailed health check endpoint — authentication required.      Returns full syst]] - rationale - gateway/ingest_api/routes/health.py
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[GatewayConfig]] - code - gateway/ingest_api/auth.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[Key Features_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Minimal health check endpoint — no authentication required.      Returns only ba]] - rationale - gateway/ingest_api/routes/health.py
- [[Purpose_193]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Related Notes_48]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Request_5]] - code - gateway/ingest_api/routes/health.py
- [[Security Note_2]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with missing Authorization header]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with valid token]] - rationale - gateway/tests/test_auth.py
- [[Test enhanced status endpoint with observatory mode and egress info.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test rate limiter allows requests under limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter blocks requests over limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter cleans up old requests]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter tracks clients separately]] - rationale - gateway/tests/test_auth.py
- [[Test status response in monitor mode.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that StatusResponse model accepts new fields.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that new fields are optional (backward compat).]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that token verification uses constant-time comparison]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[TestEnhancedStatus]] - code - gateway/tests/test_enhanced_status.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[Verify token using constant-time comparison      Uses hmac.compare_digest to pre]] - rationale - gateway/ingest_api/auth.py
- [[auth.py]] - code - gateway/ingest_api/auth.py
- [[auth.py_2]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_4]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()_1]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[python-jose_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[python-jose]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_enhanced_status.py]] - code - gateway/tests/test_enhanced_status.py
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
TABLE source_file, type FROM #community/Auth
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Telegram Proxy Inbound]]
- 5 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 4 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 3 edges to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 3 edges to [[_COMMUNITY_Soc Egress Endpoints]]
- 3 edges to [[_COMMUNITY_Dashboard]]
- 3 edges to [[_COMMUNITY_Forward (routes)]]
- 3 edges to [[_COMMUNITY_Config Validation & Router]]
- 2 edges to [[_COMMUNITY_Api (web)]]
- 1 edge to [[_COMMUNITY_Router (soc)]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_Dashboard Endpoints (web)]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Runtime Engines]]
- 1 edge to [[_COMMUNITY_Error index (07 - Errors & Troubleshooting)]]
- 1 edge to [[_COMMUNITY_Auth.py (Gateway Core)]]
- 1 edge to [[_COMMUNITY_System overview (00 - START HERE)]]
- 1 edge to [[_COMMUNITY_Ci Workflows (03 - Configuration)]]

## Top bridge nodes
- [[auth.py]] - degree 13, connects to 9 communities
- [[auth.py_2]] - degree 10, connects to 5 communities
- [[create_auth_dependency()]] - degree 20, connects to 4 communities
- [[health.py]] - degree 11, connects to 4 communities
- [[verify_token()]] - degree 13, connects to 3 communities