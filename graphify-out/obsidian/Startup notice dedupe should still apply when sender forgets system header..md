---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "examples/docker-compose.minimal.yml"
location: "L2222"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/examples/docker-composeminimalyml
---

# Startup notice dedupe should still apply when sender forgets system header.

## Connections
- [[.test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/examples/docker-composeminimalyml