---
type: community
members: 94
---

# Community 282

**Members:** 94 nodes

## Members
- [[.__init__()_75]] - code - gateway/security/egress_filter.py
- [[._matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[.flush_notifications()]] - code - gateway/security/egress_filter.py
- [[.get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[.grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[.is_denylisted()]] - code - gateway/security/egress_config.py
- [[.set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[.set_event_bus()_2]] - code - gateway/security/egress_filter.py
- [[.set_notifier()]] - code - gateway/security/egress_filter.py
- [[.setup_method()_29]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_default_config()_1]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[.test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[.test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[.test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[.test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[.test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_log()]] - code - gateway/tests/test_security_hardening.py
- [[.test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[.test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_stats()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressFilter_1]] - code - gateway/security/egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[EgressFilterConfig_1]] - code - gateway/security/egress_filter.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py
- [[OpenClaw researchweb_search domains pre-approved after 210-denial SOC saturation incident]] - rationale - gateway/tests/test_egress_filter.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._1]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist wildcard matching.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test handling of invalid modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test specific egress mode environment variable.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test the management API endpoints (would need FastAPI test client).]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_282
SORT file.name ASC
```

## Connections to other communities
- 46 edges to [[_COMMUNITY_Community 53]]
- 22 edges to [[_COMMUNITY_Community 35]]
- 22 edges to [[_COMMUNITY_Community 118]]
- 15 edges to [[_COMMUNITY_Community 33]]
- 14 edges to [[_COMMUNITY_Community 6]]
- 14 edges to [[_COMMUNITY_Community 14]]
- 13 edges to [[_COMMUNITY_Community 251]]
- 8 edges to [[_COMMUNITY_Community 256]]
- 7 edges to [[_COMMUNITY_Community 74]]
- 6 edges to [[_COMMUNITY_Community 28]]
- 4 edges to [[_COMMUNITY_Community 66]]
- 4 edges to [[_COMMUNITY_Community 782]]
- 4 edges to [[_COMMUNITY_Community 60]]
- 4 edges to [[_COMMUNITY_Community 116]]
- 4 edges to [[_COMMUNITY_Community 212]]
- 3 edges to [[_COMMUNITY_Community 55]]
- 3 edges to [[_COMMUNITY_Community 94]]
- 3 edges to [[_COMMUNITY_Community 271]]
- 2 edges to [[_COMMUNITY_Community 78]]
- 2 edges to [[_COMMUNITY_Community 30]]
- 2 edges to [[_COMMUNITY_Community 133]]
- 2 edges to [[_COMMUNITY_Community 870]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 176]]
- 1 edge to [[_COMMUNITY_Community 557]]
- 1 edge to [[_COMMUNITY_Community 444]]
- 1 edge to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 1857]]
- 1 edge to [[_COMMUNITY_Community 22]]

## Top bridge nodes
- [[EgressFilter_1]] - degree 104, connects to 22 communities
- [[EgressFilterConfig]] - degree 101, connects to 20 communities
- [[EgressAction]] - degree 45, connects to 17 communities
- [[TestEgressFilter]] - degree 34, connects to 7 communities
- [[TestOpenClawResearchDomainsAllowlisted]] - degree 11, connects to 3 communities