---
type: community
members: 41
---

# _make_filter

**Members:** 41 nodes

## Members
- [[dot-test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_domain_passes()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_domain_still_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_ip()_1]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_attempt_fields()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_bare_hostname()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_denied_domain_overrides_allow()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_has_details()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_full_url()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_host_port_format()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_ipv4_mapped_ipv6_blocked()_1]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_localhost_hostname_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_filters_by_agent()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_records_attempts()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_size_limit()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_port_not_allowed()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_blocked_ssrf()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_stats_counts()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unlisted_domain_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unlisted_domain_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_does_not_match_deep_subdomain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_matches_base_domain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_one_level()]] - code - gateway/tests/test_egress_filter.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Create an EgressFilter with a simple config.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter correctly parses URLs, hostport, and bare hostnames.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode should block unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in monitor mode should allow but log unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter records attempts and provides stats.]] - rationale - gateway/tests/test_egress_filter.py
- [[IP allowlist and private-IP SSRF protection.]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs are blocked by default to prevent SSRF.]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[TestEgressAttempt]] - code - gateway/tests/test_egress_filter.py
- [[TestEnforceMode]] - code - gateway/tests/test_egress_filter.py
- [[TestIPRules]] - code - gateway/tests/test_egress_filter.py
- [[TestLogging]] - code - gateway/tests/test_egress_filter.py
- [[TestMonitorMode_1]] - code - gateway/tests/test_egress_filter.py
- [[TestURLParsing]] - code - gateway/tests/test_egress_filter.py
- [[_make_filter()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_filter
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_EgressPolicy]]
- 4 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_asyncio_5]]
- 1 edge to [[_COMMUNITY_dot-_check_impl]]

## Top bridge nodes
- [[_make_filter()]] - degree 32, connects to 3 communities
- [[TestEnforceMode]] - degree 12, connects to 2 communities
- [[TestIPRules]] - degree 11, connects to 2 communities
- [[TestEgressAttempt]] - degree 6, connects to 2 communities
- [[TestLogging]] - degree 7, connects to 1 community
