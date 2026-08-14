---
source_file: "gateway/tests/test_security_fixes.py"
type: "code"
community: "scripts/sync-cve-registry.py"
location: "L210"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/scripts/sync-cve-registrypy
---

# TestApprovalQueuePIISanitization

## Connections
- [[.test_ssh_approval_sanitizes_command_pii()]] - `method` [EXTRACTED]
- [[Approval queue details must be PII-sanitized before storage]] - `rationale_for` [EXTRACTED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[SSHHostConfig]] - `uses` [INFERRED]
- [[SSHProxy]] - `uses` [INFERRED]
- [[test_security_fixes.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/scripts/sync-cve-registrypy