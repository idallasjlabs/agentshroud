---
type: community
cohesion: 0.10
members: 40
---

# test_soc_egress_endpoints.py

**Cohesion:** 0.10 - loosely connected
**Members:** 40 nodes

## Members
- [[dot-test_base64_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classic_override_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classic_payloads_individually()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_context_injection_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_detection_breakdown_by_category()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_encoding_bypass_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_multilingual_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_overall_detection_rate_meets_threshold()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_payload_count_meets_minimum()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_persona_hijack_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_prompt_extraction_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_url_encoded_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_zero_width_space_stripped()]] - code - gateway/tests/test_adversarial_injection.py
- [[Classic instruction-override payloads — should have near-100% detection.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Combined detected if ANY defense layer triggers.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Context  document retrieval poisoning payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Encoding bypass variants — validates InputNormalizer multi-pass decode.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[End-to-end all 110+ payloads against combined defense layer.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Ensure the payload library stays above 100 entries (CI regression gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier]] - code - gateway/tests/test_adversarial_injection.py
- [[Multilingual injection variants.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Persona hijack  DAN-style payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard]] - code - gateway/tests/test_adversarial_injection.py
- [[Report per-category detection rates for observability (not a gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if HeuristicClassifier flags as injection or uncertain.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if InputNormalizer changes the text (encoding detected).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if PromptGuard assigns a non-zero score or blocks.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[System prompt extraction payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestClassicOverride]] - code - gateway/tests/test_adversarial_injection.py
- [[TestContextInjection]] - code - gateway/tests/test_adversarial_injection.py
- [[TestEncodingBypass]] - code - gateway/tests/test_adversarial_injection.py
- [[TestMultilingual]] - code - gateway/tests/test_adversarial_injection.py
- [[TestOverallDetectionRate]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPersonaHijack]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPromptExtraction]] - code - gateway/tests/test_adversarial_injection.py
- [[_any_detector_fires()]] - code - gateway/tests/test_adversarial_injection.py
- [[_heuristic_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[_normalizer_transforms()]] - code - gateway/tests/test_adversarial_injection.py
- [[_prompt_guard_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[test_adversarial_injection.py]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_egress_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_PromptGuard]]
- 10 edges to [[_COMMUNITY_HeuristicClassifier]]
- 9 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 4 edges to [[_COMMUNITY_TestHeuristicClassifierDirectly]]

## Top bridge nodes
- [[test_adversarial_injection.py]] - degree 16, connects to 4 communities
- [[HeuristicClassifier]] - degree 15, connects to 3 communities
- [[PromptGuard]] - degree 15, connects to 3 communities
- [[TestEncodingBypass]] - degree 9, connects to 3 communities
- [[TestOverallDetectionRate]] - degree 8, connects to 2 communities
