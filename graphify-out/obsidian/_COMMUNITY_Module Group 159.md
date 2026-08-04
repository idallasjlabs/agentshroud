---
type: community
cohesion: 0.13
members: 30
---

# Module Group 159

**Cohesion:** 0.13 - loosely connected
**Members:** 30 nodes

## Members
- [[.test_base64_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_classic_override_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_classic_payloads_individually()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_context_injection_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_encoding_bypass_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_multilingual_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_persona_hijack_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_url_encoded_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_zero_width_space_stripped()]] - code - gateway/tests/test_adversarial_injection.py
- [[Classic instruction-override payloads — should have near-100% detection.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Combined detected if ANY defense layer triggers.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Context  document retrieval poisoning payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Encoding bypass variants — validates InputNormalizer multi-pass decode.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier_1]] - code - gateway/tests/test_adversarial_injection.py
- [[Multilingual injection variants.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Persona hijack  DAN-style payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard_1]] - code - gateway/tests/test_adversarial_injection.py
- [[Return True if HeuristicClassifier flags as injection or uncertain.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if InputNormalizer changes the text (encoding detected).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if PromptGuard assigns a non-zero score or blocks.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestClassicOverride]] - code - gateway/tests/test_adversarial_injection.py
- [[TestContextInjection]] - code - gateway/tests/test_adversarial_injection.py
- [[TestEncodingBypass]] - code - gateway/tests/test_adversarial_injection.py
- [[TestMultilingual]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPersonaHijack]] - code - gateway/tests/test_adversarial_injection.py
- [[_any_detector_fires()]] - code - gateway/tests/test_adversarial_injection.py
- [[_heuristic_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[_normalizer_transforms()]] - code - gateway/tests/test_adversarial_injection.py
- [[_prompt_guard_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[test_adversarial_injection.py]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_159
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Module Group 197]]
- 8 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 7 edges to [[_COMMUNITY_Module Group 464]]
- 6 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 4 edges to [[_COMMUNITY_Module Group 604]]
- 2 edges to [[_COMMUNITY_Module Group 606]]
- 2 edges to [[_COMMUNITY_Module Group 605]]

## Top bridge nodes
- [[test_adversarial_injection.py]] - degree 16, connects to 7 communities
- [[HeuristicClassifier_1]] - degree 15, connects to 5 communities
- [[PromptGuard_1]] - degree 15, connects to 5 communities
- [[_any_detector_fires()]] - degree 17, connects to 2 communities
- [[TestEncodingBypass]] - degree 8, connects to 2 communities
