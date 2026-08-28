---
type: community
cohesion: 0.30
members: 14
---

# Community 685

**Cohesion:** 0.30 - loosely connected
**Members:** 14 nodes

## Members
- [[._patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id.      ``ghsa_i]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - rationale - gateway/security/daily_cve_report.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_685
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 100]]
- 3 edges to [[_COMMUNITY_Community 122]]
- 1 edge to [[_COMMUNITY_Community 380]]

## Top bridge nodes
- [[check_upstream_cves()]] - degree 13, connects to 3 communities
- [[TestCheckUpstreamCves]] - degree 9, connects to 1 community
- [[_make_github_advisory()]] - degree 6, connects to 1 community