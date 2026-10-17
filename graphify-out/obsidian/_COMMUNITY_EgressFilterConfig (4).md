---
type: community
members: 13
---

# EgressFilterConfig (4)

**Members:** 13 nodes

## Members
- [[dot-setup_method()_36]] - code - gateway/tests/test_security_hardening.py
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
TABLE source_file, type FROM #community/EgressFilterConfig_4
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 3 edges to [[_COMMUNITY_ContextSegment]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (3)]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (2)]]

## Top bridge nodes
- [[TestPromptGuardEvasion]] - degree 26, connects to 7 communities
- [[dot-setup_method()_36]] - degree 2, connects to 1 community
