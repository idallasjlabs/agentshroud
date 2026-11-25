---
type: community
members: 69
---

# EgressFilterConfig

**Members:** 69 nodes

## Members
- [[dot-__init__()_220]] - code - gateway/security/egress_filter.py
- [[dot-_matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[dot-from_environment()]] - code - gateway/security/egress_config.py
- [[dot-get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-is_denylisted()]] - code - gateway/security/egress_config.py
- [[dot-test_config_roundtrip()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_default_config()_6]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_defaults_to_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_url_parsing()_1]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[GENERATED FILE — do not hand-edit. Feed-source hostnames derived from…]] - rationale - gateway/security/feed_hosts.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard). Single…]] - rationale - gateway/security/egress_config.py
- [[Set the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._4]] - rationale - gateway/tests/test_egress_enforce.py
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
- [[TestEgressConfigDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[Update egress allowlist configuration (owner only).]] - rationale - gateway/web/management.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[egress_config.py_2]] - code - gateway/security/egress_config.py
- [[egress_filter.py_2]] - code - gateway/security/egress_filter.py
- [[feed_hosts.py]] - code - gateway/security/feed_hosts.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[put_3]] - code
- [[set_egress_config()]] - code - gateway/security/egress_config.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[update_egress_allowlist()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_EgressFilter]]
- 21 edges to [[_COMMUNITY_EgressAction]]
- 7 edges to [[_COMMUNITY_management.py]]
- 6 edges to [[_COMMUNITY_EgressPolicy]]
- 4 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 4 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 1 edge to [[_COMMUNITY__make_filter]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_dot-verify_entry]]
- 1 edge to [[_COMMUNITY_test_module_stats.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_ApprovalMode]]
- 1 edge to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]

## Top bridge nodes
- [[egress_filter.py_2]] - degree 22, connects to 12 communities
- [[EgressFilterConfig]] - degree 65, connects to 11 communities
- [[egress_config.py_2]] - degree 16, connects to 8 communities
- [[domain_matches()]] - degree 8, connects to 4 communities
- [[TestEgressFilterEnforcement]] - degree 14, connects to 2 communities
