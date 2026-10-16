---
type: community
cohesion: 0.20
members: 12
---

# ._run_proxy()

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-_run_proxy()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_decoded_body_drops_upstream_encoding_and_recomputes_length()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_multiple_set_cookie_headers_are_not_folded()]] - code - gateway/tests/test_main_endpoints.py
- [[Set-Cookie folding in hermes_dashboard_proxy]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[TestHermesDashboardProxyHeaders]] - code - gateway/tests/test_main_endpoints.py
- [[__aenter__()]] - code - gateway/tests/test_main_endpoints.py
- [[__aexit__()]] - code - gateway/tests/test_main_endpoints.py
- [[__init__()]] - code - gateway/tests/test_main_endpoints.py
- [[_body()]] - code - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy must relay upstream headers header-by-header. Found on…]] - rationale - gateway/tests/test_main_endpoints.py
- [[multi_items()]] - code - gateway/tests/test_main_endpoints.py
- [[request()]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_run_proxy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 1 edge to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]

## Top bridge nodes
- [[Set-Cookie folding in hermes_dashboard_proxy]] - degree 3, connects to 2 communities
- [[TestHermesDashboardProxyHeaders]] - degree 7, connects to 1 community
