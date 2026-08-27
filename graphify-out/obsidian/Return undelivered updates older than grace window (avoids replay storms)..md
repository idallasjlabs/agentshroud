---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "Community 148"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_148
---

# Return undelivered updates older than grace window (avoids replay storms).

## Connections
- [[.pull_undelivered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_148