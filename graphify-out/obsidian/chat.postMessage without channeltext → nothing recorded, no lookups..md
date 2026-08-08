---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "Slack API Proxy"
location: "L293"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_API_Proxy
---

# chat.postMessage without channel/text → nothing recorded, no lookups.

## Connections
- [[.test_missing_channel_or_text_skips_tracking()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_API_Proxy