---
type: community
cohesion: 0.02
members: 133
---

# EgressFilterConfig

**Cohesion:** 0.02 - loosely connected
**Members:** 133 nodes

## Members
- [[dot-__init__()_120]] - code - gateway/security/egress_filter.py
- [[dot-_matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[dot-flush_notifications()]] - code - gateway/security/egress_filter.py
- [[dot-from_environment()]] - code - gateway/security/egress_config.py
- [[dot-get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_8]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[dot-grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[dot-is_denylisted()]] - code - gateway/security/egress_config.py
- [[dot-matches_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[dot-set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[dot-set_event_bus()]] - code - gateway/security/egress_filter.py
- [[dot-set_notifier()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_26]] - code - gateway/tests/test_security_hardening.py
- [[dot-setup_method()_27]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_roundtrip()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_default_config()_5]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_log()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_stats()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressFilter_1]] - code - gateway/security/egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[FEED_HOSTS]] - code - gateway/security/feed_hosts.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py
- [[PERMANENT_EGRESS_DOMAINS]] - code - gateway/security/egress_config.py
- [[PERMANENT_EGRESS_DOMAINS canonical allowlist]] - code - gateway/security/egress_config.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[Public does domain match any pattern in the effective default allowlist…]] - rationale - gateway/security/egress_config.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard). Single…]] - rationale - gateway/security/egress_config.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[Set the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._3]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist wildcard matching.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test handling of invalid modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test specific egress mode environment variable.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that config can be saved and retrieved.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test the management API endpoints (would need FastAPI test client).]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[Update egress allowlist configuration (owner only).]] - rationale - gateway/web/management.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[egress_config.py]] - code - gateway/security/egress_config.py
- [[egress_filter()]] - code - gateway/tests/test_security_integration.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[set_egress_config()]] - code - gateway/security/egress_config.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py
- [[update_egress_allowlist()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 87 edges to [[_COMMUNITY_EgressFilterConfig_1]]
- 23 edges to [[_COMMUNITY_AgentRegistry]]
- 21 edges to [[_COMMUNITY_TrustConfig]]
- 20 edges to [[_COMMUNITY_AlertDispatcher]]
- 16 edges to [[_COMMUNITY_KillSwitchMonitor_1]]
- 12 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py_1]]
- 10 edges to [[_COMMUNITY_MiddlewareManager_8]]
- 9 edges to [[_COMMUNITY_ContextSegment]]
- 8 edges to [[_COMMUNITY_EgressFilterConfig_2]]
- 8 edges to [[_COMMUNITY_MiddlewareManager_3]]
- 8 edges to [[_COMMUNITY_egress_filter.py]]
- 8 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 7 edges to [[_COMMUNITY_TestSSRFDetection_1]]
- 6 edges to [[_COMMUNITY_TestPathIsolationManager]]
- 6 edges to [[_COMMUNITY_AuditChain]]
- 5 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_1]]
- 5 edges to [[_COMMUNITY_CrossBotTrustLedger_1]]
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 3 edges to [[_COMMUNITY_WebProxy]]
- 3 edges to [[_COMMUNITY_main.py]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager_2]]
- 1 edge to [[_COMMUNITY_ResourceGuard_1]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_DataExfilVolumeGuard]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_migrate-cve-registry-ghsa.py]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_TestSSRFDetection]]

## Top bridge nodes
- [[EgressFilter_1]] - degree 103, connects to 19 communities
- [[EgressFilterConfig]] - degree 103, connects to 16 communities
- [[EgressAction]] - degree 45, connects to 14 communities
- [[test_security_hardening.py]] - degree 30, connects to 11 communities
- [[TestEgressFilter]] - degree 34, connects to 8 communities
