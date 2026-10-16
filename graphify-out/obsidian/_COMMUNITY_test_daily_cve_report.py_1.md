---
type: community
cohesion: 0.09
members: 32
---

# test_daily_cve_report.py

**Cohesion:** 0.09 - loosely connected
**Members:** 32 nodes

## Members
- [[dot-test_custom_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_default_prefix()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_log_dir_created_if_missing()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_report_content_persisted()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_10]] - code - gateway/security/daily_cve_report.py
- [[Any_11]] - code - gateway/security/trivy_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Custom report_prefix is used verbatim.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Default report_prefix produces a 'trivy-' filename.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/trivy_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Saved file is valid JSON containing the report keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[TestTrivySaveReport]] - code - gateway/tests/test_security_toolchain.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[generate_summary()]] - code - gateway/security/trivy_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[save_report creates the log directory if it does not exist.]] - rationale - gateway/tests/test_security_toolchain.py
- [[save_report()]] - code - gateway/security/trivy_report.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 6 edges to [[_COMMUNITY_parse_trivy_output]]
- 4 edges to [[_COMMUNITY_export-bot-conversations.py_1]]
- 4 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 3 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 3 edges to [[_COMMUNITY_format_upstream_cve_alert]]
- 3 edges to [[_COMMUNITY_test_daily_cve_report.py_2]]
- 3 edges to [[_COMMUNITY__build_image_targets]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 25, connects to 9 communities
- [[trivy_report.py]] - degree 8, connects to 5 communities
- [[generate_summary()]] - degree 10, connects to 4 communities
- [[run_upstream_cve_check()]] - degree 9, connects to 4 communities
- [[save_report()]] - degree 11, connects to 3 communities
