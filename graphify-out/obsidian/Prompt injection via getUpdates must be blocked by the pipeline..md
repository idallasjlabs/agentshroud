---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "models.py"
location: "L156"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/modelspy
---

# Prompt injection via getUpdates must be blocked by the pipeline.

## Connections
- [[.test_prompt_injection_blocked_on_getUpdates()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/modelspy