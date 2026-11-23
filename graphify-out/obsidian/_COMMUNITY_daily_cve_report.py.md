---
type: community
members: 47
---

# daily_cve_report.py

**Members:** 47 nodes

## Members
- [[dot-_cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_alert_does_not_claim_registration()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_alert_says_when_no_fix_is_published()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_alert_shows_fixed_in_version()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_alert_titled_for_agent_label()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_cve_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_severity_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_total_count()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_handles_missing_optional_fields()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_no_more_indicator_when_under_item_limit()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_plural_header_for_multiple_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_singular_header_for_one_cve()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_summary_under_telegram_limit_for_100_cves()]] - code - gateway/tests/test_daily_cve_report.py
- [[Any_52]] - code
- [[Background loop checks for new upstream agent CVEs once per day at report_hour…]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day. This is a…]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC. Runs…]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to…]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Daily CVE Report — container vulnerability digest + upstream agent CVE watch.…]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly. Runs a single…]] - rationale - gateway/security/daily_cve_report.py
- [[Format a Telegram alert for newly detected upstream CVEs. The alert is titled…]] - rationale - gateway/security/daily_cve_report.py
- [[Per-agent GHSA ids already alerted. Unreadable state means alert again, never…]] - rationale - gateway/security/daily_cve_report.py
- [[Return the CVE-pipeline config for bot_id (raises KeyError if unknown). Args…]] - rationale - gateway/security/agent_cve_registry.py
- [[Run a Trivy scan, format the report, and send via Telegram. Args bot_token…]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently. Iterates…]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success. ``text`` is…]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatUpstreamCveAlert]] - code - gateway/tests/test_daily_cve_report.py
- [[The gateway never writes the registry, so the alert must not say it did. It…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_load_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_run()_8]] - code - gateway/soc/router.py
- [[_save_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime_4]] - code
- [[format_upstream_cve_alert()]] - code - gateway/security/daily_cve_report.py
- [[get_agent_cve_source()]] - code - gateway/security/agent_cve_registry.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 5 edges to [[_COMMUNITY_parse_trivy_output]]
- 4 edges to [[_COMMUNITY_asyncio]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 3 edges to [[_COMMUNITY__make_report]]
- 3 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 3 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_run_trivy_scan]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_load_config]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 28, connects to 8 communities
- [[run_and_send_cve_report()]] - degree 18, connects to 7 communities
- [[get_agent_cve_source()]] - degree 6, connects to 2 communities
- [[Any_52]] - degree 6, connects to 2 communities
- [[_run()_8]] - degree 3, connects to 2 communities
