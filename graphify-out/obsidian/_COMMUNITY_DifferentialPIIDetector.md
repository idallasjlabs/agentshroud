---
type: community
members: 82
---

# DifferentialPIIDetector

**Members:** 82 nodes

## Members
- [[dot-__init__()_202]] - code - gateway/security/differential_pii_detector.py
- [[dot-__init__()_203]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-__post_init__()_8]] - code - gateway/security/differential_pii_detector.py
- [[dot-_deduplicate()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_detect_pii()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_detect_presidio()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_detect_regex()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_detector_with_fake()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-_init_presidio()_1]] - code - gateway/security/differential_pii_detector.py
- [[dot-_redact()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_scan()]] - code - gateway/security/differential_pii_detector.py
- [[dot-from_confidence()]] - code - gateway/security/differential_pii_detector.py
- [[dot-scan_prompt()]] - code - gateway/security/differential_pii_detector.py
- [[dot-scan_tool_result()_3]] - code - gateway/security/differential_pii_detector.py
- [[dot-test_bare_city_name_not_flagged_but_street_address_is()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_clean_content_no_hits()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_core_ssn_unioned_when_presidio_misses_it()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_default_config_has_correct_floors()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_dotted_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_email_redacted_in_output()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_pii_hit_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_plain_email_caught_in_prompt()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_plain_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_presidio_analyze_restricted_to_pii_entities()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_presidio_exception_falls_back_to_regex()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_presidio_result_becomes_pii_hit()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_redact_on_hit_false_preserves_original()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_redacted_content_is_original_when_no_pii()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_report_has_required_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_scan_produces_report_with_correct_floor_used()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_spaced_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_tool_specific_floor_override()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_unknown_tool_uses_default_floor()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_us_ssn_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_weak_hit_present_in_tool_result_only()]] - code - gateway/tests/test_differential_pii_detector.py
- [[dot-test_zero_width_space_injection_caught()]] - code - gateway/tests/test_differential_pii_detector.py
- [[A single PII detection result.]] - rationale - gateway/security/differential_pii_detector.py
- [[A weak-confidence hit (0.75) must appear in tool results but not prompts.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts. This…]] - rationale - gateway/security/differential_pii_detector.py
- [[Attempt to initialise Presidio deterministically; else regex. SECURITY never…]] - rationale - gateway/security/differential_pii_detector.py
- [[Configuration for DifferentialPIIDetector. Attributes…]] - rationale - gateway/security/differential_pii_detector.py
- [[Core scan normalize adversarial patterns, then run PII recognition.]] - rationale - gateway/security/differential_pii_detector.py
- [[Differential PII Detector for Tool Results — Module 28 (v1.2.0) IEC 62443 FR3…]] - rationale - gateway/security/differential_pii_detector.py
- [[DifferentialPIIConfig]] - code - gateway/security/differential_pii_detector.py
- [[DifferentialPIIDetector]] - code - gateway/security/differential_pii_detector.py
- [[Email with Unicode dot separators.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Email with spaces added to defeat naive regex a l i c e @ e x a m p l e . c o m]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Exercise the Presidio detection path with an injected fake analyzer. The real…]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Full scan result for a tool result or prompt.]] - rationale - gateway/security/differential_pii_detector.py
- [[IntEnum_4]] - code
- [[PII split with zero-width space.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[PIIHit]] - code - gateway/security/differential_pii_detector.py
- [[PIIHitSeverity]] - code - gateway/security/differential_pii_detector.py
- [[Regex-based PII detection (Presidio fallback).]] - rationale - gateway/security/differential_pii_detector.py
- [[Relative risk of a detected PII entity.]] - rationale - gateway/security/differential_pii_detector.py
- [[Remove overlapping hits, preferring higher confidence.]] - rationale - gateway/security/differential_pii_detector.py
- [[Replace detected PII tokens with ENTITY_TYPE placeholders.]] - rationale - gateway/security/differential_pii_detector.py
- [[Run PII detection, returning hits at or above floor.]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a prompt with the standard (higher) confidence floor. Args content…]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a tool result with the lower confidence floor. Args tool_name Name of…]] - rationale - gateway/security/differential_pii_detector.py
- [[Strip common adversarial encoding tricks, return (normalized, count_removed).]] - rationale - gateway/security/differential_pii_detector.py
- [[TestAdversarialFormattingCaught]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestAsymmetricFloor]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestDifferentialPIIDetectorConstruction]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestPerToolConfiguration]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestPresidioPathContract]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestRedaction]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestStandardPIIAlwaysCaught]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestToolResultPIIReport]] - code - gateway/tests/test_differential_pii_detector.py
- [[Tests for Module 28 — Differential PII Detector for Tool Results. IEC 62443 FR3…]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[ToolResultPIIReport]] - code - gateway/security/differential_pii_detector.py
- [[Use Presidio (entity-restricted) unioned with the core regex. Two guarantees…]] - rationale - gateway/security/differential_pii_detector.py
- [[_FakeRecognizerResult_1]] - code - gateway/tests/test_differential_pii_detector.py
- [[_analyze()]] - code - gateway/tests/test_differential_pii_detector.py
- [[_boom()_27]] - code - gateway/tests/test_differential_pii_detector.py
- [[_collapse_spaced()]] - code - gateway/security/differential_pii_detector.py
- [[_normalize_adversarial()]] - code - gateway/security/differential_pii_detector.py
- [[default_config()_4]] - code - gateway/tests/test_differential_pii_detector.py
- [[detector()]] - code - gateway/tests/test_differential_pii_detector.py
- [[differential_pii_detector.py]] - code - gateway/security/differential_pii_detector.py
- [[fixture_129]] - code
- [[test_differential_pii_detector.py]] - code - gateway/tests/test_differential_pii_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DifferentialPIIDetector
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_A2AProxy]]
- 3 edges to [[_COMMUNITY_TestDeterministicPresidioInit]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[DifferentialPIIDetector]] - degree 48, connects to 4 communities
- [[DifferentialPIIConfig]] - degree 13, connects to 2 communities
- [[test_differential_pii_detector.py]] - degree 17, connects to 1 community
