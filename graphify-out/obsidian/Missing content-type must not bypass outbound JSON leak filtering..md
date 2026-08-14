---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "ESP32 Firmware"
location: "L1862"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# Missing content-type must not bypass outbound JSON leak filtering.

## Connections
- [[.test_json_without_content_type_is_still_filtered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ESP32_Firmware