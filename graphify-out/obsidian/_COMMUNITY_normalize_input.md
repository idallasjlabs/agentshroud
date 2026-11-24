---
type: community
members: 96
---

# normalize_input

**Members:** 96 nodes

## Members
- [[dot-__init__()_199]] - code - gateway/security/heuristic_classifier.py
- [[dot-_classify_heuristic()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_classify_ml()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_compute_unicode_anomaly()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_looks_like_hypothetical_execution_question()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_looks_like_identity_enumeration_query()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_score_signal()]] - code - gateway/security/heuristic_classifier.py
- [[dot-_try_load_model()]] - code - gateway/security/heuristic_classifier.py
- [[dot-classify()]] - code - gateway/security/heuristic_classifier.py
- [[dot-is_injection()]] - code - gateway/security/heuristic_classifier.py
- [[dot-is_uncertain()]] - code - gateway/security/heuristic_classifier.py
- [[dot-setup_method()_38]] - code - gateway/tests/test_heuristic_classifier.py
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
- [[dot-test_looks_like_hypothetical_execution_question_detects_approval_wording()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_looks_like_identity_enumeration_query_detects_owner_id_probe()]] - code - gateway/tests/test_telegram_proxy_inbound.py
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
- [[dot-test_url_encoded_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_zero_width_space_stripped()]] - code - gateway/tests/test_adversarial_injection.py
- [[Adversarial Prompt Injection Test Suite — v0.9.0 Tests AgentShroud defenses…]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Classic instruction-override payloads — should have near-100% detection.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[ClassificationResult]] - code - gateway/security/heuristic_classifier.py
- [[Classify text for injection probability. Args text Input text to classify…]] - rationale - gateway/security/heuristic_classifier.py
- [[Combined detected if ANY defense layer triggers.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Context  document retrieval poisoning payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Detect collaborator prompts attempting ownercollaborator identity disclosure.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect policy questions about execution behavior (not actual execution asks).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect unusual Unicode patterns that suggest evasion.]] - rationale - gateway/security/heuristic_classifier.py
- [[Encoding bypass variants — validates InputNormalizer multi-pass decode.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[End-to-end all 110+ payloads against combined defense layer.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Ensure the payload library stays above 100 entries (CI regression gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Heuristic Injection Classifier — multi-signal scoring for injection detection.…]] - rationale - gateway/security/heuristic_classifier.py
- [[Heuristic injection classifier using multi-signal analysis. Scoring approach -…]] - rationale - gateway/security/heuristic_classifier.py
- [[Heuristic-based classification using multi-signal analysis.]] - rationale - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier]] - code - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Input Normalization — pre-process text before security scanning. Strips…]] - rationale - gateway/security/input_normalizer.py
- [[Multilingual injection variants.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Normalize input text to defeat encoding-based evasion. Applied before all…]] - rationale - gateway/security/input_normalizer.py
- [[Pattern_5]] - code
- [[Persona hijack  DAN-style payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
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
- [[TestEncodingBypass]] - code - gateway/tests/test_adversarial_injection.py
- [[TestHeuristicClassifier]] - code - gateway/tests/test_heuristic_classifier.py
- [[TestHeuristicClassifierDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[TestMultilingual]] - code - gateway/tests/test_adversarial_injection.py
- [[TestOverallDetectionRate]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPersonaHijack]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPromptExtraction]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPromptGuardDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[Tests for heuristic injection classifier.]] - rationale - gateway/tests/test_heuristic_classifier.py
- [[EXPERIMENTAL Attempt to load a fine-tuned ML model. Returns True on success.…]] - rationale - gateway/security/heuristic_classifier.py
- [[EXPERIMENTAL ML model classification placeholder.]] - rationale - gateway/security/heuristic_classifier.py
- [[_any_detector_fires()]] - code - gateway/tests/test_adversarial_injection.py
- [[_heuristic_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[_normalizer_transforms()]] - code - gateway/tests/test_adversarial_injection.py
- [[_prompt_guard_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[heuristic_classifier.py]] - code - gateway/security/heuristic_classifier.py
- [[input_normalizer.py_2]] - code - gateway/security/input_normalizer.py
- [[normalize_input()]] - code - gateway/security/input_normalizer.py
- [[parametrize_26]] - code
- [[test_adversarial_injection.py]] - code - gateway/tests/test_adversarial_injection.py
- [[test_heuristic_classifier.py]] - code - gateway/tests/test_heuristic_classifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/normalize_input
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 13 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 12 edges to [[_COMMUNITY_lifespan.py]]
- 8 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 7 edges to [[_COMMUNITY_TestOutboundClassifierHelpers]]
- 5 edges to [[_COMMUNITY_prompt_guard.py]]
- 3 edges to [[_COMMUNITY_make_event]]
- 3 edges to [[_COMMUNITY_ToolResultInjectionScanner]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_dot-_looks_like_safe_collaborator_info_query]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]
- 1 edge to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_dot-_normalize_command_token]]
- 1 edge to [[_COMMUNITY_TestBuildCollaboratorSafeInfoResponse]]

## Top bridge nodes
- [[normalize_input()]] - degree 81, connects to 14 communities
- [[input_normalizer.py_2]] - degree 11, connects to 7 communities
- [[HeuristicClassifier]] - degree 27, connects to 4 communities
- [[test_adversarial_injection.py]] - degree 20, connects to 2 communities
- [[_any_detector_fires()]] - degree 17, connects to 1 community
