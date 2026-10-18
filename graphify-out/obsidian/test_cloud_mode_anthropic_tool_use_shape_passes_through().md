---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "_make_proxy()"
location: "L302"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# test_cloud_mode_anthropic_tool_use_shape_passes_through()

## Connections
- [[Cloud mode Anthropic tool_use responses are unmodified (baseline parity).]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_7]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
