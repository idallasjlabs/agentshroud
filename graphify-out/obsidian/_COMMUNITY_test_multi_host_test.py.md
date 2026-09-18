---
type: community
cohesion: 0.47
members: 9
---

# test_multi_host_test.py

**Cohesion:** 0.47 - moderately connected
**Members:** 9 nodes

## Members
- [[.test_wrapper_all_pass()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_wrapper_dry_run_never_calls_ssh()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_wrapper_env_host_override()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_wrapper_mixed_exit_codes_fail()]] - code - gateway/tests/test_multi_host_test.py
- [[Path_47]] - code - gateway/tests/test_multi_host_test.py
- [[TestWrapperSubprocess]] - code - gateway/tests/test_multi_host_test.py
- [[_run_wrapper()]] - code - gateway/tests/test_multi_host_test.py
- [[_write_exec()]] - code - gateway/tests/test_multi_host_test.py
- [[test_multi_host_test.py]] - code - gateway/tests/test_multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_multi_host_testpy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_MultiHostResult]]
- 5 edges to [[_COMMUNITY_HostStatus]]
- 3 edges to [[_COMMUNITY_run_multi_host()]]
- 3 edges to [[_COMMUNITY_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_TestTail]]
- 2 edges to [[_COMMUNITY_ssh_runner()]]
- 2 edges to [[_COMMUNITY_TestParserAndCommandResolution]]
- 2 edges to [[_COMMUNITY_main()]]
- 2 edges to [[_COMMUNITY_TestParseHosts]]

## Top bridge nodes
- [[test_multi_host_test.py]] - degree 26, connects to 9 communities
- [[TestWrapperSubprocess]] - degree 8, connects to 2 communities
- [[Path_47]] - degree 5, connects to 2 communities