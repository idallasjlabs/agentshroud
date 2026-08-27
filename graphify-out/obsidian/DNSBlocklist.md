---
source_file: "gateway/proxy/dns_blocklist.py"
type: "code"
community: "Community 141"
location: "L61"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_141
---

# DNSBlocklist

## Connections
- [[.__init__()_20]] - `method` [EXTRACTED]
- [[._periodic_update_loop()]] - `method` [EXTRACTED]
- [[.download_blocklist()]] - `method` [EXTRACTED]
- [[.is_blocked()]] - `method` [EXTRACTED]
- [[.load_from_text()]] - `method` [EXTRACTED]
- [[.parse_hosts_line()]] - `method` [EXTRACTED]
- [[.setup_method()_3]] - `calls` [EXTRACTED]
- [[.setup_method()_4]] - `calls` [EXTRACTED]
- [[.setup_method()_2]] - `calls` [EXTRACTED]
- [[.start_periodic_updates()]] - `method` [EXTRACTED]
- [[.stats()]] - `method` [EXTRACTED]
- [[.stop()]] - `method` [EXTRACTED]
- [[.test_custom_denylist()]] - `calls` [EXTRACTED]
- [[.test_download_failure_falls_back_to_cache()]] - `calls` [EXTRACTED]
- [[.test_download_failure_no_cache_returns_none()]] - `calls` [EXTRACTED]
- [[.test_download_success_caches_to_disk()]] - `calls` [EXTRACTED]
- [[.test_hosts_line_without_domain_returns_none()]] - `calls` [EXTRACTED]
- [[.test_parent_allowlist_overrides_grandparent_block()]] - `calls` [EXTRACTED]
- [[.test_periodic_loop_survives_errors_until_cancelled()]] - `calls` [EXTRACTED]
- [[.test_start_creates_task()]] - `calls` [EXTRACTED]
- [[.test_stats_attributes()]] - `calls` [EXTRACTED]
- [[.test_stats_returns_counts()]] - `calls` [EXTRACTED]
- [[.test_stop_cancels_task()]] - `calls` [EXTRACTED]
- [[.test_update_rebuilds_blocked_domains()]] - `calls` [EXTRACTED]
- [[.test_wildcard_denylist_blocks_subdomains()]] - `calls` [EXTRACTED]
- [[.update()]] - `method` [EXTRACTED]
- [[DNSForwarderProtocol]] - `uses` [INFERRED]
- [[DatagramTransport]] - `uses` [INFERRED]
- [[Domain blocklist with Pi-hole-compatible list parsing.]] - `rationale_for` [EXTRACTED]
- [[Test DNS Blocklist Suite]] - `references` [EXTRACTED]
- [[TestBlocklistDownload]] - `uses` [INFERRED]
- [[TestBlocklistUpdate]] - `uses` [INFERRED]
- [[TestBlocklistWildcardsAndAllowlist]] - `uses` [INFERRED]
- [[TestCanvasAuthHelpers]] - `uses` [INFERRED]
- [[TestCanvasHTTP]] - `uses` [INFERRED]
- [[TestCanvasLifespan]] - `uses` [INFERRED]
- [[TestCanvasWebSocket]] - `uses` [INFERRED]
- [[TestDNSForwarderProtocol]] - `uses` [INFERRED]
- [[TestForwardQuery]] - `uses` [INFERRED]
- [[TestImportFallback]] - `uses` [INFERRED]
- [[TestIsBlocked]] - `uses` [INFERRED]
- [[TestLifecycle]] - `uses` [INFERRED]
- [[TestLoadFromText]] - `uses` [INFERRED]
- [[TestParseDomainName]] - `uses` [INFERRED]
- [[TestParseHostsLine]] - `uses` [INFERRED]
- [[TestParseQuery]] - `uses` [INFERRED]
- [[TestStartDNSForwarder]] - `uses` [INFERRED]
- [[TestStats]] - `uses` [INFERRED]
- [[_BlockAll]] - `uses` [INFERRED]
- [[_BlockNone]] - `uses` [INFERRED]
- [[_FakeAsyncClient]] - `uses` [INFERRED]
- [[_FakeUpstreamResponse]] - `uses` [INFERRED]
- [[_FakeUpstreamWS]] - `uses` [INFERRED]
- [[_FakeWSConnect]] - `uses` [INFERRED]
- [[dns_blocklist.py]] - `contains` [EXTRACTED]
- [[dns_forwarder.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_dns_blocklist.py]] - `imports` [EXTRACTED]
- [[test_dns_canvas_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_141