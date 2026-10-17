---
type: community
members: 89
---

# EgressFilterConfig (3)

**Members:** 89 nodes

## Members
- [[dot-__init__()_158]] - code - gateway/security/prompt_guard.py
- [[dot-_check_impl()]] - code - gateway/security/egress_filter.py
- [[dot-_is_ipv6()]] - code - gateway/security/egress_filter.py
- [[dot-_is_private_ip()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[dot-_record()_1]] - code - gateway/security/egress_filter.py
- [[dot-check()_4]] - code - gateway/security/egress_filter.py
- [[dot-check_async()]] - code - gateway/security/egress_filter.py
- [[dot-flush_notifications()]] - code - gateway/security/egress_filter.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_policy()_1]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_16]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[dot-grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[dot-matches_domain()]] - code - gateway/security/egress_filter.py
- [[dot-matches_ip()]] - code - gateway/security/egress_filter.py
- [[dot-matches_port()]] - code - gateway/security/egress_filter.py
- [[dot-set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[dot-set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[dot-set_event_bus()_1]] - code - gateway/security/egress_filter.py
- [[dot-set_notifier()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_29]] - code - gateway/tests/test_security_hardening.py
- [[dot-setup_method()_30]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_log()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_stats()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[Args             block_threshold Score at or above which input is blocked.]] - rationale - gateway/security/prompt_guard.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed.          Args             agent_id]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards).          Wildca]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP.          Cover]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[EgressFilter_2]] - code - gateway/security/egress_filter.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the_1]] - rationale - gateway/security/egress_filter.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig_3
SORT file.name ASC
```

## Connections to other communities
- 46 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 34 edges to [[_COMMUNITY_EgressFilterConfig]]
- 33 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 25 edges to [[_COMMUNITY_TrustConfig]]
- 21 edges to [[_COMMUNITY_AgentRegistry]]
- 15 edges to [[_COMMUNITY_ContextSegment]]
- 8 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 4 edges to [[_COMMUNITY_ContextSegment (2)]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (2)_1]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (4)]]
- 3 edges to [[_COMMUNITY_main.py_1]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (4)]]
- 2 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_DataExfilVolumeGuard]]
- 1 edge to [[_COMMUNITY_migrate-cve-registry-ghsa.py]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 1 edge to [[_COMMUNITY_TestSSRFDetection]]

## Top bridge nodes
- [[EgressFilter_2]] - degree 103, connects to 20 communities
- [[test_security_hardening.py]] - degree 30, connects to 9 communities
- [[TestSecureZero]] - degree 23, connects to 7 communities
- [[TestEgressFilter]] - degree 34, connects to 6 communities
- [[TestEgressSSRF]] - degree 28, connects to 6 communities
