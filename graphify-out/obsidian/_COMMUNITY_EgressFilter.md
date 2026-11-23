---
type: community
members: 96
---

# EgressFilter

**Members:** 96 nodes

## Members
- [[dot-__init__()_175]] - code - gateway/security/egress_filter.py
- [[dot-_matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[dot-flush_notifications()]] - code - gateway/security/egress_filter.py
- [[dot-get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[dot-is_denylisted()]] - code - gateway/security/egress_config.py
- [[dot-set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[dot-set_event_bus()]] - code - gateway/security/egress_filter.py
- [[dot-set_notifier()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_29]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_roundtrip()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_url_parsing()_1]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[AgentShroud Management Dashboard routes. All manage routes require…]] - rationale - gateway/web/management.py
- [[BaseModel_9]] - code
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[EgressAllowlistResponse]] - code - gateway/web/management.py
- [[EgressAllowlistUpdate]] - code - gateway/web/management.py
- [[EgressFilter]] - code - gateway/security/egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[Falco runtime security alerts viewer.]] - rationale - gateway/web/management.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[GENERATED FILE — do not hand-edit. Feed-source hostnames derived from…]] - rationale - gateway/security/feed_hosts.py
- [[Get current egress allowlist configuration.]] - rationale - gateway/web/management.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Record a time-limited interactive approval for a domain. Called by the Telegram…]] - rationale - gateway/security/egress_filter.py
- [[Request model for updating egress allowlist.]] - rationale - gateway/web/management.py
- [[Response model for egress allowlist.]] - rationale - gateway/web/management.py
- [[Security tools overview — links to all tool-specific dashboards.]] - rationale - gateway/web/management.py
- [[Send pending egress notifications via Telegram. Called from request handler.…]] - rationale - gateway/security/egress_filter.py
- [[Serve the SSH hosts page.]] - rationale - gateway/web/management.py
- [[Serve the approval queue page.]] - rationale - gateway/web/management.py
- [[Serve the audit log page.]] - rationale - gateway/web/management.py
- [[Serve the collaborators page (dynamic — fetches live activity data).]] - rationale - gateway/web/management.py
- [[Serve the emergency kill switch page.]] - rationale - gateway/web/management.py
- [[Serve the main dashboard page.]] - rationale - gateway/web/management.py
- [[Serve the main management dashboard.]] - rationale - gateway/web/management.py
- [[Serve the security modules page (dynamic — fetches live data).]] - rationale - gateway/web/management.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[Set the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test handling of invalid modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that config can be saved and retrieved.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test the management API endpoints (would need FastAPI test client).]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[Update egress allowlist configuration (owner only).]] - rationale - gateway/web/management.py
- [[Wazuh HIDS alerts and FIM events viewer.]] - rationale - gateway/web/management.py
- [[approvals()]] - code - gateway/web/management.py
- [[audit()_1]] - code - gateway/web/management.py
- [[collaborators()]] - code - gateway/web/management.py
- [[dashboard()]] - code - gateway/web/management.py
- [[dashboard_main()]] - code - gateway/web/management.py
- [[egress_config.py_2]] - code - gateway/security/egress_config.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py
- [[egress_filter.py_2]] - code - gateway/security/egress_filter.py
- [[falco_dashboard()]] - code - gateway/web/management.py
- [[feed_hosts.py]] - code - gateway/security/feed_hosts.py
- [[get_3]] - code
- [[get_egress_allowlist()]] - code - gateway/web/management.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[killswitch()_1]] - code - gateway/web/management.py
- [[management.py]] - code - gateway/web/management.py
- [[modules()]] - code - gateway/web/management.py
- [[put_2]] - code
- [[security_overview()]] - code - gateway/web/management.py
- [[set_egress_config()]] - code - gateway/security/egress_config.py
- [[ssh()]] - code - gateway/web/management.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[update_egress_allowlist()]] - code - gateway/web/management.py
- [[wazuh_dashboard()]] - code - gateway/web/management.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilter
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_EgressPolicy]]
- 13 edges to [[_COMMUNITY_dot-_check_impl]]
- 11 edges to [[_COMMUNITY_asyncio_5]]
- 8 edges to [[_COMMUNITY_TestEgressFilterConfig]]
- 7 edges to [[_COMMUNITY_KeyRotationManager]]
- 6 edges to [[_COMMUNITY_TestEgressFilter]]
- 6 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 6 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 6 edges to [[_COMMUNITY_test_security_integration.py]]
- 5 edges to [[_COMMUNITY_test_module_stats.py]]
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 4 edges to [[_COMMUNITY__make_filter]]
- 4 edges to [[_COMMUNITY_middleware.py]]
- 4 edges to [[_COMMUNITY_WebProxy]]
- 4 edges to [[_COMMUNITY_DraftEntry]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TestEgressSSRF]]
- 2 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_test_web_api_coverage.py]]
- 1 edge to [[_COMMUNITY_ingest_apimodels.py]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_fastapi]]

## Top bridge nodes
- [[EgressFilter]] - degree 75, connects to 19 communities
- [[egress_filter.py_2]] - degree 22, connects to 13 communities
- [[EgressFilterConfig]] - degree 65, connects to 10 communities
- [[egress_config.py_2]] - degree 16, connects to 8 communities
- [[management.py]] - degree 30, connects to 6 communities
