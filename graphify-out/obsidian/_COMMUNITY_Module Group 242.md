---
type: community
cohesion: 0.19
members: 19
---

# Module Group 242

**Cohesion:** 0.19 - loosely connected
**Members:** 19 nodes

## Members
- [[.__init__()_64]] - code - gateway/security/falco_monitor.py
- [[._handle_critical()]] - code - gateway/security/falco_monitor.py
- [[._process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[.run()_4]] - code - gateway/security/falco_monitor.py
- [[.stop()_9]] - code - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Path_10]] - code - gateway/security/falco_monitor.py
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Watcher works without a lockdown module — only logs.]] - rationale - gateway/tests/test_falco_watcher.py
- [[_make_alert()]] - code - gateway/tests/test_falco_watcher.py
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
TABLE source_file, type FROM #community/Module_Group_242
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 141]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[FalcoAlertWatcher]] - degree 16, connects to 2 communities
- [[._process_new_alerts()]] - degree 4, connects to 1 community
- [[test_critical_alert_triggers_lockdown()]] - degree 4, connects to 1 community
- [[._handle_critical()]] - degree 3, connects to 1 community
- [[Path_10]] - degree 2, connects to 1 community
