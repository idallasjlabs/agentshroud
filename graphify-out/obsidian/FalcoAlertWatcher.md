---
source_file: "gateway/security/falco_monitor.py"
type: "code"
community: "Gateway Security Module"
location: "L182"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# FalcoAlertWatcher

## Connections
- [[.__init__()_77]] - `method` [EXTRACTED]
- [[._handle_critical()]] - `method` [EXTRACTED]
- [[._process_new_alerts()]] - `method` [EXTRACTED]
- [[.run()_4]] - `method` [EXTRACTED]
- [[.stop()_10]] - `method` [EXTRACTED]
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - `rationale_for` [EXTRACTED]
- [[falco_monitor.py]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_critical_alert_triggers_lockdown()]] - `calls` [EXTRACTED]
- [[test_deduplication_same_alert_twice()]] - `calls` [EXTRACTED]
- [[test_falco_watcher.py]] - `imports` [EXTRACTED]
- [[test_missing_alert_dir_noop()]] - `calls` [EXTRACTED]
- [[test_multiple_critical_alerts()]] - `calls` [EXTRACTED]
- [[test_no_progressive_lockdown_configured()]] - `calls` [EXTRACTED]
- [[test_stop_halts_run_loop()]] - `calls` [EXTRACTED]
- [[test_warning_alert_not_blocked()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Security_Module