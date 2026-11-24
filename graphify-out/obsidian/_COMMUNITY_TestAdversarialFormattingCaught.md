---
type: community
members: 7
---

# TestAdversarialFormattingCaught

**Members:** 7 nodes

## Members
- [[dot-test_dotted_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_spaced_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_zero_width_space_injection_caught()]] - code - gateway/tests/test_differential_pii_detector.py
- [[Email with Unicode dot separators.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Email with spaces added to defeat naive regex a l i c e @ e x a m p l e . c o m]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[PII split with zero-width space.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[TestAdversarialFormattingCaught]] - code - gateway/tests/test_differential_pii_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAdversarialFormattingCaught
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_test_differential_pii_detector.py]]

## Top bridge nodes
- [[TestAdversarialFormattingCaught]] - degree 5, connects to 2 communities
- [[dot-test_dotted_email_caught_in_tool_result()]] - degree 3, connects to 1 community
- [[dot-test_spaced_email_caught_in_tool_result()]] - degree 3, connects to 1 community
- [[dot-test_zero_width_space_injection_caught()]] - degree 3, connects to 1 community
