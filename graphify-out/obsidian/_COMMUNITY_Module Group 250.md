---
type: community
cohesion: 0.19
members: 18
---

# Module Group 250

**Cohesion:** 0.19 - loosely connected
**Members:** 18 nodes

## Members
- [[._patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_new_cve_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_without_cve_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_cve_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[Any_33]] - code - gateway/security/daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch OpenClaw GitHub Security Advisories and return CVEs not in the registry.]] - rationale - gateway/security/daily_cve_report.py
- [[Fetch upstream CVEs, alert via Telegram if new ones are found.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[Send a message via Telegram Bot API. Returns True on success.]] - rationale - gateway/security/daily_cve_report.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[_send_telegram()]] - code - gateway/security/daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[run_upstream_cve_check()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_250
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Module Group 169]]
- 4 edges to [[_COMMUNITY_Module Group 176]]
- 2 edges to [[_COMMUNITY_Module Group 333]]

## Top bridge nodes
- [[check_upstream_cves()]] - degree 11, connects to 2 communities
- [[run_upstream_cve_check()]] - degree 7, connects to 2 communities
- [[Any_33]] - degree 5, connects to 2 communities
- [[_send_telegram()]] - degree 4, connects to 2 communities
- [[TestCheckUpstreamCves]] - degree 8, connects to 1 community
