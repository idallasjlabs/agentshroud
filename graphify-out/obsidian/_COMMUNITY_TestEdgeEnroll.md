---
type: community
members: 8
---

# TestEdgeEnroll

**Members:** 8 nodes

## Members
- [[dot-test_confirm_required()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_disabled_edge_is_503()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_killed_vendor_cannot_enroll()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_owner_only()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_returns_working_code_once_and_never_logs_it()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_ttl_capped_at_900()]] - code - gateway/tests/test_soc_edge.py
- [[dot-test_vendor_must_exist_and_be_enabled()]] - code - gateway/tests/test_soc_edge.py
- [[TestEdgeEnroll]] - code - gateway/tests/test_soc_edge.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEdgeEnroll
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_TestEdgeKill]]

## Top bridge nodes
- [[TestEdgeEnroll]] - degree 8, connects to 1 community
- [[dot-test_owner_only()]] - degree 2, connects to 1 community
