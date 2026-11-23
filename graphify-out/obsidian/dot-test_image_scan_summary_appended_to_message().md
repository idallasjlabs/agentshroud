---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "_make_report"
location: "L1340"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_report
---

# .test_image_scan_summary_appended_to_message()

## Connections
- [[Message sent via Telegram includes a Container Image Scans section.]] - `rationale_for` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans]] - `method` [EXTRACTED]
- [[_fake_send()_16]] - `contains` [EXTRACTED]
- [[_fake_send()_5]] - `indirect_call` [INFERRED]
- [[_fake_trivy_scan()_3]] - `contains` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `indirect_call` [INFERRED]
- [[asyncio_20]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_report
