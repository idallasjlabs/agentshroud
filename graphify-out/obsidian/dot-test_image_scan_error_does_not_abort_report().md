---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "_make_report"
location: "L1391"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_report
---

# .test_image_scan_error_does_not_abort_report()

## Connections
- [[A failing image scan appends an error line but does not raise.]] - `rationale_for` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans]] - `method` [EXTRACTED]
- [[_fake_send()_14]] - `contains` [EXTRACTED]
- [[_fake_send()_5]] - `indirect_call` [INFERRED]
- [[_fake_trivy_scan()_1]] - `contains` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `indirect_call` [INFERRED]
- [[asyncio_20]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_report
