---
source_file: "gateway/security/memory_lifecycle.py"
type: "code"
community: "Egress & RBAC Security Core"
location: "L39"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# ContentThreat

## Connections
- [[.__post_init__()_5]] - `method` [EXTRACTED]
- [[.get_recent_threats()]] - `references` [EXTRACTED]
- [[.sanitize_content()]] - `references` [EXTRACTED]
- [[.scan_content_for_threats()]] - `references` [EXTRACTED]
- [[.test_threat_cleanup()]] - `calls` [EXTRACTED]
- [[.validate_memory_write()]] - `references` [EXTRACTED]
- [[Detected threat in memory file content.]] - `rationale_for` [EXTRACTED]
- [[MemoryLifecycleConfig]] - `uses` [INFERRED]
- [[MemorySecurityConfig]] - `uses` [INFERRED]
- [[TestMemoryIntegrityConfig]] - `uses` [INFERRED]
- [[TestMemoryIntegrityMonitor]] - `uses` [INFERRED]
- [[TestMemoryLifecycleManager]] - `uses` [INFERRED]
- [[TestMemorySecurityIntegration]] - `uses` [INFERRED]
- [[memory_lifecycle.py]] - `contains` [EXTRACTED]
- [[test_memory_lifecycle.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress__RBAC_Security_Core