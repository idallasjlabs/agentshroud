---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "LLM Proxy Resource Guard"
location: "L447"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/LLM_Proxy_Resource_Guard
---

# check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.

## Connections
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/LLM_Proxy_Resource_Guard