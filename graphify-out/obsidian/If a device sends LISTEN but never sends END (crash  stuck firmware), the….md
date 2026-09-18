---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "asyncio"
location: "L2140"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/asyncio
---

# If a device sends LISTEN but never sends END (crash / stuck firmware), the…

## Connections
- [[test_listen_without_end_times_out()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/asyncio