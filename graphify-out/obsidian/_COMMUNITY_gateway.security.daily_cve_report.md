---
type: community
cohesion: 0.09
members: 39
---

# gateway.security.daily_cve_report

**Cohesion:** 0.09 - loosely connected
**Members:** 39 nodes

## Members
- [[._cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_states_auto_registered_under_review()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_titled_for_agent_label()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_total_count()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_handles_missing_optional_fields()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_more_indicator_when_under_item_limit()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_plural_header_for_multiple_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_singular_header_for_one_cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_summary_under_telegram_limit_for_100_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[Any_15]] - code
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day. This is a…]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to…]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Daily CVE Report — container vulnerability digest + upstream agent CVE watch.…]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly. Runs a single…]] - rationale - gateway/security/daily_cve_report.py
- [[Format a Telegram alert for newly detected upstream CVEs. The alert is titled…]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently. Iterates…]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success. ``text`` is…]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestFormatUpstreamCveAlert]] - code - gateway/tests/test_daily_cve_report.py
- [[The alert says CVEs are auto-registered under_review (honest, not 'add…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler]] - code - gateway/security/daily_cve_report.py
- [[format_upstream_cve_alert]] - code - gateway/security/daily_cve_report.py
- [[gateway.security.daily_cve_report]] - code - gateway/security/daily_cve_report.py
- [[ghsa_ingest_scheduler]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents]] - code - gateway/security/daily_cve_report.py
- [[upstream_cve_check_scheduler]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gatewaysecuritydaily_cve_report
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 11 edges to [[_COMMUNITY_asyncio]]
- 3 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_gateway.security.agent_cve_registry]]
- 2 edges to [[_COMMUNITY__build_image_targets]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY_AgentShroud™ Security Policy]]
- 1 edge to [[_COMMUNITY_auto_remediate_cves.py]]
- 1 edge to [[_COMMUNITY_CronStateMonitor]]
- 1 edge to [[_COMMUNITY_check_upstream_cves()]]
- 1 edge to [[_COMMUNITY_format_cve_report()]]
- 1 edge to [[_COMMUNITY_format_upstream_cve_alert()]]

## Top bridge nodes
- [[gateway.security.daily_cve_report]] - degree 29, connects to 11 communities
- [[Any_15]] - degree 12, connects to 6 communities
- [[run_upstream_cve_check]] - degree 8, connects to 2 communities
- [[_already_sent_today]] - degree 6, connects to 2 communities
- [[cve_report_scheduler]] - degree 5, connects to 2 communities