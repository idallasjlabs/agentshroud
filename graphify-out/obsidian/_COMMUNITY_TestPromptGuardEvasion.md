---
type: community
cohesion: 0.15
members: 13
---

# TestPromptGuardEvasion

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-setup_method()_35]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_double_base64_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_fullwidth_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_homoglyph_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_mixed_case_still_caught()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_rtl_override_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_zero_width_evasion()]] - code - gateway/tests/test_security_hardening.py
- [[Double-encoded base64 injection should be caught.]] - rationale - gateway/tests/test_security_hardening.py
- [[Fullwidth chars NFKC-normalized — injection defeated.]] - rationale - gateway/tests/test_security_hardening.py
- [[Mix of Latin and Cyrillic should trigger homoglyph detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[TestPromptGuardEvasion]] - code - gateway/tests/test_security_hardening.py
- [[Tests for prompt guard evasion techniques.]] - rationale - gateway/tests/test_security_hardening.py
- [[Zero-width chars between letters should not bypass detection.]] - rationale - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPromptGuardEvasion
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 4 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]

## Top bridge nodes
- [[TestPromptGuardEvasion]] - degree 26, connects to 7 communities
- [[dot-setup_method()_35]] - degree 2, connects to 1 community
