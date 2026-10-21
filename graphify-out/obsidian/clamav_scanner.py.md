---
source_file: "gateway/security/clamav_scanner.py"
type: "code"
community: "parse_clamscan_output"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/parse_clamscan_output
---

# clamav_scanner.py

## Connections
- [[FR3 System Integrity]] - `references` [EXTRACTED]
- [[alert_dispatcher.py]] - `references` [EXTRACTED]
- [[clamav_1]] - `references` [INFERRED]
- [[clamd_available()]] - `contains` [EXTRACTED]
- [[drift_detector.py]] - `references` [EXTRACTED]
- [[generate_summary()]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `imports_from` [EXTRACTED]
- [[lifespan.py]] - `imports_from` [EXTRACTED]
- [[parse_clamscan_output()]] - `contains` [EXTRACTED]
- [[preferred_scan_binary()]] - `contains` [EXTRACTED]
- [[run_clamscan()]] - `contains` [EXTRACTED]
- [[save_report()]] - `contains` [EXTRACTED]
- [[scan_bytes()]] - `contains` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `imports_from` [EXTRACTED]
- [[test_security_audit.py]] - `imports_from` [EXTRACTED]
- [[update_virus_db()]] - `contains` [EXTRACTED]
- [[web_content_scanner.py_2]] - `semantically_similar_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/parse_clamscan_output
