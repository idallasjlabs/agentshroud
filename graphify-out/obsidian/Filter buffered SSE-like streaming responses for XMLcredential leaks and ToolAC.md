---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "._filter_streaming_event()"
location: "L1731"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_filter_streaming_event
---

# Filter buffered SSE-like streaming responses for XML/credential leaks and ToolAC

## Connections
- [[._filter_outbound_streaming()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_filter_streaming_event