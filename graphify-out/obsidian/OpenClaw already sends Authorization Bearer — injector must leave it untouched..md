---
source_file: "gateway/tests/test_llm_proxy.py"
type: "rationale"
community: "Llm Proxy"
location: "L375"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Llm_Proxy
---

# OpenClaw already sends Authorization: Bearer — injector must leave it untouched.

## Connections
- [[test_credential_injector_does_not_overwrite_existing_bearer()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Llm_Proxy