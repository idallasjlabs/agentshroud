---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "_make_report"
location: "L1312"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_report
---

# .test_image_scans_run_for_each_target()

## Connections
- [[TestRunAndSendCveReportImageScans]] - `method` [EXTRACTED]
- [[_fake_send()_17]] - `contains` [EXTRACTED]
- [[_fake_send()_5]] - `indirect_call` [INFERRED]
- [[_fake_trivy_scan()_4]] - `contains` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `indirect_call` [INFERRED]
- [[asyncio_20]] - `references` [EXTRACTED]
- [[run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each…]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_report
