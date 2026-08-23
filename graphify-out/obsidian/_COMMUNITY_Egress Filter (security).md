---
type: community
cohesion: 0.03
members: 81
---

# Egress Filter (security)

**Cohesion:** 0.03 - loosely connected
**Members:** 81 nodes

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
- [[.test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_egress_filter_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[.test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_log()]] - code - gateway/tests/test_security_hardening.py
- [[.test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[.test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_stats()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
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
- [[Set interactive egress approval queue.]] - rationale - gateway/security/egress_filter.py
- [[Set optional event bus for real-time egress telemetry.]] - rationale - gateway/security/egress_filter.py
- [[Set the Telegram notifier for egress approval requests.]] - rationale - gateway/security/egress_filter.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Filter_security
SORT file.name ASC
```

## Connections to other communities
- 39 edges to [[_COMMUNITY_Egress Filter]]
- 15 edges to [[_COMMUNITY_Egress Filter]]
- 14 edges to [[_COMMUNITY_Egress Filter]]
- 11 edges to [[_COMMUNITY_Security Hardening]]
- 10 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 7 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 5 edges to [[_COMMUNITY_Module Stats]]
- 4 edges to [[_COMMUNITY_Security Hardening]]
- 3 edges to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 3 edges to [[_COMMUNITY_System overview (00 - START HERE)]]
- 3 edges to [[_COMMUNITY_E2e Proxy]]
- 2 edges to [[_COMMUNITY_Soc Egress Endpoints]]
- 2 edges to [[_COMMUNITY_Redteam Probes]]
- 1 edge to [[_COMMUNITY_Url Analyzer]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Data Exfil Volume Guard]]
- 1 edge to [[_COMMUNITY_All Modules Enforce]]
- 1 edge to [[_COMMUNITY_Egress Enforce]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_A2a Policy (security)]]
- 1 edge to [[_COMMUNITY_Migrate Cve Registry Ghsa (scripts)]]
- 1 edge to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Progressive Trust Integration]]
- 1 edge to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 1 edge to [[_COMMUNITY_Security Regressions V1 2]]

## Top bridge nodes
- [[EgressFilter_1]] - degree 104, connects to 18 communities
- [[TestEgressFilter]] - degree 34, connects to 10 communities
- [[EgressAttempt]] - degree 22, connects to 4 communities
- [[._record()_1]] - degree 6, connects to 2 communities
- [[.setup_method()_29]] - degree 4, connects to 2 communities