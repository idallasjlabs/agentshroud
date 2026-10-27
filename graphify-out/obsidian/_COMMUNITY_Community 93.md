---
type: community
members: 42
---

# Community 93

**Members:** 42 nodes

## Members
- [[.set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[.setup_method()_33]] - code - gateway/tests/test_security_hardening.py
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
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.mail.me.com587.]] - rationale - gateway/tests/test_egress_filter.py
- [[v0.9.0 cron-email fix SMTPIMAP ports 465587993 allowed for OpenClaw cron email]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_93
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Community 21]]
- 22 edges to [[_COMMUNITY_Community 0]]
- 18 edges to [[_COMMUNITY_Community 17]]
- 11 edges to [[_COMMUNITY_Community 52]]
- 6 edges to [[_COMMUNITY_Community 68]]
- 5 edges to [[_COMMUNITY_Community 11]]
- 4 edges to [[_COMMUNITY_Community 162]]
- 3 edges to [[_COMMUNITY_Community 43]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 146]]
- 2 edges to [[_COMMUNITY_Community 123]]
- 2 edges to [[_COMMUNITY_Community 1119]]
- 2 edges to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 41]]
- 1 edge to [[_COMMUNITY_Community 509]]
- 1 edge to [[_COMMUNITY_Community 431]]
- 1 edge to [[_COMMUNITY_Community 888]]
- 1 edge to [[_COMMUNITY_Community 792]]
- 1 edge to [[_COMMUNITY_Community 947]]
- 1 edge to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 22]]

## Top bridge nodes
- [[EgressPolicy]] - degree 100, connects to 22 communities
- [[TestEgressSSRF]] - degree 28, connects to 9 communities
- [[TestEgressPolicy]] - degree 15, connects to 4 communities
- [[TestSMTPIMAPPorts]] - degree 14, connects to 4 communities
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - degree 6, connects to 2 communities