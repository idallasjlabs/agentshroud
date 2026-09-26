---
source_file: "gateway/ingest_api/lifespan.py"
type: "rationale"
community: "test_telegram_proxy_outbound.py"
location: "L62"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_telegram_proxy_outboundpy
---

# Suppress noisy uvicorn warning spam for malformed probe traffic.

## Connections
- [[_DropInvalidHTTPRequestFilter]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_telegram_proxy_outboundpy