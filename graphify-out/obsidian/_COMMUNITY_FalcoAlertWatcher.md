---
type: community
members: 22
---

# FalcoAlertWatcher

**Members:** 22 nodes

## Members
- [[dot-__init__()_211]] - code - gateway/security/falco_monitor.py
- [[dot-_handle_critical()]] - code - gateway/security/falco_monitor.py
- [[dot-_process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[dot-run()_12]] - code - gateway/security/falco_monitor.py
- [[dot-stop()_11]] - code - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Path_73]] - code
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.…]] - rationale - gateway/security/falco_monitor.py
- [[Tests for FalcoAlertWatcher — enforcement bridge from Falco alerts to…]] - rationale - gateway/tests/test_falco_watcher.py
- [[Watcher works without a lockdown module — only logs.]] - rationale - gateway/tests/test_falco_watcher.py
- [[_make_alert()]] - code - gateway/tests/test_falco_watcher.py
- [[asyncio_81]] - code
- [[counting_poll()]] - code - gateway/tests/test_falco_watcher.py
- [[test_critical_alert_triggers_lockdown()]] - code - gateway/tests/test_falco_watcher.py
- [[test_deduplication_same_alert_twice()]] - code - gateway/tests/test_falco_watcher.py
- [[test_falco_watcher.py]] - code - gateway/tests/test_falco_watcher.py
- [[test_missing_alert_dir_noop()]] - code - gateway/tests/test_falco_watcher.py
- [[test_multiple_critical_alerts()]] - code - gateway/tests/test_falco_watcher.py
- [[test_no_progressive_lockdown_configured()]] - code - gateway/tests/test_falco_watcher.py
- [[test_stop_halts_run_loop()]] - code - gateway/tests/test_falco_watcher.py
- [[test_warning_alert_not_blocked()]] - code - gateway/tests/test_falco_watcher.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FalcoAlertWatcher
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 3 edges to [[_COMMUNITY_test_progressive_lockdown.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[FalcoAlertWatcher]] - degree 20, connects to 4 communities
- [[test_falco_watcher.py]] - degree 11, connects to 1 community
- [[test_critical_alert_triggers_lockdown()]] - degree 5, connects to 1 community
- [[dot-_process_new_alerts()]] - degree 4, connects to 1 community
- [[dot-_handle_critical()]] - degree 3, connects to 1 community
