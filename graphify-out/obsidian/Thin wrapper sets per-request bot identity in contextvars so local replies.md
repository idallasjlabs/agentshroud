---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "TestPathIsolationManager"
location: "L2908"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestPathIsolationManager
---

# Thin wrapper: sets per-request bot identity in contextvars so local replies

## Connections
- [[.proxy_request()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestPathIsolationManager