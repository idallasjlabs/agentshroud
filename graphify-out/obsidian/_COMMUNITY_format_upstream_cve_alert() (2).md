---
type: community
cohesion: 0.28
members: 17
---

# format_upstream_cve_alert() (2)

**Cohesion:** 0.28 - loosely connected
**Members:** 17 nodes

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
- [[Format a Telegram alert for newly detected upstream CVEs. The alert is titled…]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatUpstreamCveAlert]] - code - gateway/tests/test_daily_cve_report.py
- [[The gateway never writes the registry, so the alert must not say it did. It…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[format_upstream_cve_alert()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/format_upstream_cve_alert_2
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_sync-cve-registry.py]]

## Top bridge nodes
- [[format_upstream_cve_alert()]] - degree 17, connects to 1 community
- [[TestFormatUpstreamCveAlert]] - degree 14, connects to 1 community
