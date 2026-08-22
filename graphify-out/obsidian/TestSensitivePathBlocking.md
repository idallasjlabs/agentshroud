---
source_file: "gateway/tests/test_file_sandbox.py"
type: "code"
community: "Privilege Separation & File Sandbox"
location: "L86"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Privilege_Separation__File_Sandbox
---

# TestSensitivePathBlocking

## Connections
- [[.test_credential_file_flagged()]] - `method` [EXTRACTED]
- [[.test_enforce_blocks_outside_allowed()]] - `method` [EXTRACTED]
- [[.test_enforce_blocks_sensitive()]] - `method` [EXTRACTED]
- [[.test_env_file_flagged()]] - `method` [EXTRACTED]
- [[.test_etc_passwd_flagged()]] - `method` [EXTRACTED]
- [[.test_etc_shadow_flagged()]] - `method` [EXTRACTED]
- [[.test_ssh_private_key_flagged()]] - `method` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[PIIScanner]] - `uses` [INFERRED]
- [[test_file_sandbox.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Privilege_Separation__File_Sandbox