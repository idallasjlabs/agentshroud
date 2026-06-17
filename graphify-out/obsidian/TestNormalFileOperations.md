---
source_file: "gateway/tests/test_file_sandbox.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L57"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestNormalFileOperations

## Connections
- [[.test_monitor_mode_allows_everything()]] - `method` [EXTRACTED]
- [[.test_project_files_allowed()]] - `method` [EXTRACTED]
- [[.test_tmp_read_allowed()]] - `method` [EXTRACTED]
- [[.test_tmp_write_allowed()]] - `method` [EXTRACTED]
- [[.test_workspace_read_allowed()]] - `method` [EXTRACTED]
- [[.test_workspace_write_allowed()]] - `method` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[PIIScanner]] - `uses` [INFERRED]
- [[test_file_sandbox.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection