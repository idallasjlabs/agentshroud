---
type: community
members: 108
---

# EgressFilterConfig

**Members:** 108 nodes

## Members
- [[dot-__init__()_105]] - code - gateway/security/egress_filter.py
- [[dot-_matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[dot-from_environment()]] - code - gateway/security/egress_config.py
- [[dot-get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-is_denylisted()]] - code - gateway/security/egress_config.py
- [[dot-matches_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-test_config_roundtrip()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_default_config()_3]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressAllowlistResponse]] - code - gateway/web/management.py
- [[EgressAllowlistUpdate]] - code - gateway/web/management.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[EgressFilterConfig_1]] - code - gateway/security/egress_filter.py
- [[FEED_HOSTS]] - code - gateway/security/feed_hosts.py
- [[Falco runtime security alerts viewer.]] - rationale - gateway/web/management.py
- [[Get current egress allowlist configuration.]] - rationale - gateway/web/management.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[PERMANENT_EGRESS_DOMAINS]] - code - gateway/security/egress_config.py
- [[PERMANENT_EGRESS_DOMAINS canonical allowlist]] - code - gateway/security/egress_config.py
- [[Public does domain match any pattern in the effective default allowlist…]] - rationale - gateway/security/egress_config.py
- [[Request model for updating egress allowlist.]] - rationale - gateway/web/management.py
- [[Response model for egress allowlist.]] - rationale - gateway/web/management.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard). Single…]] - rationale - gateway/security/egress_config.py
- [[Security tools overview — links to all tool-specific dashboards.]] - rationale - gateway/web/management.py
- [[Serve the SSH hosts page.]] - rationale - gateway/web/management.py
- [[Serve the approval queue page.]] - rationale - gateway/web/management.py
- [[Serve the audit log page.]] - rationale - gateway/web/management.py
- [[Serve the collaborators page (dynamic — fetches live activity data).]] - rationale - gateway/web/management.py
- [[Serve the emergency kill switch page.]] - rationale - gateway/web/management.py
- [[Serve the main dashboard page.]] - rationale - gateway/web/management.py
- [[Serve the main management dashboard.]] - rationale - gateway/web/management.py
- [[Serve the security modules page (dynamic — fetches live data).]] - rationale - gateway/web/management.py
- [[Set the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._2]] - rationale - gateway/tests/test_egress_enforce.py
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
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[Update egress allowlist configuration (owner only).]] - rationale - gateway/web/management.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py
- [[Wazuh HIDS alerts and FIM events viewer.]] - rationale - gateway/web/management.py
- [[approvals()]] - code - gateway/web/management.py
- [[audit()_1]] - code - gateway/web/management.py
- [[collaborators()]] - code - gateway/web/management.py
- [[dashboard()]] - code - gateway/web/management.py
- [[dashboard.html (Control Center Template)]] - code - gateway/web/templates/dashboard.html
- [[dashboard_main()]] - code - gateway/web/management.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[egress_config.py]] - code - gateway/security/egress_config.py
- [[falco_dashboard()]] - code - gateway/web/management.py
- [[get_egress_allowlist()]] - code - gateway/web/management.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[killswitch()]] - code - gateway/web/management.py
- [[management.py]] - code - gateway/web/management.py
- [[modules()]] - code - gateway/web/management.py
- [[security_overview()]] - code - gateway/web/management.py
- [[set_egress_config()]] - code - gateway/security/egress_config.py
- [[ssh()]] - code - gateway/web/management.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[update_egress_allowlist()]] - code - gateway/web/management.py
- [[wazuh_dashboard()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 46 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 34 edges to [[_COMMUNITY_EgressFilterConfig (3)]]
- 10 edges to [[_COMMUNITY_AlertDispatcher (2) (2)]]
- 6 edges to [[_COMMUNITY_KeyRotationManager (2)_1]]
- 4 edges to [[_COMMUNITY_egress_filter.py]]
- 4 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (2)_1]]
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 3 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 3 edges to [[_COMMUNITY_WebProxy]]
- 3 edges to [[_COMMUNITY_UserSessionManager]]
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (4)]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_ContextSegment (2)]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (4)]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_WebProxyConfig]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[EgressAction]] - degree 45, connects to 14 communities
- [[EgressFilterConfig]] - degree 103, connects to 12 communities
- [[egress_config.py]] - degree 12, connects to 6 communities
- [[management.py]] - degree 26, connects to 4 communities
- [[EgressAllowlistResponse]] - degree 6, connects to 3 communities
