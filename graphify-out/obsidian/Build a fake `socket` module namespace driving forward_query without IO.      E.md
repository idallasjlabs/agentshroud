---
source_file: "gateway/tests/test_dns_canvas_coverage.py"
type: "rationale"
community: "TestLeakDetection"
location: "L68"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestLeakDetection
---

# Build a fake `socket` module namespace driving forward_query without I/O.      E

## Connections
- [[make_fake_socket_module()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestLeakDetection
