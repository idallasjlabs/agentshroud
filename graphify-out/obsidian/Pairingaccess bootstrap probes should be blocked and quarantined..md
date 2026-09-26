---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "bsp_iot_button_create()"
location: "L4112"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/bsp_iot_button_create
---

# Pairing/access bootstrap probes should be blocked and quarantined.

## Connections
- [[.test_collaborator_hidden_channel_exfil_request_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]
- [[.test_collaborator_pairing_access_probe_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/bsp_iot_button_create