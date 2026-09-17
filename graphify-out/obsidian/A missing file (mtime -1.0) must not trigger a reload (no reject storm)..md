---
source_file: "gateway/tests/test_config_hot_reload.py"
type: "rationale"
community: "test_config_hot_reload.py"
location: "L246"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_config_hot_reloadpy
---

# A missing file (mtime -1.0) must not trigger a reload (no reject storm).

## Connections
- [[test_watcher_ignores_missing_file()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_config_hot_reloadpy