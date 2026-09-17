---
type: community
cohesion: 0.17
members: 12
---

# Community 791

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[A2AGovernanceProxy._check_peer]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._process]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._sanitize_message]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_inbound]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_outbound]] - code - gateway/security/a2a_governance.py
- [[CredentialInjector.scan_for_credential_leak]] - code - gateway/security/credential_injector.py
- [[PIISanitizer.block_credentials]] - code - gateway/ingest_api/sanitizer.py
- [[ToolACLEnforcer._can_use_tool_impl]] - code - gateway/security/tool_acl.py
- [[TrustManager.get_trust]] - code - gateway/security/trust_manager.py
- [[TrustManager.is_tool_allowed]] - code - gateway/security/trust_manager.py
- [[test_console_source_not_blocked]] - code - gateway/tests/test_block_credentials.py
- [[test_telegram_blocks_password]] - code - gateway/tests/test_block_credentials.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_791
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 137]]

## Top bridge nodes
- [[ToolACLEnforcer._can_use_tool_impl]] - degree 2, connects to 1 community