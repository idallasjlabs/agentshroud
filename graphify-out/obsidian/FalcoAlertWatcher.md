---
source_file: "gateway/security/falco_monitor.py"
type: "code"
community: "Community 75"
location: "L182"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_75
---

# FalcoAlertWatcher

## Connections
- [[.__init__()_95]] - `method` [EXTRACTED]
- [[._handle_critical()]] - `method` [EXTRACTED]
- [[._process_new_alerts()]] - `method` [EXTRACTED]
- [[.run()_8]] - `method` [EXTRACTED]
- [[.stop()_10]] - `method` [EXTRACTED]
- [[.test_falco_critical_escalates_instance_shared_with_telegram()]] - `calls` [EXTRACTED]
- [[FakeClock]] - `uses` [INFERRED]
- [[FakePipelineResult]] - `uses` [INFERRED]
- [[FakeRBAC]] - `uses` [INFERRED]
- [[PassthroughPipeline]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `conceptually_related_to` [INFERRED]
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy_1]] - `uses` [INFERRED]
- [[Test Falco Watcher Module]] - `references` [EXTRACTED]
- [[TestCollabLockdownNotifications]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestDecay]] - `uses` [INFERRED]
- [[TestEscalateTo]] - `uses` [INFERRED]
- [[TestLifespanWiring]] - `uses` [INFERRED]
- [[TestLockedCommand]] - `uses` [INFERRED]
- [[TestPrincipalKeys]] - `uses` [INFERRED]
- [[TestProgressiveLockdownUnit]] - `uses` [INFERRED]
- [[TestSuspendedDropNotice]] - `uses` [INFERRED]
- [[TestTelegramProxyInjection]] - `uses` [INFERRED]
- [[TestUnlockCommand]] - `uses` [INFERRED]
- [[falco_monitor.py]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_critical_alert_triggers_lockdown()]] - `calls` [EXTRACTED]
- [[test_deduplication_same_alert_twice()]] - `calls` [EXTRACTED]
- [[test_falco_watcher.py]] - `imports` [EXTRACTED]
- [[test_missing_alert_dir_noop()]] - `calls` [EXTRACTED]
- [[test_multiple_critical_alerts()]] - `calls` [EXTRACTED]
- [[test_no_progressive_lockdown_configured()]] - `calls` [EXTRACTED]
- [[test_progressive_lockdown.py]] - `imports` [EXTRACTED]
- [[test_stop_halts_run_loop()]] - `calls` [EXTRACTED]
- [[test_warning_alert_not_blocked()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_75