---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "_make_update"
location: "L5210"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_update
---

# .test_self_diagnose_with_zero_width_char_is_handled_locally()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Zero-width obfuscation should not bypass self-diagnose local handling.]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_22]] - `references` [EXTRACTED]
- [[fake_urlopen()_75]] - `contains` [EXTRACTED]
- [[fake_urlopen()_51]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/_make_update
