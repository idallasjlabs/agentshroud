---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "_fw_client()"
location: "L3665"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_fw_client
---

# Authenticated request but no firmware on disk → 404 (not a 500/empty 200).

## Connections
- [[test_firmware_bin_404_when_absent()]] - `rationale_for` [EXTRACTED]
- [[test_firmware_bin_404_when_absent()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_fw_client