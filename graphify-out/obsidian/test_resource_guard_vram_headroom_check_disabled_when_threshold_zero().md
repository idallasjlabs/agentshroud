---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "LLM Proxy Resource Guard"
location: "L476"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLM_Proxy_Resource_Guard
---

# test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()

## Connections
- [[ResourceGuard]] - `calls` [EXTRACTED]
- [[ResourceLimits]] - `calls` [EXTRACTED]
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - `rationale_for` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLM_Proxy_Resource_Guard