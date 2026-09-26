---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "ElevenLabs Text-to-Dialogue API"
location: "L137"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ElevenLabs_Text-to-Dialogue_API
---

# If pipeline crashes, owner messages should still go through.

## Connections
- [[.test_outbound_owner_exempt_from_fail_closed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ElevenLabs_Text-to-Dialogue_API