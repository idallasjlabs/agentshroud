---
type: community
cohesion: 0.05
members: 61
---

# FalcoAlertWatcher

**Cohesion:** 0.05 - loosely connected
**Members:** 61 nodes

## Members
- [[dot-__init__()_167]] - code - gateway/security/falco_monitor.py
- [[dot-_handle_critical()]] - code - gateway/security/falco_monitor.py
- [[dot-_process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[dot-run()_6]] - code - gateway/security/falco_monitor.py
- [[dot-stop()_12]] - code - gateway/security/falco_monitor.py
- [[dot-test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[Alert Levels]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Any_63]] - code - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Integration_2]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Integration with Gateway]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Key OSSEC Config Sections (Inferred)]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Network Enforcement]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Path_49]] - code - gateway/security/falco_monitor.py
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Priority Levels_1]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_153]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_154]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Related Notes_57]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Related Notes_58]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Relationship to Other Security Modules]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Rules Defined]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Shell Spawning Exceptions]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Test Falco Watcher Module]] - code - gateway/tests/test_falco_watcher.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[Watcher works without a lockdown module — only logs.]] - rationale - gateway/tests/test_falco_watcher.py
- [[What Wazuh Monitors in AgentShroud]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[_make_alert()]] - code - gateway/tests/test_falco_watcher.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime_5]] - code - gateway/security/falco_monitor.py
- [[falco-rules]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco-rules.yaml]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco_monitor.py_2]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()_1]] - code - gateway/security/falco_monitor.py
- [[read_alerts()_1]] - code - gateway/security/falco_monitor.py
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
- 10 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 4 edges to [[_COMMUNITY_scanner_integration.py]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_KillSwitchMonitor_1]]
- 1 edge to [[_COMMUNITY_AsyncMock_1]]
- 1 edge to [[_COMMUNITY_TrustConfig_1]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_7]]

## Top bridge nodes
- [[falco_monitor.py_2]] - degree 16, connects to 7 communities
- [[FalcoAlertWatcher]] - degree 18, connects to 2 communities
- [[read_alerts()_1]] - degree 10, connects to 2 communities
- [[TestFalcoParser]] - degree 8, connects to 2 communities
- [[is_agentshroud_rule()]] - degree 7, connects to 2 communities
