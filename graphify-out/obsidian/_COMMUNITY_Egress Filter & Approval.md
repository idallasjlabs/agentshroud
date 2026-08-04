---
type: community
cohesion: 0.05
members: 83
---

# Egress Filter & Approval

**Cohesion:** 0.05 - loosely connected
**Members:** 83 nodes

## Members
- [[.from_environment()]] - code - gateway/security/egress_config.py
- [[.test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_passes()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_still_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_ip()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
- [[.test_attempt_fields()]] - code - gateway/tests/test_egress_filter.py
- [[.test_bare_hostname()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
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
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
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
- [[ApprovalResult]] - code - gateway/security/egress_approval.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[Create an EgressFilter with a simple config.]] - rationale - gateway/tests/test_egress_filter.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter_2]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter correctly parses URLs, hostport, and bare hostnames.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode should block unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in monitor mode should allow but log unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter records attempts and provides stats.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[IP allowlist and private-IP SSRF protection.]] - rationale - gateway/tests/test_egress_filter.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[Per-agent policies override the default.]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs are blocked by default to prevent SSRF.]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[Result of an approval request.]] - rationale - gateway/security/egress_approval.py
- [[TestEgressAttempt]] - code - gateway/tests/test_egress_filter.py
- [[TestEnforceMode]] - code - gateway/tests/test_egress_filter.py
- [[TestIPRules]] - code - gateway/tests/test_egress_filter.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestLogging]] - code - gateway/tests/test_egress_filter.py
- [[TestMonitorMode]] - code - gateway/tests/test_egress_filter.py
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[TestURLParsing]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[_make_filter()]] - code - gateway/tests/test_egress_filter.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval should purge expired entries on each call.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval with a malformed date should not raise or store anything.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.mail.me.com587.]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_filter.py]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_allows_domain()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_cleans_stale_entries()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_invalid_iso_is_ignored()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Filter__Approval
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Module Group 71]]
- 34 edges to [[_COMMUNITY_Module Group 88]]
- 18 edges to [[_COMMUNITY_Module Group 79]]
- 10 edges to [[_COMMUNITY_Module Group 240]]
- 9 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 5 edges to [[_COMMUNITY_Module Group 283]]
- 3 edges to [[_COMMUNITY_Module Group 200]]
- 3 edges to [[_COMMUNITY_Module Group 483]]
- 3 edges to [[_COMMUNITY_Module Group 72]]
- 3 edges to [[_COMMUNITY_Sidecar Security Scanner]]
- 3 edges to [[_COMMUNITY_Module Group 124]]
- 2 edges to [[_COMMUNITY_Module Group 216]]
- 1 edge to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 1 edge to [[_COMMUNITY_Module Group 522]]
- 1 edge to [[_COMMUNITY_Module Group 117]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Agent Isolation & Container Config]]
- 1 edge to [[_COMMUNITY_Alert Dispatcher]]
- 1 edge to [[_COMMUNITY_Module Group 66]]
- 1 edge to [[_COMMUNITY_Module Group 323]]
- 1 edge to [[_COMMUNITY_Module Group 285]]
- 1 edge to [[_COMMUNITY_Module Group 150]]

## Top bridge nodes
- [[EgressFilterConfig]] - degree 91, connects to 18 communities
- [[ApprovalResult]] - degree 19, connects to 5 communities
- [[test_egress_filter.py]] - degree 26, connects to 3 communities
- [[EgressFilter_2]] - degree 18, connects to 3 communities
- [[TestEnforceMode]] - degree 15, connects to 3 communities
