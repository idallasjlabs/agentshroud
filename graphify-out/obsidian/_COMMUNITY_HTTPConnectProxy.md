---
type: community
members: 89
---

# HTTPConnectProxy

**Members:** 89 nodes

## Members
- [[dot-__init__()_214]] - code - gateway/tests/test_http_proxy.py
- [[dot-close()_20]] - code - gateway/tests/test_http_proxy.py
- [[dot-close()_21]] - code - gateway/tests/test_http_proxy.py
- [[dot-drain()_2]] - code - gateway/tests/test_http_proxy.py
- [[dot-drain()_3]] - code - gateway/tests/test_http_proxy.py
- [[dot-get_extra_info()_1]] - code - gateway/tests/test_http_proxy.py
- [[dot-get_stats()_17]] - code - gateway/proxy/http_proxy.py
- [[dot-start()_1]] - code - gateway/proxy/http_proxy.py
- [[dot-stop()_12]] - code - gateway/proxy/http_proxy.py
- [[dot-write()_2]] - code - gateway/tests/test_http_proxy.py
- [[dot-write()_3]] - code - gateway/tests/test_http_proxy.py
- [[Asyncio HTTP CONNECT proxy server. Intercepts CONNECT tunnel requests,…]] - rationale - gateway/proxy/http_proxy.py
- [[CONNECT to a private IP is blocked by SSRF protection.]] - rationale - gateway/tests/test_http_proxy.py
- [[Create a StreamReader loaded with data and a mock StreamWriter.]] - rationale - gateway/tests/test_http_proxy.py
- [[HTTPConnectProxy]] - code - gateway/proxy/http_proxy.py
- [[HTTPConnectProxy ships with a populated default allowlist.]] - rationale - gateway/tests/test_http_proxy.py
- [[Minimal asyncio.StreamWriter mock that captures written bytes.]] - rationale - gateway/tests/test_http_proxy.py
- [[None peer falls back to generic label without error.]] - rationale - gateway/tests/test_http_proxy.py
- [[Return proxy traffic statistics.]] - rationale - gateway/proxy/http_proxy.py
- [[Second call for same IP uses cache; rDNS is only called once, fDNS never.]] - rationale - gateway/tests/test_http_proxy.py
- [[Start the CONNECT proxy server.]] - rationale - gateway/proxy/http_proxy.py
- [[Startup registry hit returns correct bot_id immediately.]] - rationale - gateway/tests/test_http_proxy.py
- [[Stop the CONNECT proxy server.]] - rationale - gateway/proxy/http_proxy.py
- [[System bypass domains should be logged to the SOC decision history.]] - rationale - gateway/tests/test_http_proxy.py
- [[System bypass domains should not error when egress_filter is None.]] - rationale - gateway/tests/test_http_proxy.py
- [[Tests for HTTPConnectProxy — CONNECT tunnel server on port 8181.]] - rationale - gateway/tests/test_http_proxy.py
- [[Unknown IP resolved via reverse-DNS to a known bot hostname → correct bot_id…]] - rationale - gateway/tests/test_http_proxy.py
- [[Unknown IP whose rDNS doesn't match any bot, and fDNS fails → generic label,…]] - rationale - gateway/tests/test_http_proxy.py
- [[Unknown IP with no bot_hostnames registered → generic label, cached.]] - rationale - gateway/tests/test_http_proxy.py
- [[_DummyTargetWriter_1]] - code - gateway/tests/test_http_proxy.py
- [[_MockWriter_1]] - code - gateway/tests/test_http_proxy.py
- [[_fake_clamscan()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_fake_clamscan()_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_fake_clamscan()_2]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_fake_clamscan()_3]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_fdns()]] - code - gateway/tests/test_http_proxy.py
- [[_make_stream()_1]] - code - gateway/tests/test_http_proxy.py
- [[_open_conn()_3]] - code - gateway/tests/test_http_proxy.py
- [[_open_conn()_4]] - code - gateway/tests/test_http_proxy.py
- [[_open_conn()_5]] - code - gateway/tests/test_http_proxy.py
- [[_open_conn()_6]] - code - gateway/tests/test_http_proxy.py
- [[_rdns()]] - code - gateway/tests/test_http_proxy.py
- [[api.telegram.org must NOT be a system bypass domain. Direct CONNECT tunnels to…]] - rationale - gateway/tests/test_http_proxy.py
- [[asyncio_82]] - code
- [[check_async()_63]] - code - gateway/tests/test_http_proxy.py
- [[check_async()_64]] - code - gateway/tests/test_http_proxy.py
- [[check_async()_65]] - code - gateway/tests/test_http_proxy.py
- [[clamscan binary missing (sidecar down) - no exception, temp file removed.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[clamscan runs must never share the default executor with LLM upstream calls…]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[log_external_decision()_3]] - code - gateway/tests/test_http_proxy.py
- [[rDNS fails; forward DNS resolves bot hostname to source IP → correct bot_id…]] - rationale - gateway/tests/test_http_proxy.py
- [[rDNS fails; forward DNS resolves to a DIFFERENT IP → generic label, cached.]] - rationale - gateway/tests/test_http_proxy.py
- [[rDNS failure + fDNS failure → generic label, cached, no exception.]] - rationale - gateway/tests/test_http_proxy.py
- [[rDNS returns non-matching hostname; forward DNS matches → correct bot_id cached.]] - rationale - gateway/tests/test_http_proxy.py
- [[start() binds a real loopback server; a client gets a parsed response; stop()…]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[test_agent_id_for_peer_cached_after_first_lookup()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_forward_dns_hit()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_forward_dns_no_ip_match()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_known_ip()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_lazy_rdns_error()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_lazy_rdns_hit()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_lazy_rdns_miss()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_none_peer()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_rdns_miss_forward_dns_hit()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_unknown_no_hostnames()]] - code - gateway/tests/test_http_proxy.py
- [[test_blocked_domain_is_tracked_in_recent()]] - code - gateway/tests/test_http_proxy.py
- [[test_clamav_scan_clean_records_nothing()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_infected_records_stats()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_unavailable_degrades_silently()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_unlink_failure_swallowed()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scans_use_dedicated_single_thread_executor()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_connect_blocked_domain_returns_403()]] - code - gateway/tests/test_http_proxy.py
- [[test_connect_denied_by_egress_filter_returns_403()]] - code - gateway/tests/test_http_proxy.py
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - code - gateway/tests/test_http_proxy.py
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - code - gateway/tests/test_http_proxy.py
- [[test_default_allowed_domains_non_empty()]] - code - gateway/tests/test_http_proxy.py
- [[test_http_proxy.py]] - code - gateway/tests/test_http_proxy.py
- [[test_initial_stats_are_zero()]] - code - gateway/tests/test_http_proxy.py
- [[test_malformed_request_line_returns_400()]] - code - gateway/tests/test_http_proxy.py
- [[test_non_connect_method_returns_405()]] - code - gateway/tests/test_http_proxy.py
- [[test_proxy_created_with_custom_web_proxy()]] - code - gateway/tests/test_http_proxy.py
- [[test_proxy_created_with_default_web_proxy()]] - code - gateway/tests/test_http_proxy.py
- [[test_proxy_created_with_egress_filter()]] - code - gateway/tests/test_http_proxy.py
- [[test_ssrf_attempt_returns_403()]] - code - gateway/tests/test_http_proxy.py
- [[test_start_serves_and_stop_closes_loopback()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_stats_structure()]] - code - gateway/tests/test_http_proxy.py
- [[test_system_bypass_domain_logs_external_decision()]] - code - gateway/tests/test_http_proxy.py
- [[test_system_bypass_without_egress_filter()]] - code - gateway/tests/test_http_proxy.py
- [[test_telegram_is_force_blocked_not_bypass()]] - code - gateway/tests/test_http_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HTTPConnectProxy
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_test_http_proxy_coverage.py]]
- 21 edges to [[_COMMUNITY_WebProxy]]
- 7 edges to [[_COMMUNITY_EgressFilter]]
- 7 edges to [[_COMMUNITY_dot-_relay]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_web_proxy.py]]

## Top bridge nodes
- [[HTTPConnectProxy]] - degree 84, connects to 6 communities
- [[test_http_proxy.py]] - degree 41, connects to 3 communities
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - degree 11, connects to 2 communities
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - degree 10, connects to 2 communities
- [[test_connect_denied_by_egress_filter_returns_403()]] - degree 9, connects to 2 communities
