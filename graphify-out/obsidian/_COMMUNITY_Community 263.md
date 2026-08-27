---
type: community
members: 64
---

# Community 263

**Members:** 64 nodes

## Members
- [[.__init__()_85]] - code - gateway/security/heuristic_classifier.py
- [[._classify_heuristic()]] - code - gateway/security/heuristic_classifier.py
- [[._classify_ml()]] - code - gateway/security/heuristic_classifier.py
- [[._compute_unicode_anomaly()]] - code - gateway/security/heuristic_classifier.py
- [[._score_signal()]] - code - gateway/security/heuristic_classifier.py
- [[._try_load_model()]] - code - gateway/security/heuristic_classifier.py
- [[.classify()]] - code - gateway/security/heuristic_classifier.py
- [[.test_base64_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_classic_override_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_classic_payloads_individually()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_classifier_flags_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_context_injection_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_detection_breakdown_by_category()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_encoding_bypass_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_high_confidence_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_multilingual_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_overall_detection_rate_meets_threshold()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_payload_count_meets_minimum()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_persona_hijack_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_prompt_extraction_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_url_encoded_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_zero_width_space_stripped()]] - code - gateway/tests/test_adversarial_injection.py
- [[Classic instruction-override payloads — should have near-100% detection.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Classify text for injection probability.          Args             text Input]] - rationale - gateway/security/heuristic_classifier.py
- [[Combined detected if ANY defense layer triggers.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Context  document retrieval poisoning payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Detect unusual Unicode patterns that suggest evasion.]] - rationale - gateway/security/heuristic_classifier.py
- [[Encoding bypass variants — validates InputNormalizer multi-pass decode.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[End-to-end all 110+ payloads against combined defense layer.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Ensure the payload library stays above 100 entries (CI regression gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Heuristic injection classifier using multi-signal analysis.      Scoring approac]] - rationale - gateway/security/heuristic_classifier.py
- [[Heuristic-based classification using multi-signal analysis.]] - rationale - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier]] - code - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier_1]] - code - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Multilingual injection variants.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Normalize input text to defeat encoding-based evasion.      Applied before all s]] - rationale - gateway/security/input_normalizer.py
- [[Pattern]] - code - gateway/security/heuristic_classifier.py
- [[Persona hijack  DAN-style payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard_1]] - code - gateway/tests/test_adversarial_injection.py
- [[PromptGuard scans high-confidence classic payloads with non-zero score.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Report per-category detection rates for observability (not a gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if HeuristicClassifier flags as injection or uncertain.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if InputNormalizer changes the text (encoding detected).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if PromptGuard assigns a non-zero score or blocks.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Score a single signal pattern. Returns 0.0–1.0.]] - rationale - gateway/security/heuristic_classifier.py
- [[System prompt extraction payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestClassicOverride]] - code - gateway/tests/test_adversarial_injection.py
- [[TestContextInjection]] - code - gateway/tests/test_adversarial_injection.py
- [[TestEncodingBypass]] - code - gateway/tests/test_adversarial_injection.py
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
- [[normalize_input()]] - code - gateway/security/input_normalizer.py
- [[test_adversarial_injection.py]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_263
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_Community 4]]
- 15 edges to [[_COMMUNITY_Community 116]]
- 10 edges to [[_COMMUNITY_Community 93]]
- 6 edges to [[_COMMUNITY_Community 270]]
- 4 edges to [[_COMMUNITY_Community 6]]
- 4 edges to [[_COMMUNITY_Community 862]]
- 3 edges to [[_COMMUNITY_Community 1118]]
- 2 edges to [[_COMMUNITY_Community 1130]]
- 2 edges to [[_COMMUNITY_Community 1347]]
- 2 edges to [[_COMMUNITY_Community 54]]
- 1 edge to [[_COMMUNITY_Community 134]]
- 1 edge to [[_COMMUNITY_Community 799]]
- 1 edge to [[_COMMUNITY_Community 659]]
- 1 edge to [[_COMMUNITY_Community 16]]

## Top bridge nodes
- [[normalize_input()]] - degree 80, connects to 12 communities
- [[HeuristicClassifier]] - degree 26, connects to 3 communities
- [[test_adversarial_injection.py]] - degree 16, connects to 1 community
- [[PromptGuard_1]] - degree 15, connects to 1 community
- [[HeuristicClassifier_1]] - degree 15, connects to 1 community