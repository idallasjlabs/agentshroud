---
source_file: "gateway/security/resource_guard.py"
type: "code"
community: "VRAMHeadroomError"
location: "L25"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/VRAMHeadroomError
---

# VRAMHeadroomError

## Connections
- [[dot-check_vram_headroom()]] - `calls` [EXTRACTED]
- [[Exception_4]] - `inherits` [EXTRACTED]
- [[Raised when a local-model call is rejected because estimated VRAM usage would…]] - `rationale_for` [EXTRACTED]
- [[TestVramHeadroom]] - `uses` [INFERRED]
- [[resource_guard.py]] - `contains` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `imports` [EXTRACTED]
- [[test_resource_guard_limits.py]] - `imports` [EXTRACTED]
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - `uses` [INFERRED]
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - `uses` [INFERRED]
- [[test_vram_headroom_error_is_not_resource_warning()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/VRAMHeadroomError
