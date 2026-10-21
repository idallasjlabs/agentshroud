---
type: community
members: 116
---

# TestOutboundPipelineIntegration

**Members:** 116 nodes

## Members
- [[dot-__init__()_105]] - code - gateway/tests/test_egress_filter.py
- [[dot-log_event()_1]] - code - gateway/tests/test_egress_filter.py
- [[dot-set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[dot-test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_domain_passes()_1]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_domain_still_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_ip()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_attempt_fields()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_bare_hostname()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_denied_domain_overrides_allow()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_has_details()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_blocks_mcp_exfil()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_emits_egress_event_to_event_bus()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_full_url()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_host_port_format()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_ipv4_mapped_ipv6_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_localhost_hostname_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_filters_by_agent()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_records_attempts()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_log_size_limit()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_port_not_allowed()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_blocked_ssrf()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_stats_counts()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_allowed_when_approved()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_denied_when_denied()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unlisted_domain_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unlisted_domain_blocked()_1]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_does_not_match_deep_subdomain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_matches_base_domain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_wildcard_one_level()]] - code - gateway/tests/test_egress_filter.py
- [[A domain with an active timed approval should be allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[An expired timed approval should be evicted and the domain denied.]] - rationale - gateway/tests/test_egress_filter.py
- [[ApprovalResult]] - code - gateway/security/egress_approval.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Create an EgressFilter with a simple config.]] - rationale - gateway/tests/test_egress_filter.py
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter_1]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter correctly parses URLs, hostport, and bare hostnames.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode should block unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in monitor mode should allow but log unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter records attempts and provides stats.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[FakeAuditStore_1]] - code - gateway/tests/test_egress_filter.py
- [[IP allowlist and private-IP SSRF protection.]] - rationale - gateway/tests/test_egress_filter.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW]] - rationale - gateway/tests/test_egress_filter.py
- [[Per-agent policies override the default.]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs are blocked by default to prevent SSRF.]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[Result of an approval request.]] - rationale - gateway/security/egress_approval.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressAttempt]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestEnforceMode]] - code - gateway/tests/test_egress_filter.py
- [[TestIPRules]] - code - gateway/tests/test_egress_filter.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestLogging]] - code - gateway/tests/test_egress_filter.py
- [[TestMonitorMode]] - code - gateway/tests/test_egress_filter.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[TestURLParsing]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[_make_filter()]] - code - gateway/tests/test_egress_filter.py
- [[egress_filter()]] - code - gateway/tests/test_security_integration.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval should purge expired entries on each call.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval with a malformed date should not raise or store anything.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_filter.py]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_allows_domain()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_cleans_stale_entries()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_invalid_iso_is_ignored()]] - code - gateway/tests/test_egress_filter.py
- [[v0.9.0 cron-email fix SMTPIMAP ports 465587993 allowed for OpenClaw cron email]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundPipelineIntegration
SORT file.name ASC
```

## Connections to other communities
- 56 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 22 edges to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 19 edges to [[_COMMUNITY_First iteration ingests + records; second sees dedup and skips. (2)]]
- 8 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 7 edges to [[_COMMUNITY__wrap_response()]]
- 6 edges to [[_COMMUNITY_SkillGuard]]
- 3 edges to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 3 edges to [[_COMMUNITY_AgentTarget]]
- 3 edges to [[_COMMUNITY_PortManager]]
- 2 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY__wrap_response() (3)_1]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy()]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 1 edge to [[_COMMUNITY__wrap_response() (4)]]
- 1 edge to [[_COMMUNITY_test_playback_state.c]]
- 1 edge to [[_COMMUNITY__wrap_response() (5)]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (3)_1]]
- 1 edge to [[_COMMUNITY_socrouter.py (2)]]

## Top bridge nodes
- [[EgressPolicy]] - degree 97, connects to 22 communities
- [[TestEnforceMode]] - degree 16, connects to 4 communities
- [[test_egress_filter.py]] - degree 29, connects to 3 communities
- [[EgressFilter_1]] - degree 21, connects to 3 communities
- [[TestEgressPolicy]] - degree 15, connects to 3 communities
