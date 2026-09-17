---
type: community
cohesion: 0.39
members: 8
---

# TestTail

**Cohesion:** 0.39 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_empty()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_keeps_last_n_lines()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_only_newlines()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_shorter_than_n()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_strips_trailing_newline()]] - code - gateway/tests/test_multi_host_test.py
- [[Return the last ``lines`` non-trailing-empty lines of ``text``.]] - rationale - gateway/tools/multi_host_test.py
- [[TestTail]] - code - gateway/tests/test_multi_host_test.py
- [[tail()]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTail
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_MultiHostResult]]
- 1 edge to [[_COMMUNITY_HostStatus]]
- 1 edge to [[_COMMUNITY_multi_host_test.py]]
- 1 edge to [[_COMMUNITY_run_multi_host()]]

## Top bridge nodes
- [[TestTail]] - degree 9, connects to 3 communities
- [[tail()]] - degree 9, connects to 3 communities