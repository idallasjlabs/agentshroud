---
type: community
cohesion: 0.13
members: 22
---

# Op Proxy

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[.test_allowed_path_different_item()]] - code - gateway/tests/test_op_proxy.py
- [[.test_allowed_path_passes()]] - code - gateway/tests/test_op_proxy.py
- [[.test_allowed_path_without_space_variant()]] - code - gateway/tests/test_op_proxy.py
- [[.test_atlassian_token_allowed()]] - code - gateway/tests/test_op_proxy.py
- [[.test_disallowed_vault_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_disallowed_vault_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[.test_empty_reference_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_malformed_reference_returns_422()]] - code - gateway/tests/test_op_proxy.py
- [[.test_missing_op_prefix_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_op_subprocess_failure_returns_502()]] - code - gateway/tests/test_op_proxy.py
- [[.test_path_traversal_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_path_traversal_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[.test_requires_auth()_4]] - code - gateway/tests/test_op_proxy.py
- [[.test_valid_reference_returns_value()]] - code - gateway/tests/test_op_proxy.py
- [[Endpoint returns 401 without auth override._1]] - rationale - gateway/tests/test_op_proxy.py
- [[Return True if the op reference matches an allowed path pattern.]] - rationale - gateway/ingest_api/main.py
- [[SCRUM-81 Hermes weekly Jira review needs tokenemaildomain fields.]] - rationale - gateway/tests/test_op_proxy.py
- [[TestIsOpReferenceAllowed]] - code - gateway/tests/test_op_proxy.py
- [[TestOpProxyEndpoint]] - code - gateway/tests/test_op_proxy.py
- [[_is_op_reference_allowed()]] - code - gateway/ingest_api/main.py
- [[client()_12]] - code - gateway/tests/test_op_proxy.py
- [[test_op_proxy.py]] - code - gateway/tests/test_op_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Op_Proxy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Ingest API Main & Models]]

## Top bridge nodes
- [[_is_op_reference_allowed()]] - degree 12, connects to 1 community
- [[test_op_proxy.py]] - degree 6, connects to 1 community