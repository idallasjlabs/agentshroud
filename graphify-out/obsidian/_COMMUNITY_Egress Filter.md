---
type: community
cohesion: 0.07
members: 34
---

# Egress Filter

**Cohesion:** 0.07 - loosely connected
**Members:** 34 nodes

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
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[egress_filter()_1]] - code - gateway/tests/test_security_integration.py
- [[v0.9.0 cron-email fix SMTPIMAP ports 465587993 allowed for OpenClaw cron email]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Filter
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Egress Filter]]
- 22 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 14 edges to [[_COMMUNITY_Egress Filter (security)]]
- 11 edges to [[_COMMUNITY_Security Hardening]]
- 10 edges to [[_COMMUNITY_Egress Filter]]
- 7 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 5 edges to [[_COMMUNITY_Security Hardening]]
- 3 edges to [[_COMMUNITY_E2e Proxy]]
- 2 edges to [[_COMMUNITY_Redteam Probes]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 1 edge to [[_COMMUNITY_Git Guard (security)]]
- 1 edge to [[_COMMUNITY_Security Audit]]
- 1 edge to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Progressive Trust Integration]]
- 1 edge to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 1 edge to [[_COMMUNITY_Security Regressions V1 2]]

## Top bridge nodes
- [[EgressPolicy]] - degree 100, connects to 17 communities
- [[TestEgressSSRF]] - degree 28, connects to 10 communities
- [[egress_filter()_1]] - degree 4, connects to 3 communities
- [[TestEgressPolicy]] - degree 15, connects to 2 communities
- [[.set_agent_policy()]] - degree 3, connects to 1 community