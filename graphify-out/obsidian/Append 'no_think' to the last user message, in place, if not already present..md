---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: ".proxy_messages()"
location: "L430"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_messages
---

# Append '/no_think' to the last user message, in place, if not already present.

## Connections
- [[._suppress_qwen3_thinking()]] - `rationale_for` [EXTRACTED]
- [[._suppress_qwen3_thinking()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_messages