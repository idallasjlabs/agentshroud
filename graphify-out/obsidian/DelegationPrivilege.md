---
source_file: "gateway/security/delegation.py"
type: "code"
community: "DelegationManager"
location: "L47"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/DelegationManager
---

# DelegationPrivilege

## Connections
- [[._filter_inbound_updates()]] - `calls` [EXTRACTED]
- [[._revoke_by_user_privilege()]] - `references` [EXTRACTED]
- [[.delegate()]] - `references` [EXTRACTED]
- [[.is_delegated()]] - `references` [EXTRACTED]
- [[.revoke()]] - `references` [EXTRACTED]
- [[Any_66]] - `uses` [INFERRED]
- [[DelegationManager]] - `uses` [INFERRED]
- [[Enum_3]] - `inherits` [EXTRACTED]
- [[Subset of privileges that can be delegated by the owner.]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[TestAccessControl_2]] - `uses` [INFERRED]
- [[TestDelegateBasic]] - `uses` [INFERRED]
- [[TestIsDelegated]] - `uses` [INFERRED]
- [[TestListAndCleanup]] - `uses` [INFERRED]
- [[TestRedelegation]] - `uses` [INFERRED]
- [[TestRevoke]] - `uses` [INFERRED]
- [[TestSerialization_2]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[create_delegation()]] - `calls` [EXTRACTED]
- [[delegation.py]] - `contains` [EXTRACTED]
- [[revoke_delegation()]] - `calls` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[str_2]] - `inherits` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_delegation.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/DelegationManager