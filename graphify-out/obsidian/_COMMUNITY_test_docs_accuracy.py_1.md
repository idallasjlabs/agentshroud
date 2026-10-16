---
type: community
cohesion: 0.25
members: 8
---

# test_docs_accuracy.py

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_all_module_attrs_exist_after_init()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_endpoint_reports_no_key_collisions_and_high_total()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_manage_modules_endpoint_uses_the_same_registry()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_readme_p1_count_matches_middleware_manager()]] - code - gateway/tests/test_docs_accuracy.py
- [[Execute the real endpoint against a fully-populated app_state and         verify]] - rationale - gateway/tests/test_docs_accuracy.py
- [[TestManageModulesEndpointAccuracy]] - code - gateway/tests/test_docs_accuracy.py
- [[The endpoint's P1 section must be generated from ALL_MODULE_ATTRS,         not a]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Verify managemodules enumerates every module MiddlewareManager wires.      Mid]] - rationale - gateway/tests/test_docs_accuracy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_docs_accuracypy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_test_docs_accuracy.py]]
- 1 edge to [[_COMMUNITY_PIIConfig]]

## Top bridge nodes
- [[TestManageModulesEndpointAccuracy]] - degree 8, connects to 3 communities
- [[dot-test_endpoint_reports_no_key_collisions_and_high_total()]] - degree 3, connects to 1 community
- [[dot-test_all_module_attrs_exist_after_init()]] - degree 2, connects to 1 community
- [[dot-test_readme_p1_count_matches_middleware_manager()]] - degree 2, connects to 1 community
