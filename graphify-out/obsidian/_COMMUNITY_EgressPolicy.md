---
type: community
cohesion: 0.03
members: 113
---

# EgressPolicy

**Cohesion:** 0.03 - loosely connected
**Members:** 113 nodes

## Members
- [[.__init__()_71]] - code - gateway/tests/test_egress_filter.py
- [[.log_event()]] - code - gateway/tests/test_egress_filter.py
- [[.matches_domain()]] - code - gateway/security/egress_filter.py
- [[.matches_ip()]] - code - gateway/security/egress_filter.py
- [[.matches_port()]] - code - gateway/security/egress_filter.py
- [[.set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[.test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_passes()_1]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_domain_still_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_ip()_1]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
- [[.test_attempt_fields()]] - code - gateway/tests/test_egress_filter.py
- [[.test_bare_hostname()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[.test_denied_domain_overrides_allow()]] - code - gateway/tests/test_egress_filter.py
- [[.test_deny_has_details()]] - code - gateway/tests/test_egress_filter.py
- [[.test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[.test_egress_filter_blocks_mcp_exfil()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_emits_egress_event_to_event_bus()]] - code - gateway/tests/test_egress_filter.py
- [[.test_full_url()]] - code - gateway/tests/test_egress_filter.py
- [[.test_host_port_format()]] - code - gateway/tests/test_egress_filter.py
- [[.test_ipv4_mapped_ipv6_blocked()_1]] - code - gateway/tests/test_egress_filter.py
- [[.test_localhost_hostname_blocked()]] - code - gateway/tests/test_egress_filter.py
- [[.test_log_filters_by_agent()]] - code - gateway/tests/test_egress_filter.py
- [[.test_log_records_attempts()]] - code - gateway/tests/test_egress_filter.py
- [[.test_log_size_limit()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[.test_port_not_allowed()]] - code - gateway/tests/test_egress_filter.py
- [[.test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[.test_private_ip_blocked_ssrf()]] - code - gateway/tests/test_egress_filter.py
- [[.test_stats_counts()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unknown_domain_allowed_when_approved()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unknown_domain_denied_when_denied()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unlisted_domain_allowed_in_monitor()]] - code - gateway/tests/test_egress_filter.py
- [[.test_unlisted_domain_blocked()_1]] - code - gateway/tests/test_egress_filter.py
- [[.test_wildcard_does_not_match_deep_subdomain()]] - code - gateway/tests/test_egress_filter.py
- [[.test_wildcard_matches_base_domain()]] - code - gateway/tests/test_egress_filter.py
- [[.test_wildcard_one_level()]] - code - gateway/tests/test_egress_filter.py
- [[A domain with an active timed approval should be allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[An expired timed approval should be evicted and the domain denied.]] - rationale - gateway/tests/test_egress_filter.py
- [[ApprovalResult]] - code - gateway/security/egress_approval.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards).          Wildca]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
- [[Create an EgressFilter with a simple config.]] - rationale - gateway/tests/test_egress_filter.py
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressAttempt stores the right fields.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter_1]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter correctly parses URLs, hostport, and bare hostnames.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode should block unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter in monitor mode should allow but log unlisted destinations.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter records attempts and provides stats.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[FakeAuditStore]] - code - gateway/tests/test_egress_filter.py
- [[IP allowlist and private-IP SSRF protection.]] - rationale - gateway/tests/test_egress_filter.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
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
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[TestURLParsing]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[_make_filter()]] - code - gateway/tests/test_egress_filter.py
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
TABLE source_file, type FROM #community/EgressPolicy
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_EgressFilter]]
- 32 edges to [[_COMMUNITY_EgressFilterConfig]]
- 22 edges to [[_COMMUNITY_EgressAction]]
- 17 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_test_security_audit.py]]
- 4 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 4 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 4 edges to [[_COMMUNITY_EncryptedStore]]
- 3 edges to [[_COMMUNITY_StdioConnection]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_TestFileSandbox]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_test_security_integration.py]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[EgressPolicy]] - degree 100, connects to 15 communities
- [[ApprovalResult]] - degree 22, connects to 4 communities
- [[TestEnforceMode]] - degree 16, connects to 4 communities
- [[test_egress_filter.py]] - degree 29, connects to 3 communities
- [[EgressFilter_1]] - degree 21, connects to 3 communities