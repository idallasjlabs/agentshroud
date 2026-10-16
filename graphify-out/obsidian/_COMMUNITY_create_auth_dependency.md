---
type: community
cohesion: 0.03
members: 102
---

# create_auth_dependency

**Cohesion:** 0.03 - loosely connected
**Members:** 102 nodes

## Members
- [[dot-__init__()_173]] - code - gateway/ingest_api/ledger.py
- [[dot-check()_6]] - code - gateway/ingest_api/auth.py
- [[dot-get_entry()]] - code - gateway/ingest_api/ledger.py
- [[dot-get_stats()_17]] - code - gateway/ingest_api/ledger.py
- [[dot-query()]] - code - gateway/ingest_api/ledger.py
- [[dot-test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[Any_69]] - code - gateway/ingest_api/ledger.py
- [[ApprovalDecision_1]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest_3]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth Methods]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._3]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/approval.py
- [[AuthRequired_4]] - code - gateway/ingest_api/routes/health.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Current Usage]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Detailed health check endpoint — authentication required.      Returns full syst]] - rationale - gateway/ingest_api/routes/health.py
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[Fetch a single ledger entry by ID          Args             entry_id Entry UUI]] - rationale - gateway/ingest_api/ledger.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[GatewayConfig_4]] - code - gateway/ingest_api/auth.py
- [[Get aggregate statistics          Returns             Dictionary with total ent]] - rationale - gateway/ingest_api/ledger.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[Key Features_2]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[LedgerConfig_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerEntry]] - code - gateway/ingest_api/models.py
- [[LedgerEntry_1]] - code - gateway/ingest_api/ledger.py
- [[LedgerQueryResponse]] - code - gateway/ingest_api/models.py
- [[LedgerQueryResponse_1]] - code - gateway/ingest_api/ledger.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Minimal health check endpoint — no authentication required.      Returns only ba]] - rationale - gateway/ingest_api/routes/health.py
- [[Paginated ledger query results]] - rationale - gateway/ingest_api/models.py
- [[Purpose_157]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Query ledger entries with pagination and filters          Args             page]] - rationale - gateway/ingest_api/ledger.py
- [[Related Notes_60]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Related Notes_61]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Request_8]] - code - gateway/ingest_api/routes/approval.py
- [[Request_9]] - code - gateway/ingest_api/routes/health.py
- [[Security Note_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Single entry from the data ledger]] - rationale - gateway/ingest_api/models.py
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Store configuration          Actual database connection created in initialize().]] - rationale - gateway/ingest_api/ledger.py
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
- [[auth.py]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_4]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[event_bus.py_1]] - code - gateway/ingest_api/event_bus.py
- [[gatewayREADME]] - document - gateway/README.md
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()]] - code - gateway/ingest_api/routes/health.py
- [[health_check_detail()]] - code - gateway/ingest_api/routes/health.py
- [[ingest_apiauth.py]] - code - gateway/ingest_api/auth.py
- [[ingest_apimodels.py]] - code - gateway/ingest_api/models.py
- [[ledger.py_1]] - code - gateway/ingest_api/ledger.py
- [[list_pending_approvals()_1]] - code - gateway/ingest_api/routes/approval.py
- [[python-jose_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[python-jose]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[state.py]] - code - gateway/ingest_api/state.py
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
- 16 edges to [[_COMMUNITY_PIIConfig]]
- 11 edges to [[_COMMUNITY_test_dashboard.py]]
- 10 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 8 edges to [[_COMMUNITY_test_forward_stream.py]]
- 8 edges to [[_COMMUNITY_RateLimiter]]
- 7 edges to [[_COMMUNITY_AgentTarget_1]]
- 6 edges to [[_COMMUNITY__FakeRBAC]]
- 5 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 4 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 3 edges to [[_COMMUNITY_make_event]]
- 3 edges to [[_COMMUNITY_test_security.py]]
- 2 edges to [[_COMMUNITY_Request]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_Restart Procedure]]
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 2 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 2 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_3]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_All Dependencies_1]]
- 1 edge to [[_COMMUNITY_TestPathIsolationManager_5]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_1]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY__wrap_response]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_Features]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_UserSessionManager_3]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_`SecurityPipeline`]]
- 1 edge to [[_COMMUNITY_get_engine]]
- 1 edge to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_main.py]]

## Top bridge nodes
- [[state.py]] - degree 36, connects to 20 communities
- [[ingest_apimodels.py]] - degree 27, connects to 11 communities
- [[gatewayREADME]] - degree 11, connects to 7 communities
- [[ingest_apiauth.py]] - degree 12, connects to 5 communities
- [[auth.py]] - degree 10, connects to 5 communities
