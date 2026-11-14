---
type: community
members: 36
---

# Community 368

**Members:** 36 nodes

## Members
- [[._cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_does_not_claim_registration()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_says_when_no_fix_is_published()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_shows_fixed_in_version()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_titled_for_agent_label()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_total_count()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_handles_missing_optional_fields()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_more_indicator_when_under_item_limit()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_plural_header_for_multiple_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_singular_header_for_one_cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_summary_under_telegram_limit_for_100_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[Any_47]] - code - gateway/security/daily_cve_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[Format a Telegram alert for newly detected upstream CVEs.      The alert is titl]] - rationale - gateway/security/daily_cve_report.py
- [[Per-agent GHSA ids already alerted. Unreadable state means alert again, never si]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatUpstreamCveAlert]] - code - gateway/tests/test_daily_cve_report.py
- [[The gateway never writes the registry, so the alert must not say it did.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_load_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_save_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[format_upstream_cve_alert()]] - code - gateway/security/daily_cve_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_368
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 127]]
- 4 edges to [[_COMMUNITY_Community 131]]
- 3 edges to [[_COMMUNITY_Community 74]]
- 3 edges to [[_COMMUNITY_Community 736]]
- 3 edges to [[_COMMUNITY_Community 1139]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 42]]
- 2 edges to [[_COMMUNITY_Community 1200]]
- 1 edge to [[_COMMUNITY_Community 50]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 27, connects to 8 communities
- [[run_upstream_cve_check()]] - degree 10, connects to 2 communities
- [[Any_47]] - degree 6, connects to 2 communities
- [[format_upstream_cve_alert()]] - degree 17, connects to 1 community
- [[TestFormatUpstreamCveAlert]] - degree 14, connects to 1 community