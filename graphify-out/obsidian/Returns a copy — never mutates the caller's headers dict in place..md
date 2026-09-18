---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "LLMProxy"
location: "L652"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/LLMProxy
---

# Returns a copy — never mutates the caller's headers dict in place.

## Connections
- [[test_local_backend_headers_does_not_mutate_input()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/LLMProxy