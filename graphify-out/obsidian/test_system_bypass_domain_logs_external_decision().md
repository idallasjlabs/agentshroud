---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L319"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# test_system_bypass_domain_logs_external_decision()

## Connections
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[System bypass domains should be logged to the SOC decision history.]] - `rationale_for` [EXTRACTED]
- [[_MockWriter_1]] - `calls` [EXTRACTED]
- [[_make_stream()_1]] - `calls` [EXTRACTED]
- [[_open_conn()_5]] - `contains` [EXTRACTED]
- [[_open_conn()_3]] - `indirect_call` [INFERRED]
- [[asyncio_83]] - `references` [EXTRACTED]
- [[log_external_decision()_1]] - `contains` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
