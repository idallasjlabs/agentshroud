---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: ".proxy_messages()"
location: "L1500"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_messages
---

# Scan inbound user message text for PII and injection.

## Connections
- [[._scan_inbound()]] - `rationale_for` [EXTRACTED]
- [[._scan_inbound()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_messages