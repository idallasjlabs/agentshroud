---
type: community
members: 82
---

# test_soc_egress_endpoints.py

**Members:** 82 nodes

## Members
- [[dot-__init__()_151]] - code - gateway/security/heuristic_classifier.py
- [[dot-_classify_heuristic()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_classify_ml()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_compute_unicode_anomaly()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_score_signal()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_try_load_model()]] - code - gateway/security/heuristic_classifier.py
- [[dot-classify()]] - code - gateway/security/heuristic_classifier.py
- [[dot-is_injection()]] - code - gateway/security/heuristic_classifier.py
- [[dot-is_uncertain()]] - code - gateway/security/heuristic_classifier.py
- [[dot-setup_method()_29]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_backward_compat_alias()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_base64_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_benign_text_low_score()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_classic_override_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classic_payloads_individually()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classification_result_properties()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_classifier_flags_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_clear_injection_high_score()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_context_injection_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_cyrillic_homoglyph()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_detection_breakdown_by_category()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_empty_text()_1]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_encoding_bypass_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_encoding_evasion()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_exfiltration_attempt()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_high_confidence_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_long_benign_text()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_model_not_loaded_by_default()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_multi_signal_increases_confidence()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_multilingual_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_overall_detection_rate_meets_threshold()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_payload_count_meets_minimum()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_persona_hijack_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_prompt_extraction_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_roleplay_attack()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_separator_injection()]] - code - gateway/tests/test_heuristic_classifier.py
- [[dot-test_unicode_anomaly()]] - code - gateway/tests/test_heuristic_classifier.py
- [[Classic instruction-override payloads — should have near-100% detection.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[ClassificationResult]] - code - gateway/security/heuristic_classifier.py
- [[Classify text for injection probability.          Args             text Input]] - rationale - gateway/security/heuristic_classifier.py
- [[Combined detected if ANY defense layer triggers.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Context  document retrieval poisoning payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Detect unusual Unicode patterns that suggest evasion.]] - rationale - gateway/security/heuristic_classifier.py
- [[End-to-end all 110+ payloads against combined defense layer.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Ensure the payload library stays above 100 entries (CI regression gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Heuristic injection classifier using multi-signal analysis.      Scoring approac]] - rationale - gateway/security/heuristic_classifier.py
- [[Heuristic-based classification using multi-signal analysis.]] - rationale - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier]] - code - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier_1]] - code - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[InjectionClassifier alias should still work.]] - rationale - gateway/tests/test_heuristic_classifier.py
- [[Multilingual injection variants.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Pattern_1]] - code - gateway/security/heuristic_classifier.py
- [[Persona hijack  DAN-style payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard_1]] - code - gateway/tests/test_adversarial_injection.py
- [[PromptGuard scans high-confidence classic payloads with non-zero score.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Report per-category detection rates for observability (not a gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Result of injection classification.]] - rationale - gateway/security/heuristic_classifier.py
- [[Return True if HeuristicClassifier flags as injection or uncertain.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if InputNormalizer changes the text (encoding detected).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if PromptGuard assigns a non-zero score or blocks.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Score a single signal pattern. Returns 0.0–1.0.]] - rationale - gateway/security/heuristic_classifier.py
- [[System prompt extraction payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Test the heuristic injection classifier.]] - rationale - gateway/tests/test_heuristic_classifier.py
- [[TestClassicOverride]] - code - gateway/tests/test_adversarial_injection.py
- [[TestContextInjection]] - code - gateway/tests/test_adversarial_injection.py
- [[TestHeuristicClassifier]] - code - gateway/tests/test_heuristic_classifier.py
- [[TestHeuristicClassifierDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[TestMultilingual]] - code - gateway/tests/test_adversarial_injection.py
- [[TestOverallDetectionRate]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPersonaHijack]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPromptExtraction]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPromptGuardDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[EXPERIMENTAL Attempt to load a fine-tuned ML model. Returns True on success.]] - rationale - gateway/security/heuristic_classifier.py
- [[EXPERIMENTAL ML model classification placeholder.]] - rationale - gateway/security/heuristic_classifier.py
- [[_any_detector_fires()]] - code - gateway/tests/test_adversarial_injection.py
- [[_heuristic_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[_normalizer_transforms()]] - code - gateway/tests/test_adversarial_injection.py
- [[_prompt_guard_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[heuristic_classifier.py (HeuristicClassifier)]] - code - gateway/security/heuristic_classifier.py
- [[test_adversarial_injection.py]] - code - gateway/tests/test_adversarial_injection.py
- [[test_heuristic_classifier.py]] - code - gateway/tests/test_heuristic_classifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_egress_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 10 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[HeuristicClassifier_1]] - degree 24, connects to 2 communities
- [[test_adversarial_injection.py]] - degree 16, connects to 2 communities
- [[HeuristicClassifier]] - degree 15, connects to 1 community
- [[PromptGuard_1]] - degree 15, connects to 1 community
- [[ClassificationResult]] - degree 10, connects to 1 community
