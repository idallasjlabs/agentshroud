---
type: community
cohesion: 0.04
members: 59
---

# EgressFilter

**Cohesion:** 0.04 - loosely connected
**Members:** 59 nodes

## Members
- [[dot-flush_notifications()]] - code - gateway/security/egress_filter.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_12]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[dot-grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[dot-set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[dot-set_event_bus()_1]] - code - gateway/security/egress_filter.py
- [[dot-set_notifier()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_15]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_log()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_stats()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[EgressFilter_2]] - code - gateway/security/egress_filter.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilter
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_EgressFilterConfig]]
- 18 edges to [[_COMMUNITY_AgentRegistry]]
- 10 edges to [[_COMMUNITY_EgressPolicy]]
- 10 edges to [[_COMMUNITY_EgressAttempt]]
- 9 edges to [[_COMMUNITY__make_filter]]
- 8 edges to [[_COMMUNITY_MiddlewareManager]]
- 7 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 4 edges to [[_COMMUNITY_test_egress_filter.py]]
- 4 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY_main.py]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TestEgressSSRF]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_DataExfilVolumeGuard]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_DataLedger]]
- 1 edge to [[_COMMUNITY_TestSSRFDetection]]
- 1 edge to [[_COMMUNITY_migrate-cve-registry-ghsa.py]]

## Top bridge nodes
- [[EgressFilter_2]] - degree 103, connects to 18 communities
- [[TestEgressFilter]] - degree 34, connects to 7 communities
- [[egress_filter()]] - degree 4, connects to 3 communities
- [[egress_filter()_1]] - degree 4, connects to 3 communities
- [[dot-setup_method()_15]] - degree 4, connects to 2 communities
