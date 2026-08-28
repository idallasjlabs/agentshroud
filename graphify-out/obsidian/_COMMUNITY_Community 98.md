---
type: community
cohesion: 0.05
members: 58
---

# Community 98

**Cohesion:** 0.05 - loosely connected
**Members:** 58 nodes

## Members
- [[.test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_passes()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_still_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_ip()]] - code - gateway/tests/test_egress_filter.py
- [[.test_attempt_fields()]] - code - gateway/tests/test_egress_filter.py
- [[.test_bare_hostname()]] - code - gateway/tests/test_egress_filter.py
- [[.test_denied_domain_overrides_allow()]] - code - gateway/tests/test_egress_filter.py
- [[.test_deny_has_details()]] - code - gateway/tests/test_egress_filter.py
- [[.test_emits_egress_event_to_event_bus()]] - code - gateway/tests/test_egress_filter.py
- [[.test_full_url()]] - code - gateway/tests/test_egress_filter.py
- [[.test_host_port_format()]] - code - gateway/tests/test_egress_filter.py
- [[.test_ipv4_mapped_ipv6_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[.test_localhost_hostname_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[.test_log_filters_by_agent()]] - code - gateway/tests/test_egress_filter.py
- [[.test_log_records_attempts()]] - code - gateway/tests/test_egress_filter.py
- [[.test_log_size_limit()]] - code - gateway/tests/test_egress_filter.py
- [[.test_port_not_allowed()]] - code - gateway/tests/test_egress_filter.py
- [[.test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[.test_private_ip_blocked_ssrf()]] - code - gateway/tests/test_egress_filter.py
- [[.test_stats_counts()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unknown_domain_allowed_when_approved()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unknown_domain_denied_when_denied()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unlisted_domain_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unlisted_domain_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[.test_wildcard_does_not_match_deep_subdomain()]] - code - gateway/tests/test_egress_filter.py
- [[.test_wildcard_matches_base_domain()]] - code - gateway/tests/test_egress_filter.py
- [[.test_wildcard_one_level()]] - code - gateway/tests/test_egress_filter.py
- [[A domain with an active timed approval should be allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[An expired timed approval should be evicted and the domain denied.]] - rationale - gateway/tests/test_egress_filter.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Create an EgressFilter with a simple config.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter correctly parses URLs, hostport, and bare hostnames.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode should block unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in monitor mode should allow but log unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter records attempts and provides stats.]] - rationale - gateway/tests/test_egress_filter.py
- [[IP allowlist and private-IP SSRF protection.]] - rationale - gateway/tests/test_egress_filter.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs are blocked by default to prevent SSRF.]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[TestEgressAttempt]] - code - gateway/tests/test_egress_filter.py
- [[TestEnforceMode]] - code - gateway/tests/test_egress_filter.py
- [[TestIPRules]] - code - gateway/tests/test_egress_filter.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestLogging]] - code - gateway/tests/test_egress_filter.py
- [[TestMonitorMode]] - code - gateway/tests/test_egress_filter.py
- [[TestURLParsing]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[_make_filter()]] - code - gateway/tests/test_egress_filter.py
- [[grant_timed_approval should purge expired entries on each call.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval with a malformed date should not raise or store anything.]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_filter.py]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_allows_domain()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_cleans_stale_entries()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_invalid_iso_is_ignored()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_98
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_Community 50]]
- 18 edges to [[_COMMUNITY_Community 78]]
- 15 edges to [[_COMMUNITY_Community 217]]
- 9 edges to [[_COMMUNITY_Community 20]]
- 2 edges to [[_COMMUNITY_Community 103]]

## Top bridge nodes
- [[test_egress_filter.py]] - degree 29, connects to 4 communities
- [[TestEnforceMode]] - degree 16, connects to 4 communities
- [[TestIPRules]] - degree 14, connects to 4 communities
- [[TestInteractiveApproval]] - degree 12, connects to 4 communities
- [[TestLogging]] - degree 12, connects to 4 communities