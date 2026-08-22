---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "Llm Proxy"
location: "L307"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Llm_Proxy
---

# _TrackingInjector

## Connections
- [[.__init__()_170]] - `method` [EXTRACTED]
- [[.inject_headers()]] - `method` [EXTRACTED]
- [[Fake CredentialInjector that records inject_headers calls and applies Anthropic]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `uses` [INFERRED]
- [[test_credential_injector_called_in_streaming_path()]] - `calls` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - `calls` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()]] - `calls` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()]] - `calls` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Llm_Proxy