---
source_file: "gateway/security/clamav_scanner.py"
type: "code"
community: "PipelineAction"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PipelineAction
---

# clamav_scanner.py

## Connections
- [[clamd_available()]] - `contains` [EXTRACTED]
- [[generate_summary()_3]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `imports_from` [EXTRACTED]
- [[lifespan.py]] - `imports_from` [EXTRACTED]
- [[parse_clamscan_output()]] - `contains` [EXTRACTED]
- [[preferred_scan_binary()]] - `contains` [EXTRACTED]
- [[run_clamscan()_1]] - `contains` [EXTRACTED]
- [[save_report()_1]] - `contains` [EXTRACTED]
- [[scan_bytes()]] - `contains` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `imports_from` [EXTRACTED]
- [[test_security_audit.py]] - `imports_from` [EXTRACTED]
- [[test_security_toolchain.py]] - `imports_from` [EXTRACTED]
- [[update_virus_db()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PipelineAction
