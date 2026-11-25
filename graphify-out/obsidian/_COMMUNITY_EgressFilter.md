---
type: community
members: 56
---

# EgressFilter

**Members:** 56 nodes

## Members
- [[dot-_check_impl()]] - code - gateway/security/egress_filter.py
- [[dot-_is_ipv6()]] - code - gateway/security/egress_filter.py
- [[dot-_is_private_ip()_2]] - code - gateway/security/egress_filter.py
- [[dot-_matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[dot-_matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[dot-_record()_2]] - code - gateway/security/egress_filter.py
- [[dot-check()_6]] - code - gateway/security/egress_filter.py
- [[dot-check_async()]] - code - gateway/security/egress_filter.py
- [[dot-flush_notifications()]] - code - gateway/security/egress_filter.py
- [[dot-get_log()]] - code - gateway/security/egress_filter.py
- [[dot-get_policy()_1]] - code - gateway/security/egress_filter.py
- [[dot-get_stats()_13]] - code - gateway/security/egress_filter.py
- [[dot-get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[dot-grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[dot-set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[dot-set_event_bus()_2]] - code - gateway/security/egress_filter.py
- [[dot-set_notifier()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_29]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_log()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_stats()_2]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_parsing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed. Args agent_id The agent making…]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP. Covers RFC…]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[EgressFilter]] - code - gateway/security/egress_filter.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80), then…_1]] - rationale - gateway/security/egress_filter.py
- [[Record a time-limited interactive approval for a domain. Called by the Telegram…]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.…]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilter
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_EgressFilterConfig]]
- 12 edges to [[_COMMUNITY_EgressAction]]
- 10 edges to [[_COMMUNITY_EgressPolicy]]
- 5 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 5 edges to [[_COMMUNITY_test_module_stats.py]]
- 4 edges to [[_COMMUNITY__make_filter]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 2 edges to [[_COMMUNITY_TestModuleInstantiationInEnforceMode]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]

## Top bridge nodes
- [[EgressFilter]] - degree 75, connects to 15 communities
- [[TestEgressFilter]] - degree 21, connects to 4 communities
- [[EgressAttempt]] - degree 8, connects to 3 communities
- [[egress_filter()]] - degree 5, connects to 3 communities
- [[egress_filter()_1]] - degree 5, connects to 3 communities
