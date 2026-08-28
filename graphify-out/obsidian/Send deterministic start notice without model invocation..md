---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "Adversarial Injection Guards"
location: "L7685"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Adversarial_Injection_Guards
---

# Send deterministic /start notice without model invocation.

## Connections
- [[._send_local_start_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Adversarial_Injection_Guards