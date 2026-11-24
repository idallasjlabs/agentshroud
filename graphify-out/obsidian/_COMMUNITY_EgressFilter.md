---
type: community
members: 140
---

# EgressFilter

**Members:** 140 nodes

## Members
- [[dot-__init__()_172]] - code - gateway/security/egress_filter.py
- [[dot-_check_impl()]] - code - gateway/security/egress_filter.py
- [[dot-_is_ipv6()]] - code - gateway/security/egress_filter.py
- [[dot-_is_private_ip()_2]] - code - gateway/security/egress_filter.py
- [[dot-_matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[dot-_matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[dot-_record()_2]] - code - gateway/security/egress_filter.py
- [[dot-check()_5]] - code - gateway/security/egress_filter.py
- [[dot-check_async()]] - code - gateway/security/egress_filter.py
- [[dot-flush_notifications()]] - code - gateway/security/egress_filter.py
- [[dot-get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_policy()_1]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_12]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[dot-grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[dot-is_denylisted()]] - code - gateway/security/egress_config.py
- [[dot-set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[dot-set_event_bus()_2]] - code - gateway/security/egress_filter.py
- [[dot-set_notifier()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_30]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_config_roundtrip()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_log()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_stats()_2]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[A domain with an active timed approval should be allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[An expired timed approval should be evicted and the domain denied.]] - rationale - gateway/tests/test_egress_filter.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if an outbound connection is allowed. Args agent_id The agent making…]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Check if host is a private, loopback, link-local, or reserved IP. Covers RFC…]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter]] - code - gateway/security/egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[Enum_38]] - code
- [[Even if trust allows an action, egress filter blocks unauthorized destinations.]] - rationale - gateway/tests/test_security_integration.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[GENERATED FILE — do not hand-edit. Feed-source hostnames derived from…]] - rationale - gateway/security/feed_hosts.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed by the…]] - rationale - gateway/tests/test_egress_filter.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80), then…_1]] - rationale - gateway/security/egress_filter.py
- [[Record a time-limited interactive approval for a domain. Called by the Telegram…]] - rationale - gateway/security/egress_filter.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard). Single…]] - rationale - gateway/security/egress_config.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.…]] - rationale - gateway/security/egress_filter.py
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
- [[TestEgressAttempt]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved. These…]] - rationale - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[egress_config.py_2]] - code - gateway/security/egress_config.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py
- [[egress_filter.py_2]] - code - gateway/security/egress_filter.py
- [[feed_hosts.py]] - code - gateway/security/feed_hosts.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[grant_timed_approval should purge expired entries on each call.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval with a malformed date should not raise or store anything.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.mail.me.com587.]] - rationale - gateway/tests/test_egress_filter.py
- [[set_egress_config()]] - code - gateway/security/egress_config.py
- [[str_21]] - code
- [[test_egress_blocks_unauthorized_after_trust_check()]] - code - gateway/tests/test_security_integration.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[test_egress_filter.py]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_allows_domain()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_cleans_stale_entries()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_invalid_iso_is_ignored()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilter
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_EgressPolicy]]
- 17 edges to [[_COMMUNITY__make_filter]]
- 17 edges to [[_COMMUNITY_asyncio_4]]
- 9 edges to [[_COMMUNITY_test_security_integration.py]]
- 8 edges to [[_COMMUNITY_lifespan.py]]
- 8 edges to [[_COMMUNITY_test_module_stats.py]]
- 8 edges to [[_COMMUNITY_TestEgressFilterConfig]]
- 8 edges to [[_COMMUNITY_management.py]]
- 7 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 6 edges to [[_COMMUNITY_TrustManager]]
- 6 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 5 edges to [[_COMMUNITY_AgentRegistry]]
- 5 edges to [[_COMMUNITY_run]]
- 5 edges to [[_COMMUNITY_WebProxy]]
- 3 edges to [[_COMMUNITY_egress_approval.py]]
- 3 edges to [[_COMMUNITY_make_event]]
- 2 edges to [[_COMMUNITY_PathIsolationManager]]
- 2 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_dot-verify_entry]]

## Top bridge nodes
- [[EgressFilter]] - degree 75, connects to 14 communities
- [[EgressFilterConfig]] - degree 65, connects to 10 communities
- [[egress_filter.py_2]] - degree 22, connects to 10 communities
- [[EgressAction]] - degree 36, connects to 8 communities
- [[egress_config.py_2]] - degree 16, connects to 8 communities
