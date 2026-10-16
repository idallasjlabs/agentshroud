---
type: community
cohesion: 0.04
members: 66
---

# create_auth_dependency

**Cohesion:** 0.04 - loosely connected
**Members:** 66 nodes

## Members
- [[dot-check()_5]] - code - gateway/ingest_api/auth.py
- [[dot-test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[ApprovalDecision_1]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest_3]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._3]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/approval.py
- [[AuthRequired_4]] - code - gateway/ingest_api/routes/health.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Detailed health check endpoint — authentication required.      Returns full syst]] - rationale - gateway/ingest_api/routes/health.py
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[GatewayConfig_4]] - code - gateway/ingest_api/auth.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Minimal health check endpoint — no authentication required.      Returns only ba]] - rationale - gateway/ingest_api/routes/health.py
- [[Request_7]] - code - gateway/ingest_api/routes/approval.py
- [[Request_8]] - code - gateway/ingest_api/routes/health.py
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
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
- [[Verify token using constant-time comparison      Uses hmac.compare_digest to pre]] - rationale - gateway/ingest_api/auth.py
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[auth.py_1]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_4]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[ingest_apiauth.py]] - code - gateway/ingest_api/auth.py
- [[list_pending_approvals()_1]] - code - gateway/ingest_api/routes/approval.py
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
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
TABLE source_file, type FROM #community/create_auth_dependency
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_RateLimiter]]
- 6 edges to [[_COMMUNITY_DataLedger]]
- 4 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 4 edges to [[_COMMUNITY_make_event]]
- 3 edges to [[_COMMUNITY_test_security.py]]
- 3 edges to [[_COMMUNITY_forward.py]]
- 3 edges to [[_COMMUNITY_test_dashboard.py]]
- 2 edges to [[_COMMUNITY_activity_websocket]]
- 2 edges to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_Request]]
- 1 edge to [[_COMMUNITY_ApprovalQueueItem]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_load_config]]
- 1 edge to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_get_engine]]
- 1 edge to [[_COMMUNITY_python-jose]]

## Top bridge nodes
- [[approval.py]] - degree 15, connects to 7 communities
- [[ingest_apiauth.py]] - degree 12, connects to 7 communities
- [[auth.py_1]] - degree 10, connects to 6 communities
- [[verify_token()]] - degree 13, connects to 3 communities
- [[health.py]] - degree 9, connects to 3 communities
