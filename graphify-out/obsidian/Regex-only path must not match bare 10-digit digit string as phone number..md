---
source_file: "gateway/tests/test_sanitizer.py"
type: "rationale"
community: "Sanitizer"
location: "L117"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Sanitizer
---

# Regex-only path must not match bare 10-digit digit string as phone number.

## Connections
- [[test_regex_fallback_requires_separator()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Sanitizer