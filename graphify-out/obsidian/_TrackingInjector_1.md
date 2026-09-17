---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "LLMProxy"
location: "L388"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxy
---

# _TrackingInjector

## Connections
- [[.__init__()_207]] - `method` [EXTRACTED]
- [[.inject_headers()_2]] - `method` [EXTRACTED]
- [[Fake CredentialInjector that records inject_headers calls and applies Anthropic]] - `rationale_for` [EXTRACTED]
- [[LLMProxy_2]] - `uses` [INFERRED]
- [[test_credential_injector_called_in_streaming_path()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_does_not_overwrite_existing_bearer()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_injects_bearer_for_anthropic_x_api_key()_1]] - `calls` [EXTRACTED]
- [[test_credential_injector_not_applied_for_non_anthropic_dest()_1]] - `calls` [EXTRACTED]
- [[test_llm_proxy.py_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxy