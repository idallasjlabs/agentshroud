---
type: community
cohesion: 0.03
members: 75
---

# EgressAction

**Cohesion:** 0.03 - loosely connected
**Members:** 75 nodes

## Members
- [[.__init__()_74]] - code - gateway/security/prompt_guard.py
- [[.setup_method()_15]] - code - gateway/tests/test_security_hardening.py
- [[.setup_method()_25]] - code - gateway/tests/test_security_hardening.py
- [[.setup_method()_12]] - code - gateway/tests/test_security_hardening.py
- [[.setup_method()_13]] - code - gateway/tests/test_security_hardening.py
- [[.teardown_method()_3]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_allowed_basic()]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_denied_high_trust()]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_unknown_agent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_base64_encoded_injection()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_benign_base64()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[.test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[.test_clean_input()]] - code - gateway/tests/test_security_hardening.py
- [[.test_combined_attack_high_score()]] - code - gateway/tests/test_security_hardening.py
- [[.test_custom_pattern()]] - code - gateway/tests/test_security_hardening.py
- [[.test_dan_jailbreak()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_delimiter_injection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_double_base64_injection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_empty_input()_3]] - code - gateway/tests/test_security_hardening.py
- [[.test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_failure_decreases_score()]] - code - gateway/tests/test_security_hardening.py
- [[.test_forget_everything()]] - code - gateway/tests/test_security_hardening.py
- [[.test_fullwidth_detection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_trust()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_trust_unknown()]] - code - gateway/tests/test_security_hardening.py
- [[.test_history()]] - code - gateway/tests/test_security_hardening.py
- [[.test_homoglyph_detection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_ignore_instructions()]] - code - gateway/tests/test_security_hardening.py
- [[.test_indirect_injection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_mixed_case_still_caught()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_instructions_override()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_none_input()]] - code - gateway/tests/test_security_hardening.py
- [[.test_prompt_extraction()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_prompt_leak_question()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_agent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_idempotent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_role_reassignment()_2]] - code - gateway/tests/test_security_hardening.py
- [[.test_rtl_override()]] - code - gateway/tests/test_security_hardening.py
- [[.test_rtl_override_detection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_sanitized_output()]] - code - gateway/tests/test_security_hardening.py
- [[.test_score_never_negative()]] - code - gateway/tests/test_security_hardening.py
- [[.test_sqlite_persistence()]] - code - gateway/tests/test_security_hardening.py
- [[.test_success_increases_score()]] - code - gateway/tests/test_security_hardening.py
- [[.test_trust_level_progression()]] - code - gateway/tests/test_security_hardening.py
- [[.test_unicode_zero_width()]] - code - gateway/tests/test_security_hardening.py
- [[.test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[.test_warn_threshold()]] - code - gateway/tests/test_security_hardening.py
- [[.test_xml_tag_injection()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_zero_width_evasion()]] - code - gateway/tests/test_security_hardening.py
- [[Args             block_threshold Score at or above which input is blocked.]] - rationale - gateway/security/prompt_guard.py
- [[Double-encoded base64 injection should be caught.]] - rationale - gateway/tests/test_security_hardening.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[Fullwidth chars NFKC-normalized — injection defeated.]] - rationale - gateway/tests/test_security_hardening.py
- [[Mix of Latin and Cyrillic should trigger homoglyph detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestPromptGuard_1]] - code - gateway/tests/test_security_hardening.py
- [[TestPromptGuardEvasion]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for prompt guard evasion techniques.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[Zero-width chars between letters should not bypass detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressAction
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_EncryptedStore]]
- 27 edges to [[_COMMUNITY_AgentRegistry]]
- 25 edges to [[_COMMUNITY_TrustManager]]
- 22 edges to [[_COMMUNITY_EgressPolicy]]
- 15 edges to [[_COMMUNITY_EgressFilterConfig]]
- 13 edges to [[_COMMUNITY_EgressFilter]]
- 10 edges to [[_COMMUNITY_TrustConfig]]
- 7 edges to [[_COMMUNITY_TrustLevel]]
- 7 edges to [[_COMMUNITY_lifespan.py]]
- 7 edges to [[_COMMUNITY_KeyVaultConfig]]
- 3 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 3 edges to [[_COMMUNITY_test_http_proxy.py]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_test_security_integration.py]]

## Top bridge nodes
- [[EgressAction]] - degree 45, connects to 10 communities
- [[TestPromptGuard_1]] - degree 40, connects to 10 communities
- [[TestTrustManager]] - degree 35, connects to 10 communities
- [[test_security_hardening.py]] - degree 30, connects to 10 communities
- [[TestEgressSSRF]] - degree 28, connects to 10 communities