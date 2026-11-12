---
type: community
members: 55
---

# Community 1119

**Members:** 55 nodes

## Members
- [[._check_impl()]] - code - gateway/security/egress_filter.py
- [[._is_ipv6()]] - code - gateway/security/egress_filter.py
- [[._is_private_ip()_2]] - code - gateway/security/egress_filter.py
- [[._matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[._matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[._record()_2]] - code - gateway/security/egress_filter.py
- [[.check()_5]] - code - gateway/security/egress_filter.py
- [[.check_async()]] - code - gateway/security/egress_filter.py
- [[.flush_notifications()]] - code - gateway/security/egress_filter.py
- [[.get_log()]] - code - gateway/security/egress_filter.py
- [[.get_policy()]] - code - gateway/security/egress_filter.py
- [[.get_stats()_16]] - code - gateway/security/egress_filter.py
- [[.get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[.grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[.set_approval_queue()]] - code - gateway/security/egress_filter.py
- [[.set_event_bus()_2]] - code - gateway/security/egress_filter.py
- [[.set_notifier()]] - code - gateway/security/egress_filter.py
- [[.setup_method()_29]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[.test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[.test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[.test_log()]] - code - gateway/tests/test_security_hardening.py
- [[.test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[.test_stats()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[Async egress check with interactive approval for unknown domains.]] - rationale - gateway/security/egress_filter.py
- [[Check if IP matches any IPCIDR in the list.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed.          Args             agent_id]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP.          Cover]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt]] - code - gateway/security/egress_filter.py
- [[EgressFilter_1]] - code - gateway/security/egress_filter.py
- [[Filter outbound connections based on allowlists with enforcemonitor modes.]] - rationale - gateway/security/egress_filter.py
- [[Get effective policy for an agent.]] - rationale - gateway/security/egress_filter.py
- [[Get egress attempt log, optionally filtered by agent.]] - rationale - gateway/security/egress_filter.py
- [[Get summary statistics of egress attempts.]] - rationale - gateway/security/egress_filter.py
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the]] - rationale - gateway/security/egress_filter.py
- [[Record a time-limited interactive approval for a domain.          Called by the]] - rationale - gateway/security/egress_filter.py
- [[Return top destination domains by volume.]] - rationale - gateway/security/egress_filter.py
- [[Send pending egress notifications via Telegram. Called from request handler.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1119
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_Community 21]]
- 21 edges to [[_COMMUNITY_Community 17]]
- 20 edges to [[_COMMUNITY_Community 93]]
- 13 edges to [[_COMMUNITY_Community 7]]
- 8 edges to [[_COMMUNITY_Community 72]]
- 7 edges to [[_COMMUNITY_Community 52]]
- 6 edges to [[_COMMUNITY_Community 300]]
- 5 edges to [[_COMMUNITY_Community 162]]
- 3 edges to [[_COMMUNITY_Community 94]]
- 2 edges to [[_COMMUNITY_Community 85]]
- 2 edges to [[_COMMUNITY_Community 73]]
- 2 edges to [[_COMMUNITY_Community 2004]]
- 2 edges to [[_COMMUNITY_Community 1002]]
- 2 edges to [[_COMMUNITY_Community 123]]
- 2 edges to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 27]]
- 1 edge to [[_COMMUNITY_Community 1000]]
- 1 edge to [[_COMMUNITY_Community 205]]
- 1 edge to [[_COMMUNITY_Community 888]]
- 1 edge to [[_COMMUNITY_Community 792]]
- 1 edge to [[_COMMUNITY_Community 947]]
- 1 edge to [[_COMMUNITY_Community 265]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 11]]

## Top bridge nodes
- [[EgressFilter_1]] - degree 103, connects to 20 communities
- [[TestEgressFilter]] - degree 34, connects to 9 communities
- [[EgressAttempt]] - degree 22, connects to 5 communities
- [[._record()_2]] - degree 6, connects to 2 communities
- [[.setup_method()_29]] - degree 4, connects to 2 communities