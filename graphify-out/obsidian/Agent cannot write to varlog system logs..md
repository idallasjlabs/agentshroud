---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "._make_proxy()"
location: "L178"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# Agent cannot write to /var/log/ system logs.

## Connections
- [[dot-test_var_log_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy
