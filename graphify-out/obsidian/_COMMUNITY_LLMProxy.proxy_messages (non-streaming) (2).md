---
type: community
cohesion: 0.19
members: 18
---

# LLMProxy.proxy_messages (non-streaming) (2)

**Cohesion:** 0.19 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-__init__()_161]] - code - gateway/security/falco_monitor.py
- [[dot-run()_6]] - code - gateway/security/falco_monitor.py
- [[dot-stop()_11]] - code - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Path_50]] - code - gateway/security/falco_monitor.py
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
TABLE source_file, type FROM #community/LLMProxyproxy_messages_non-streaming_2
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_SecurityPipeline (2)]]

## Top bridge nodes
- [[FalcoAlertWatcher]] - degree 17, connects to 2 communities
- [[test_critical_alert_triggers_lockdown()]] - degree 4, connects to 1 community
- [[dot-run()_6]] - degree 3, connects to 1 community
- [[Path_50]] - degree 2, connects to 1 community
