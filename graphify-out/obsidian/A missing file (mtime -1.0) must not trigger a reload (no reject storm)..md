---
source_file: "gateway/tests/test_config_hot_reload.py"
type: "rationale"
community: "Slack API Proxy"
location: "L246"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_API_Proxy
---

# A missing file (mtime -1.0) must not trigger a reload (no reject storm).

## Connections
- [[test_watcher_ignores_missing_file()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_API_Proxy