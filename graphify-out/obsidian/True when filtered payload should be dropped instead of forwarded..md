---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "Adversarial Injection Guards"
location: "L4177"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Adversarial_Injection_Guards
---

# True when filtered payload should be dropped instead of forwarded.

## Connections
- [[._is_suppressed_outbound_payload()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Adversarial_Injection_Guards