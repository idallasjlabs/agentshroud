---
type: community
members: 53
---

# lifespan()

**Members:** 53 nodes

## Members
- [[dot-check()_2]] - code - gateway/ingest_api/auth.py
- [[ApprovalDecision]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/health.py
- [[AuthRequired]] - code - gateway/ingest_api/routes/approval.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/dashboard.py
- [[Build compact egress dashboard snapshot for websocketAPI clients.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[GatewayConfig]] - code - gateway/ingest_api/auth.py
- [[JSON stats for dashboard]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Minimal health check endpoint — no authentication required.      Returns only ba]] - rationale - gateway/ingest_api/routes/health.py
- [[Request_1]] - code - gateway/ingest_api/routes/approval.py
- [[Request_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[Request_3]] - code - gateway/ingest_api/routes/health.py
- [[Return a short-lived WS-only auth token for cookie-authenticated sessions.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
- [[Validate a WebSocket token (single-use, time-limited).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket]] - code - gateway/ingest_api/routes/approval.py
- [[WebSocket_1]] - code - gateway/ingest_api/routes/dashboard.py
- [[WebSocket endpoint for real-time approval notifications      Protocol     1. Cl]] - rationale - gateway/ingest_api/routes/approval.py
- [[WebSocket for real-time activity feed]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket stream specialized for egresssecurity dashboard updates.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[_build_egress_live_snapshot()]] - code - gateway/ingest_api/routes/dashboard.py
- [[_validate_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[activity_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[approval_websocket()]] - code - gateway/ingest_api/routes/approval.py
- [[auth.py]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_2]] - code - gateway/ingest_api/routes/dashboard.py
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/health.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[dashboard.py]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_stats()]] - code - gateway/ingest_api/routes/dashboard.py
- [[dashboard_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[egress_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[event_bus.py]] - code - gateway/ingest_api/event_bus.py
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[health.py]] - code - gateway/ingest_api/routes/health.py
- [[health_check()]] - code - gateway/ingest_api/routes/health.py
- [[ingest_apiauth.py]] - code - gateway/ingest_api/auth.py
- [[list_pending_approvals()]] - code - gateway/ingest_api/routes/approval.py
- [[python-jose_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py
- [[test_build_egress_live_snapshot_enriches_pending_metrics()]] - code - gateway/tests/test_dashboard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/lifespan
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 10 edges to [[_COMMUNITY__make_proxy()]]
- 8 edges to [[_COMMUNITY_lifespan() (2)]]
- 8 edges to [[_COMMUNITY_TestOutboundInfoFilter (2)_1]]
- 4 edges to [[_COMMUNITY_MCPPermissionManager]]
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py (3)]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 2 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_test_fieldflare_route_strips_unsupported_fields_streaming]]
- 1 edge to [[_COMMUNITY_lifespan() (3)]]
- 1 edge to [[_COMMUNITY_GroupConfig]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_TestPatternDetection]]
- 1 edge to [[_COMMUNITY_pick_latest_stable]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3)]]
- 1 edge to [[_COMMUNITY_Workflow (follow in order)]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_test_gemini_openai_translator.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (4)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (7)]]

## Top bridge nodes
- [[ingest_apiauth.py]] - degree 12, connects to 6 communities
- [[auth.py]] - degree 10, connects to 6 communities
- [[dashboard.py]] - degree 22, connects to 5 communities
- [[approval.py]] - degree 15, connects to 4 communities
- [[create_auth_dependency()]] - degree 18, connects to 3 communities
