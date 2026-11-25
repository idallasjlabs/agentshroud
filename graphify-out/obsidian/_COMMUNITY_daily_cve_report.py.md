---
type: community
members: 29
---

# daily_cve_report.py

**Members:** 29 nodes

## Members
- [[dot-test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[Any_52]] - code
- [[Background loop checks for new upstream agent CVEs once per day at report_hour…]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day. This is a…]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC. Runs…]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to…]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Daily CVE Report — container vulnerability digest + upstream agent CVE watch.…]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly. Runs a single…]] - rationale - gateway/security/daily_cve_report.py
- [[Per-agent GHSA ids already alerted. Unreadable state means alert again, never…]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently. Iterates…]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success. ``text`` is…]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_load_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_save_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime_4]] - code
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 4 edges to [[_COMMUNITY_asyncio_1]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 3 edges to [[_COMMUNITY_format_upstream_cve_alert]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY__build_image_targets]]
- 2 edges to [[_COMMUNITY_list_cve_agents]]
- 1 edge to [[_COMMUNITY_run_trivy_scan]]
- 1 edge to [[_COMMUNITY_parse_trivy_output]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 28, connects to 11 communities
- [[Any_52]] - degree 6, connects to 4 communities
- [[run_upstream_cve_check()]] - degree 10, connects to 3 communities
- [[cve_report_scheduler()]] - degree 5, connects to 2 communities
- [[run_upstream_cve_check_all_agents()]] - degree 7, connects to 1 community
