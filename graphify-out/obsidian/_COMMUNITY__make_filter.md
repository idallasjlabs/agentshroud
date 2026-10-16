---
type: community
cohesion: 0.07
members: 50
---

# _make_filter

**Cohesion:** 0.07 - loosely connected
**Members:** 50 nodes

## Members
- [[dot-test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_domain_passes()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_domain_still_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_ip()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_attempt_fields()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_bare_hostname()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_denied_domain_overrides_allow()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_has_details()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_emits_egress_event_to_event_bus()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_full_url()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_host_port_format()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_ipv4_mapped_ipv6_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_localhost_hostname_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_filters_by_agent()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_records_attempts()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_size_limit()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_port_not_allowed()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_blocked_ssrf()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_stats_counts()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_allowed_when_approved()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_denied_when_denied()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unlisted_domain_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unlisted_domain_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_does_not_match_deep_subdomain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_matches_base_domain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_one_level()]] - code - gateway/tests/test_egress_filter.py
- [[ApprovalResult]] - code - gateway/security/egress_approval.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Create an EgressFilter with a simple config.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter correctly parses URLs, hostport, and bare hostnames.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode should block unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in monitor mode should allow but log unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter records attempts and provides stats.]] - rationale - gateway/tests/test_egress_filter.py
- [[IP allowlist and private-IP SSRF protection.]] - rationale - gateway/tests/test_egress_filter.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs are blocked by default to prevent SSRF.]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[Result of an approval request.]] - rationale - gateway/security/egress_approval.py
- [[TestEgressAttempt]] - code - gateway/tests/test_egress_filter.py
- [[TestEnforceMode]] - code - gateway/tests/test_egress_filter.py
- [[TestIPRules]] - code - gateway/tests/test_egress_filter.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestLogging]] - code - gateway/tests/test_egress_filter.py
- [[TestMonitorMode]] - code - gateway/tests/test_egress_filter.py
- [[TestURLParsing]] - code - gateway/tests/test_egress_filter.py
- [[_make_filter()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_filter
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_EgressFilterConfig]]
- 18 edges to [[_COMMUNITY_EgressPolicy]]
- 17 edges to [[_COMMUNITY_test_egress_filter.py]]
- 9 edges to [[_COMMUNITY_EgressFilter]]
- 8 edges to [[_COMMUNITY_EgressAttempt]]
- 5 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 3 edges to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[ApprovalResult]] - degree 22, connects to 6 communities
- [[TestEnforceMode]] - degree 16, connects to 6 communities
- [[EgressFilter]] - degree 21, connects to 5 communities
- [[TestIPRules]] - degree 14, connects to 5 communities
- [[TestInteractiveApproval]] - degree 12, connects to 5 communities
