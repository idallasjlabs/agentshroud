---
type: community
cohesion: 0.36
members: 8
---

# HostStatus

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_255_is_unreachable()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_nonzero_is_fail()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_zero_is_pass()]] - code - gateway/tests/test_multi_host_test.py
- [[HostStatus]] - code - gateway/tools/multi_host_test.py
- [[Map a runner exit code to a HostStatus.]] - rationale - gateway/tools/multi_host_test.py
- [[Outcome classification for a single host.]] - rationale - gateway/tools/multi_host_test.py
- [[TestClassify_1]] - code - gateway/tests/test_multi_host_test.py
- [[classify()_1]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HostStatus
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 4 edges to [[_COMMUNITY_MultiHostResult]]
- 3 edges to [[_COMMUNITY_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_run_multi_host()]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_main()]]
- 1 edge to [[_COMMUNITY_TestParseHosts]]
- 1 edge to [[_COMMUNITY_TestParserAndCommandResolution]]
- 1 edge to [[_COMMUNITY_ssh_runner()]]
- 1 edge to [[_COMMUNITY_TestTail]]

## Top bridge nodes
- [[HostStatus]] - degree 18, connects to 10 communities
- [[classify()_1]] - degree 8, connects to 3 communities
- [[TestClassify_1]] - degree 7, connects to 2 communities