---
type: community
cohesion: 0.18
members: 17
---

# _any_detector_fires()

**Cohesion:** 0.18 - loosely connected
**Members:** 17 nodes

## Members
- [[.test_base64_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_classic_override_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_classic_payloads_individually()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_encoding_bypass_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_url_encoded_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_zero_width_space_stripped()]] - code - gateway/tests/test_adversarial_injection.py
- [[Classic instruction-override payloads — should have near-100% detection.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Combined detected if ANY defense layer triggers.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Encoding bypass variants — validates InputNormalizer multi-pass decode.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard_1]] - code - gateway/tests/test_adversarial_injection.py
- [[Return True if InputNormalizer changes the text (encoding detected).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if PromptGuard assigns a non-zero score or blocks.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestClassicOverride]] - code - gateway/tests/test_adversarial_injection.py
- [[TestEncodingBypass]] - code - gateway/tests/test_adversarial_injection.py
- [[_any_detector_fires()]] - code - gateway/tests/test_adversarial_injection.py
- [[_normalizer_transforms()]] - code - gateway/tests/test_adversarial_injection.py
- [[_prompt_guard_detects()]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_any_detector_fires
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_test_adversarial_injection.py]]
- 6 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_TestOverallDetectionRate]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_HeuristicClassifier]]
- 2 edges to [[_COMMUNITY_TestPromptExtraction]]
- 1 edge to [[_COMMUNITY_TestPromptGuardDirectly]]

## Top bridge nodes
- [[PromptGuard_1]] - degree 15, connects to 6 communities
- [[TestEncodingBypass]] - degree 9, connects to 4 communities
- [[_any_detector_fires()]] - degree 17, connects to 3 communities
- [[TestClassicOverride]] - degree 6, connects to 3 communities
- [[.test_base64_payload_normalized()]] - degree 6, connects to 2 communities