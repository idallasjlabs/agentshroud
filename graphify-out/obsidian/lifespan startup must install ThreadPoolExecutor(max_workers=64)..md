---
source_file: "gateway/tests/test_telegram_executor.py"
type: "rationale"
community: "_wrap_response()"
location: "L18"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_wrap_response
---

# lifespan startup must install ThreadPoolExecutor(max_workers=64).

## Connections
- [[test_lifespan_installs_64_worker_executor()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_wrap_response