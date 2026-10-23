---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "._make_proxy()"
location: "L170"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_make_proxy
---

# Agent cannot write to /usr/bin/ system binaries.

## Connections
- [[dot-test_usr_bin_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_make_proxy
