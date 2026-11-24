---
type: community
members: 21
---

# DifferentialPIIDetector

**Members:** 21 nodes

## Members
- [[dot-__init__()_201]] - code - gateway/security/differential_pii_detector.py
- [[dot-_init_presidio()_1]] - code - gateway/security/differential_pii_detector.py
- [[dot-test_clean_content_no_hits()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_email_redacted_in_output()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_pii_hit_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_plain_email_caught_in_prompt()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_plain_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_redact_on_hit_false_preserves_original()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_redacted_content_is_original_when_no_pii()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_report_has_required_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_scan_produces_report_with_correct_floor_used()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_us_ssn_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_weak_hit_present_in_tool_result_only()]] - code - gateway/tests/test_differential_pii_detector.py
- [[A weak-confidence hit (0.75) must appear in tool results but not prompts.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts. This…]] - rationale - gateway/security/differential_pii_detector.py
- [[Attempt to initialise Presidio deterministically; else regex. SECURITY never…]] - rationale - gateway/security/differential_pii_detector.py
- [[DifferentialPIIDetector]] - code - gateway/security/differential_pii_detector.py
- [[TestAsymmetricFloor]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestRedaction]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestStandardPIIAlwaysCaught]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestToolResultPIIReport]] - code - gateway/tests/test_differential_pii_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DifferentialPIIDetector
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_differential_pii_detector.py]]
- 7 edges to [[_COMMUNITY_TestPresidioPathContract]]
- 6 edges to [[_COMMUNITY_PIIHit]]
- 5 edges to [[_COMMUNITY_differential_pii_detector.py]]
- 4 edges to [[_COMMUNITY_TestAdversarialFormattingCaught]]
- 3 edges to [[_COMMUNITY_A2AProxy]]
- 1 edge to [[_COMMUNITY_TestDeterministicPresidioInit]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[DifferentialPIIDetector]] - degree 48, connects to 9 communities
- [[TestToolResultPIIReport]] - degree 6, connects to 2 communities
- [[TestRedaction]] - degree 6, connects to 1 community
- [[TestStandardPIIAlwaysCaught]] - degree 6, connects to 1 community
- [[TestAsymmetricFloor]] - degree 4, connects to 1 community
