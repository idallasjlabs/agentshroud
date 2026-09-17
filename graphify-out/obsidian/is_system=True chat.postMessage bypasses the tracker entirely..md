---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "Slack Proxy & Main Endpoint Tests"
location: "L306"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_Proxy__Main_Endpoint_Tests
---

# is_system=True chat.postMessage bypasses the tracker entirely.

## Connections
- [[dot-test_system_message_not_tracked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_Proxy__Main_Endpoint_Tests