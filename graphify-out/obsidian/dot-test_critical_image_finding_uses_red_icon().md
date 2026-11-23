---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "_make_report"
location: "L1420"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_report
---

# .test_critical_image_finding_uses_red_icon()

## Connections
- [[A critical finding in an image scan uses the red icon.]] - `rationale_for` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans]] - `method` [EXTRACTED]
- [[_fake_send()_13]] - `contains` [EXTRACTED]
- [[_fake_send()_5]] - `indirect_call` [INFERRED]
- [[_fake_trivy_scan()]] - `contains` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `indirect_call` [INFERRED]
- [[asyncio_20]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_report
