---
source_file: "gateway/tests/test_bots_ssh_exec_wrapper.py"
type: "rationale"
community: "ESP32 Firmware"
location: "L150"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ESP32_Firmware
---

# The wrapper must NOT shell out to python3/python for JSON building.      Regress

## Connections
- [[test_wrapper_has_no_python_dependency()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ESP32_Firmware