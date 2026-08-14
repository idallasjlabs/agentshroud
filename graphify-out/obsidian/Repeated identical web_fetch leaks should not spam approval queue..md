---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "ESP32 Firmware"
location: "L2657"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# Repeated identical web_fetch leaks should not spam approval queue.

## Connections
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ESP32_Firmware