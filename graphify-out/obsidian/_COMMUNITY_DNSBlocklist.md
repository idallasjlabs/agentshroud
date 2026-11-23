---
type: community
members: 64
---

# DNSBlocklist

**Members:** 64 nodes

## Members
- [[dot-__init__()_191]] - code - gateway/proxy/dns_blocklist.py
- [[dot-_periodic_update_loop()]] - code - gateway/proxy/dns_blocklist.py
- [[dot-download_blocklist()]] - code - gateway/proxy/dns_blocklist.py
- [[dot-is_blocked()]] - code - gateway/proxy/dns_blocklist.py
- [[dot-load_from_text()]] - code - gateway/proxy/dns_blocklist.py
- [[dot-parse_hosts_line()]] - code - gateway/proxy/dns_blocklist.py
- [[dot-setup_method()_33]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-setup_method()_34]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-start_periodic_updates()]] - code - gateway/proxy/dns_blocklist.py
- [[dot-stats()]] - code - gateway/proxy/dns_blocklist.py
- [[dot-stop()_11]] - code - gateway/proxy/dns_blocklist.py
- [[dot-test_allowlist_overrides_blocklist()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_allowlist_skip()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_case_normalization()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_comments_skipped()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_custom_denylist()_1]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_deduplication()_1]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_download_failure_falls_back_to_cache()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_download_failure_no_cache_returns_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_download_success_caches_to_disk()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_empty_text()_1]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_exact_match()_1]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_hosts_line_without_domain_returns_none()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_multi_line_parsing()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_not_blocked()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_parent_allowlist_overrides_grandparent_block()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_parent_domain_wildcard()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_periodic_loop_survives_errors_until_cancelled()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_start_creates_task()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_stats_attributes()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_stats_returns_counts()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_stop_cancels_task()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_system_allowlist()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_trailing_dot_normalization()]] - code - gateway/tests/test_dns_blocklist.py
- [[dot-test_update_rebuilds_blocked_domains()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-test_wildcard_denylist_blocks_subdomains()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[dot-update()]] - code - gateway/proxy/dns_blocklist.py
- [[Background loop update blocklists every UPDATE_INTERVAL_SECONDS.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Check if a domain should be blocked. Checks the domain and all parent domains…]] - rationale - gateway/proxy/dns_blocklist.py
- [[DNSBlocklist]] - code - gateway/proxy/dns_blocklist.py
- [[Domain blocklist with Pi-hole-compatible list parsing.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Download a blocklist URL. Uses the gateway's own HTTP client.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Download all blocklists and rebuild the blocked domains set.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Lifecycle start_periodic_updates()stop() task management.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[Parse a single line from a hosts-format or domain-only blocklist. Supports -…]] - rationale - gateway/proxy/dns_blocklist.py
- [[Parse blocklist text and add domains. Returns count of new domains.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Path_67]] - code
- [[Return blocklist statistics.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Start background task for periodic blocklist updates.]] - rationale - gateway/proxy/dns_blocklist.py
- [[Stop periodic updates.]] - rationale - gateway/proxy/dns_blocklist.py
- [[TestBlocklistDownload]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestBlocklistUpdate]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestBlocklistWildcardsAndAllowlist]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestIsBlocked]] - code - gateway/tests/test_dns_blocklist.py
- [[TestLifecycle]] - code - gateway/tests/test_dns_blocklist.py
- [[TestLoadFromText]] - code - gateway/tests/test_dns_blocklist.py
- [[TestStats_1]] - code - gateway/tests/test_dns_blocklist.py
- [[Tests for the in-process DNS blocklist (replaced Pi-hole integration).]] - rationale - gateway/tests/test_dns_blocklist.py
- [[asyncio_76]] - code
- [[is_blocked() — exact match, parent-domain wildcard, allowlist, denylist, case.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[load_from_text() — multi-line parsing, dedup, allowlist skip.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[stats() returns the expected keys.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[stats() — verify blockedallowlistdenylist counts.]] - rationale - gateway/tests/test_dns_blocklist.py
- [[test_dns_blocklist.py]] - code - gateway/tests/test_dns_blocklist.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DNSBlocklist
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_dns_canvas_coverage.py]]
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY_TestParseHostsLine]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[DNSBlocklist]] - degree 42, connects to 4 communities
- [[test_dns_blocklist.py]] - degree 9, connects to 2 communities
- [[TestBlocklistDownload]] - degree 5, connects to 1 community
- [[TestBlocklistWildcardsAndAllowlist]] - degree 5, connects to 1 community
- [[TestBlocklistUpdate]] - degree 4, connects to 1 community
