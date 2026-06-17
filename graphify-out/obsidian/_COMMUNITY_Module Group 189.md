---
type: community
cohesion: 0.08
members: 25
---

# Module Group 189

**Cohesion:** 0.08 - loosely connected
**Members:** 25 nodes

## Members
- [[._validate_user_id()]] - code - gateway/security/session_manager.py
- [[.body_not_empty()]] - code - gateway/ingest_api/models.py
- [[.check_resource()]] - code - gateway/security/resource_guard.py
- [[.content_not_empty()]] - code - gateway/ingest_api/models.py
- [[.get_blob_key_id()]] - code - gateway/security/encrypted_store.py
- [[.get_merged_context()]] - code - gateway/security/session_manager.py
- [[.get_or_create_group_session()]] - code - gateway/security/session_manager.py
- [[.subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[.validate_default_url()]] - code - gateway/ingest_api/config.py
- [[.validate_mode()]] - code - gateway/security/group_config.py
- [[.validate_source()]] - code - gateway/ingest_api/models.py
- [[.validate_targets()]] - code - gateway/ingest_api/config.py
- [[Check if resource usage is allowed for an agent.          Args             agen]] - rationale - gateway/security/resource_guard.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[Get or create a shared workspace + MEMORY.md for a group.]] - rationale - gateway/security/session_manager.py
- [[GroupSession]] - code - gateway/security/session_manager.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Return user MEMORY.md + all accessible group MEMORY.md contents for prompt injec]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal.          Only allows al]] - rationale - gateway/security/session_manager.py
- [[Validate that default_url uses httphttps and targets an internal Docker host.]] - rationale - gateway/ingest_api/config.py
- [[Validate that each target URL uses httphttps and targets an internal Docker hos]] - rationale - gateway/ingest_api/config.py
- [[ValueError]] - code
- [[_is_connect_error matches connection-level failures only.]] - rationale - gateway/tests/test_llm_proxy.py
- [[session_manager.py]] - code - gateway/security/session_manager.py
- [[test_is_connect_error_classification()]] - code - gateway/tests/test_llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_189
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 3 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 3 edges to [[_COMMUNITY_Module Group 66]]
- 2 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Enhanced Approval Queue]]
- 1 edge to [[_COMMUNITY_Approval Queue Core]]
- 1 edge to [[_COMMUNITY_Module Group 300]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 371]]
- 1 edge to [[_COMMUNITY_Module Group 156]]
- 1 edge to [[_COMMUNITY_Module Group 167]]
- 1 edge to [[_COMMUNITY_Module Group 251]]
- 1 edge to [[_COMMUNITY_Module Group 458]]
- 1 edge to [[_COMMUNITY_RBAC Configuration]]
- 1 edge to [[_COMMUNITY_Module Group 186]]
- 1 edge to [[_COMMUNITY_Group Config & Teams]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Webhook Receiver]]
- 1 edge to [[_COMMUNITY_Module Group 111]]
- 1 edge to [[_COMMUNITY_Module Group 73]]

## Top bridge nodes
- [[ValueError]] - degree 28, connects to 14 communities
- [[session_manager.py]] - degree 4, connects to 3 communities
- [[.get_or_create_group_session()]] - degree 6, connects to 1 community
- [[._validate_user_id()]] - degree 5, connects to 1 community
- [[.get_merged_context()]] - degree 4, connects to 1 community