---
source_file: "gateway/tests/test_security_hardening.py"
type: "code"
community: "Module Group 79"
location: "L842"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Module_Group_79
---

# TestEgressSSRF

## Connections
- [[.setup_method()_30]] - `method` [EXTRACTED]
- [[.test_block_ipv4_mapped_ipv6_loopback()]] - `method` [EXTRACTED]
- [[.test_block_ipv4_mapped_ipv6_private()]] - `method` [EXTRACTED]
- [[.test_block_ipv4_private()]] - `method` [EXTRACTED]
- [[.test_block_ipv6_link_local()]] - `method` [EXTRACTED]
- [[.test_block_ipv6_loopback()]] - `method` [EXTRACTED]
- [[.test_block_ipv6_ula()]] - `method` [EXTRACTED]
- [[.test_block_link_local()]] - `method` [EXTRACTED]
- [[.test_block_localhost_variants()]] - `method` [EXTRACTED]
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
- [[Tests for SSRF protection in egress filter.]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Module_Group_79