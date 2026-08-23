---
type: community
cohesion: 0.10
members: 31
---

# Falco Monitor (security)

**Cohesion:** 0.10 - loosely connected
**Members:** 31 nodes

## Members
- [[.__init__()_80]] - code - gateway/security/falco_monitor.py
- [[._handle_critical()]] - code - gateway/security/falco_monitor.py
- [[._process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[.run()_4]] - code - gateway/security/falco_monitor.py
- [[.stop()_10]] - code - gateway/security/falco_monitor.py
- [[.test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_40]] - code - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Path_11]] - code - gateway/security/falco_monitor.py
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Test Falco Watcher Module]] - code - gateway/tests/test_falco_watcher.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[Watcher works without a lockdown module — only logs.]] - rationale - gateway/tests/test_falco_watcher.py
- [[_make_alert()]] - code - gateway/tests/test_falco_watcher.py
- [[datetime_3]] - code - gateway/security/falco_monitor.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
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
TABLE source_file, type FROM #community/Falco_Monitor_security
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Security Toolchain]]
- 4 edges to [[_COMMUNITY_Scanner Integration Coverage]]
- 3 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Scanner Integration (security)]]
- 1 edge to [[_COMMUNITY_Slack Proxy Coverage]]

## Top bridge nodes
- [[read_alerts()]] - degree 10, connects to 3 communities
- [[FalcoAlertWatcher]] - degree 18, connects to 2 communities
- [[parse_alert()]] - degree 6, connects to 2 communities
- [[TestFalcoSummary_1]] - degree 6, connects to 2 communities
- [[Any_40]] - degree 5, connects to 1 community