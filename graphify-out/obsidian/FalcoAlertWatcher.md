---
source_file: "gateway/security/falco_monitor.py"
type: "code"
community: "LLMProxy.proxy_messages (non-streaming) (2)"
location: "L182"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxyproxy_messages_non-streaming_2
---

# FalcoAlertWatcher

## Connections
- [[dot-__init__()_161]] - `method` [EXTRACTED]
- [[dot-_handle_critical()]] - `method` [EXTRACTED]
- [[dot-_process_new_alerts()]] - `method` [EXTRACTED]
- [[dot-run()_6]] - `method` [EXTRACTED]
- [[dot-stop()_11]] - `method` [EXTRACTED]
- [[SecurityPipeline_1]] - `conceptually_related_to` [INFERRED]
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - `rationale_for` [EXTRACTED]
- [[Test Falco Watcher Module]] - `references` [EXTRACTED]
- [[falco_monitor.py]] - `contains` [EXTRACTED]
- [[test_critical_alert_triggers_lockdown()]] - `calls` [EXTRACTED]
- [[test_deduplication_same_alert_twice()]] - `calls` [EXTRACTED]
- [[test_falco_watcher.py]] - `imports` [EXTRACTED]
- [[test_missing_alert_dir_noop()]] - `calls` [EXTRACTED]
- [[test_multiple_critical_alerts()]] - `calls` [EXTRACTED]
- [[test_no_progressive_lockdown_configured()]] - `calls` [EXTRACTED]
- [[test_stop_halts_run_loop()]] - `calls` [EXTRACTED]
- [[test_warning_alert_not_blocked()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxyproxy_messages_non-streaming_2
