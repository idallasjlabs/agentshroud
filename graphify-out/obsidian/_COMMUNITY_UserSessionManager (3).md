---
type: community
cohesion: 0.07
members: 28
---

# UserSessionManager (3)

**Cohesion:** 0.07 - loosely connected
**Members:** 28 nodes

## Members
- [[dot-test_dashboard_cookie_auth_serves_html()]] - code - gateway/tests/test_security_fixes.py
- [[AsyncClient]] - code - gateway/proxy/collaborator_greeter.py
- [[Forward content → PII sanitized → ledger entry created → event bus fired.]] - rationale - gateway/tests/test_e2e.py
- [[Forward without auth returns 401403.]] - rationale - gateway/tests/test_e2e.py
- [[Fully initialized async client with lifespan.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboard with valid cookie auth returns HTML.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboard with valid cookie serves HTML]] - rationale - gateway/tests/test_security_fixes.py
- [[GET dashboard without auth returns 403.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboardstats returns JSON stats.]] - rationale - gateway/tests/test_e2e.py
- [[GET status returns service info.]] - rationale - gateway/tests/test_e2e.py
- [[Submit SSH command → approval queued.]] - rationale - gateway/tests/test_e2e.py
- [[client()_5]] - code - gateway/tests/test_dashboard.py
- [[client()_6]] - code - gateway/tests/test_dashboard_endpoints.py
- [[client()_7]] - code - gateway/tests/test_e2e.py
- [[client()_8]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[client()_9]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[client()_10]] - code - gateway/tests/test_security_fixes.py
- [[client()_11]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[client()_12]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_dashboard_requires_auth()]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_returns_html()]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_serves_html()]] - code - gateway/tests/test_dashboard.py
- [[test_dashboard_stats_returns_json()]] - code - gateway/tests/test_e2e.py
- [[test_e2e.py]] - code - gateway/tests/test_e2e.py
- [[test_forward_pii_sanitized_and_ledger_entry()]] - code - gateway/tests/test_e2e.py
- [[test_forward_without_auth_rejected()]] - code - gateway/tests/test_e2e.py
- [[test_ssh_submit_queues_approval()]] - code - gateway/tests/test_e2e.py
- [[test_status_endpoint()]] - code - gateway/tests/test_e2e.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager_3
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 2 edges to [[_COMMUNITY_export-bot-conversations.py (2)]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager (2)]]
- 2 edges to [[_COMMUNITY_TestOutboundInfoFilter (2)]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Value Proposition]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[test_e2e.py]] - degree 13, connects to 5 communities
- [[AsyncClient]] - degree 10, connects to 1 community
- [[dot-test_dashboard_cookie_auth_serves_html()]] - degree 3, connects to 1 community
- [[client()_5]] - degree 2, connects to 1 community
- [[client()_6]] - degree 2, connects to 1 community
