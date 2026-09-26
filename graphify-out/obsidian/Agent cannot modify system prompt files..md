---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Enum"
location: "L118"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Enum
---

# Agent cannot modify system prompt files.

## Connections
- [[.test_system_prompt_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Enum