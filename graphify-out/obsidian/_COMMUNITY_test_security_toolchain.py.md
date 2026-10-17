---
type: community
members: 68
---

# test_security_toolchain.py

**Members:** 68 nodes

## Members
- [[dot-test_all_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_empty_summaries()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_error_status_gets_50()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_format_report_string()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_generate_report()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_fim_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_rootkit_events()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_a()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_b()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_c()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_d()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_f()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_history_persistence()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_level_to_severity()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_mixed_severities()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_one_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_fim_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_rootkit_event()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_partial_tools()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_perfect_score()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_score_floor()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_trend_empty_db()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_77]] - code - gateway/security/health_report.py
- [[Any_78]] - code - gateway/security/wazuh_client.py
- [[Calculate score for a single tool (0-100).      Args         summary Tool summ]] - rationale - gateway/security/health_report.py
- [[Calculate weighted overall security score.      Args         summaries Dict ma]] - rationale - gateway/security/health_report.py
- [[Connection_1]] - code - gateway/security/health_report.py
- [[Convert score to letter grade.      Args         score Numeric score (0-100).]] - rationale - gateway/security/health_report.py
- [[Filter alerts to file integrity monitoring events only.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Filter alerts to rootkit detection events only.      Args         alerts List]] - rationale - gateway/security/wazuh_client.py
- [[Format a health report as a human-readable string.      Args         report Fu]] - rationale - gateway/security/health_report.py
- [[Generate a full health report.      Args         summaries Dict mapping tool n]] - rationale - gateway/security/health_report.py
- [[Generate a summary dict suitable for the health report.      Args         alert_1]] - rationale - gateway/security/wazuh_client.py
- [[Get score trend for the last N days.      Args         days Number of days to]] - rationale - gateway/security/health_report.py
- [[Initialize the SQLite database for history tracking.      Args         db_path]] - rationale - gateway/security/health_report.py
- [[Map Wazuh alert level to severity string.      Args         level Wazuh alert]] - rationale - gateway/security/wazuh_client.py
- [[Parse a single Wazuh alert.      Args         raw Raw Wazuh alert JSON.      R]] - rationale - gateway/security/wazuh_client.py
- [[Path_57]] - code - gateway/security/health_report.py
- [[Path_58]] - code - gateway/security/wazuh_client.py
- [[Read Wazuh alerts from the alert directory.      Args         alert_dir Direct]] - rationale - gateway/security/wazuh_client.py
- [[Save a health report to history.      Args         score Overall score.]] - rationale - gateway/security/health_report.py
- [[TestHealthOverallScore]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthScoring]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[calculate_overall_score()]] - code - gateway/security/health_report.py
- [[calculate_tool_score()]] - code - gateway/security/health_report.py
- [[datetime_6]] - code - gateway/security/wazuh_client.py
- [[format_report()]] - code - gateway/security/health_report.py
- [[generate_report()]] - code - gateway/security/health_report.py
- [[generate_summary()_3]] - code - gateway/security/wazuh_client.py
- [[get_fim_events()]] - code - gateway/security/wazuh_client.py
- [[get_rootkit_events()]] - code - gateway/security/wazuh_client.py
- [[get_trend()]] - code - gateway/security/health_report.py
- [[health_report.py_2]] - code - gateway/security/health_report.py
- [[init_db()]] - code - gateway/security/health_report.py
- [[level_to_severity()]] - code - gateway/security/wazuh_client.py
- [[parse_alert()_1]] - code - gateway/security/wazuh_client.py
- [[read_alerts()_1]] - code - gateway/security/wazuh_client.py
- [[save_to_history()]] - code - gateway/security/health_report.py
- [[score_to_grade()]] - code - gateway/security/health_report.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py
- [[wazuh-ossec]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[wazuh_client.py_2]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_toolchainpy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 10 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 7 edges to [[_COMMUNITY_parse_clamscan_output]]
- 5 edges to [[_COMMUNITY_parse_trivy_output]]
- 4 edges to [[_COMMUNITY_parse_trivy_output (2)]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 2 edges to [[_COMMUNITY_test_collaborator_greeter.py (2)]]
- 2 edges to [[_COMMUNITY_Path (3)]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher (2)]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (7)]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2) (2)]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_TestStartupScannerKeying]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 42, connects to 7 communities
- [[health_report.py_2]] - degree 18, connects to 6 communities
- [[wazuh_client.py_2]] - degree 14, connects to 5 communities
- [[generate_summary()_3]] - degree 13, connects to 5 communities
- [[read_alerts()_1]] - degree 9, connects to 3 communities
