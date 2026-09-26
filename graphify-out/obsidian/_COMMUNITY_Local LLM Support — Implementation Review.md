---
type: community
cohesion: 0.15
members: 13
---

# Local LLM Support — Implementation Review

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[.setup_method()_32]] - code - gateway/tests/test_security_hardening.py
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
TABLE source_file, type FROM #community/Local_LLM_Support__Implementation_Review
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_ConsentFramework]]
- 3 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_ServiceManager]]
- 2 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[TestPromptGuardEvasion]] - degree 26, connects to 9 communities
- [[.setup_method()_32]] - degree 2, connects to 1 community