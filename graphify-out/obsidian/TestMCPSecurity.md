---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L464"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Environment_Guard__Leak_Detection
---

# TestMCPSecurity

## Connections
- [[.test_context_guard_tool_manipulation()]] - `method` [EXTRACTED]
- [[.test_egress_filter_blocks_mcp_exfil()]] - `method` [EXTRACTED]
- [[.test_file_sandbox_mcp_write()]] - `method` [EXTRACTED]
- [[.test_mcp_proxy_module_exists()]] - `method` [EXTRACTED]
- [[.test_prompt_guard_catches_tool_injection()]] - `method` [EXTRACTED]
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
- [[Test MCP tool proxy security controls.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Environment_Guard__Leak_Detection