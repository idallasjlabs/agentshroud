---
type: community
cohesion: 0.12
members: 17
---

# Module Group 272

**Cohesion:** 0.12 - loosely connected
**Members:** 17 nodes

## Members
- [[Forward content → PII sanitized → ledger entry created → event bus fired.]] - rationale - gateway/tests/test_e2e.py
- [[Forward without auth returns 401403.]] - rationale - gateway/tests/test_e2e.py
- [[Fully initialized async client with lifespan.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboard with valid cookie auth returns HTML.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboard without auth returns 403.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboardstats returns JSON stats.]] - rationale - gateway/tests/test_e2e.py
- [[GET status returns service info.]] - rationale - gateway/tests/test_e2e.py
- [[Submit SSH command → approval queued.]] - rationale - gateway/tests/test_e2e.py
- [[client()_4]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_requires_auth()_1]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_returns_html()]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_stats_returns_json()]] - code - gateway/tests/test_e2e.py
- [[test_e2e.py]] - code - gateway/tests/test_e2e.py
- [[test_forward_pii_sanitized_and_ledger_entry()]] - code - gateway/tests/test_e2e.py
- [[test_forward_without_auth_rejected()]] - code - gateway/tests/test_e2e.py
- [[test_ssh_submit_queues_approval()]] - code - gateway/tests/test_e2e.py
- [[test_status_endpoint()]] - code - gateway/tests/test_e2e.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_272
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 311]]
- 1 edge to [[_COMMUNITY_RBAC Configuration]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]

## Top bridge nodes
- [[test_e2e.py]] - degree 11, connects to 3 communities
- [[client()_4]] - degree 3, connects to 1 community
