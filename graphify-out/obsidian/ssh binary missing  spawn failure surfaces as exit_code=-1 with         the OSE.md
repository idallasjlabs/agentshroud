---
source_file: "gateway/tests/test_ssh_write_file_endpoint.py"
type: "rationale"
community: "Ssh Write File Endpoint"
location: "L550"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Ssh_Write_File_Endpoint
---

# ssh binary missing / spawn failure surfaces as exit_code=-1 with         the OSE

## Connections
- [[.test_write_file_oserror_from_subprocess()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Ssh_Write_File_Endpoint