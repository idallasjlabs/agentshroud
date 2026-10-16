---
source_file: "gateway/tests/test_tool_result_injection.py"
type: "rationale"
community: "InjectionAction"
location: "L123"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/InjectionAction
---

# Zero-width chars are stripped by normalize_input, so injection is still caught.

## Connections
- [[dot-test_zero_width_chars_dont_bypass_detection()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/InjectionAction
