---
type: community
cohesion: 0.15
members: 13
---

# Module Group 323

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[.setup_method()_29]] - code - gateway/tests/test_security_hardening.py
- [[.test_double_base64_injection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_fullwidth_detection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_homoglyph_detection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_mixed_case_still_caught()]] - code - gateway/tests/test_security_hardening.py
- [[.test_rtl_override_detection()]] - code - gateway/tests/test_security_hardening.py
- [[.test_zero_width_evasion()]] - code - gateway/tests/test_security_hardening.py
- [[Double-encoded base64 injection should be caught.]] - rationale - gateway/tests/test_security_hardening.py
- [[Fullwidth chars NFKC-normalized — injection defeated.]] - rationale - gateway/tests/test_security_hardening.py
- [[Mix of Latin and Cyrillic should trigger homoglyph detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[TestPromptGuardEvasion]] - code - gateway/tests/test_security_hardening.py
- [[Tests for prompt guard evasion techniques.]] - rationale - gateway/tests/test_security_hardening.py
- [[Zero-width chars between letters should not bypass detection.]] - rationale - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_323
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 79]]
- 3 edges to [[_COMMUNITY_Agent Isolation & Container Config]]
- 3 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 2 edges to [[_COMMUNITY_Alert Dispatcher]]
- 2 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Egress Filter & Approval]]
- 1 edge to [[_COMMUNITY_Module Group 88]]
- 1 edge to [[_COMMUNITY_Module Group 71]]
- 1 edge to [[_COMMUNITY_Module Group 66]]

## Top bridge nodes
- [[TestPromptGuardEvasion]] - degree 26, connects to 10 communities
- [[.setup_method()_29]] - degree 2, connects to 1 community
