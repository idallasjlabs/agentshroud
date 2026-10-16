---
type: community
cohesion: 0.07
members: 59
---

# HeuristicClassifier

**Cohesion:** 0.07 - loosely connected
**Members:** 59 nodes

## Members
- [[dot-__init__()_28]] - code - gateway/security/heuristic_classifier.py
- [[dot-_extract_owner_target()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_extract_owner_target_resolved()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_resolve_pending_username_target()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_try_load_model()]] - code - gateway/security/heuristic_classifier.py
- [[dot-test_base64_payload_normalized()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classic_override_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classic_payloads_individually()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classifier_flags_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_context_injection_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_detection_breakdown_by_category()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_encoding_bypass_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_high_confidence_payloads()]] - code - gateway/tests/test_adversarial_injection.py
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
- [[Heuristic injection classifier using multi-signal analysis.      Scoring approac]] - rationale - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier]] - code - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier_1]] - code - gateway/security/heuristic_classifier.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Multilingual injection variants.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Normalize input text to defeat encoding-based evasion.      Applied before all s]] - rationale - gateway/security/input_normalizer.py
- [[Parse owner command target as numeric id or known collaborator alias.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persona hijack  DAN-style payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard]] - code - gateway/tests/test_adversarial_injection.py
- [[PromptGuard scans high-confidence classic payloads with non-zero score.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Report per-category detection rates for observability (not a gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Resolve owner target from pending-request username aliases (e.g., approve ana).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Resolve target by id, static alias, or pending username alias.          Resoluti]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if HeuristicClassifier flags as injection or uncertain.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if InputNormalizer changes the text (encoding detected).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if PromptGuard assigns a non-zero score or blocks.]] - rationale - gateway/tests/test_adversarial_injection.py
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
- [[_any_detector_fires()]] - code - gateway/tests/test_adversarial_injection.py
- [[_heuristic_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[_normalizer_transforms()]] - code - gateway/tests/test_adversarial_injection.py
- [[_prompt_guard_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[normalize_input()]] - code - gateway/security/input_normalizer.py
- [[test_adversarial_injection.py]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HeuristicClassifier
SORT file.name ASC
```

## Connections to other communities
- 48 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 15 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 12 edges to [[_COMMUNITY_PIIConfig]]
- 8 edges to [[_COMMUNITY_HeuristicClassifier_1]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_dot-_proxy_request_impl]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_Action]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_ContextSegment]]

## Top bridge nodes
- [[normalize_input()]] - degree 80, connects to 8 communities
- [[HeuristicClassifier_1]] - degree 26, connects to 3 communities
- [[TestOverallDetectionRate]] - degree 8, connects to 2 communities
- [[test_adversarial_injection.py]] - degree 16, connects to 1 community
- [[HeuristicClassifier]] - degree 15, connects to 1 community
