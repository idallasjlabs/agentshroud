---
type: community
cohesion: 0.20
members: 18
---

# Community 501

**Cohesion:** 0.20 - loosely connected
**Members:** 18 nodes

## Members
- [[._handle_critical()]] - code - gateway/security/falco_monitor.py
- [[._process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[.run()_4]] - code - gateway/security/falco_monitor.py
- [[.stop()_10]] - code - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Test Falco Watcher Module]] - code - gateway/tests/test_falco_watcher.py
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
TABLE source_file, type FROM #community/Community_501
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 112]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 1 edge to [[_COMMUNITY_Community 410]]
- 1 edge to [[_COMMUNITY_Community 24]]

## Top bridge nodes
- [[FalcoAlertWatcher]] - degree 18, connects to 4 communities
- [[._process_new_alerts()]] - degree 4, connects to 1 community
- [[test_critical_alert_triggers_lockdown()]] - degree 4, connects to 1 community
- [[._handle_critical()]] - degree 3, connects to 1 community