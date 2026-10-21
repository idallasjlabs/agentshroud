---
type: community
members: 52
---

# FalcoAlertWatcher

**Members:** 52 nodes

## Members
- [[dot-__init__()_47]] - code - gateway/security/falco_monitor.py
- [[dot-_handle_critical()]] - code - gateway/security/falco_monitor.py
- [[dot-_process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[dot-run()]] - code - gateway/security/falco_monitor.py
- [[dot-stop()_1]] - code - gateway/security/falco_monitor.py
- [[dot-test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[Alert Levels]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Any_11]] - code - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Integration_1]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Integration with Gateway]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Key OSSEC Config Sections (Inferred)]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Network Enforcement]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Path_9]] - code - gateway/security/falco_monitor.py
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Priority Levels]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_16]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_17]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Related Notes_19]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Related Notes_20]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Relationship to Other Security Modules]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Rules Defined]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Shell Spawning Exceptions]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Test Falco Watcher Module]] - code - gateway/tests/test_falco_watcher.py
- [[TestFalcoSummary]] - code - gateway/tests/test_security_toolchain.py
- [[Watcher works without a lockdown module — only logs.]] - rationale - gateway/tests/test_falco_watcher.py
- [[What Wazuh Monitors in AgentShroud]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[_make_alert()]] - code - gateway/tests/test_falco_watcher.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime_1]] - code - gateway/security/falco_monitor.py
- [[falco-rules]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco-rules.yaml]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
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
- [[wazuh-ossec.conf]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[wazuh-ossec]] - document - docs/vault/03 - Configuration/wazuh-ossec.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FalcoAlertWatcher
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_FalcoAlertWatcher (2)]]
- 2 edges to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py (2)]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_TrustConfig (2)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (7)]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]

## Top bridge nodes
- [[falco_monitor.py]] - degree 15, connects to 7 communities
- [[read_alerts()]] - degree 10, connects to 3 communities
- [[wazuh-ossec]] - degree 6, connects to 3 communities
- [[TestFalcoSummary]] - degree 6, connects to 2 communities
- [[FalcoAlertWatcher]] - degree 17, connects to 1 community
