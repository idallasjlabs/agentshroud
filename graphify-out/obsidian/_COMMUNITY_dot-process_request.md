---
type: community
members: 17
---

# .process_request

**Members:** 17 nodes

## Members
- [[dot-_check_cross_session_access()]] - code - gateway/ingest_api/middleware.py
- [[dot-_check_rbac_permissions()]] - code - gateway/ingest_api/middleware.py
- [[dot-_enforce_session_isolation()]] - code - gateway/ingest_api/middleware.py
- [[dot-_extract_user_id()]] - code - gateway/ingest_api/middleware.py
- [[dot-_is_owner()]] - code - gateway/ingest_api/middleware.py
- [[dot-_is_tool_call_request()]] - code - gateway/ingest_api/middleware.py
- [[dot-process_request()]] - code - gateway/ingest_api/middleware.py
- [[dot-process_tool_result()]] - code - gateway/ingest_api/middleware.py
- [[Any]] - code
- [[Check RBAC permissions for the request.]] - rationale - gateway/ingest_api/middleware.py
- [[Check for unauthorized cross-session access attempts. Implementation note…]] - rationale - gateway/ingest_api/middleware.py
- [[Check if user_id is the system owner via RBAC config (single source of truth).]] - rationale - gateway/ingest_api/middleware.py
- [[Enforce per-user, per-bot session isolation rules. Each (user_id, bot_id) pair…]] - rationale - gateway/ingest_api/middleware.py
- [[Extract user ID from request data.]] - rationale - gateway/ingest_api/middleware.py
- [[Process request through all middleware modules.]] - rationale - gateway/ingest_api/middleware.py
- [[Process tool result through PII sanitization before it reaches agent Args…]] - rationale - gateway/ingest_api/middleware.py
- [[Return True only when the request contains actual tool calls or tool results.…]] - rationale - gateway/ingest_api/middleware.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/process_request
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_MiddlewareResult]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[dot-process_request()]] - degree 15, connects to 4 communities
- [[dot-_check_rbac_permissions()]] - degree 6, connects to 3 communities
- [[dot-_check_cross_session_access()]] - degree 5, connects to 2 communities
- [[dot-_enforce_session_isolation()]] - degree 5, connects to 2 communities
- [[dot-_is_owner()]] - degree 4, connects to 2 communities
