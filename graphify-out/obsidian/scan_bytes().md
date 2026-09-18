---
source_file: "gateway/security/clamav_scanner.py"
type: "code"
community: "test_clamav_pipeline.py"
location: "L157"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_clamav_pipelinepy
---

# scan_bytes()

## Connections
- [[Any_63]] - `references` [EXTRACTED]
- [[Stream bytes to clamdscan for inline malware scanning.      Uses ``clamdscan --s]] - `rationale_for` [EXTRACTED]
- [[clamav_scanner.py_2]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[parse_clamscan_output()]] - `calls` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `imports` [EXTRACTED]
- [[test_scan_bytes_binary_not_found()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_clean()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_empty_input()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_infected()]] - `calls` [EXTRACTED]
- [[test_scan_bytes_timeout()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_clamav_pipelinepy