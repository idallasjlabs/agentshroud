---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Auth & Exception Types"
location: "L189"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Auth__Exception_Types
---

# TestConcurrency

## Connections
- [[.test_alert_dispatcher_concurrent_dispatch()]] - `method` [EXTRACTED]
- [[.test_context_guard_session_isolation_under_load()]] - `method` [EXTRACTED]
- [[.test_drift_detector_concurrent_writes()]] - `method` [EXTRACTED]
- [[.test_prompt_guard_concurrent_scans()]] - `method` [EXTRACTED]
- [[.test_trust_manager_rapid_updates()]] - `method` [EXTRACTED]
- [[AlertDispatcher]] - `uses` [INFERRED]
- [[ConsentDecision]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressChannel]] - `uses` [INFERRED]
- [[EgressEvent]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[EntropyCalculator]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MetadataGuard]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEventType]] - `uses` [INFERRED]
- [[SubagentMonitor]] - `uses` [INFERRED]
- [[Test thread safety and race conditions in security modules.]] - `rationale_for` [EXTRACTED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Auth__Exception_Types