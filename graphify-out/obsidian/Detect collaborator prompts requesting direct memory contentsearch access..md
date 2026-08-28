---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "Adversarial Injection Guards"
location: "L1619"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Adversarial_Injection_Guards
---

# Detect collaborator prompts requesting direct memory content/search access.

## Connections
- [[._looks_like_cross_user_messaging_request()]] - `rationale_for` [EXTRACTED]
- [[._looks_like_memory_access_request()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Adversarial_Injection_Guards