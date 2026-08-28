---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "Adversarial Injection Guards"
location: "L1767"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Adversarial_Injection_Guards
---

# Detect requests to encode sensitive/internal content for exfiltration.

## Connections
- [[._looks_like_encoded_exfil_request()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Adversarial_Injection_Guards