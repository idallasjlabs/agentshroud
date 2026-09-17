---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "._filter_streaming_event()"
location: "L1542"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_filter_streaming_event
---

# Filter outbound LLM response for credential leaks and XML.

## Connections
- [[._filter_outbound()]] - `rationale_for` [EXTRACTED]
- [[._filter_outbound()_2]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_filter_streaming_event