---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "_make_proxy"
location: "L293"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# chat.postMessage without channel/text → nothing recorded, no lookups.

## Connections
- [[dot-test_missing_channel_or_text_skips_tracking()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy
