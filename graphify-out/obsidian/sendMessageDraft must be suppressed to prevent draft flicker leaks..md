---
source_file: "gateway/tests/test_telegram_pipeline.py"
type: "rationale"
community: "Pipeline (proxy)"
location: "L216"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Pipeline_proxy
---

# sendMessageDraft must be suppressed to prevent draft flicker leaks.

## Connections
- [[.test_send_message_draft_also_runs_outbound_filtering()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Pipeline_proxy