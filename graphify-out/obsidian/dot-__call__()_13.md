---
source_file: "gateway/inbound_edge/edge_app.py"
type: "code"
community: "test_edge_fuzz.py"
location: "L423"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_edge_fuzzpy
---

# .__call__()

## Connections
- [[dot-_send_plain()]] - `calls` [EXTRACTED]
- [[EdgeGuard]] - `method` [EXTRACTED]
- [[replay()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_edge_fuzzpy
