---
source_file: "gateway/tests/test_telegram_executor.py"
type: "rationale"
community: "scripts/export-telegram-history.py"
location: "L18"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/scripts/export-telegram-historypy
---

# lifespan startup must install ThreadPoolExecutor(max_workers=64).

## Connections
- [[test_lifespan_installs_64_worker_executor()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/scripts/export-telegram-historypy