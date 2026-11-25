---
source_file: "gateway/security/credential_injector.py"
type: "code"
community: "CredentialInjector"
location: "L98"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/CredentialInjector
---

# CredentialInjector

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_212]] - `method` [EXTRACTED]
- [[dot-_load_credentials()]] - `method` [EXTRACTED]
- [[dot-_load_default_mappings()]] - `method` [EXTRACTED]
- [[dot-_make_anthropic_injector()]] - `references` [EXTRACTED]
- [[dot-get_all_loaded_values()]] - `method` [EXTRACTED]
- [[dot-get_status()_2]] - `method` [EXTRACTED]
- [[dot-has_credential()]] - `method` [EXTRACTED]
- [[dot-inject_headers()_1]] - `method` [EXTRACTED]
- [[dot-injector()]] - `calls` [EXTRACTED]
- [[dot-injector()_1]] - `calls` [EXTRACTED]
- [[dot-injector_with_secrets()]] - `calls` [EXTRACTED]
- [[dot-scan_for_credential_leak()]] - `method` [EXTRACTED]
- [[dot-test_leak_detection_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_no_injection_when_disabled()]] - `calls` [EXTRACTED]
- [[Injects credentials into outbound requests based on destination domain. The…]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestCredentialInjection]] - `uses` [INFERRED]
- [[TestCredentialInjector]] - `uses` [INFERRED]
- [[TestCredentialLeakDetection]] - `uses` [INFERRED]
- [[TestLeakDetection]] - `uses` [INFERRED]
- [[TestLoadAllSecretFileValues]] - `uses` [INFERRED]
- [[TestOAuthInjection]] - `uses` [INFERRED]
- [[credential_injector.py]] - `contains` [EXTRACTED]
- [[injector()]] - `uses` [INFERRED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[test_credential_injector.py]] - `imports` [EXTRACTED]
- [[test_credential_isolation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/CredentialInjector
