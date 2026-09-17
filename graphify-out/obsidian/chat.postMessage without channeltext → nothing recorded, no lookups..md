---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "Slack Proxy & Main Endpoint Tests"
location: "L293"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_Proxy__Main_Endpoint_Tests
---

# chat.postMessage without channel/text → nothing recorded, no lookups.

## Connections
- [[dot-test_missing_channel_or_text_skips_tracking()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_Proxy__Main_Endpoint_Tests