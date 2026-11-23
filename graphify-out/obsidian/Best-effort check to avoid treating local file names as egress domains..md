---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "._extract_first_egress_target"
location: "L1142"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_extract_first_egress_target
---

# Best-effort check to avoid treating local file names as egress domains.

## Connections
- [[dot-_looks_like_filename_reference()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_extract_first_egress_target
