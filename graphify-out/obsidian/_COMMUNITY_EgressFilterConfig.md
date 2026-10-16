---
type: community
cohesion: 0.05
members: 57
---

# EgressFilterConfig

**Cohesion:** 0.05 - loosely connected
**Members:** 57 nodes

## Members
- [[dot-__init__()_194]] - code - gateway/security/egress_filter.py
- [[dot-_matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[dot-from_environment()]] - code - gateway/security/egress_config.py
- [[dot-get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-is_denylisted()]] - code - gateway/security/egress_config.py
- [[dot-test_config_roundtrip()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_default_config()_8]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilterConfig_1]] - code - gateway/security/egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[FEED_HOSTS]] - code - gateway/security/feed_hosts.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[PERMANENT_EGRESS_DOMAINS]] - code - gateway/security/egress_config.py
- [[PERMANENT_EGRESS_DOMAINS canonical allowlist]] - code - gateway/security/egress_config.py
- [[Rule agentshroud-ssrf-httpx]] - concept - .semgrep.yml
- [[Rule agentshroud-ssrf-requests]] - concept - .semgrep.yml
- [[Set the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._5]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist wildcard matching.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test handling of invalid modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test specific egress mode environment variable.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that config can be saved and retrieved.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test the management API endpoints (would need FastAPI test client).]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[Update egress allowlist configuration (owner only).]] - rationale - gateway/web/management.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py
- [[egress_config.py_2]] - code - gateway/security/egress_config.py
- [[egress_filter.py_1]] - code - gateway/security/egress_filter.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[set_egress_config()]] - code - gateway/security/egress_config.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[update_egress_allowlist()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_EgressFilter]]
- 21 edges to [[_COMMUNITY_AgentRegistry]]
- 20 edges to [[_COMMUNITY__make_filter]]
- 13 edges to [[_COMMUNITY_test_egress_filter.py]]
- 13 edges to [[_COMMUNITY_EgressPolicy]]
- 8 edges to [[_COMMUNITY_GitGuard]]
- 7 edges to [[_COMMUNITY_management.py]]
- 5 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 4 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_EgressAttempt]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY_Enum]]
- 3 edges to [[_COMMUNITY_WebProxyConfig]]
- 3 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_WebProxy]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_TestEgressSSRF]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_agentshroud.yaml]]
- 2 edges to [[_COMMUNITY_AgentShroud Semgrep SAST Configuration]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_dot-analyze_message]]
- 1 edge to [[_COMMUNITY_DataExfilVolumeGuard]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_A2AMethod]]
- 1 edge to [[_COMMUNITY_AGENTSHROUD_MODE]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_DataLedger]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]

## Top bridge nodes
- [[egress_filter.py_1]] - degree 27, connects to 20 communities
- [[EgressFilterConfig]] - degree 103, connects to 15 communities
- [[EgressAction]] - degree 45, connects to 13 communities
- [[egress_config.py_2]] - degree 12, connects to 6 communities
- [[TestOpenClawResearchDomainsAllowlisted]] - degree 11, connects to 5 communities
