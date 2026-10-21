---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "format_cve_report() (2)"
location: "L1391"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/format_cve_report_2
---

# .test_image_scan_error_does_not_abort_report()

## Connections
- [[A failing image scan appends an error line but does not raise.]] - `rationale_for` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans]] - `method` [EXTRACTED]
- [[_fake_send()_1]] - `contains` [EXTRACTED]
- [[_fake_send()_14]] - `indirect_call` [INFERRED]
- [[_fake_trivy_scan()_1]] - `contains` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/format_cve_report_2
