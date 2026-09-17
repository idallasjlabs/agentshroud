---
type: community
cohesion: 0.27
members: 12
---

# _is_op_reference_allowed()

**Cohesion:** 0.27 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_allowed_path_different_item()]] - code - gateway/tests/test_op_proxy.py
- [[.test_allowed_path_passes()]] - code - gateway/tests/test_op_proxy.py
- [[.test_allowed_path_without_space_variant()]] - code - gateway/tests/test_op_proxy.py
- [[.test_atlassian_token_allowed()]] - code - gateway/tests/test_op_proxy.py
- [[.test_disallowed_vault_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_empty_reference_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_missing_op_prefix_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[.test_path_traversal_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[Return True if the op reference matches an allowed path pattern.]] - rationale - gateway/ingest_api/main.py
- [[SCRUM-81 Hermes weekly Jira review needs tokenemaildomain fields.]] - rationale - gateway/tests/test_op_proxy.py
- [[TestIsOpReferenceAllowed]] - code - gateway/tests/test_op_proxy.py
- [[_is_op_reference_allowed()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_is_op_reference_allowed
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[_is_op_reference_allowed()]] - degree 12, connects to 1 community
- [[TestIsOpReferenceAllowed]] - degree 9, connects to 1 community