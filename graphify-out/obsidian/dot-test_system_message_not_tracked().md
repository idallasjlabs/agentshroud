---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "code"
community: "_make_proxy"
location: "L305"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# .test_system_message_not_tracked()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[TestOutboundTracking]] - `method` [EXTRACTED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_7]] - `references` [EXTRACTED]
- [[is_system=True chat.postMessage bypasses the tracker entirely.]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
