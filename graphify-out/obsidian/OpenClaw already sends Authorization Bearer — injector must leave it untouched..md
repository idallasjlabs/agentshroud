---
source_file: "gateway/tests/test_llm_proxy.py"
type: "rationale"
community: "test_voice_gateway.py"
location: "L456"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# OpenClaw already sends Authorization: Bearer — injector must leave it untouched.

## Connections
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_voice_gatewaypy
