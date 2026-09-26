---
type: community
cohesion: 0.06
members: 60
---

# test_http_proxy.py

**Cohesion:** 0.06 - loosely connected
**Members:** 60 nodes

## Members
- [[.test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_passes()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_still_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_ip()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
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
- [[ApprovalResult]] - code - gateway/security/egress_approval.py
- [[Create an EgressFilter with a simple config.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter correctly parses URLs, hostport, and bare hostnames.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode should block unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in monitor mode should allow but log unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter records attempts and provides stats.]] - rationale - gateway/tests/test_egress_filter.py
- [[IP allowlist and private-IP SSRF protection.]] - rationale - gateway/tests/test_egress_filter.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[Per-agent policies override the default.]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs are blocked by default to prevent SSRF.]] - rationale - gateway/tests/test_egress_filter.py
- [[Result of an approval request.]] - rationale - gateway/security/egress_approval.py
- [[TestEgressAttempt]] - code - gateway/tests/test_egress_filter.py
- [[TestEnforceMode]] - code - gateway/tests/test_egress_filter.py
- [[TestIPRules]] - code - gateway/tests/test_egress_filter.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestLogging]] - code - gateway/tests/test_egress_filter.py
- [[TestMonitorMode]] - code - gateway/tests/test_egress_filter.py
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
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
TABLE source_file, type FROM #community/test_http_proxypy
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 23 edges to [[_COMMUNITY_ConsentFramework]]
- 20 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 4 edges to [[_COMMUNITY_Path]]
- 3 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 2 edges to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]

## Top bridge nodes
- [[ApprovalResult]] - degree 22, connects to 5 communities
- [[TestEnforceMode]] - degree 16, connects to 4 communities
- [[_make_filter()]] - degree 33, connects to 3 communities
- [[test_egress_filter.py]] - degree 29, connects to 3 communities
- [[TestIPRules]] - degree 14, connects to 3 communities