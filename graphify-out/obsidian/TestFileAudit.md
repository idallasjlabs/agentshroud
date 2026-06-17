---
source_file: "gateway/tests/test_file_sandbox.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L167"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestFileAudit

## Connections
- [[.test_audit_has_path()]] - `method` [EXTRACTED]
- [[.test_read_logged()]] - `method` [EXTRACTED]
- [[.test_temp_file_tracking()]] - `method` [EXTRACTED]
- [[.test_write_logged()]] - `method` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[PIIScanner]] - `uses` [INFERRED]
- [[test_file_sandbox.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection