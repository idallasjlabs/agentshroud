---
type: community
members: 63
---

# EgressPolicy

**Members:** 63 nodes

## Members
- [[dot-matches_domain()]] - code - gateway/security/egress_filter.py
- [[dot-matches_ip()]] - code - gateway/security/egress_filter.py
- [[dot-matches_port()]] - code - gateway/security/egress_filter.py
- [[dot-set_agent_policy()]] - code - gateway/security/egress_filter.py
- [[dot-test_agent_specific_policy()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_imaps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtp_submission()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_default_policy_allows_smtps()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_blocks_mcp_exfil()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_matches_domain_exact()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_domain_wildcard()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_cidr()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_invalid()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_ip_single()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_matches_port_empty_allows_all()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - code - gateway/tests/test_egress_filter.py
- [[A domain with an active timed approval should be allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[An expired timed approval should be evicted and the domain denied.]] - rationale - gateway/tests/test_egress_filter.py
- [[Check if IP matches any allowed IPCIDR.]] - rationale - gateway/security/egress_filter.py
- [[Check if domain matches any allowed domain (supports wildcards). Wildcards only…]] - rationale - gateway/security/egress_filter.py
- [[Check if port is allowed.]] - rationale - gateway/security/egress_filter.py
- [[Egress filter should be available for MCP network calls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Egress policy for an agent or global default.]] - rationale - gateway/security/egress_filter.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy]] - code - gateway/security/egress_filter.py
- [[EgressPolicy default allows port 465 (SMTPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 587 (SMTP submissionSTARTTLS).]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressPolicy default allows port 993 (IMAPS).]] - rationale - gateway/tests/test_egress_filter.py
- [[Enum_12]] - code
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Per-agent policies override the default.]] - rationale - gateway/tests/test_egress_filter.py
- [[Port 465 on an un-allowlisted domain is still denied in enforce mode.]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed by the…]] - rationale - gateway/tests/test_egress_filter.py
- [[Set a per-agent egress policy.]] - rationale - gateway/security/egress_filter.py
- [[TestEgressPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[TestPerAgentPolicy]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[Unit tests for EgressPolicy matching methods.]] - rationale - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved. These…]] - rationale - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[grant_timed_approval should purge expired entries on each call.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval with a malformed date should not raise or store anything.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.gmail.com465.]] - rationale - gateway/tests/test_egress_filter.py
- [[http_connect_proxy policy allows CONNECT smtp.mail.me.com587.]] - rationale - gateway/tests/test_egress_filter.py
- [[str_7]] - code
- [[test_egress_filter.py]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_allows_domain()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_cleans_stale_entries()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_invalid_iso_is_ignored()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressPolicy
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_EgressFilter]]
- 19 edges to [[_COMMUNITY__make_filter]]
- 11 edges to [[_COMMUNITY_asyncio_5]]
- 5 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 4 edges to [[_COMMUNITY_test_security_integration.py]]
- 3 edges to [[_COMMUNITY_TestEgressFilter]]
- 3 edges to [[_COMMUNITY_dot-_check_impl]]
- 3 edges to [[_COMMUNITY_TestEgressSSRF]]
- 2 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_test_module_stats.py]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_DraftEntry]]

## Top bridge nodes
- [[EgressPolicy]] - degree 58, connects to 17 communities
- [[EgressAction]] - degree 36, connects to 11 communities
- [[test_egress_filter.py]] - degree 30, connects to 5 communities
- [[TestInteractiveApproval]] - degree 10, connects to 3 communities
- [[TestSMTPIMAPPorts]] - degree 12, connects to 1 community
