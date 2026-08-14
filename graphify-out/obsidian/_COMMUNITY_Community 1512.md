---
type: community
members: 3
---

# Community 1512

**Members:** 3 nodes

## Members
- [[.test_bots_inventory_matches_the_real_container_name()]] - code - gateway/tests/test_main_endpoints.py
- [[TestHealthCheckDetailBotsInventory]] - code - gateway/tests/test_main_endpoints.py
- [[health_check_detail's per-bot inventory must key the Docker lookup by     each b]] - rationale - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1512
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Egress & RBAC Security Core]]
- 1 edge to [[_COMMUNITY_PII Sanitizer Pipeline]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]

## Top bridge nodes
- [[TestHealthCheckDetailBotsInventory]] - degree 4, connects to 2 communities
- [[.test_bots_inventory_matches_the_real_container_name()]] - degree 2, connects to 1 community