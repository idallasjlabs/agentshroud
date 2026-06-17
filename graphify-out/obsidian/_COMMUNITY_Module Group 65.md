---
type: community
cohesion: 0.06
members: 58
---

# Module Group 65

**Cohesion:** 0.06 - loosely connected
**Members:** 58 nodes

## Members
- [[.__init__()_118]] - code - gateway/tests/test_http_proxy.py
- [[.close()_10]] - code - gateway/tests/test_http_proxy.py
- [[.close()_9]] - code - gateway/tests/test_http_proxy.py
- [[.drain()_1]] - code - gateway/tests/test_http_proxy.py
- [[.drain()]] - code - gateway/tests/test_http_proxy.py
- [[.get_extra_info()]] - code - gateway/tests/test_http_proxy.py
- [[.get_stats()_3]] - code - gateway/proxy/http_proxy.py
- [[.start()]] - code - gateway/proxy/http_proxy.py
- [[.stop()_1]] - code - gateway/proxy/http_proxy.py
- [[.write()_1]] - code - gateway/tests/test_http_proxy.py
- [[.write()]] - code - gateway/tests/test_http_proxy.py
- [[Asyncio HTTP CONNECT proxy server.      Intercepts CONNECT tunnel requests, vali]] - rationale - gateway/proxy/http_proxy.py
- [[CONNECT to a private IP is blocked by SSRF protection.]] - rationale - gateway/tests/test_http_proxy.py
- [[Create a StreamReader loaded with data and a mock StreamWriter.]] - rationale - gateway/tests/test_http_proxy.py
- [[HTTPConnectProxy]] - code - gateway/proxy/http_proxy.py
- [[HTTPConnectProxy ships with a populated default allowlist.]] - rationale - gateway/tests/test_http_proxy.py
- [[Minimal asyncio.StreamWriter mock that captures written bytes.]] - rationale - gateway/tests/test_http_proxy.py
- [[None peer falls back to generic label without error.]] - rationale - gateway/tests/test_http_proxy.py
- [[Return proxy traffic statistics.]] - rationale - gateway/proxy/http_proxy.py
- [[Second call for same IP uses cache; rDNS is only called once.]] - rationale - gateway/tests/test_http_proxy.py
- [[Start the CONNECT proxy server.]] - rationale - gateway/proxy/http_proxy.py
- [[Startup registry hit returns correct bot_id immediately.]] - rationale - gateway/tests/test_http_proxy.py
- [[Stop the CONNECT proxy server.]] - rationale - gateway/proxy/http_proxy.py
- [[System bypass domains should be logged to the SOC decision history.]] - rationale - gateway/tests/test_http_proxy.py
- [[System bypass domains should not error when egress_filter is None.]] - rationale - gateway/tests/test_http_proxy.py
- [[Unknown IP resolved via reverse-DNS to a known bot hostname → correct bot_id cac]] - rationale - gateway/tests/test_http_proxy.py
- [[Unknown IP whose rDNS doesn't match any bot → generic label, cached.]] - rationale - gateway/tests/test_http_proxy.py
- [[Unknown IP with no bot_hostnames registered → generic label, cached.]] - rationale - gateway/tests/test_http_proxy.py
- [[_DummyTargetWriter]] - code - gateway/tests/test_http_proxy.py
- [[_MockWriter]] - code - gateway/tests/test_http_proxy.py
- [[_make_stream()]] - code - gateway/tests/test_http_proxy.py
- [[api.telegram.org must NOT be a system bypass domain.      Direct CONNECT tunnels]] - rationale - gateway/tests/test_http_proxy.py
- [[rDNS failure (e.g. NXDOMAIN) → generic label, cached, no exception.]] - rationale - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_cached_after_first_lookup()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_known_ip()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_lazy_rdns_error()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_lazy_rdns_hit()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_lazy_rdns_miss()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_none_peer()]] - code - gateway/tests/test_http_proxy.py
- [[test_agent_id_for_peer_unknown_no_hostnames()]] - code - gateway/tests/test_http_proxy.py
- [[test_blocked_domain_is_tracked_in_recent()]] - code - gateway/tests/test_http_proxy.py
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
- [[test_stats_structure()]] - code - gateway/tests/test_http_proxy.py
- [[test_system_bypass_domain_logs_external_decision()]] - code - gateway/tests/test_http_proxy.py
- [[test_system_bypass_without_egress_filter()]] - code - gateway/tests/test_http_proxy.py
- [[test_telegram_is_force_blocked_not_bypass()]] - code - gateway/tests/test_http_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_65
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_HTTP Proxy Coverage Tests]]
- 22 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 6 edges to [[_COMMUNITY_Module Group 303]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_Module Group 386]]
- 3 edges to [[_COMMUNITY_Module Group 79]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 240]]

## Top bridge nodes
- [[HTTPConnectProxy]] - degree 80, connects to 7 communities
- [[test_http_proxy.py]] - degree 32, connects to 2 communities
- [[_MockWriter]] - degree 21, connects to 2 communities
- [[_DummyTargetWriter]] - degree 8, connects to 2 communities
- [[test_blocked_domain_is_tracked_in_recent()]] - degree 6, connects to 1 community