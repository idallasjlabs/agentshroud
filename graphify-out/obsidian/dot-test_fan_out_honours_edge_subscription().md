---
source_file: "gateway/tests/test_soc_edge.py"
type: "code"
community: "soc/models.py"
location: "L691"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/soc/modelspy
---

# .test_fan_out_honours_edge_subscription()

## Connections
- [[EventBus]] - `calls` [EXTRACTED]
- [[SOCWebSocketHandler]] - `calls` [EXTRACTED]
- [[TestEdgeEventOverWebSocket]] - `method` [EXTRACTED]
- [[_send()_1]] - `indirect_call` [INFERRED]
- [[make_event()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/soc/modelspy
