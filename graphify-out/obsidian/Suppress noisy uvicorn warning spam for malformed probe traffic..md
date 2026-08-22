---
source_file: "gateway/ingest_api/lifespan.py"
type: "rationale"
community: "Security Audit & Watchtower Tests"
location: "L62"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Audit__Watchtower_Tests
---

# Suppress noisy uvicorn warning spam for malformed probe traffic.

## Connections
- [[_DropInvalidHTTPRequestFilter]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Audit__Watchtower_Tests