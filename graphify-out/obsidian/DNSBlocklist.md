---
source_file: "gateway/proxy/dns_blocklist.py"
type: "code"
community: "DNSBlocklist"
location: "L61"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/DNSBlocklist
---

# DNSBlocklist

## Connections
- [[dot-__init__()_187]] - `method` [EXTRACTED]
- [[dot-_periodic_update_loop()]] - `method` [EXTRACTED]
- [[dot-download_blocklist()]] - `method` [EXTRACTED]
- [[dot-is_blocked()]] - `method` [EXTRACTED]
- [[dot-load_from_text()]] - `method` [EXTRACTED]
- [[dot-parse_hosts_line()]] - `method` [EXTRACTED]
- [[dot-setup_method()_33]] - `calls` [EXTRACTED]
- [[dot-setup_method()_34]] - `calls` [EXTRACTED]
- [[dot-setup_method()_7]] - `calls` [EXTRACTED]
- [[dot-start_periodic_updates()]] - `method` [EXTRACTED]
- [[dot-stats()]] - `method` [EXTRACTED]
- [[dot-stop()_9]] - `method` [EXTRACTED]
- [[dot-test_custom_denylist()_1]] - `calls` [EXTRACTED]
- [[dot-test_download_failure_falls_back_to_cache()]] - `calls` [EXTRACTED]
- [[dot-test_download_failure_no_cache_returns_none()]] - `calls` [EXTRACTED]
- [[dot-test_download_success_caches_to_disk()]] - `calls` [EXTRACTED]
- [[dot-test_hosts_line_without_domain_returns_none()]] - `calls` [EXTRACTED]
- [[dot-test_parent_allowlist_overrides_grandparent_block()]] - `calls` [EXTRACTED]
- [[dot-test_periodic_loop_survives_errors_until_cancelled()]] - `calls` [EXTRACTED]
- [[dot-test_start_creates_task()]] - `calls` [EXTRACTED]
- [[dot-test_stats_attributes()]] - `calls` [EXTRACTED]
- [[dot-test_stats_returns_counts()]] - `calls` [EXTRACTED]
- [[dot-test_stop_cancels_task()]] - `calls` [EXTRACTED]
- [[dot-test_update_rebuilds_blocked_domains()]] - `calls` [EXTRACTED]
- [[dot-test_wildcard_denylist_blocks_subdomains()]] - `calls` [EXTRACTED]
- [[dot-update()]] - `method` [EXTRACTED]
- [[Domain blocklist with Pi-hole-compatible list parsing.]] - `rationale_for` [EXTRACTED]
- [[TestBlocklistDownload]] - `uses` [INFERRED]
- [[TestBlocklistUpdate]] - `uses` [INFERRED]
- [[TestBlocklistWildcardsAndAllowlist]] - `uses` [INFERRED]
- [[TestImportFallback]] - `uses` [INFERRED]
- [[TestIsBlocked]] - `uses` [INFERRED]
- [[TestLifecycle]] - `uses` [INFERRED]
- [[TestLoadFromText]] - `uses` [INFERRED]
- [[TestParseHostsLine]] - `uses` [INFERRED]
- [[TestStats_1]] - `uses` [INFERRED]
- [[dns_blocklist.py]] - `contains` [EXTRACTED]
- [[dns_forwarder.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_dns_blocklist.py]] - `imports` [EXTRACTED]
- [[test_dns_canvas_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/DNSBlocklist
