---
type: community
cohesion: 0.06
members: 48
---

# test_security_toolchain.py

**Cohesion:** 0.06 - loosely connected
**Members:** 48 nodes

## Members
- [[dot-test_clean_when_installed_not_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_clean_when_installed_not_running()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_13]] - code - gateway/security/wazuh_client.py
- [[Check if a rule is AgentShroud-specific.      Args         rule_name Falco rul]] - rationale - gateway/security/falco_monitor.py
- [[Filter alerts to file integrity monitoring events only.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only.      Args         alerts List]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Map Wazuh alert level to severity string.      Args         level Wazuh alert]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Wazuh alert.      Args         raw Raw Wazuh alert JSON.      R]] - rationale - gateway/security/wazuh_client.py
- [[Path_7]] - code - gateway/security/wazuh_client.py
- [[Read Wazuh alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/wazuh_client.py
- [[Return latest Falco alert summary from the local alert directory.      CC-20 If]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Wazuh alert summary from the shared alert volume.      wazuh-agent]] - rationale - gateway/security/scanner_integration.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestGetFalcoSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetWazuhSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary]] - code - gateway/tests/test_security_toolchain.py
- [[datetime_1]] - code - gateway/security/wazuh_client.py
- [[generate_summary()]] - code - gateway/security/wazuh_client.py
- [[get_falco_summary()]] - code - gateway/security/scanner_integration.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[get_wazuh_summary()]] - code - gateway/security/scanner_integration.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py
- [[wazuh_client.py]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_toolchainpy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_scanner_integration.py]]
- 11 edges to [[_COMMUNITY_test_security_toolchain.py_1]]
- 9 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 8 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 6 edges to [[_COMMUNITY_parse_clamscan_output]]
- 5 edges to [[_COMMUNITY_AlertDispatcher]]
- 5 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 4 edges to [[_COMMUNITY_Path_2]]
- 4 edges to [[_COMMUNITY_parse_trivy_output]]
- 2 edges to [[_COMMUNITY_scanner_integration.py_1]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_TestStartupScannerKeying]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 42, connects to 9 communities
- [[wazuh_client.py]] - degree 14, connects to 6 communities
- [[get_wazuh_summary()]] - degree 14, connects to 4 communities
- [[generate_summary()]] - degree 13, connects to 4 communities
- [[get_falco_summary()]] - degree 13, connects to 3 communities
