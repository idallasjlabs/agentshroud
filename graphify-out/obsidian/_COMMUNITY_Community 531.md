---
type: community
members: 56
---

# Community 531

**Members:** 56 nodes

## Members
- [[.__init__()_80]] - code - gateway/security/falco_monitor.py
- [[._handle_critical()]] - code - gateway/security/falco_monitor.py
- [[._process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[.run()_4]] - code - gateway/security/falco_monitor.py
- [[.stop()_10]] - code - gateway/security/falco_monitor.py
- [[.test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_40]] - code - gateway/security/falco_monitor.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Integration]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Network Enforcement]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Path_11]] - code - gateway/security/falco_monitor.py
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Priority Levels_1]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_178]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Related Notes_22]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Rules Defined]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Shell Spawning Exceptions]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Test Falco Watcher Module]] - code - gateway/tests/test_falco_watcher.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[Watcher works without a lockdown module — only logs.]] - rationale - gateway/tests/test_falco_watcher.py
- [[_make_alert()]] - code - gateway/tests/test_falco_watcher.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime_3]] - code - gateway/security/falco_monitor.py
- [[falco-rules]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco-rules.yaml]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
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
- [[wazuh-ossec]] - document - docs/vault/03 - Configuration/wazuh-ossec.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_531
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 102]]
- 4 edges to [[_COMMUNITY_Community 0]]
- 3 edges to [[_COMMUNITY_Community 185]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 29]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 253]]
- 1 edge to [[_COMMUNITY_Community 112]]
- 1 edge to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 431]]
- 1 edge to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 72]]
- 1 edge to [[_COMMUNITY_Community 312]]
- 1 edge to [[_COMMUNITY_Community 49]]
- 1 edge to [[_COMMUNITY_Community 37]]
- 1 edge to [[_COMMUNITY_Community 2017]]

## Top bridge nodes
- [[falco_monitor.py]] - degree 17, connects to 7 communities
- [[alert_dispatcher.py]] - degree 9, connects to 7 communities
- [[generate_summary()_1]] - degree 8, connects to 3 communities
- [[wazuh-ossec]] - degree 6, connects to 3 communities
- [[FalcoAlertWatcher]] - degree 18, connects to 2 communities