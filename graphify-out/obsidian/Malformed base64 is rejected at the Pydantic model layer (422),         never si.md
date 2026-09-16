---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "Approval Queue (WebSocket)"
location: "L267"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval_Queue_WebSocket
---

# Malformed base64 is rejected at the Pydantic model layer (422),         never si

## Connections
- [[dot-test_write_file_invalid_base64_rejected()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Approval_Queue_WebSocket