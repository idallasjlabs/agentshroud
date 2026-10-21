---
source_file: "gateway/security/clamav_scanner.py"
type: "code"
community: "asyncio"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# preferred_scan_binary()

## Connections
- [[clamav_scanner.py]] - `contains` [EXTRACTED]
- [[clamd_available()]] - `calls` [EXTRACTED]
- [[clamdscan' when the resident clamd can take the scan, else 'clamscan'.]] - `rationale_for` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_preferred_scan_binary_falls_back_when_daemon_dead()]] - `calls` [EXTRACTED]
- [[test_preferred_scan_binary_uses_daemon_when_listening()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/asyncio
