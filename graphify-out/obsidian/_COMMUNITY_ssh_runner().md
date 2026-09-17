---
type: community
cohesion: 0.40
members: 6
---

# ssh_runner()

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Members
- [[.test_ssh_runner_none_streams()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_ssh_runner_uses_subprocess()]] - code - gateway/tests/test_multi_host_test.py
- [[HostRunner]] - code - gateway/tools/multi_host_test.py
- [[Return a HostRunner that executes the command on the host over SSH.      SSH con]] - rationale - gateway/tools/multi_host_test.py
- [[TestSshRunner]] - code - gateway/tests/test_multi_host_test.py
- [[ssh_runner()]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ssh_runner
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_main()]]
- 2 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_MultiHostResult]]
- 1 edge to [[_COMMUNITY_HostStatus]]
- 1 edge to [[_COMMUNITY_run_multi_host()]]
- 1 edge to [[_COMMUNITY_multi_host_test.py]]

## Top bridge nodes
- [[ssh_runner()]] - degree 7, connects to 3 communities
- [[TestSshRunner]] - degree 6, connects to 3 communities
- [[HostRunner]] - degree 3, connects to 2 communities