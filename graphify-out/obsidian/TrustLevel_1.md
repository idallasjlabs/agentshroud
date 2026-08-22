---
source_file: "gateway/security/trust_manager.py"
type: "code"
community: "Progressive Trust Integration"
location: "L31"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Progressive_Trust_Integration
---

# TrustLevel

## Connections
- [[.__init__()_127]] - `references` [EXTRACTED]
- [[._force_demotion()]] - `references` [EXTRACTED]
- [[._promotion_allowed()]] - `references` [EXTRACTED]
- [[._score_to_level()]] - `references` [EXTRACTED]
- [[._update_score()]] - `references` [EXTRACTED]
- [[.get_trust()]] - `references` [EXTRACTED]
- [[.record_failure()]] - `references` [EXTRACTED]
- [[.record_success()]] - `references` [EXTRACTED]
- [[.record_violation()]] - `references` [EXTRACTED]
- [[.register_agent()]] - `references` [EXTRACTED]
- [[IntEnum]] - `inherits` [EXTRACTED]
- [[PIISanitizer_3]] - `uses` [INFERRED]
- [[ProgressiveTrustConfig]] - `uses` [INFERRED]
- [[ProgressiveTrustConfig_2]] - `uses` [INFERRED]
- [[PromptGuard]] - `conceptually_related_to` [INFERRED]
- [[Role_1]] - `conceptually_related_to` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
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
- [[TestEnforcementModeResolver]] - `uses` [INFERRED]
- [[TestEnumMapping]] - `uses` [INFERRED]
- [[TestGatedPromotion]] - `uses` [INFERRED]
- [[TestHermesDashboardBridgeReachability]] - `uses` [INFERRED]
- [[TestHermesDashboardForwarderBinding]] - `uses` [INFERRED]
- [[TestHermesEgressAllowlist]] - `uses` [INFERRED]
- [[TestHermesTrustSeeding]] - `uses` [INFERRED]
- [[TestHistory]] - `uses` [INFERRED]
- [[TestPersistence_2]] - `uses` [INFERRED]
- [[TestProgressiveTrustConfigUnit]] - `uses` [INFERRED]
- [[TestPromptGuard_1]] - `uses` [INFERRED]
- [[TestPromptGuardEvasion]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestSessionPathSeparation]] - `uses` [INFERRED]
- [[TestToolACLComposition]] - `uses` [INFERRED]
- [[TestToolGating]] - `uses` [INFERRED]
- [[TestTrustLevels_1]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestTrustProgression]] - `uses` [INFERRED]
- [[TestTypedViolations]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `conceptually_related_to` [INFERRED]
- [[TrustLevel]] - `uses` [INFERRED]
- [[TrustLevel_2]] - `uses` [INFERRED]
- [[TrustManager_4]] - `uses` [INFERRED]
- [[TrustManager._update_score() (progressive promotion gate)]] - `references` [EXTRACTED]
- [[UserSession]] - `references` [EXTRACTED]
- [[ViolationType]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_e2e.py]] - `references` [EXTRACTED]
- [[test_progressive_trust_integration.py]] - `imports` [EXTRACTED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]
- [[test_security_regressions_v1_2.py]] - `imports` [EXTRACTED]
- [[test_trust_manager.py]] - `imports` [EXTRACTED]
- [[trust_manager.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Progressive_Trust_Integration