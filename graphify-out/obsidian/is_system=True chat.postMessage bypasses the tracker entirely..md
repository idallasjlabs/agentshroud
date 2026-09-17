---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "SlackAPIProxy"
location: "L306"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SlackAPIProxy
---

# is_system=True chat.postMessage bypasses the tracker entirely.

## Connections
- [[.test_system_message_not_tracked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SlackAPIProxy