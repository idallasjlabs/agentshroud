---
type: community
cohesion: 0.05
members: 88
---

# Community 45

**Cohesion:** 0.05 - loosely connected
**Members:** 88 nodes

## Members
- [[.__init__()_71]] - code - gateway/security/differential_pii_detector.py
- [[.__init__()_148]] - code - gateway/tests/test_differential_pii_detector.py
- [[.__post_init__()_4]] - code - gateway/security/differential_pii_detector.py
- [[._deduplicate()]] - code - gateway/security/differential_pii_detector.py
- [[._detect_pii()]] - code - gateway/security/differential_pii_detector.py
- [[._detect_presidio()]] - code - gateway/security/differential_pii_detector.py
- [[._detect_regex()]] - code - gateway/security/differential_pii_detector.py
- [[._detector_with_fake()]] - code - gateway/tests/test_differential_pii_detector.py
- [[._init_presidio()_1]] - code - gateway/security/differential_pii_detector.py
- [[._redact()]] - code - gateway/security/differential_pii_detector.py
- [[._scan()]] - code - gateway/security/differential_pii_detector.py
- [[.from_confidence()]] - code - gateway/security/differential_pii_detector.py
- [[.scan_prompt()]] - code - gateway/security/differential_pii_detector.py
- [[.scan_tool_result()_1]] - code - gateway/security/differential_pii_detector.py
- [[.test_bare_city_name_not_flagged_but_street_address_is()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_cannot_set_tool_floor_above_prompt_floor()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_cannot_set_tool_floor_below_minimum()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_clean_content_no_hits()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_core_ssn_unioned_when_presidio_misses_it()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_default_config_has_correct_floors()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_dotted_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_email_redacted_in_output()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_init_does_not_construct_bare_analyzer_engine()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_init_wires_explicit_nlp_engine_when_model_present()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_pii_hit_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_plain_email_caught_in_prompt()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_plain_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_presidio_analyze_restricted_to_pii_entities()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_presidio_exception_falls_back_to_regex()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_presidio_result_becomes_pii_hit()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_redact_on_hit_false_preserves_original()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_redacted_content_is_original_when_no_pii()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_regex_fallback_when_model_absent()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_report_has_required_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_scan_produces_report_with_correct_floor_used()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_spaced_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_tool_specific_floor_override()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_unknown_tool_uses_default_floor()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_us_ssn_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_weak_hit_present_in_tool_result_only()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_zero_width_space_injection_caught()]] - code - gateway/tests/test_differential_pii_detector.py
- [[A single PII detection result.]] - rationale - gateway/security/differential_pii_detector.py
- [[A weak-confidence hit (0.75) must appear in tool results but not prompts.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts.      Thi]] - rationale - gateway/security/differential_pii_detector.py
- [[Attempt to initialise Presidio deterministically; else regex.          SECURITY]] - rationale - gateway/security/differential_pii_detector.py
- [[Configuration for DifferentialPIIDetector.      Attributes         tool_result_]] - rationale - gateway/security/differential_pii_detector.py
- [[Core scan normalize adversarial patterns, then run PII recognition.]] - rationale - gateway/security/differential_pii_detector.py
- [[DifferentialPIIConfig_1]] - code - gateway/tests/test_differential_pii_detector.py
- [[DifferentialPIIConfig]] - code - gateway/security/differential_pii_detector.py
- [[DifferentialPIIDetector_1]] - code - gateway/tests/test_differential_pii_detector.py
- [[DifferentialPIIDetector]] - code - gateway/security/differential_pii_detector.py
- [[Email with Unicode dot separators.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Email with spaces added to defeat naive regex a l i c e @ e x a m p l e . c o m]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Exercise the Presidio detection path with an injected fake analyzer.      The re]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Full scan result for a tool result or prompt.]] - rationale - gateway/security/differential_pii_detector.py
- [[PII Sanitizer Mitigation (Presidio + custom regex)]] - rationale - docs/security/threat-model.md
- [[PII Sanitizer Module Badge Icon]] - image - branding/icons/modules/pii-sanitizer-256x256.png
- [[PII split with zero-width space.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[PIIHit]] - code - gateway/security/differential_pii_detector.py
- [[PIIHitSeverity]] - code - gateway/security/differential_pii_detector.py
- [[Presidio init must be deterministic and must NEVER trigger a runtime     model a]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Regex-based PII detection (Presidio fallback).]] - rationale - gateway/security/differential_pii_detector.py
- [[Relative risk of a detected PII entity.]] - rationale - gateway/security/differential_pii_detector.py
- [[Remove overlapping hits, preferring higher confidence.]] - rationale - gateway/security/differential_pii_detector.py
- [[Replace detected PII tokens with ENTITY_TYPE placeholders.]] - rationale - gateway/security/differential_pii_detector.py
- [[Run PII detection, returning hits at or above floor.]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a prompt with the standard (higher) confidence floor.          Args]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a tool result with the lower confidence floor.          Args             t]] - rationale - gateway/security/differential_pii_detector.py
- [[Strip common adversarial encoding tricks, return (normalized, count_removed).]] - rationale - gateway/security/differential_pii_detector.py
- [[TestAdversarialFormattingCaught]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestAsymmetricFloor]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestDeterministicPresidioInit]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestDifferentialPIIDetectorConstruction]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestPerToolConfiguration]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestPresidioPathContract]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestRedaction]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestStandardPIIAlwaysCaught]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestToolResultPIIReport]] - code - gateway/tests/test_differential_pii_detector.py
- [[The default-model auto-download path must never be taken.          If Presidio i]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[ToolResultPIIReport]] - code - gateway/security/differential_pii_detector.py
- [[Use Presidio (entity-restricted) unioned with the core regex.          Two guara]] - rationale - gateway/security/differential_pii_detector.py
- [[When the pinned model loads, Presidio is built with an explicit         ``nlp_en]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[_FakeRecognizerResult]] - code - gateway/tests/test_differential_pii_detector.py
- [[_normalize_adversarial()]] - code - gateway/security/differential_pii_detector.py
- [[default_config()]] - code - gateway/tests/test_differential_pii_detector.py
- [[detector()]] - code - gateway/tests/test_differential_pii_detector.py
- [[differential_pii_detector.py]] - code - gateway/security/differential_pii_detector.py
- [[test_differential_pii_detector.py]] - code - gateway/tests/test_differential_pii_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_45
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Community 110]]
- 2 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 2 edges to [[_COMMUNITY_Community 205]]
- 1 edge to [[_COMMUNITY_Community 19]]
- 1 edge to [[_COMMUNITY_Community 102]]
- 1 edge to [[_COMMUNITY_Community 199]]
- 1 edge to [[_COMMUNITY_Community 281]]
- 1 edge to [[_COMMUNITY_Community 55]]
- 1 edge to [[_COMMUNITY_Community 519]]

## Top bridge nodes
- [[DifferentialPIIDetector]] - degree 38, connects to 5 communities
- [[DifferentialPIIConfig]] - degree 25, connects to 2 communities
- [[differential_pii_detector.py]] - degree 9, connects to 2 communities
- [[PIIHitSeverity]] - degree 17, connects to 1 community
- [[PII Sanitizer Module Badge Icon]] - degree 2, connects to 1 community