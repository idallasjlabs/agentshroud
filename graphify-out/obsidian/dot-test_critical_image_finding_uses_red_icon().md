---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "format_cve_report() (2)"
location: "L1420"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/format_cve_report_2
---

# .test_critical_image_finding_uses_red_icon()

## Connections
- [[A critical finding in an image scan uses the red icon.]] - `rationale_for` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans]] - `method` [EXTRACTED]
- [[_fake_send()]] - `contains` [EXTRACTED]
- [[_fake_send()_14]] - `indirect_call` [INFERRED]
- [[_fake_trivy_scan()]] - `contains` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/format_cve_report_2
