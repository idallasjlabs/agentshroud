---
source_file: "gateway/tests/test_session_isolation.py"
type: "rationale"
community: "URL/Domain Validation Tests"
location: "L466"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/URL/Domain_Validation_Tests
---

# Input normalization should strip zero-width obfuscation before guards run.

## Connections
- [[.test_middleware_normalizes_invisible_unicode()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/URL/Domain_Validation_Tests