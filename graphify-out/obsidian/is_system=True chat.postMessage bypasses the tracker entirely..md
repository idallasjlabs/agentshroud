---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "AsyncMock"
location: "L306"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AsyncMock
---

# is_system=True chat.postMessage bypasses the tracker entirely.

## Connections
- [[dot-test_system_message_not_tracked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AsyncMock
