---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "test_trust_manager.py"
location: "L430"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_trust_managerpy
---

# Append '/no_think' to the last user message, in place, if not already present.

## Connections
- [[._suppress_qwen3_thinking()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_trust_managerpy