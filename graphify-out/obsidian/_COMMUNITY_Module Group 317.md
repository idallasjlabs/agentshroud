---
type: community
cohesion: 0.17
members: 13
---

# Module Group 317

**Cohesion:** 0.17 - loosely connected
**Members:** 13 nodes

## Members
- [[.test_backslash_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_dotdot_path_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_encoded_traversal_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_mixed_case_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_proxy_returns_400_on_traversal()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_proxy_returns_400_on_traversal_in_query()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_safe_path_passes()]] - code - gateway/tests/test_main_endpoints.py
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[TestHermesDashboardPathTraversal]] - code - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy must reject traversal sequences before forwarding.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in path.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in query string.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_317
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 235]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]

## Top bridge nodes
- [[hermes_dashboard_proxy()]] - degree 7, connects to 3 communities
- [[TestHermesDashboardPathTraversal]] - degree 11, connects to 2 communities