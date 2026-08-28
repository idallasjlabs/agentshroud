---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "Adversarial Injection Guards"
location: "L7101"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Adversarial_Injection_Guards
---

# Best-effort Telegram sender with bounded retries.

## Connections
- [[._send_telegram_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Adversarial_Injection_Guards