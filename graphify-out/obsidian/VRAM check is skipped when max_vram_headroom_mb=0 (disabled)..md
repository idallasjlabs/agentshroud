---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "LLM Proxy Resource Guard"
location: "L477"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/LLM_Proxy_Resource_Guard
---

# VRAM check is skipped when max_vram_headroom_mb=0 (disabled).

## Connections
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/LLM_Proxy_Resource_Guard