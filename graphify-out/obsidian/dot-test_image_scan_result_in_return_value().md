---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "format_cve_report() (2)"
location: "L1367"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/format_cve_report_2
---

# .test_image_scan_result_in_return_value()

## Connections
- [[Return value includes image_scans list.]] - `rationale_for` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans]] - `method` [EXTRACTED]
- [[_fake_send()_2]] - `contains` [EXTRACTED]
- [[_fake_send()_14]] - `indirect_call` [INFERRED]
- [[_fake_trivy_scan()_2]] - `contains` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/format_cve_report_2
