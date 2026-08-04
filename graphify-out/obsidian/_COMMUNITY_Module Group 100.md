---
type: community
cohesion: 0.07
members: 43
---

# Module Group 100

**Cohesion:** 0.07 - loosely connected
**Members:** 43 nodes

## Members
- [[.is_blocked()]] - code - gateway/proxy/dns_blocklist.py
- [[.is_blocked()_2]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.setup_method()_3]] - code - gateway/tests/test_dns_blocklist.py
- [[.stats()]] - code - gateway/proxy/dns_blocklist.py
- [[.stop()]] - code - gateway/proxy/dns_blocklist.py
- [[.test_allowlist_overrides_blocklist()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_case_normalization()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_custom_denylist()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_download_failure_falls_back_to_cache()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_download_failure_no_cache_returns_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_download_success_caches_to_disk()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_exact_match()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_hosts_line_without_domain_returns_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_not_blocked()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_parent_allowlist_overrides_grandparent_block()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_parent_domain_wildcard()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_periodic_loop_survives_errors_until_cancelled()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_start_creates_task()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_stats_attributes()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_stats_returns_counts()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_stop_cancels_task()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_system_allowlist()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_trailing_dot_normalization()]] - code - gateway/tests/test_dns_blocklist.py
- [[.test_update_rebuilds_blocked_domains()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_wildcard_denylist_blocks_subdomains()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[Blocklist stub that blocks nothing.]] - rationale - gateway/tests/test_dns_canvas_coverage.py
- [[Check if a domain should be blocked.          Checks the domain and all parent d]] - rationale - gateway/proxy/dns_blocklist.py
- [[DNSBlocklist]] - code - gateway/proxy/dns_blocklist.py
- [[Domain blocklist with Pi-hole-compatible list parsing.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Lifecycle start_periodic_updates()stop() task management.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[Return blocklist statistics.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Stop periodic updates.]] - rationale - gateway/proxy/dns_blocklist.py
- [[TestBlocklistDownload]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestBlocklistUpdate]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestBlocklistWildcardsAndAllowlist]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestIsBlocked]] - code - gateway/tests/test_dns_blocklist.py
- [[TestLifecycle]] - code - gateway/tests/test_dns_blocklist.py
- [[TestStats]] - code - gateway/tests/test_dns_blocklist.py
- [[_BlockNone]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[is_blocked() — exact match, parent-domain wildcard, allowlist, denylist, case.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[stats() returns the expected keys.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[stats() — verify blockedallowlistdenylist counts.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[test_dns_blocklist.py]] - code - gateway/tests/test_dns_blocklist.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_100
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Module Group 275]]
- 9 edges to [[_COMMUNITY_Module Group 265]]
- 7 edges to [[_COMMUNITY_Module Group 302]]
- 4 edges to [[_COMMUNITY_Module Group 74]]
- 3 edges to [[_COMMUNITY_Module Group 441]]
- 3 edges to [[_COMMUNITY_Module Group 307]]
- 3 edges to [[_COMMUNITY_Module Group 291]]
- 3 edges to [[_COMMUNITY_Module Group 222]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 247]]
- 1 edge to [[_COMMUNITY_Module Group 487]]
- 1 edge to [[_COMMUNITY_Module Group 430]]
- 1 edge to [[_COMMUNITY_Module Group 318]]

## Top bridge nodes
- [[DNSBlocklist]] - degree 59, connects to 12 communities
- [[_BlockNone]] - degree 6, connects to 3 communities
- [[test_dns_blocklist.py]] - degree 6, connects to 2 communities
- [[TestBlocklistDownload]] - degree 6, connects to 2 communities
- [[TestBlocklistWildcardsAndAllowlist]] - degree 6, connects to 2 communities
