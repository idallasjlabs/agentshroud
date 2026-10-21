---
type: community
members: 50
---

# TelegramAPIProxy (2)

**Members:** 50 nodes

## Members
- [[dot-__init__()_38]] - code - gateway/security/prompt_guard.py
- [[dot-setup_method()_6]] - code - gateway/tests/test_security_hardening.py
- [[dot-setup_method()_7]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_base64_encoded_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_benign_base64()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_clean_input()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_combined_attack_high_score()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_custom_pattern()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_dan_jailbreak()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_delimiter_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_empty_input()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_forget_everything()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_ignore_instructions()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_indirect_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_instructions_override()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_none_input()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_prompt_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_prompt_leak_question()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_role_reassignment()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_rtl_override()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_sanitized_output()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_unicode_zero_width()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_warn_threshold()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_xml_tag_injection()]] - code - gateway/tests/test_security_hardening.py
- [[Args             block_threshold Score at or above which input is blocked.]] - rationale - gateway/security/prompt_guard.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestPromptGuard]] - code - gateway/tests/test_security_hardening.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy_2
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 22 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 22 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 20 edges to [[_COMMUNITY_socrouter.py]]
- 17 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 16 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 14 edges to [[_COMMUNITY_PortManager]]
- 3 edges to [[_COMMUNITY_DelegationManager]]
- 3 edges to [[_COMMUNITY__pcm_bytes]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy (3)_1]]
- 3 edges to [[_COMMUNITY_socrouter.py (2)]]
- 2 edges to [[_COMMUNITY_ADR-006 Multi-Runtime Container Support]]
- 2 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_First iteration ingests + records; second sees dedup and skips. (2)]]

## Top bridge nodes
- [[EgressAction]] - degree 45, connects to 14 communities
- [[test_security_hardening.py]] - degree 30, connects to 9 communities
- [[TestPromptGuard]] - degree 40, connects to 7 communities
- [[TestEgressSSRF]] - degree 28, connects to 7 communities
- [[TestSecureZero]] - degree 23, connects to 7 communities
