---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "test_trust_manager.py"
location: "L1500"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_trust_managerpy
---

# Scan inbound user message text for PII and injection.

## Connections
- [[._scan_inbound()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_trust_managerpy