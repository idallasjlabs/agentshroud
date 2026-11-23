---
type: community
members: 7
---

# TestModuleConfigDefaults

**Members:** 7 nodes

## Members
- [[dot-test_dns_filter_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_egress_monitor_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_killswitch_dry_run_disabled()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_subagent_monitor_default_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[Kill switch dry_run must be False — real termination on anomaly.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[TestModuleConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[Verify individual module configs default to enforce mode.]] - rationale - gateway/tests/test_all_modules_enforce.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestModuleConfigDefaults
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_EgressEvent]]
- 2 edges to [[_COMMUNITY_SubagentMonitor]]
- 2 edges to [[_COMMUNITY_KillSwitchConfig]]
- 1 edge to [[_COMMUNITY_test_all_modules_enforce.py]]

## Top bridge nodes
- [[TestModuleConfigDefaults]] - degree 10, connects to 5 communities
- [[dot-test_killswitch_dry_run_disabled()]] - degree 3, connects to 1 community
- [[dot-test_dns_filter_default_enforce()]] - degree 2, connects to 1 community
- [[dot-test_egress_monitor_default_enforce()]] - degree 2, connects to 1 community
- [[dot-test_subagent_monitor_default_enforce()]] - degree 2, connects to 1 community
