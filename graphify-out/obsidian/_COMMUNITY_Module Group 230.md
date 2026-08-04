---
type: community
cohesion: 0.14
members: 20
---

# Module Group 230

**Cohesion:** 0.14 - loosely connected
**Members:** 20 nodes

## Members
- [[.test_allowed_path_different_item()]] - code - gateway/tests/test_op_proxy.py
- [[.test_allowed_path_passes()]] - code - gateway/tests/test_op_proxy.py
- [[.test_allowed_path_without_space_variant()]] - code - gateway/tests/test_op_proxy.py
- [[.test_disallowed_vault_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_disallowed_vault_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[.test_empty_reference_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_malformed_reference_returns_422()]] - code - gateway/tests/test_op_proxy.py
- [[.test_missing_op_prefix_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_op_subprocess_failure_returns_502()]] - code - gateway/tests/test_op_proxy.py
- [[.test_path_traversal_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_path_traversal_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[.test_requires_auth()_3]] - code - gateway/tests/test_op_proxy.py
- [[.test_valid_reference_returns_value()]] - code - gateway/tests/test_op_proxy.py
- [[Endpoint returns 401 without auth override._2]] - rationale - gateway/tests/test_op_proxy.py
- [[Return True if the op reference matches an allowed path pattern.]] - rationale - gateway/ingest_api/main.py
- [[TestIsOpReferenceAllowed]] - code - gateway/tests/test_op_proxy.py
- [[TestOpProxyEndpoint]] - code - gateway/tests/test_op_proxy.py
- [[_is_op_reference_allowed()]] - code - gateway/ingest_api/main.py
- [[client()_9]] - code - gateway/tests/test_op_proxy.py
- [[test_op_proxy.py]] - code - gateway/tests/test_op_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_230
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]

## Top bridge nodes
- [[_is_op_reference_allowed()]] - degree 11, connects to 1 community
- [[test_op_proxy.py]] - degree 5, connects to 1 community
