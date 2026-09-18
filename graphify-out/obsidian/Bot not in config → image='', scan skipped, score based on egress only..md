---
source_file: "gateway/tests/test_soc_bots.py"
type: "rationale"
community: "test_soc_bots.py"
location: "L749"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# Bot not in config → image='', scan skipped, score based on egress only.

## Connections
- [[.test_missing_bot_returns_empty_image()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_soc_botspy