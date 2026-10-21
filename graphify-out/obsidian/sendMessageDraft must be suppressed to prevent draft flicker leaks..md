---
source_file: "gateway/tests/test_telegram_pipeline.py"
type: "rationale"
community: "Phase Review: P0 — Core Pipeline Wiring"
location: "L216"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Phase_Review_P0__Core_Pipeline_Wiring
---

# sendMessageDraft must be suppressed to prevent draft flicker leaks.

## Connections
- [[dot-test_send_message_draft_also_runs_outbound_filtering()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Phase_Review_P0__Core_Pipeline_Wiring
