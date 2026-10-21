---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ApprovalQueueConfig (2)"
location: "L274"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# If pipeline crashes, non-owner messages must be blocked (fail-closed).

## Connections
- [[dot-test_pipeline_error_fails_closed_for_non_owner()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ApprovalQueueConfig_2
