---
source_file: "gateway/proxy/telegram_egress_notify.py"
type: "rationale"
community: "_is_stale_callback_error()"
location: "L39"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_is_stale_callback_error
---

# urllib HTTPError carries the response body on .read(); fall back to str.

## Connections
- [[_err_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_is_stale_callback_error