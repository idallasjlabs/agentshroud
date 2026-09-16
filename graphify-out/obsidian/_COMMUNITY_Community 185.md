---
type: community
cohesion: 0.09
members: 38
---

# Community 185

**Cohesion:** 0.09 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-setup_method()_15]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_allowed_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[CIDR in policy allowlist should match.]] - rationale - gateway/tests/test_egress_filter.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressFilter_1]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).]] - rationale - gateway/tests/test_egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
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
TABLE source_file, type FROM #community/Community_185
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_Community 81]]
- 16 edges to [[_COMMUNITY_Community 167]]
- 13 edges to [[_COMMUNITY_Community 52]]
- 11 edges to [[_COMMUNITY_Session Manager & PIIContext Guard]]
- 11 edges to [[_COMMUNITY_Community 182]]
- 10 edges to [[_COMMUNITY_Encrypted Store & Drift Detector]]
- 9 edges to [[_COMMUNITY_P3 Infrastructure Security Modules]]
- 4 edges to [[_COMMUNITY_Proxy Sidecar & Forwarder]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 3 edges to [[_COMMUNITY_Community 92]]
- 2 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 2 edges to [[_COMMUNITY_Community 322]]
- 1 edge to [[_COMMUNITY_Ingest API & RBAC Core]]
- 1 edge to [[_COMMUNITY_Community 86]]
- 1 edge to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 1 edge to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 1 edge to [[_COMMUNITY_Community 48]]
- 1 edge to [[_COMMUNITY_Agent Isolation & Group Config Tests]]
- 1 edge to [[_COMMUNITY_Prompt Guard & Context Integrity]]

## Top bridge nodes
- [[EgressPolicy]] - degree 100, connects to 19 communities
- [[EgressFilter_1]] - degree 21, connects to 4 communities
- [[TestEgressPolicy]] - degree 15, connects to 4 communities
- [[TestSMTPIMAPPorts]] - degree 14, connects to 4 communities
- [[egress_filter()]] - degree 4, connects to 3 communities