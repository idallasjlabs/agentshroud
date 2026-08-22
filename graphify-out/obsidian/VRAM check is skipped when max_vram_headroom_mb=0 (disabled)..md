---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "Resource Guard & Local Model Parity"
location: "L479"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Resource_Guard__Local_Model_Parity
---

# VRAM check is skipped when max_vram_headroom_mb=0 (disabled).

## Connections
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Resource_Guard__Local_Model_Parity