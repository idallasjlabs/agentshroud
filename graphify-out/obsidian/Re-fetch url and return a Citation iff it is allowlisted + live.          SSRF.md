---
source_file: "gateway/security/citation_verifier.py"
type: "rationale"
community: "_call_agent_stream()"
location: "L143"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_call_agent_stream
---

# Re-fetch *url* and return a Citation iff it is allowlisted + live.          SSRF

## Connections
- [[._verify_url()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_call_agent_stream