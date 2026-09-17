---
type: community
cohesion: 0.19
members: 19
---

# check_upstream_cves()

**Cohesion:** 0.19 - loosely connected
**Members:** 19 nodes

## Members
- [[._patch_urllib()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_raises_on_network_error()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_empty_when_all_known()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_new_advisory_not_in_registry()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_whose_cve_is_already_tracked()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_without_ghsa_id()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ghsa_already_in_registry()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_uses_github_token_in_header()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[Any_65]] - code
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id.      ``ghsa_i]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - rationale - gateway/security/daily_cve_report.py
- [[Return a summary of the advisory registry for the specified agent.      Counts a]] - rationale - gateway/security/agent_cve_registry.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_AGENT_CVE_REGISTRIES]] - code - gateway/security/agent_cve_registry.py
- [[_HERMES_CVE_REGISTRY_1]] - code - gateway/security/agent_cve_registry.py
- [[_make_github_advisory()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[get_agent_cve_summary()]] - code - gateway/security/agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_upstream_cves
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_check_upstream_cves]]
- 1 edge to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 1 edge to [[_COMMUNITY_plan_remediation()]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY__t()]]

## Top bridge nodes
- [[_AGENT_CVE_REGISTRIES]] - degree 6, connects to 3 communities
- [[check_upstream_cves()]] - degree 14, connects to 2 communities
- [[TestCheckUpstreamCves_1]] - degree 9, connects to 1 community
- [[_make_github_advisory()_1]] - degree 6, connects to 1 community
- [[get_agent_cve_summary()]] - degree 4, connects to 1 community