---
type: community
members: 8
---

# Migration Path (SSH → Distributed Node)

**Members:** 8 nodes

## Members
- [[dot-test_empty()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_keeps_last_n_lines()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_only_newlines()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_shorter_than_n()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_strips_trailing_newline()]] - code - gateway/tests/test_multi_host_test.py
- [[Return the last ``lines`` non-trailing-empty lines of ``text``.]] - rationale - gateway/tools/multi_host_test.py
- [[TestTail]] - code - gateway/tests/test_multi_host_test.py
- [[tail()]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Migration_Path_SSH__Distributed_Node
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_VIII. Evaluation]]
- 2 edges to [[_COMMUNITY_parse_trivy_output]]
- 1 edge to [[_COMMUNITY_Docker Compose (infra diagram)]]
- 1 edge to [[_COMMUNITY_LOW Findings]]
- 1 edge to [[_COMMUNITY_AgentShroud (system, C4 context) (3)]]

## Top bridge nodes
- [[TestTail]] - degree 9, connects to 3 communities
- [[tail()]] - degree 9, connects to 3 communities
