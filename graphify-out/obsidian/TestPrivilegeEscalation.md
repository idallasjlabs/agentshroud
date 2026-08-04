---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Subagent Monitor"
location: "L517"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Subagent_Monitor
---

# TestPrivilegeEscalation

## Connections
- [[.test_consent_required_for_sensitive_ops()]] - `method` [EXTRACTED]
- [[.test_session_cannot_impersonate()]] - `method` [EXTRACTED]
- [[.test_subagent_monitor_tracks_events()]] - `method` [EXTRACTED]
- [[.test_trust_cannot_exceed_max()]] - `method` [EXTRACTED]
- [[.test_unregistered_agent_blocked()]] - `method` [EXTRACTED]
- [[.test_violation_drops_trust_significantly()]] - `method` [EXTRACTED]
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
- [[Test trust boundaries and privilege escalation prevention.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Subagent_Monitor
