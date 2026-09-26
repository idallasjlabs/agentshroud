---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "_make_proxy()"
location: "L4833"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# When tracker is None, /activity returns honest error, not silent empty.

## Connections
- [[.test_activity_command_reports_tracker_unhealthy()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy