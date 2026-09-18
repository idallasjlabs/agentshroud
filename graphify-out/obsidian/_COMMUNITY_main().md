---
type: community
cohesion: 0.22
members: 13
---

# main()

**Cohesion:** 0.22 - loosely connected
**Members:** 13 nodes

## Members
- [[.render_summary()]] - code - gateway/tools/multi_host_test.py
- [[.test_dry_run_default_command()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_dry_run_touches_nothing()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_main_all_pass_with_injected_runner()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_main_default_hosts()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_main_failure_nonzero_exit()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_main_unreachable_nonzero_exit()]] - code - gateway/tests/test_multi_host_test.py
- [[CLI entry point. Returns the aggregated exit code (0 = all passed).]] - rationale - gateway/tools/multi_host_test.py
- [[Render an aligned PASSFAIL table plus a totals line.]] - rationale - gateway/tools/multi_host_test.py
- [[TestMain_1]] - code - gateway/tests/test_multi_host_test.py
- [[main()_30]] - code - gateway/tools/multi_host_test.py
- [[multi-host-test.sh]] - code - scripts/multi-host-test.sh
- [[multi-host-test.sh script]] - code - scripts/multi-host-test.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/main
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_run_multi_host()]]
- 3 edges to [[_COMMUNITY_MultiHostResult]]
- 3 edges to [[_COMMUNITY_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_ssh_runner()]]
- 2 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 1 edge to [[_COMMUNITY_HostStatus]]
- 1 edge to [[_COMMUNITY_TestParserAndCommandResolution]]
- 1 edge to [[_COMMUNITY_TestParseHosts]]

## Top bridge nodes
- [[main()_30]] - degree 18, connects to 6 communities
- [[TestMain_1]] - degree 10, connects to 3 communities
- [[.test_main_all_pass_with_injected_runner()]] - degree 3, connects to 1 community
- [[.test_main_failure_nonzero_exit()]] - degree 3, connects to 1 community
- [[.test_main_unreachable_nonzero_exit()]] - degree 3, connects to 1 community