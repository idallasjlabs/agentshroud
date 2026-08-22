---
source_file: "gateway/security/clamav_scanner.py"
type: "code"
community: "Tool Chain & CVE Triage"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tool_Chain__CVE_Triage
---

# clamav_scanner.py

## Connections
- [[FR3 System Integrity]] - `references` [EXTRACTED]
- [[alert_dispatcher.py]] - `references` [EXTRACTED]
- [[clamav]] - `references` [INFERRED]
- [[drift_detector.py]] - `references` [EXTRACTED]
- [[generate_summary()]] - `contains` [EXTRACTED]
- [[lifespan.py]] - `imports_from` [EXTRACTED]
- [[parse_clamscan_output()]] - `contains` [EXTRACTED]
- [[run_clamscan()]] - `contains` [EXTRACTED]
- [[save_report()]] - `contains` [EXTRACTED]
- [[scan_bytes()]] - `contains` [EXTRACTED]
- [[test_security_audit.py]] - `imports_from` [EXTRACTED]
- [[update_virus_db()]] - `contains` [EXTRACTED]
- [[web_content_scanner.py]] - `semantically_similar_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Tool_Chain__CVE_Triage