---
type: community
cohesion: 0.04
members: 65
---

# Community 78

**Cohesion:** 0.04 - loosely connected
**Members:** 65 nodes

## Members
- [[._check_impl()]] - code - gateway/security/egress_filter.py
- [[._is_ipv6()]] - code - gateway/security/egress_filter.py
- [[._is_private_ip()_2]] - code - gateway/security/egress_filter.py
- [[._matches_allowlist_domain()]] - code - gateway/security/egress_filter.py
- [[._matches_ip_list()]] - code - gateway/security/egress_filter.py
- [[._record()_1]] - code - gateway/security/egress_filter.py
- [[.check()_5]] - code - gateway/security/egress_filter.py
- [[.check_async()]] - code - gateway/security/egress_filter.py
- [[.flush_notifications()]] - code - gateway/security/egress_filter.py
- [[.get_log()]] - code - gateway/security/egress_filter.py
- [[.get_policy()]] - code - gateway/security/egress_filter.py
- [[.get_stats()_16]] - code - gateway/security/egress_filter.py
- [[.get_top_destinations()]] - code - gateway/security/egress_filter.py
- [[.grant_timed_approval()]] - code - gateway/security/egress_filter.py
- [[.matches_domain()]] - code - gateway/security/egress_filter.py
- [[.matches_ip()]] - code - gateway/security/egress_filter.py
- [[.matches_port()]] - code - gateway/security/egress_filter.py
- [[.set_agent_policy()]] - code - gateway/security/egress_filter.py
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
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if an outbound connection is allowed.          Args             agent_id]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards).          Wildca]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any domain in the allowlist (supports wildcards).]] - rationale - gateway/security/egress_filter.py
- [[Check if host is a private, loopback, link-local, or reserved IP.          Cover]] - rationale - gateway/security/egress_filter.py
- [[Check if host looks like an IPv6 address.]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
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
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_78
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 50]]
- 18 edges to [[_COMMUNITY_Community 98]]
- 17 edges to [[_COMMUNITY_Community 217]]
- 10 edges to [[_COMMUNITY_Community 30]]
- 9 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 6 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 6 edges to [[_COMMUNITY_Community 227]]
- 5 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 4 edges to [[_COMMUNITY_Community 51]]
- 4 edges to [[_COMMUNITY_Community 28]]
- 3 edges to [[_COMMUNITY_Community 85]]
- 3 edges to [[_COMMUNITY_Progressive Trust]]
- 2 edges to [[_COMMUNITY_Community 21]]
- 2 edges to [[_COMMUNITY_Community 48]]
- 2 edges to [[_COMMUNITY_Community 174]]
- 2 edges to [[_COMMUNITY_Community 420]]
- 2 edges to [[_COMMUNITY_Community 157]]
- 2 edges to [[_COMMUNITY_Community 116]]
- 1 edge to [[_COMMUNITY_Community 26]]
- 1 edge to [[_COMMUNITY_Community 181]]
- 1 edge to [[_COMMUNITY_Community 246]]

## Top bridge nodes
- [[EgressFilter_1]] - degree 104, connects to 18 communities
- [[TestEgressFilter]] - degree 34, connects to 7 communities
- [[EgressAttempt]] - degree 22, connects to 4 communities
- [[egress_filter()]] - degree 4, connects to 3 communities
- [[egress_filter()_1]] - degree 4, connects to 3 communities