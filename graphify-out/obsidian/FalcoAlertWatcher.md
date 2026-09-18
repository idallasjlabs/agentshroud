---
source_file: "gateway/security/falco_monitor.py"
type: "code"
community: "falco_monitor.py"
location: "L182"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/falco_monitorpy
---

# FalcoAlertWatcher

## Connections
- [[.__init__()_203]] - `method` [EXTRACTED]
- [[._handle_critical()]] - `method` [EXTRACTED]
- [[._process_new_alerts()]] - `method` [EXTRACTED]
- [[.run()_6]] - `method` [EXTRACTED]
- [[.stop()_12]] - `method` [EXTRACTED]
- [[SecurityPipeline_1]] - `conceptually_related_to` [INFERRED]
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - `rationale_for` [EXTRACTED]
- [[Test Falco Watcher Module]] - `references` [EXTRACTED]
- [[falco_monitor.py_2]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_critical_alert_triggers_lockdown()]] - `calls` [EXTRACTED]
- [[test_deduplication_same_alert_twice()]] - `calls` [EXTRACTED]
- [[test_falco_watcher.py]] - `imports` [EXTRACTED]
- [[test_missing_alert_dir_noop()]] - `calls` [EXTRACTED]
- [[test_multiple_critical_alerts()]] - `calls` [EXTRACTED]
- [[test_no_progressive_lockdown_configured()]] - `calls` [EXTRACTED]
- [[test_stop_halts_run_loop()]] - `calls` [EXTRACTED]
- [[test_warning_alert_not_blocked()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/falco_monitorpy