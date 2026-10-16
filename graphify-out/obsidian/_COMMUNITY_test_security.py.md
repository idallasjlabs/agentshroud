---
type: community
cohesion: 0.03
members: 77
---

# test_security.py

**Cohesion:** 0.03 - loosely connected
**Members:** 77 nodes

## Members
- [[An empty share-sheet payload is rejected before it reaches the pipeline.]] - rationale - gateway/tests/test_security.py
- [[Auth Methods]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/health.py
- [[Create authentication dependency callable      This is a synchronous wrapper tha]] - rationale - gateway/ingest_api/auth.py
- [[Current Usage]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Every content_type an iOS Shortcut can emit is accepted with source=shortcut.]] - rationale - gateway/tests/test_security.py
- [[Factory that returns authentication dependency for FastAPI      This allows us t]] - rationale - gateway/ingest_api/auth.py
- [[GatewayConfig_4]] - code - gateway/ingest_api/auth.py
- [[Key Features_2]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Purpose_118]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Related Notes_49]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Request_7]] - code - gateway/ingest_api/routes/health.py
- [[Security Note_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[Test PII detection with special characters nearby]] - rationale - gateway/tests/test_security.py
- [[Test all valid sources are accepted]] - rationale - gateway/tests/test_security.py
- [[Test auth dependency with invalid auth scheme]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with missing Authorization header]] - rationale - gateway/tests/test_auth.py
- [[Test auth dependency with valid token]] - rationale - gateway/tests/test_auth.py
- [[Test content with Unicode characters]] - rationale - gateway/tests/test_security.py
- [[Test content with multiple instances of same PII type]] - rationale - gateway/tests/test_security.py
- [[Test handling of extremely long content (10MB)]] - rationale - gateway/tests/test_security.py
- [[Test handling of malformed metadata]] - rationale - gateway/tests/test_security.py
- [[Test handling of null bytes (potential injection attack)]] - rationale - gateway/tests/test_security.py
- [[Test handling of very large content (1MB+)]] - rationale - gateway/tests/test_security.py
- [[Test overlapping or nested PII patterns]] - rationale - gateway/tests/test_security.py
- [[Test rate limiting behavior]] - rationale - gateway/tests/test_security.py
- [[Test that SQL injection is prevented]] - rationale - gateway/tests/test_security.py
- [[Test that XSS payloads are safely stored]] - rationale - gateway/tests/test_security.py
- [[Test that common false positives are handled]] - rationale - gateway/tests/test_security.py
- [[Test that empty content is rejected]] - rationale - gateway/tests/test_security.py
- [[Test that invalid source is rejected]] - rationale - gateway/tests/test_security.py
- [[Test that token verification uses constant-time comparison]] - rationale - gateway/tests/test_auth.py
- [[Test token verification with valid token]] - rationale - gateway/tests/test_auth.py
- [[The iOSmacOS Shortcuts source value ('shortcut') is on the allowlist.]] - rationale - gateway/tests/test_security.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[Verify token using constant-time comparison      Uses hmac.compare_digest to pre]] - rationale - gateway/ingest_api/auth.py
- [[auth.py_1]] - document - docs/vault/02 - Modules/Gateway Core/auth.py.md
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/health.py
- [[content_type is a closed Literal set; a shortcut cannot invent new types.]] - rationale - gateway/tests/test_security.py
- [[create_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[gatewayingest_apiauth.py (RateLimiter, verify_token)]] - code - gateway/ingest_api/auth.py
- [[get_auth_dependency()]] - code - gateway/ingest_api/auth.py
- [[python-jose_1]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[python-jose]] - document - docs/vault/05 - Dependencies/python-jose.md
- [[rate_limiter (module-level instance)]] - code - gateway/ingest_api/auth.py
- [[test_auth.py]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_scheme()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_invalid_token()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_missing_header()]] - code - gateway/tests/test_auth.py
- [[test_auth_dependency_valid_token()]] - code - gateway/tests/test_auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_empty_content_rejection()]] - code - gateway/tests/test_security.py
- [[test_extremely_long_content()]] - code - gateway/tests/test_security.py
- [[test_false_positive_patterns()]] - code - gateway/tests/test_security.py
- [[test_invalid_source_rejection()]] - code - gateway/tests/test_security.py
- [[test_malformed_json_metadata()]] - code - gateway/tests/test_security.py
- [[test_multiple_same_type_pii()]] - code - gateway/tests/test_security.py
- [[test_nested_pii_patterns()]] - code - gateway/tests/test_security.py
- [[test_null_bytes_in_content()]] - code - gateway/tests/test_security.py
- [[test_rate_limiter()]] - code - gateway/tests/test_security.py
- [[test_security.py]] - code - gateway/tests/test_security.py
- [[test_shortcut_content_types_accepted()]] - code - gateway/tests/test_security.py
- [[test_shortcut_empty_content_rejected()]] - code - gateway/tests/test_security.py
- [[test_shortcut_rejects_unknown_content_type()]] - code - gateway/tests/test_security.py
- [[test_shortcut_source_accepted()]] - code - gateway/tests/test_security.py
- [[test_special_characters_in_pii()]] - code - gateway/tests/test_security.py
- [[test_sql_injection_attempt()]] - code - gateway/tests/test_security.py
- [[test_timing_attack_resistance()]] - code - gateway/tests/test_security.py
- [[test_unicode_content()]] - code - gateway/tests/test_security.py
- [[test_valid_sources()]] - code - gateway/tests/test_security.py
- [[test_verify_token_constant_time()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_invalid()]] - code - gateway/tests/test_auth.py
- [[test_verify_token_valid()]] - code - gateway/tests/test_auth.py
- [[test_very_large_content()]] - code - gateway/tests/test_security.py
- [[test_xss_attempt()]] - code - gateway/tests/test_security.py
- [[verify_token()]] - code - gateway/ingest_api/auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_securitypy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_RateLimiter]]
- 9 edges to [[_COMMUNITY_AgentTarget]]
- 7 edges to [[_COMMUNITY_DataLedger]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_test_dashboard.py]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_All Dependencies]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY_api.py]]

## Top bridge nodes
- [[auth.py_1]] - degree 10, connects to 5 communities
- [[create_auth_dependency()]] - degree 18, connects to 3 communities
- [[verify_token()]] - degree 13, connects to 3 communities
- [[get_auth_dependency()]] - degree 8, connects to 3 communities
- [[test_security.py]] - degree 25, connects to 2 communities
