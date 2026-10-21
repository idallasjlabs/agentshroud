---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "ApprovalQueueConfig (2)"
location: "L5283"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ApprovalQueueConfig_2
---

# When update_id is missing, dedupe should fall back to message_id identity.

## Connections
- [[dot-test_healthcheck_local_notice_dedupe_handles_missing_update_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ApprovalQueueConfig_2
