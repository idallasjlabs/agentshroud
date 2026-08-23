---
source_file: "gateway/tests/test_telegram_executor.py"
type: "rationale"
community: "Telegram Executor"
location: "L18"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Telegram_Executor
---

# lifespan startup must install ThreadPoolExecutor(max_workers=64).

## Connections
- [[test_lifespan_installs_64_worker_executor()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Telegram_Executor