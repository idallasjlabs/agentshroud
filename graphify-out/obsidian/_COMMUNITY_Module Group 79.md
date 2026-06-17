---
type: community
cohesion: 0.05
members: 51
---

# Module Group 79

**Cohesion:** 0.05 - loosely connected
**Members:** 51 nodes

## Members
- [[.__init__()_87]] - code - gateway/security/prompt_guard.py
- [[.setup_method()_30]] - code - gateway/tests/test_security_hardening.py
- [[.setup_method()_24]] - code - gateway/tests/test_security_hardening.py
- [[.test_base64_encoded_injection()]] - code - gateway/tests/test_security_hardening.py
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
- [[.test_empty_input()_3]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_forget_everything()]] - code - gateway/tests/test_security_hardening.py
- [[.test_ignore_instructions()]] - code - gateway/tests/test_security_hardening.py
- [[.test_indirect_injection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_instructions_override()]] - code - gateway/tests/test_security_hardening.py
- [[.test_none_input()]] - code - gateway/tests/test_security_hardening.py
- [[.test_prompt_extraction()]] - code - gateway/tests/test_security_hardening.py
- [[.test_prompt_leak_question()]] - code - gateway/tests/test_security_hardening.py
- [[.test_role_reassignment()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_rtl_override()]] - code - gateway/tests/test_security_hardening.py
- [[.test_sanitized_output()]] - code - gateway/tests/test_security_hardening.py
- [[.test_unicode_zero_width()]] - code - gateway/tests/test_security_hardening.py
- [[.test_warn_threshold()]] - code - gateway/tests/test_security_hardening.py
- [[.test_xml_tag_injection()_1]] - code - gateway/tests/test_security_hardening.py
- [[Args             block_threshold Score at or above which input is blocked.]] - rationale - gateway/security/prompt_guard.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[TestPromptGuard_1]] - code - gateway/tests/test_security_hardening.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_79
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Agent Isolation & Container Config]]
- 20 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 18 edges to [[_COMMUNITY_Egress Filter & Approval]]
- 17 edges to [[_COMMUNITY_Alert Dispatcher]]
- 15 edges to [[_COMMUNITY_Module Group 66]]
- 14 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 12 edges to [[_COMMUNITY_Module Group 88]]
- 9 edges to [[_COMMUNITY_Module Group 71]]
- 6 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 4 edges to [[_COMMUNITY_Module Group 240]]
- 4 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 4 edges to [[_COMMUNITY_Module Group 323]]
- 4 edges to [[_COMMUNITY_Module Group 285]]
- 3 edges to [[_COMMUNITY_Module Group 65]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 1 edge to [[_COMMUNITY_Module Group 283]]
- 1 edge to [[_COMMUNITY_Module Group 216]]
- 1 edge to [[_COMMUNITY_Module Group 161]]

## Top bridge nodes
- [[EgressAction]] - degree 39, connects to 14 communities
- [[test_security_hardening.py]] - degree 29, connects to 11 communities
- [[ThreatAction]] - degree 20, connects to 10 communities
- [[TestPromptGuard_1]] - degree 40, connects to 9 communities
- [[TestEgressSSRF]] - degree 28, connects to 9 communities