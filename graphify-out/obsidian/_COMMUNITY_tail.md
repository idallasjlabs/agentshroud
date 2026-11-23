---
type: community
members: 8
---

# tail

**Members:** 8 nodes

## Members
- [[dot-test_empty()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_keeps_last_n_lines()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_only_newlines()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_shorter_than_n()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_strips_trailing_newline()_1]] - code - gateway/tests/test_multi_host_test.py
- [[Return the last ``lines`` non-trailing-empty lines of ``text``.]] - rationale - gateway/tools/multi_host_test.py
- [[TestTail]] - code - gateway/tests/test_multi_host_test.py
- [[tail()]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/tail
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 1 edge to [[_COMMUNITY_run_multi_host]]
- 1 edge to [[_COMMUNITY_multi_host_test.py]]

## Top bridge nodes
- [[tail()]] - degree 9, connects to 3 communities
- [[TestTail]] - degree 6, connects to 1 community
