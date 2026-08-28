---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "Community 24"
location: "L293"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_24
---

# chat.postMessage without channel/text → nothing recorded, no lookups.

## Connections
- [[.test_missing_channel_or_text_skips_tracking()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_24