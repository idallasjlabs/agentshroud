---
source_file: "gateway/tests/test_tool_result_injection.py"
type: "rationale"
community: "InjectionSeverity"
location: "L107"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/InjectionSeverity
---

# Benign base64 content should not trigger encoded injection.

## Connections
- [[.test_base64_clean_content_not_flagged()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/InjectionSeverity