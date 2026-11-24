---
source_file: "gateway/tests/test_telegram_pipeline.py"
type: "code"
community: "test_telegram_pipeline.py"
location: "L215"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_telegram_pipelinepy
---

# .test_send_message_draft_also_runs_outbound_filtering()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[TestOutboundPipelineWired]] - `method` [EXTRACTED]
- [[_make_pipeline_result()]] - `calls` [EXTRACTED]
- [[_make_proxy()_3]] - `calls` [EXTRACTED]
- [[asyncio_67]] - `references` [EXTRACTED]
- [[fake_forward()_3]] - `indirect_call` [INFERRED]
- [[sendMessageDraft must be suppressed to prevent draft flicker leaks.]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_telegram_pipelinepy
