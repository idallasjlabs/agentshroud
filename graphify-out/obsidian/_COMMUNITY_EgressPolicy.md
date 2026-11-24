---
type: community
members: 41
---

# EgressPolicy

**Members:** 41 nodes

## Members
- [[dot-matches_domain()]] - code - gateway/security/egress_filter.py
- [[dot-matches_ip()]] - code - gateway/security/egress_filter.py
- [[dot-matches_port()]] - code - gateway/security/egress_filter.py
- [[dot-set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[dot-setup_method()_8]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_blocks_mcp_exfil()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards). Wildcards only…]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 993 (IMAPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[Per-agent policies override the default.]] - rationale - gateway/tests/test_egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressPolicy
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_EgressFilter]]
- 6 edges to [[_COMMUNITY__make_filter]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_asyncio_4]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_test_security_integration.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[EgressPolicy]] - degree 58, connects to 13 communities
- [[TestEgressSSRF]] - degree 14, connects to 2 communities
- [[TestEgressPolicy]] - degree 10, connects to 1 community
- [[TestPerAgentPolicy]] - degree 5, connects to 1 community
- [[dot-set_agent_policy()]] - degree 3, connects to 1 community
