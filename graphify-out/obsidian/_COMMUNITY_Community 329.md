---
type: community
cohesion: 0.08
members: 26
---

# Community 329

**Cohesion:** 0.08 - loosely connected
**Members:** 26 nodes

## Members
- [[AsyncClient]] - code - gateway/proxy/collaborator_greeter.py
- [[Forward content → PII sanitized → ledger entry created → event bus fired.]] - rationale - gateway/tests/test_e2e.py
- [[Forward without auth returns 401403.]] - rationale - gateway/tests/test_e2e.py
- [[Fully initialized async client with lifespan.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboard with valid cookie auth returns HTML.]] - rationale - gateway/tests/test_e2e.py
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
TABLE source_file, type FROM #community/Community_329
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 65]]
- 2 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 2 edges to [[_COMMUNITY_Community 181]]
- 1 edge to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_Community 104]]
- 1 edge to [[_COMMUNITY_Community 116]]
- 1 edge to [[_COMMUNITY_Proxy Sidecar & Forwarder]]
- 1 edge to [[_COMMUNITY_SOC Auth & Audit Store]]
- 1 edge to [[_COMMUNITY_Community 386]]
- 1 edge to [[_COMMUNITY_Approval Queue (WebSocket)]]

## Top bridge nodes
- [[test_e2e.py]] - degree 13, connects to 5 communities
- [[AsyncClient]] - degree 10, connects to 1 community
- [[client()_5]] - degree 2, connects to 1 community
- [[client()_6]] - degree 2, connects to 1 community
- [[test_dashboard_serves_html()]] - degree 2, connects to 1 community