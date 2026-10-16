---
type: community
cohesion: 0.13
members: 22
---

# ApprovalHardening

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-test_basic_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_default_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_denied_request_creation()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_format_hardened_message_basic()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_format_hardened_message_with_normalization()]] - code - gateway/tests/test_approval_hardening.py
- [[dot-test_format_hardened_message_with_security_concerns()]] - code - gateway/tests/test_approval_hardening.py
- [[DeceptionDetection]] - code - gateway/security/approval_hardening.py
- [[DeniedRequest]] - code - gateway/security/approval_hardening.py
- [[Record of a denied approval request.]] - rationale - gateway/security/approval_hardening.py
- [[Result of deception detection analysis.]] - rationale - gateway/security/approval_hardening.py
- [[Test DeceptionDetection dataclass.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test DeniedRequest dataclass.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test basic detection result creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test basic hardened message formatting.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test denied request creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection with default values.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardened message formatting when description is normalized.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardened message formatting with security concerns.]] - rationale - gateway/tests/test_approval_hardening.py
- [[TestDeceptionDetection]] - code - gateway/tests/test_approval_hardening.py
- [[TestDeniedRequest]] - code - gateway/tests/test_approval_hardening.py
- [[approval_hardening.py]] - code - gateway/security/approval_hardening.py
- [[test_approval_hardening.py]] - code - gateway/tests/test_approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalHardening
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ApprovalHardening_1]]
- 7 edges to [[_COMMUNITY_ApprovalHardening_2]]
- 6 edges to [[_COMMUNITY_ApprovalHardening]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 1 edge to [[_COMMUNITY_ApprovalHardening_4]]

## Top bridge nodes
- [[DeceptionDetection]] - degree 18, connects to 3 communities
- [[DeniedRequest]] - degree 9, connects to 3 communities
- [[test_approval_hardening.py]] - degree 8, connects to 3 communities
- [[approval_hardening.py]] - degree 6, connects to 3 communities
- [[TestDeceptionDetection]] - degree 8, connects to 2 communities
