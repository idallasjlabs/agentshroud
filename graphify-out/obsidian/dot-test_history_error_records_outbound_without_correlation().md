---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "code"
community: "AsyncMock"
location: "L221"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AsyncMock
---

# .test_history_error_records_outbound_without_correlation()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[History lookup returns ok=False → no inbound record; outbound still logged,…]] - `rationale_for` [EXTRACTED]
- [[TestOutboundTracking]] - `method` [EXTRACTED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_7]] - `references` [EXTRACTED]
- [[fake_api()_1]] - `contains` [EXTRACTED]
- [[fake_api()_3]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/AsyncMock
