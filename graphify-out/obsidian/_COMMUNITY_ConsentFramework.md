---
type: community
cohesion: 0.03
members: 91
---

# ConsentFramework

**Cohesion:** 0.03 - loosely connected
**Members:** 91 nodes

## Members
- [[.__init__()_109]] - code - gateway/security/prompt_guard.py
- [[._matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[.get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[.is_denylisted()]] - code - gateway/security/egress_config.py
- [[.matches_allowlist()]] - code - gateway/security/egress_config.py
- [[.setup_method()_29]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_ip()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_allowed_specific_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_default_config()_1]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denied_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_ip()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denied_port()]] - code - gateway/tests/test_security_hardening.py
- [[.test_deny_all_false()]] - code - gateway/tests/test_security_hardening.py
- [[.test_denylist_monitor_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_overrides_allowlist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[.test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[.test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[.test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_enforce_mode_blocks_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_invalid_mode_handling()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_log()]] - code - gateway/tests/test_security_hardening.py
- [[.test_logging_differences_by_mode()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_monitor_mode_allows_unknown_domains()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_per_agent_policy()]] - code - gateway/tests/test_security_hardening.py
- [[.test_port_filtering()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_private_ip_blocking()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_stats()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_parsing()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_url_parsing()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_url_port_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_allowlist_matching()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_wildcard_base_domain()]] - code - gateway/tests/test_security_hardening.py
- [[.test_wildcard_domain()]] - code - gateway/tests/test_security_hardening.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Args             block_threshold Score at or above which input is blocked.]] - rationale - gateway/security/prompt_guard.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilterConfig]] - code - gateway/security/egress_config.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[FEED_HOSTS]] - code - gateway/security/feed_hosts.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[PERMANENT_EGRESS_DOMAINS]] - code - gateway/security/egress_config.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[Public does domain match any pattern in the effective default allowlist]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilter with enforcemonitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test URL parsing for domains and ports.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._1]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist behavior in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist wildcard matching.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test handling of invalid modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test port-based filtering.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test specific egress mode environment variable.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that denylist overrides allowlist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that enforce mode blocks domains not in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that logging differs between enforce and monitor modes.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that monitor mode allows unknown domains but logs them.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test that private IPs are blocked regardless of mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test the management API endpoints (would need FastAPI test client).]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test wildcard matching in allowlist.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilter]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterEnforcement]] - code - gateway/tests/test_egress_enforce.py
- [[TestEgressManagementAPI]] - code - gateway/tests/test_egress_enforce.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved.      T]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_enforce.py]] - code - gateway/tests/test_egress_enforce.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConsentFramework
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_lifespan.py]]
- 32 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 29 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 23 edges to [[_COMMUNITY_test_http_proxy.py]]
- 19 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 11 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 10 edges to [[_COMMUNITY_SkillGuard]]
- 8 edges to [[_COMMUNITY_LLMProxy]]
- 7 edges to [[_COMMUNITY_ServiceManager]]
- 6 edges to [[_COMMUNITY_TrustConfig]]
- 5 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 5 edges to [[_COMMUNITY_RBACConfig]]
- 4 edges to [[_COMMUNITY_chatbotmain.py]]
- 4 edges to [[_COMMUNITY_Local LLM Support — Implementation Review]]
- 4 edges to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy;]]
- 3 edges to [[_COMMUNITY__call_agent_stream()]]
- 3 edges to [[_COMMUNITY_test_approval_queue.py]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 3 edges to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE]]
- 3 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]
- 1 edge to [[_COMMUNITY_rbac_config.py]]

## Top bridge nodes
- [[EgressFilterConfig]] - degree 103, connects to 19 communities
- [[EgressAction]] - degree 45, connects to 14 communities
- [[test_security_hardening.py]] - degree 30, connects to 12 communities
- [[TestSecureZero]] - degree 23, connects to 9 communities
- [[TestEgressFilter]] - degree 34, connects to 8 communities