---
source_file: "gateway/tests/test_agent_isolation.py"
type: "code"
community: "Security Hardening"
location: "L17"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Hardening
---

# ContainerConfig

## Connections
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig]] - `uses` [INFERRED]
- [[IsolationStatus]] - `uses` [INFERRED]
- [[IsolationVerifier]] - `uses` [INFERRED]
- [[_make_config()]] - `references` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Hardening