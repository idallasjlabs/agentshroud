---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_self_diagnose_dedupe_handles_missing_update_id_same_message()"
location: "L5401"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_self_diagnose_dedupe_handles_missing_update_id_same_message
---

# .test_self_diagnostic_dedupe_handles_missing_update_id_same_message()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[When update_id is missing, same message_id should dedupe self-diagnostic…]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_urlopen()_1]] - `contains` [EXTRACTED]
- [[fake_urlopen()_40]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_self_diagnose_dedupe_handles_missing_update_id_same_message
