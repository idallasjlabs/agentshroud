---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Session Manager & PII/Context Guard"
location: "L95"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Session_Manager__PII/Context_Guard
---

# Verify hmac.compare_digest is available for constant-time comparison.

## Connections
- [[dot-test_hmac_comparison_for_secrets()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Session_Manager__PII/Context_Guard