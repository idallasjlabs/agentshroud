---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "Alert Thresholds (approval queue 1h timeout, con"
location: "L2657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Alert_Thresholds_approval_queue_1h_timeout_con
---

# Repeated identical web_fetch leaks should not spam approval queue.

## Connections
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Alert_Thresholds_approval_queue_1h_timeout_con