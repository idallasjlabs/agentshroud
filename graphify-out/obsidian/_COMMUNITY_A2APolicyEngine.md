---
type: community
cohesion: 0.05
members: 58
---

# A2APolicyEngine

**Cohesion:** 0.05 - loosely connected
**Members:** 58 nodes

## Members
- [[.check()]] - code - gateway/ingest_api/auth.py
- [[ApprovalDecision_1]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest_4]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth Methods]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/approval.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/approval.py
- [[Check if client is within rate limit          Args             client_id Usual]] - rationale - gateway/ingest_api/auth.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Current Usage]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[GatewayConfig]] - code - gateway/ingest_api/auth.py
- [[Key Features_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Purpose_193]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Related Notes_48]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Request_2]] - code - gateway/ingest_api/routes/approval.py
- [[Security Note_2]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with missing Authorization header]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with valid token]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter allows requests under limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter blocks requests over limit]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter cleans up old requests]] - rationale - gateway/tests/test_auth.py
- [[Test rate limiter tracks clients separately]] - rationale - gateway/tests/test_auth.py
- [[Test that token verification uses constant-time comparison]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[Verify token using constant-time comparison      Uses hmac.compare_digest to pre]] - rationale - gateway/ingest_api/auth.py
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[auth.py]] - code - gateway/ingest_api/auth.py
- [[auth.py_2]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/approval.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[list_pending_approvals()]] - code - gateway/ingest_api/routes/approval.py
- [[python-jose_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[python-jose]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_rate_limiter_allows_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_blocks_excess_requests()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_separate_clients()]] - code - gateway/tests/test_auth.py
- [[test_rate_limiter_window_cleanup()]] - code - gateway/tests/test_auth.py
- [[test_timing_attack_resistance()]] - code - gateway/tests/test_security.py
- [[test_verify_token_constant_time()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_invalid()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_valid()]] - code - gateway/tests/test_auth.py
- [[verify_token()]] - code - gateway/ingest_api/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyEngine
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 8 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 6 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY_SSHProxy]]
- 3 edges to [[_COMMUNITY_RateLimiter]]
- 3 edges to [[_COMMUNITY_start-agentshroud.sh]]
- 3 edges to [[_COMMUNITY_test_jira_dev_ticket.py]]
- 2 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_InjectionSeverity]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 1 edge to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_test_playback_state.c]]
- 1 edge to [[_COMMUNITY_validate_network_security()]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_TestFileSandbox]]

## Top bridge nodes
- [[auth.py]] - degree 13, connects to 7 communities
- [[approval.py]] - degree 16, connects to 6 communities
- [[create_auth_dependency()]] - degree 20, connects to 5 communities
- [[auth.py_2]] - degree 10, connects to 5 communities
- [[verify_token()]] - degree 13, connects to 3 communities