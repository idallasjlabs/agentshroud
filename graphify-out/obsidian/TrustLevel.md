---
source_file: "gateway/security/trust_manager.py"
type: "code"
community: "TrustLevel"
location: "L29"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/TrustLevel
---

# TrustLevel

## Connections
- [[.__init__()_7]] - `references` [EXTRACTED]
- [[._force_demotion()]] - `calls` [EXTRACTED]
- [[._promotion_allowed()]] - `references` [EXTRACTED]
- [[._score_to_level()]] - `calls` [EXTRACTED]
- [[._update_score()]] - `calls` [EXTRACTED]
- [[.get_trust()]] - `calls` [EXTRACTED]
- [[.record_failure()]] - `references` [EXTRACTED]
- [[.record_success()]] - `references` [EXTRACTED]
- [[.record_violation()]] - `references` [EXTRACTED]
- [[.register_agent()]] - `references` [EXTRACTED]
- [[IntEnum]] - `inherits` [EXTRACTED]
- [[PIISanitizer_3]] - `uses` [INFERRED]
- [[PromptGuard]] - `conceptually_related_to` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[TestActionGating]] - `uses` [INFERRED]
- [[TestAgentIsolation]] - `uses` [INFERRED]
- [[TestAgentRegistration]] - `uses` [INFERRED]
- [[TestBackwardCompat]] - `uses` [INFERRED]
- [[TestBotIdIsolationInSharedMemory]] - `uses` [INFERRED]
- [[TestConfig]] - `uses` [INFERRED]
- [[TestCrossBotTrustPivot]] - `uses` [INFERRED]
- [[TestDriftDetector]] - `uses` [INFERRED]
- [[TestDriftDetectorHardened]] - `uses` [INFERRED]
- [[TestEgressFilter]] - `uses` [INFERRED]
- [[TestEgressSSRF]] - `uses` [INFERRED]
- [[TestEncryptedStore]] - `uses` [INFERRED]
- [[TestEnforcementMode]] - `uses` [INFERRED]
- [[TestEnumMapping]] - `uses` [INFERRED]
- [[TestGatedPromotion]] - `uses` [INFERRED]
- [[TestHermesDashboardBridgeReachability]] - `uses` [INFERRED]
- [[TestHermesDashboardForwarderBinding]] - `uses` [INFERRED]
- [[TestHermesEgressAllowlist]] - `uses` [INFERRED]
- [[TestHermesTrustSeeding]] - `uses` [INFERRED]
- [[TestHistory]] - `uses` [INFERRED]
- [[TestPersistence_1]] - `uses` [INFERRED]
- [[TestPromptGuard_1]] - `uses` [INFERRED]
- [[TestPromptGuardEvasion]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestSessionPathSeparation]] - `uses` [INFERRED]
- [[TestToolACLComposition]] - `uses` [INFERRED]
- [[TestToolGating]] - `uses` [INFERRED]
- [[TestTrustLevels]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestTrustProgression]] - `uses` [INFERRED]
- [[TestTypedViolations]] - `uses` [INFERRED]
- [[UserSession]] - `references` [EXTRACTED]
- [[_set_state()]] - `uses` [INFERRED]
- [[gateway.security.trust_manager]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_e2e.py]] - `references` [EXTRACTED]
- [[test_progressive_trust_integration.py]] - `imports` [EXTRACTED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]
- [[test_security_regressions_v1_2.py]] - `imports` [EXTRACTED]
- [[test_trust_manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/TrustLevel