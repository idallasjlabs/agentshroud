---
source_file: "gateway/tests/test_security_regressions_v1_2.py"
type: "rationale"
community: "TestSessionPathSeparation"
location: "L518"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestSessionPathSeparation
---

# Session directory path must embed bot_id so filesystem confirms isolation.

## Connections
- [[.test_user_session_paths_contain_bot_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestSessionPathSeparation