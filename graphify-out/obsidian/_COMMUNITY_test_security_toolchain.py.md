---
type: community
members: 52
---

# test_security_toolchain.py

**Members:** 52 nodes

## Members
- [[dot-test_all_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_empty_summaries()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_error_status_gets_50()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_format_report_string()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_generate_report()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_a()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_b()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_c()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_d()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_grade_f()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_history_persistence()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_mixed_severities()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_one_critical()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_partial_tools()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_perfect_score()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_score_floor()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_rootkit()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_trend_empty_db()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_12]] - code - gateway/security/health_report.py
- [[Calculate score for a single tool (0-100).      Args         summary Tool summ]] - rationale - gateway/security/health_report.py
- [[Calculate weighted overall security score.      Args         summaries Dict ma]] - rationale - gateway/security/health_report.py
- [[Categorize alerts by severity.      Args         alerts List of parsed alerts.]] - rationale - gateway/security/falco_monitor.py
- [[Connection]] - code - gateway/security/health_report.py
- [[Convert score to letter grade.      Args         score Numeric score (0-100).]] - rationale - gateway/security/health_report.py
- [[Format a health report as a human-readable string.      Args         report Fu]] - rationale - gateway/security/health_report.py
- [[Generate a full health report.      Args         summaries Dict mapping tool n]] - rationale - gateway/security/health_report.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Get score trend for the last N days.      Args         days Number of days to]] - rationale - gateway/security/health_report.py
- [[Initialize the SQLite database for history tracking.      Args         db_path]] - rationale - gateway/security/health_report.py
- [[Path_10]] - code - gateway/security/health_report.py
- [[Save a health report to history.      Args         score Overall score.]] - rationale - gateway/security/health_report.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthOverallScore]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthReport]] - code - gateway/tests/test_security_toolchain.py
- [[TestHealthScoring]] - code - gateway/tests/test_security_toolchain.py
- [[TestWazuhSummary]] - code - gateway/tests/test_security_toolchain.py
- [[calculate_overall_score()]] - code - gateway/security/health_report.py
- [[calculate_tool_score()]] - code - gateway/security/health_report.py
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[format_report()]] - code - gateway/security/health_report.py
- [[generate_report()]] - code - gateway/security/health_report.py
- [[generate_summary()_1]] - code - gateway/security/falco_monitor.py
- [[generate_summary()_2]] - code - gateway/security/wazuh_client.py
- [[get_trend()]] - code - gateway/security/health_report.py
- [[health_report.py]] - code - gateway/security/health_report.py
- [[init_db()]] - code - gateway/security/health_report.py
- [[save_to_history()]] - code - gateway/security/health_report.py
- [[score_to_grade()]] - code - gateway/security/health_report.py
- [[test_security_toolchain.py]] - code - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_toolchainpy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_security_toolchain.py (2)]]
- 8 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 7 edges to [[_COMMUNITY_parse_clamscan_output]]
- 7 edges to [[_COMMUNITY_AlertDispatcher]]
- 4 edges to [[_COMMUNITY_export-bot-conversations.py]]
- 4 edges to [[_COMMUNITY_parse_trivy_output]]
- 3 edges to [[_COMMUNITY_FalcoAlertWatcher (2)]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 1 edge to [[_COMMUNITY_test_collaborator_greeter.py (3)]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_egress_filter.py (3)]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY__load_latest_json]]
- 1 edge to [[_COMMUNITY_test_collaborator_greeter.py (2)]]
- 1 edge to [[_COMMUNITY_Path (3)]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_TestStartupScannerKeying]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]

## Top bridge nodes
- [[test_security_toolchain.py]] - degree 42, connects to 10 communities
- [[generate_summary()_2]] - degree 13, connects to 8 communities
- [[health_report.py]] - degree 17, connects to 7 communities
- [[generate_summary()_1]] - degree 8, connects to 3 communities
- [[TestHealthScoring]] - degree 12, connects to 1 community
