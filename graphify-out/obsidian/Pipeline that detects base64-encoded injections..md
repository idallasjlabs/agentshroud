---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "BlockingPipeline"
location: "L103"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/BlockingPipeline
---

# Pipeline that detects base64-encoded injections.

## Connections
- [[EncodingDetectingPipeline]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/BlockingPipeline