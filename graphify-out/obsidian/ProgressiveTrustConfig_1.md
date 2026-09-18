---
source_file: "gateway/security/progressive_trust_config.py"
type: "code"
community: "A2APolicyEngine"
location: "L86"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2APolicyEngine
---

# ProgressiveTrustConfig

## Connections
- [[.get_next_trust_level()]] - `method` [EXTRACTED]
- [[.get_previous_trust_level()]] - `method` [EXTRACTED]
- [[.get_trust_level_order()]] - `method` [EXTRACTED]
- [[.is_tool_allowed()_1]] - `method` [EXTRACTED]
- [[A2APeerTestDouble]] - `uses` [INFERRED]
- [[Configuration for the progressive trust system.]] - `rationale_for` [EXTRACTED]
- [[Request_2]] - `uses` [INFERRED]
- [[Response_1]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[_StubForwarder_2]] - `uses` [INFERRED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[progressive_trust_config.py]] - `contains` [EXTRACTED]
- [[test_a2a_integration.py]] - `imports` [EXTRACTED]
- [[test_a2a_ssrf_callback_is_a_severe_violation_by_default()]] - `calls` [EXTRACTED]
- [[test_a2a_ssrf_callback_penalty_matches_malicious_intent_tier()]] - `calls` [EXTRACTED]
- [[test_a2a_task_ownership_violation_has_a_configured_penalty_heavier_than_generic_policy()]] - `calls` [EXTRACTED]
- [[test_a2a_trust_scoring.py]] - `imports` [EXTRACTED]
- [[trust_manager()]] - `calls` [EXTRACTED]
- [[trust_manager()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2APolicyEngine