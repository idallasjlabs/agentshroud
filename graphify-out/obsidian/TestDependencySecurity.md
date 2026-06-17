---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L633"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Environment_Guard__Leak_Detection
---

# TestDependencySecurity

## Connections
- [[.test_no_pickle_in_security_modules()]] - `method` [EXTRACTED]
- [[.test_no_shell_true_in_subprocess()]] - `method` [EXTRACTED]
- [[.test_no_yaml_unsafe_load()]] - `method` [EXTRACTED]
- [[.test_requirements_pinned()]] - `method` [EXTRACTED]
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
- [[Test dependency and supply chain security.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Environment_Guard__Leak_Detection