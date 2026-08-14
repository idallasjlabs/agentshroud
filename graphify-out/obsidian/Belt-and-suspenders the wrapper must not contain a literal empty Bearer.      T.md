---
source_file: "gateway/tests/test_bots_ssh_exec_wrapper.py"
type: "rationale"
community: "ESP32 Firmware"
location: "L383"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# Belt-and-suspenders: the wrapper must not contain a literal empty Bearer.      T

## Connections
- [[test_wrapper_never_sends_empty_bearer()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ESP32_Firmware