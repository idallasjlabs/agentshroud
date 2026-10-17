---
type: community
members: 20
---

# ServiceManager (3)

**Members:** 20 nodes

## Members
- [[dot-test_esrch_falls_through_to_proc_scan()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_not_installed()_3]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_not_installed()_4]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_running_via_pid_file()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_running_via_pid_file()_1]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_running_via_proc_scan()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_running_via_proc_scan()_1]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_running_via_proc_scan()_2]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_running_when_kill_raises_eperm()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_standby_when_no_pid_and_no_process()]] - code - gateway/tests/test_soc_services_coverage.py
- [[dot-test_stopped_when_no_pid_and_no_process()]] - code - gateway/tests/test_soc_services_coverage.py
- [[EPERM means the process exists but is owned by another user.]] - rationale - gateway/tests/test_soc_services_coverage.py
- [[Intercept builtins.open for specific paths; delegate everything else.]] - rationale - gateway/tests/test_soc_services_coverage.py
- [[PermissionError]] - code
- [[Stale PID (ESRCH) is not EPERM — falls through to proc scan, then standby.]] - rationale - gateway/tests/test_soc_services_coverage.py
- [[TestCheckFluentBit]] - code - gateway/tests/test_soc_services_coverage.py
- [[TestCheckWazuhAgent]] - code - gateway/tests/test_soc_services_coverage.py
- [[_check_fluent_bit]] - code - gateway/soc/services.py
- [[_check_wazuh_agent]] - code - gateway/soc/services.py
- [[_patch_open()]] - code - gateway/tests/test_soc_services_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ServiceManager_3
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2)]]

## Top bridge nodes
- [[PermissionError]] - degree 6, connects to 3 communities
- [[_patch_open()]] - degree 11, connects to 1 community
- [[TestCheckWazuhAgent]] - degree 9, connects to 1 community
- [[TestCheckFluentBit]] - degree 7, connects to 1 community
- [[dot-test_running_via_proc_scan()]] - degree 3, connects to 1 community
