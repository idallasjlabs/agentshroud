---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: "_sleep()"
location: "L140"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_sleep
---

# Periodically prune rows older than retention window.

## Connections
- [[.cleanup_if_due()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_sleep