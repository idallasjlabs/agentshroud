---
type: community
members: 33
---

# Community 135

**Members:** 33 nodes

## Members
- [[._patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[Any_37]] - code - gateway/security/daily_cve_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id.      ``ghsa_i]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[Per-agent GHSA ids already alerted. Unreadable state means alert again, never si]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_load_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[_save_alerted_ghsa()]] - code - gateway/security/daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_135
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 127]]
- 4 edges to [[_COMMUNITY_Community 74]]
- 4 edges to [[_COMMUNITY_Community 131]]
- 3 edges to [[_COMMUNITY_Community 736]]
- 3 edges to [[_COMMUNITY_Community 1202]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 42]]
- 2 edges to [[_COMMUNITY_Community 1200]]
- 1 edge to [[_COMMUNITY_Community 35]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 27, connects to 8 communities
- [[check_upstream_cves()]] - degree 13, connects to 2 communities
- [[run_upstream_cve_check()]] - degree 10, connects to 2 communities
- [[Any_37]] - degree 6, connects to 2 communities
- [[TestCheckUpstreamCves]] - degree 9, connects to 1 community