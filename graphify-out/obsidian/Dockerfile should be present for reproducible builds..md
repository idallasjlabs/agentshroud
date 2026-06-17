---
source_file: "gateway/tests/test_security_audit.py"
type: "rationale"
community: "PII Sanitizer & Resource Guard"
location: "L1102"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__Resource_Guard
---

# Dockerfile should be present for reproducible builds.

## Connections
- [[.test_dockerfile_exists()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__Resource_Guard