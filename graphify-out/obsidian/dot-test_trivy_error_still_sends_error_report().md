---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "Community 82"
location: "L215"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_82
---

# .test_trivy_error_still_sends_error_report()

## Connections
- [[TestRunAndSendCveReport]] - `method` [EXTRACTED]
- [[_fake_send()_12]] - `contains` [EXTRACTED]
- [[_fake_send()_11]] - `indirect_call` [INFERRED]
- [[_make_error_report()]] - `calls` [EXTRACTED]
- [[asyncio_4]] - `references` [EXTRACTED]
- [[run_and_send_cve_report]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_82