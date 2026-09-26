---
type: community
cohesion: 0.22
members: 13
---

# TestRunAndSendCveReportImageScans

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
- [[TestMain]] - code - gateway/tests/test_multi_host_test.py
- [[main()_14]] - code - gateway/tools/multi_host_test.py
- [[multi-host-test.sh]] - code - scripts/multi-host-test.sh
- [[multi-host-test.sh script]] - code - scripts/multi-host-test.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestRunAndSendCveReportImageScans
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_TestPatternDetection]]
- 3 edges to [[_COMMUNITY_AgentShroud Red Team Adversarial Tester]]
- 3 edges to [[_COMMUNITY_AgentShroud Threat Model (STRIDE Analysis)]]
- 2 edges to [[_COMMUNITY_Required ≥ 4.5 for text, ≥ 3.0 for UI elements]]
- 2 edges to [[_COMMUNITY_Development Workflow]]
- 1 edge to [[_COMMUNITY_SECTION 1 COVER SHEET (Form PTOSB16)]]
- 1 edge to [[_COMMUNITY_Common Operations]]
- 1 edge to [[_COMMUNITY_Hermes — Podcast Production Orchestrator]]

## Top bridge nodes
- [[main()_14]] - degree 18, connects to 6 communities
- [[TestMain]] - degree 10, connects to 3 communities
- [[.test_main_all_pass_with_injected_runner()]] - degree 3, connects to 1 community
- [[.test_main_failure_nonzero_exit()]] - degree 3, connects to 1 community
- [[.test_main_unreachable_nonzero_exit()]] - degree 3, connects to 1 community