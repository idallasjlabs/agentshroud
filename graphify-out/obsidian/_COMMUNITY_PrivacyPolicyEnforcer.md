---
type: community
cohesion: 0.05
members: 61
---

# PrivacyPolicyEnforcer

**Cohesion:** 0.05 - loosely connected
**Members:** 61 nodes

## Members
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_summary_without_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_empty_stdout_is_error_not_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_nonzero_exit_code_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_whitespace_only_stdout_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_short_text_passes_through_unchanged()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_truncates_over_length_text()]] - code - gateway/tests/test_daily_cve_report.py
- [[A 0-byteempty stdout means the scan failed to produce output --         it must]] - rationale - gateway/tests/test_security_toolchain.py
- [[Any_37]] - code - gateway/security/daily_cve_report.py
- [[Any_64]] - code - gateway/security/trivy_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[Generate a summary dict suitable for the health report.      Args         alert_1]] - rationale - gateway/security/wazuh_client.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/trivy_report.py
- [[Resolve the image tag a container is ACTUALLY running, via docker CLI.      The]] - rationale - gateway/security/daily_cve_report.py
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Save a Trivy report to the log directory.      Args         report Parsed repo]] - rationale - gateway/security/trivy_report.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_running_image()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[generate_summary()_2]] - code - gateway/security/trivy_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[returncode 0 = clean, 1 = vulns found (both expected); anything         else mea]] - rationale - gateway/tests/test_security_toolchain.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[save_report()_1]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PrivacyPolicyEnforcer
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Security Verification Report]]
- 8 edges to [[_COMMUNITY_AgentShroud™ Security Policy]]
- 7 edges to [[_COMMUNITY_AgentShroud User Guide]]
- 6 edges to [[_COMMUNITY_Examples]]
- 6 edges to [[_COMMUNITY_TestTelegramWebhook]]
- 5 edges to [[_COMMUNITY_OpenSCAP]]
- 5 edges to [[_COMMUNITY_LLMProxy]]
- 4 edges to [[_COMMUNITY__wrap_response()]]
- 4 edges to [[_COMMUNITY_AgentRegistry]]
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_mcp_oauth_preflight.py]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 1 edge to [[_COMMUNITY_Browser — Secure Browser Automation]]
- 1 edge to [[_COMMUNITY_Branding Specialist (BS)]]
- 1 edge to [[_COMMUNITY_Mac App Discovery Skill]]
- 1 edge to [[_COMMUNITY_TestGroupMemoryWriteACL]]
- 1 edge to [[_COMMUNITY_test_telegram_executor.py]]
- 1 edge to [[_COMMUNITY_Incident Response (INCIDENT)]]
- 1 edge to [[_COMMUNITY_Oracle — Feedback Analyst]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 36, connects to 13 communities
- [[daily_cve_report.py]] - degree 25, connects to 8 communities
- [[run_trivy_scan()_1]] - degree 19, connects to 3 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 3 communities
- [[save_report()_1]] - degree 11, connects to 3 communities