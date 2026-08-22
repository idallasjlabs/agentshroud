---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Privilege Separation & File Sandbox"
location: "L170"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Privilege_Separation__File_Sandbox
---

# Agent cannot write to /usr/bin/ system binaries.

## Connections
- [[.test_usr_bin_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Privilege_Separation__File_Sandbox