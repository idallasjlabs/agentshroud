---
type: community
members: 6
---

# Community 2133

**Members:** 6 nodes

## Members
- [[._json_resp()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_403_without_token_still_raises()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_other_http_errors_are_not_retried()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[.test_token_refused_retries_public_endpoint_without_token()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestFetch]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[aquasecuritytrivy 403s the Actions token but serves the public feed.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2133
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 55]]
- 1 edge to [[_COMMUNITY_Community 1342]]
- 1 edge to [[_COMMUNITY_Community 480]]

## Top bridge nodes
- [[TestFetch]] - degree 6, connects to 2 communities
- [[.test_token_refused_retries_public_endpoint_without_token()]] - degree 3, connects to 1 community
- [[._json_resp()]] - degree 2, connects to 1 community
- [[.test_403_without_token_still_raises()]] - degree 2, connects to 1 community
- [[.test_other_http_errors_are_not_retried()]] - degree 2, connects to 1 community