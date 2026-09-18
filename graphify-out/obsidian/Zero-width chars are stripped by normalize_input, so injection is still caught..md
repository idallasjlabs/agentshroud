---
source_file: "gateway/tests/test_tool_result_injection.py"
type: "rationale"
community: "InjectionSeverity"
location: "L123"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/InjectionSeverity
---

# Zero-width chars are stripped by normalize_input, so injection is still caught.

## Connections
- [[.test_zero_width_chars_dont_bypass_detection()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/InjectionSeverity