---
type: community
cohesion: 0.05
members: 46
---

# Module Group 88

**Cohesion:** 0.05 - loosely connected
**Members:** 46 nodes

## Members
- [[.matches_domain()]] - code - gateway/security/egress_filter.py
- [[.matches_ip()]] - code - gateway/security/egress_filter.py
- [[.matches_port()]] - code - gateway/security/egress_filter.py
- [[.set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[.setup_method()_26]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[.test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[.test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[.test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[.test_egress_filter_blocks_mcp_exfil()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_ports_allows_all()]] - code - gateway/tests/test_security_hardening.py
- [[.test_log()]] - code - gateway/tests/test_security_hardening.py
- [[.test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[.test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[.test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[.test_stats()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards).          Wildca]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 993 (IMAPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[egress_filter()]] - code - gateway/tests/test_e2e_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_88
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_Egress Filter & Approval]]
- 13 edges to [[_COMMUNITY_Module Group 71]]
- 12 edges to [[_COMMUNITY_Module Group 79]]
- 10 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 6 edges to [[_COMMUNITY_Alert Dispatcher]]
- 5 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 4 edges to [[_COMMUNITY_Agent Isolation & Container Config]]
- 4 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 4 edges to [[_COMMUNITY_Sidecar Security Scanner]]
- 3 edges to [[_COMMUNITY_Module Group 72]]
- 3 edges to [[_COMMUNITY_Module Group 110]]
- 3 edges to [[_COMMUNITY_Module Group 66]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 240]]
- 2 edges to [[_COMMUNITY_Module Group 216]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 258]]
- 1 edge to [[_COMMUNITY_Module Group 257]]
- 1 edge to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Module Group 137]]
- 1 edge to [[_COMMUNITY_Module Group 323]]
- 1 edge to [[_COMMUNITY_Module Group 285]]
- 1 edge to [[_COMMUNITY_Context Guard & Integrity]]

## Top bridge nodes
- [[EgressPolicy]] - degree 96, connects to 22 communities
- [[TestEgressFilter]] - degree 34, connects to 9 communities
- [[TestEgressPolicy]] - degree 15, connects to 3 communities
- [[egress_filter()]] - degree 4, connects to 3 communities
- [[.setup_method()_26]] - degree 4, connects to 2 communities