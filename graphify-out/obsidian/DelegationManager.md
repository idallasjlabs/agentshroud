---
source_file: "gateway/security/delegation.py"
type: "code"
community: "Gateway Security Module"
location: "L93"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# DelegationManager

## Connections
- [[.__init__()_67]] - `method` [EXTRACTED]
- [[._load()]] - `method` [EXTRACTED]
- [[._require_owner()]] - `method` [EXTRACTED]
- [[._revoke_by_user_privilege()]] - `method` [EXTRACTED]
- [[._save()]] - `method` [EXTRACTED]
- [[.cleanup_expired()_1]] - `method` [EXTRACTED]
- [[.delegate()]] - `method` [EXTRACTED]
- [[.get_active_delegations()]] - `method` [EXTRACTED]
- [[.get_delegations_for_user()]] - `method` [EXTRACTED]
- [[.is_delegated()]] - `method` [EXTRACTED]
- [[.revoke()]] - `method` [EXTRACTED]
- [[.revoke_all_for_user()]] - `method` [EXTRACTED]
- [[DelegationManager_1]] - `uses` [INFERRED]
- [[Manages owner-away privilege delegations.      Thread-safe via file locking for]] - `rationale_for` [EXTRACTED]
- [[TestAccessControl]] - `uses` [INFERRED]
- [[TestDelegateBasic]] - `uses` [INFERRED]
- [[TestIsDelegated]] - `uses` [INFERRED]
- [[TestListAndCleanup]] - `uses` [INFERRED]
- [[TestRedelegation]] - `uses` [INFERRED]
- [[TestRevoke]] - `uses` [INFERRED]
- [[TestSerialization]] - `uses` [INFERRED]
- [[delegation.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_delegation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Security_Module