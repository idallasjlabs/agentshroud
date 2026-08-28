---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "Adversarial Injection Guards"
location: "L7054"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Adversarial_Injection_Guards
---

# Notify an unknown/unapproved user they have exceeded the access request rate lim

## Connections
- [[._send_stranger_rate_limit_notice()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Adversarial_Injection_Guards