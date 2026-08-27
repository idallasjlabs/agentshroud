---
type: community
members: 61
---

# Community 779

**Members:** 61 nodes

## Members
- [[._patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_already_ingested_helper_swallows_read_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_gives_up_and_marks_sent_after_max_retries()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_ingest_records_even_when_disk_write_fails()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_per_agent_check_error_is_isolated_not_fatal()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_retries_on_failed_send_before_giving_up()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_runs_ingest_records_then_skips_next_iteration()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ingest_when_marked_done_after_wake()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_when_already_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_successful_send_marks_sent_immediately_no_retry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failed send retries (bounded) within the same day, not next-day.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After the retry cap, the day IS marked done so the loop moves on.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Any_37]] - code - gateway/security/daily_cve_report.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop pull the GHSA feed as source of truth once per day.      This i]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id.      ``ghsa_i]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the GHSA ingest already ran today (disk-based, secondary guard).]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch one agent's upstream CVEs, alert via Telegram, honestly.      Runs a singl]] - rationale - gateway/security/daily_cve_report.py
- [[First iteration ingests + records; second sees dedup and skips.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Gateway OpenAPI Spec]] - document - gateway/openapi.json
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[OpenAPI dashboard endpoint group]] - concept - gateway/openapi.json
- [[OpenAPI management endpoint group]] - concept - gateway/openapi.json
- [[OpenAPI soc endpoint group]] - concept - gateway/openapi.json
- [[OpenAPI versions endpoint group]] - concept - gateway/openapi.json
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[Run the upstream CVE check for EVERY registered agent, independently.      Itera]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success.      ``text`` is d]] - rationale - gateway/security/daily_cve_report.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCveReportSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_ingested_ghsa_today returns False on a malformed sentinel.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_already_ingested_ghsa_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime_2]] - code - gateway/security/daily_cve_report.py
- [[ghsa_ingest_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check_all_agents()]] - code - gateway/security/daily_cve_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_779
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 184]]
- 5 edges to [[_COMMUNITY_Community 990]]
- 4 edges to [[_COMMUNITY_Community 482]]
- 4 edges to [[_COMMUNITY_Community 162]]
- 3 edges to [[_COMMUNITY_Community 6]]
- 3 edges to [[_COMMUNITY_Community 639]]
- 2 edges to [[_COMMUNITY_Community 112]]
- 2 edges to [[_COMMUNITY_Community 129]]
- 2 edges to [[_COMMUNITY_Community 679]]
- 1 edge to [[_COMMUNITY_Community 34]]
- 1 edge to [[_COMMUNITY_Community 134]]
- 1 edge to [[_COMMUNITY_Community 102]]
- 1 edge to [[_COMMUNITY_Community 521]]
- 1 edge to [[_COMMUNITY_Community 19]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 30, connects to 12 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 5 communities
- [[check_upstream_cves()]] - degree 13, connects to 2 communities
- [[run_upstream_cve_check()]] - degree 8, connects to 2 communities
- [[Any_37]] - degree 6, connects to 2 communities