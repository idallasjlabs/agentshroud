---
source_file: "gateway/tests/test_telegram_pipeline.py"
type: "code"
community: "AuditChain"
location: "L134"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditChain
---

# .test_blocked_owner_message_allowed_through_with_sanitized_text()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[TestInboundPipelineBlockedOwner]] - `method` [EXTRACTED]
- [[_getUpdates_response()]] - `calls` [EXTRACTED]
- [[_make_pipeline_result()]] - `calls` [EXTRACTED]
- [[_make_proxy()_4]] - `calls` [EXTRACTED]
- [[_make_update()_2]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditChain
