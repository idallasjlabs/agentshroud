---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "sync-cve-registry.py"
location: "L1743"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# .test_failed_send_does_not_write_stamp_or_mark_sent_date()

## Connections
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - `method` [EXTRACTED]
- [[_fake_send()_21]] - `contains` [EXTRACTED]
- [[_fake_send()_14]] - `indirect_call` [INFERRED]
- [[_make_report()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[run_and_send_cve_report()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sync-cve-registrypy
