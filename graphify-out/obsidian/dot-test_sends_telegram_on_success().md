---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "sync-cve-registry.py"
location: "L180"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# .test_sends_telegram_on_success()

## Connections
- [[TestRunAndSendCveReport]] - `method` [EXTRACTED]
- [[_fake_send()_14]] - `indirect_call` [INFERRED]
- [[_make_report()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[run_and_send_cve_report()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sync-cve-registrypy
