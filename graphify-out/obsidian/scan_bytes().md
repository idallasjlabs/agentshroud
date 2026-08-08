---
source_file: "gateway/security/clamav_scanner.py"
type: "code"
community: "Gateway Test Suite"
location: "L157"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# scan_bytes()

## Connections
- [[Any_32]] - `references` [EXTRACTED]
- [[Stream bytes to clamdscan for inline malware scanning.      Uses ``clamdscan --s]] - `rationale_for` [EXTRACTED]
- [[clamav_scanner.py]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[parse_clamscan_output()]] - `calls` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `imports` [EXTRACTED]
- [[test_scan_bytes_binary_not_found()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_clean()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_empty_input()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_infected()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_timeout()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite