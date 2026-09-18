---
type: community
cohesion: 0.15
members: 13
---

# DeceptionDetection

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[.test_basic_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_default_detection()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_hardened_message_basic()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_hardened_message_with_normalization()]] - code - gateway/tests/test_approval_hardening.py
- [[.test_format_hardened_message_with_security_concerns()]] - code - gateway/tests/test_approval_hardening.py
- [[DeceptionDetection]] - code - gateway/security/approval_hardening.py
- [[Result of deception detection analysis.]] - rationale - gateway/security/approval_hardening.py
- [[Test basic detection result creation.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test basic hardened message formatting.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test detection with default values.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardened message formatting when description is normalized.]] - rationale - gateway/tests/test_approval_hardening.py
- [[Test hardened message formatting with security concerns.]] - rationale - gateway/tests/test_approval_hardening.py
- [[approval_hardening.py]] - code - gateway/security/approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DeceptionDetection
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_DeniedRequest]]
- 6 edges to [[_COMMUNITY_Any]]
- 4 edges to [[_COMMUNITY_TestApprovalHardening]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]

## Top bridge nodes
- [[approval_hardening.py]] - degree 6, connects to 4 communities
- [[DeceptionDetection]] - degree 18, connects to 3 communities
- [[.test_format_hardened_message_basic()]] - degree 3, connects to 1 community
- [[.test_format_hardened_message_with_normalization()]] - degree 3, connects to 1 community
- [[.test_format_hardened_message_with_security_concerns()]] - degree 3, connects to 1 community