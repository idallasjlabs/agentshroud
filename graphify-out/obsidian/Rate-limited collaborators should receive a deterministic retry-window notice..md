---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Authentication & Rate Limiting"
location: "L3573"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Authentication__Rate_Limiting
---

# Rate-limited collaborators should receive a deterministic retry-window notice.

## Connections
- [[.test_collaborator_rate_limit_notice_includes_retry_window()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Authentication__Rate_Limiting