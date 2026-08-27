---
type: community
members: 34
---

# Community 118

**Members:** 34 nodes

## Members
- [[.set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[.test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
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
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 993 (IMAPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[Per-agent policies override the default.]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.mail.me.com587.]] - rationale - gateway/tests/test_egress_filter.py
- [[v0.9.0 cron-email fix SMTPIMAP ports 465587993 allowed for OpenClaw cron email]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_118
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_Community 53]]
- 24 edges to [[_COMMUNITY_Community 14]]
- 22 edges to [[_COMMUNITY_Community 282]]
- 7 edges to [[_COMMUNITY_Community 33]]
- 6 edges to [[_COMMUNITY_Community 35]]
- 3 edges to [[_COMMUNITY_Community 74]]
- 2 edges to [[_COMMUNITY_Community 6]]
- 2 edges to [[_COMMUNITY_Community 66]]
- 2 edges to [[_COMMUNITY_Community 782]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 251]]
- 1 edge to [[_COMMUNITY_Community 870]]
- 1 edge to [[_COMMUNITY_Community 64]]
- 1 edge to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 28]]
- 1 edge to [[_COMMUNITY_Community 60]]
- 1 edge to [[_COMMUNITY_Community 116]]
- 1 edge to [[_COMMUNITY_Community 55]]
- 1 edge to [[_COMMUNITY_Community 212]]

## Top bridge nodes
- [[EgressPolicy]] - degree 100, connects to 19 communities
- [[TestEgressPolicy]] - degree 15, connects to 3 communities
- [[TestSMTPIMAPPorts]] - degree 14, connects to 3 communities
- [[TestPerAgentPolicy]] - degree 9, connects to 3 communities
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - degree 6, connects to 2 communities