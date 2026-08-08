---
source_file: "gateway/tests/test_file_sandbox.py"
type: "code"
community: "File Sandbox"
location: "L148"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/File_Sandbox
---

# TestStagingPatternDetection

## Connections
- [[.test_large_write_then_network_flagged()]] - `method` [EXTRACTED]
- [[.test_large_write_without_network_not_flagged()]] - `method` [EXTRACTED]
- [[.test_small_writes_not_flagged()]] - `method` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[PIIScanner]] - `uses` [INFERRED]
- [[test_file_sandbox.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/File_Sandbox