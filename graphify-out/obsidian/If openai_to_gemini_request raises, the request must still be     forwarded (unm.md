---
source_file: "gateway/tests/test_gemini_via_openai_path.py"
type: "rationale"
community: "AgentShroud Security Hardening Plan"
location: "L106"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentShroud_Security_Hardening_Plan
---

# If openai_to_gemini_request raises, the request must still be     forwarded (unm

## Connections
- [[test_proxy_gemini_translation_failure_falls_through_gracefully()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentShroud_Security_Hardening_Plan