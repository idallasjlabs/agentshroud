---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Environment Guard & Leak Detection"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# Agent cannot modify system prompt files.

## Connections
- [[.test_system_prompt_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection