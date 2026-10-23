---
type: community
cohesion: 0.17
members: 21
---

# check_upstream_cves() (2)

**Cohesion:** 0.17 - loosely connected
**Members:** 21 nodes

## Members
- [[dot-_patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id. ``ghsa_id``…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't…]] - rationale - gateway/security/daily_cve_report.py
- [[Return the CVE-pipeline config for bot_id (raises KeyError if unknown). Args…]] - rationale - gateway/security/agent_cve_registry.py
- [[Return the resolved GitHub advisory repo slug for bot_id. Honors the per-…]] - rationale - gateway/security/agent_cve_registry.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[_AGENT_CVE_SOURCES]] - code - gateway/security/agent_cve_registry.py
- [[_AGENT_CVE_SOURCES (per-agent CVE pipeline config)]] - code - gateway/security/agent_cve_registry.py
- [[_capture_req()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[get_agent_cve_source()]] - code - gateway/security/agent_cve_registry.py
- [[get_agent_ghsa_repo()]] - code - gateway/security/agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_upstream_cves_2
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 5 edges to [[_COMMUNITY_A2APolicyEngine]]
- 4 edges to [[_COMMUNITY_browserscriptsbrowse.py]]
- 1 edge to [[_COMMUNITY__AGENT_CVE_REGISTRIES]]

## Top bridge nodes
- [[get_agent_cve_source()]] - degree 9, connects to 3 communities
- [[get_agent_ghsa_repo()]] - degree 8, connects to 3 communities
- [[check_upstream_cves()]] - degree 14, connects to 2 communities
- [[TestCheckUpstreamCves]] - degree 9, connects to 1 community
- [[_make_github_advisory()]] - degree 6, connects to 1 community
