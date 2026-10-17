---
type: community
members: 47
---

# FalcoAlertWatcher

**Members:** 47 nodes

## Members
- [[dot-_handle_critical()]] - code - gateway/security/falco_monitor.py
- [[dot-_process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[dot-test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[Alert Levels]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Any_14]] - code - gateway/security/falco_monitor.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[Generate a summary dict suitable for the health report.      Args         alert_1]] - rationale - gateway/security/falco_monitor.py
- [[Integration with Gateway]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Key OSSEC Config Sections (Inferred)]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Parse a single Falco alert.      Args         raw Raw Falco alert JSON.      R]] - rationale - gateway/security/falco_monitor.py
- [[Purpose_14]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Read Falco alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/falco_monitor.py
- [[Related Notes_20]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Relationship to Other Security Modules]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary]] - code - gateway/tests/test_security_toolchain.py
- [[What Wazuh Monitors in AgentShroud]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[datetime]] - code - gateway/security/falco_monitor.py
- [[falco-rules]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_1]] - code - gateway/security/clamav_scanner.py
- [[generate_summary()_2]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py
- [[wazuh-ossec.conf]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[wazuh-ossec]] - document - docs/vault/03 - Configuration/wazuh-ossec.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FalcoAlertWatcher
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 8 edges to [[_COMMUNITY_parse_trivy_output]]
- 7 edges to [[_COMMUNITY_test_security_toolchain.py (2)]]
- 7 edges to [[_COMMUNITY_parse_clamscan_output]]
- 5 edges to [[_COMMUNITY_AlertDispatcher]]
- 5 edges to [[_COMMUNITY_FalcoAlertWatcher (2)]]
- 3 edges to [[_COMMUNITY_scanner_integration.py]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher (3)]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (7)]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_test_collaborator_greeter.py (2)]]
- 1 edge to [[_COMMUNITY_TestStartupScannerKeying]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 42, connects to 8 communities
- [[falco_monitor.py]] - degree 16, connects to 6 communities
- [[wazuh-ossec]] - degree 6, connects to 3 communities
- [[generate_summary()_1]] - degree 5, connects to 3 communities
- [[read_alerts()]] - degree 10, connects to 2 communities
