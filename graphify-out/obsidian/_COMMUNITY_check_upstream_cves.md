---
type: community
cohesion: 0.22
members: 17
---

# check_upstream_cves

**Cohesion:** 0.22 - loosely connected
**Members:** 17 nodes

## Members
- [[._patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[Agent CVE Registry module (_AGENT_CVE_REGISTRIES etc.)]] - code - gateway/security/agent_cve_registry.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id. ``ghsa_id``…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't…]] - rationale - gateway/security/daily_cve_report.py
- [[Registry-integrity fix fabricated CVE ids replaced with synthetic ASH refs]] - rationale - gateway/security/agent_cve_registry.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[_capture_req()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves]] - code - gateway/security/daily_cve_report.py
- [[test_security_tool_entries_start_as_under_review_never_pre_claimed_mitigated]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_upstream_cves
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_asyncio]]
- 3 edges to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 2 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_sunday_run_scan_gate]]
- 1 edge to [[_COMMUNITY_check_upstream_cves()]]

## Top bridge nodes
- [[check_upstream_cves]] - degree 16, connects to 4 communities
- [[TestCheckUpstreamCves]] - degree 9, connects to 1 community
- [[._patch_urllib()]] - degree 7, connects to 1 community
- [[_make_github_advisory()]] - degree 6, connects to 1 community