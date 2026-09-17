---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "SlackAPIProxy"
location: "L378"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SlackAPIProxy
---

# Channel name is lowercased, spaces/underscores → hyphens, symbols dropped.

## Connections
- [[.test_success_returns_channel_id_with_sanitized_name()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SlackAPIProxy