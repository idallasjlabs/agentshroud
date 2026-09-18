---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TestMultipartOutboundPipeline"
location: "L5121"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestMultipartOutboundPipeline
---

# Owner multipart messages still pass through on pipeline crash (parity).

## Connections
- [[.test_multipart_owner_exempt_from_fail_closed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestMultipartOutboundPipeline