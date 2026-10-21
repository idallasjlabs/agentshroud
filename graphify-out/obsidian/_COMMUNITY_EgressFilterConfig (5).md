---
type: community
members: 55
---

# EgressFilterConfig (5)

**Members:** 55 nodes

## Members
- [[dot-__init__()_38]] - code - gateway/security/egress_filter.py
- [[dot-__init__()_39]] - code - gateway/tests/test_egress_filter.py
- [[dot-log_event()]] - code - gateway/tests/test_egress_filter.py
- [[dot-setup_method()_9]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressFilter]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[FakeAuditStore]] - code - gateway/tests/test_egress_filter.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py
- [[v0.9.0 cron-email fix SMTPIMAP ports 465587993 allowed for OpenClaw cron email]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig_5
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_EgressFilterConfig (4)]]
- 27 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 26 edges to [[_COMMUNITY_AlertDispatcher]]
- 25 edges to [[_COMMUNITY_EgressFilterConfig (3)]]
- 9 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (3)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]

## Top bridge nodes
- [[EgressPolicy]] - degree 97, connects to 12 communities
- [[EgressFilter]] - degree 21, connects to 3 communities
- [[TestEgressPolicy]] - degree 15, connects to 3 communities
- [[TestSMTPIMAPPorts]] - degree 14, connects to 3 communities
- [[FakeAuditStore]] - degree 11, connects to 3 communities
