---
source_file: "gateway/tests/test_telegram_pipeline.py"
type: "code"
community: "Phase Review: P0 — Core Pipeline Wiring"
location: "L215"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Phase_Review_P0__Core_Pipeline_Wiring
---

# .test_send_message_draft_also_runs_outbound_filtering()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[TestOutboundPipelineWired]] - `method` [EXTRACTED]
- [[_make_pipeline_result()]] - `calls` [EXTRACTED]
- [[_make_proxy()_2]] - `calls` [EXTRACTED]
- [[sendMessageDraft must be suppressed to prevent draft flicker leaks.]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Phase_Review_P0__Core_Pipeline_Wiring
