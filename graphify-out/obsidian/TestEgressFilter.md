---
source_file: "gateway/tests/test_security_hardening.py"
type: "code"
community: "EgressFilter"
location: "L406"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/EgressFilter
---

# TestEgressFilter

## Connections
- [[.setup_method()_14]] - `method` [EXTRACTED]
- [[.test_allowed_domain()]] - `method` [EXTRACTED]
- [[.test_allowed_ip()]] - `method` [EXTRACTED]
- [[.test_allowed_specific_ip()]] - `method` [EXTRACTED]
- [[.test_denied_domain()]] - `method` [EXTRACTED]
- [[.test_denied_ip()]] - `method` [EXTRACTED]
- [[.test_denied_port()]] - `method` [EXTRACTED]
- [[.test_deny_all_false()]] - `method` [EXTRACTED]
- [[.test_empty_ports_allows_all()]] - `method` [EXTRACTED]
- [[.test_log()]] - `method` [EXTRACTED]
- [[.test_per_agent_policy()]] - `method` [EXTRACTED]
- [[.test_stats()_1]] - `method` [EXTRACTED]
- [[.test_url_parsing()]] - `method` [EXTRACTED]
- [[.test_url_port_extraction()]] - `method` [EXTRACTED]
- [[.test_wildcard_base_domain()]] - `method` [EXTRACTED]
- [[.test_wildcard_domain()]] - `method` [EXTRACTED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig_1]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[IsolationStatus]] - `uses` [INFERRED]
- [[IsolationVerifier]] - `uses` [INFERRED]
- [[PatternRule]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/EgressFilter