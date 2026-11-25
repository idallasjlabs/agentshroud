---
type: community
members: 76
---

# fastapi.md

**Members:** 76 nodes

## Members
- [[dot-test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[Approval system routes. Human approval system endpoints - approve - Submit…]] - rationale - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired]] - code
- [[AuthRequired_1]] - code
- [[Create authentication dependency callable This is a synchronous wrapper that…]] - rationale - gateway/ingest_api/auth.py
- [[Detailed health check endpoint — authentication required. Returns full system…]] - rationale - gateway/ingest_api/routes/health.py
- [[Factory that returns authentication dependency for FastAPI This allows us to…]] - rationale - gateway/ingest_api/auth.py
- [[FastAPI_2]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[Health check endpoint for the AgentShroud Gateway]] - rationale - gateway/ingest_api/routes/health.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[Key FastAPI Features Used]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[List all pending approval requests Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Minimal health check endpoint — no authentication required. Returns only basic…]] - rationale - gateway/ingest_api/routes/health.py
- [[Purpose_44]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[Related Notes_10]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[Request_1]] - code
- [[Request_2]] - code
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Submit an action for human approval Called by agents when attempting sensitive…]] - rationale - gateway/ingest_api/routes/approval.py
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with invalid token]] - rationale - gateway/tests/test_auth.py
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
- [[Test token verification with invalid token]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[TestEnhancedStatus]] - code - gateway/tests/test_enhanced_status.py
- [[Tests for authentication and rate limiting]] - rationale - gateway/tests/test_auth.py
- [[Verify token using constant-time comparison Uses hmac.compare_digest to prevent…]] - rationale - gateway/ingest_api/auth.py
- [[Where Used]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[asyncio_6]] - code
- [[auth_check()]] - code - gateway/ingest_api/auth.py
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_2]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[dependency()]] - code - gateway/ingest_api/auth.py
- [[fastapi_1]] - document - docs/vault/05 - Dependencies/fastapi.md
- [[get_1]] - code
- [[get_2]] - code
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[ingest_apiauth.py]] - code - gateway/ingest_api/auth.py
- [[list_pending_approvals()_1]] - code - gateway/ingest_api/routes/approval.py
- [[post_1]] - code
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_enhanced_status.py]] - code - gateway/tests/test_enhanced_status.py
- [[test_rate_limiter_allows_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_blocks_excess_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_separate_clients()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_window_cleanup()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_constant_time()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_invalid()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_valid()]] - code - gateway/tests/test_auth.py
- [[verify_token()]] - code - gateway/ingest_api/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/fastapimd
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_ingest_apimain.py]]
- 11 edges to [[_COMMUNITY_AgentTarget]]
- 7 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 6 edges to [[_COMMUNITY_RateLimiter]]
- 4 edges to [[_COMMUNITY_test_security.py]]
- 3 edges to [[_COMMUNITY_app]]
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY_test_runtime_engines.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_EdgeOAuthService]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY__coerce_to_ws_event]]
- 1 edge to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_test_edge_fuzz.py]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]
- 1 edge to [[_COMMUNITY_test_intel_endpoint.py]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_dot-from_source]]
- 1 edge to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY__engine]]
- 1 edge to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_installer.py]]
- 1 edge to [[_COMMUNITY_management.py]]

## Top bridge nodes
- [[fastapi_1]] - degree 32, connects to 24 communities
- [[ingest_apiauth.py]] - degree 15, connects to 6 communities
- [[approval.py]] - degree 18, connects to 5 communities
- [[health.py]] - degree 13, connects to 5 communities
- [[create_auth_dependency()]] - degree 19, connects to 4 communities
