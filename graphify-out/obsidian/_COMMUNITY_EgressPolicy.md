---
type: community
cohesion: 0.10
members: 30
---

# EgressPolicy

**Cohesion:** 0.10 - loosely connected
**Members:** 30 nodes

## Members
- [[dot-set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[dot-test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[Per-agent policies override the default.]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - rationale - gateway/tests/test_egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[v0.9.0 cron-email fix SMTPIMAP ports 465587993 allowed for OpenClaw cron email]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressPolicy
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_AlertDispatcher]]
- 18 edges to [[_COMMUNITY__make_filter]]
- 13 edges to [[_COMMUNITY_EgressFilterConfig]]
- 10 edges to [[_COMMUNITY_EgressFilter]]
- 10 edges to [[_COMMUNITY_test_egress_filter.py]]
- 10 edges to [[_COMMUNITY_AgentRegistry]]
- 7 edges to [[_COMMUNITY_EgressAttempt]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TestEgressSSRF]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]

## Top bridge nodes
- [[EgressPolicy]] - degree 99, connects to 13 communities
- [[TestEgressPolicy]] - degree 15, connects to 5 communities
- [[TestSMTPIMAPPorts]] - degree 14, connects to 5 communities
- [[TestPerAgentPolicy]] - degree 9, connects to 5 communities
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - degree 5, connects to 2 communities
