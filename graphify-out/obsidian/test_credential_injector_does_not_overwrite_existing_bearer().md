---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_voice_gateway.py"
location: "L455"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# test_credential_injector_does_not_overwrite_existing_bearer()

## Connections
- [[LLMProxy]] - `uses` [INFERRED]
- [[OpenClaw already sends Authorization Bearer — injector must leave it untouched.]] - `rationale_for` [EXTRACTED]
- [[_FakeSanitizer]] - `calls` [EXTRACTED]
- [[_TrackingInjector]] - `calls` [EXTRACTED]
- [[_make_fake_urlopen()]] - `calls` [EXTRACTED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_voice_gatewaypy
