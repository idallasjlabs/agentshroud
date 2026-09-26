---
type: community
cohesion: 0.05
members: 56
---

# EgressApprovalQueue

**Cohesion:** 0.05 - loosely connected
**Members:** 56 nodes

## Members
- [[.__init__()_155]] - code - gateway/tests/test_egress_filter.py
- [[.log_event()_2]] - code - gateway/tests/test_egress_filter.py
- [[.setup_method()_33]] - code - gateway/tests/test_security_hardening.py
- [[.test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[.test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[.test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[.test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[.test_egress_filter_blocks_mcp_exfil()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[.test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressFilter_2]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[FakeAuditStore]] - code - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py
- [[v0.9.0 cron-email fix SMTPIMAP ports 465587993 allowed for OpenClaw cron email]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_test_http_proxy.py]]
- 32 edges to [[_COMMUNITY_ConsentFramework]]
- 29 edges to [[_COMMUNITY_lifespan.py]]
- 20 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 4 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 3 edges to [[_COMMUNITY_test_approval_queue.py]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 2 edges to [[_COMMUNITY__wrap_response()]]
- 2 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_Local LLM Support — Implementation Review]]
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy;]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[EgressPolicy]] - degree 100, connects to 18 communities
- [[TestEgressSSRF]] - degree 28, connects to 8 communities
- [[EgressFilter_2]] - degree 21, connects to 3 communities
- [[TestEgressPolicy]] - degree 15, connects to 3 communities
- [[TestSMTPIMAPPorts]] - degree 14, connects to 3 communities