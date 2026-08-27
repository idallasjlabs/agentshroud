---
source_file: "gateway/tests/test_telegram_pipeline.py"
type: "rationale"
community: "Community 86"
location: "L216"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_86
---

# sendMessageDraft must be suppressed to prevent draft flicker leaks.

## Connections
- [[.test_send_message_draft_also_runs_outbound_filtering()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_86