---
source_file: "gateway/tests/test_security_hardening.py"
type: "code"
community: "Security Hardening"
location: "L280"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Hardening
---

# TestTrustManager

## Connections
- [[.setup_method()_28]] - `method` [EXTRACTED]
- [[.teardown_method()_6]] - `method` [EXTRACTED]
- [[.test_action_allowed_basic()]] - `method` [EXTRACTED]
- [[.test_action_denied_high_trust()]] - `method` [EXTRACTED]
- [[.test_action_unknown_agent()]] - `method` [EXTRACTED]
- [[.test_failure_decreases_score()]] - `method` [EXTRACTED]
- [[.test_get_trust()]] - `method` [EXTRACTED]
- [[.test_get_trust_unknown()]] - `method` [EXTRACTED]
- [[.test_history()]] - `method` [EXTRACTED]
- [[.test_register_agent()]] - `method` [EXTRACTED]
- [[.test_register_idempotent()]] - `method` [EXTRACTED]
- [[.test_score_never_negative()]] - `method` [EXTRACTED]
- [[.test_sqlite_persistence()]] - `method` [EXTRACTED]
- [[.test_success_increases_score()]] - `method` [EXTRACTED]
- [[.test_trust_escalation_attack()]] - `method` [EXTRACTED]
- [[.test_trust_level_progression()]] - `method` [EXTRACTED]
- [[.test_violation_large_decrease()]] - `method` [EXTRACTED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[IsolationStatus]] - `uses` [INFERRED]
- [[IsolationVerifier]] - `uses` [INFERRED]
- [[PatternRule]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Hardening