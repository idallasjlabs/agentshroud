---
type: community
members: 95
---

# Competitive Intel Store

**Members:** 95 nodes

## Members
- [[.body_not_empty()]] - code - gateway/ingest_api/models.py
- [[.content_not_empty()]] - code - gateway/ingest_api/models.py
- [[.get_blob_key_id()]] - code - gateway/security/encrypted_store.py
- [[.subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[.validate_default_url()]] - code - gateway/ingest_api/config.py
- [[.validate_mode()]] - code - gateway/security/group_config.py
- [[.validate_source()]] - code - gateway/ingest_api/models.py
- [[.validate_targets()]] - code - gateway/ingest_api/config.py
- [[Add security headers to all responses (defense-in-depth).      Also catches Pyth]] - rationale - gateway/ingest_api/main.py
- [[An empty share-sheet payload is rejected before it reaches the pipeline.]] - rationale - gateway/tests/test_security.py
- [[Every content_type an iOS Shortcut can emit is accepted with source=shortcut.]] - rationale - gateway/tests/test_security.py
- [[Extract the key_id from an encrypted blob without decrypting.]] - rationale - gateway/security/encrypted_store.py
- [[ForwardRequest]] - code - gateway/ingest_api/models.py
- [[Reject request bodies larger than 1MB before parsing.      Checks Content-Length]] - rationale - gateway/ingest_api/main.py
- [[Request to forward content through the gateway      Received from iOS Shortcuts,]] - rationale - gateway/ingest_api/models.py
- [[Test ApprovalDecision with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test ApprovalRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test FastAPI lifespan initialization]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects empty content]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects invalid source]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test PII detection with special characters nearby]] - rationale - gateway/tests/test_security.py
- [[Test all valid sources are accepted]] - rationale - gateway/tests/test_security.py
- [[Test content with Unicode characters]] - rationale - gateway/tests/test_security.py
- [[Test content with multiple instances of same PII type]] - rationale - gateway/tests/test_security.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test handling of extremely long content (10MB)]] - rationale - gateway/tests/test_security.py
- [[Test handling of malformed metadata]] - rationale - gateway/tests/test_security.py
- [[Test handling of null bytes (potential injection attack)]] - rationale - gateway/tests/test_security.py
- [[Test handling of very large content (1MB+)]] - rationale - gateway/tests/test_security.py
- [[Test overlapping or nested PII patterns]] - rationale - gateway/tests/test_security.py
- [[Test rate limiting behavior]] - rationale - gateway/tests/test_security.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[Test routing to default target]] - rationale - gateway/tests/test_router.py
- [[Test routing with explicit route_to]] - rationale - gateway/tests/test_router.py
- [[Test routing with invalid explicit target falls back to default]] - rationale - gateway/tests/test_router.py
- [[Test that SQL injection is prevented]] - rationale - gateway/tests/test_security.py
- [[Test that XSS payloads are safely stored]] - rationale - gateway/tests/test_security.py
- [[Test that common false positives are handled]] - rationale - gateway/tests/test_security.py
- [[Test that empty content is rejected]] - rationale - gateway/tests/test_security.py
- [[Test that invalid source is rejected]] - rationale - gateway/tests/test_security.py
- [[The iOSmacOS Shortcuts source value ('shortcut') is on the allowlist.]] - rationale - gateway/tests/test_security.py
- [[Validate that default_url uses httphttps and targets an internal Docker host.]] - rationale - gateway/ingest_api/config.py
- [[Validate that each target URL uses httphttps and targets an internal Docker hos]] - rationale - gateway/ingest_api/config.py
- [[ValueError]] - code
- [[content_type is a closed Literal set; a shortcut cannot invent new types.]] - rationale - gateway/tests/test_security.py
- [[gatewayingest_apiauth.py (RateLimiter, verify_token)]] - code - gateway/ingest_api/auth.py
- [[limit_request_body re-injects a fully-read chunked body and calls downstream.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body rejects chunked bodies over 1MB with 413.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body returns a clean 400 when the client drops mid-upload.      Wi]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body()]] - code - gateway/ingest_api/main.py
- [[security_headers_middleware adds expected security headers.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware re-raises BaseExceptions that are not groups.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware returns 500 when anyio BaseExceptionGroup is raised.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware()]] - code - gateway/ingest_api/main.py
- [[test_approval_decision_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_approval_request_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_empty_content_rejection()]] - code - gateway/tests/test_security.py
- [[test_extremely_long_content()]] - code - gateway/tests/test_security.py
- [[test_false_positive_patterns()]] - code - gateway/tests/test_security.py
- [[test_forward_request_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_empty_content()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_invalid_source()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler_http_exception()]] - code - gateway/tests/test_main_simple.py
- [[test_invalid_source_rejection()]] - code - gateway/tests/test_security.py
- [[test_lifespan_initialization()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_chunked_body_over_limit_rejected()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_chunked_body_within_limit_passes_through()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_client_disconnect_returns_clean_response()]] - code - gateway/tests/test_main_simple.py
- [[test_log_requests_middleware()]] - code - gateway/tests/test_main_simple.py
- [[test_main_simple.py]] - code - gateway/tests/test_main_simple.py
- [[test_malformed_json_metadata()]] - code - gateway/tests/test_security.py
- [[test_multiple_same_type_pii()]] - code - gateway/tests/test_security.py
- [[test_nested_pii_patterns()]] - code - gateway/tests/test_security.py
- [[test_null_bytes_in_content()]] - code - gateway/tests/test_security.py
- [[test_rate_limiter()]] - code - gateway/tests/test_security.py
- [[test_resolve_target_default()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_explicit()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_invalid_explicit()]] - code - gateway/tests/test_router.py
- [[test_security.py]] - code - gateway/tests/test_security.py
- [[test_security_headers_middleware_catches_exception_group()]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_normal_response()]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_reraises_non_group()]] - code - gateway/tests/test_main_simple.py
- [[test_shortcut_content_types_accepted()]] - code - gateway/tests/test_security.py
- [[test_shortcut_empty_content_rejected()]] - code - gateway/tests/test_security.py
- [[test_shortcut_rejects_unknown_content_type()]] - code - gateway/tests/test_security.py
- [[test_shortcut_source_accepted()]] - code - gateway/tests/test_security.py
- [[test_special_characters_in_pii()]] - code - gateway/tests/test_security.py
- [[test_sql_injection_attempt()]] - code - gateway/tests/test_security.py
- [[test_unicode_content()]] - code - gateway/tests/test_security.py
- [[test_valid_sources()]] - code - gateway/tests/test_security.py
- [[test_very_large_content()]] - code - gateway/tests/test_security.py
- [[test_xss_attempt()]] - code - gateway/tests/test_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Competitive_Intel_Store
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_PII Sanitizer Pipeline]]
- 10 edges to [[_COMMUNITY_Slack API Proxy]]
- 9 edges to [[_COMMUNITY_SOC Dashboard]]
- 9 edges to [[_COMMUNITY_Gateway Security Module]]
- 6 edges to [[_COMMUNITY_Planning Docs]]
- 5 edges to [[_COMMUNITY_Architecture Docs]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 4 edges to [[_COMMUNITY_docsUSPTO_PROVISIONAL_PATENT_APPLICATION]]
- 3 edges to [[_COMMUNITY_Collaborator Prompt Classifiers]]
- 3 edges to [[_COMMUNITY_docsvault]]
- 3 edges to [[_COMMUNITY_Telegram Proxy Test Suite]]
- 3 edges to [[_COMMUNITY_Bot Skill Config]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_docsvault]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_scriptssync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_Bot Container Scripts]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Security Module]]
- 1 edge to [[_COMMUNITY_Planning Docs]]
- 1 edge to [[_COMMUNITY_Egress & RBAC Security Core]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Forward Routing & Approval]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Group Workspace Isolation]]

## Top bridge nodes
- [[ValueError]] - degree 29, connects to 16 communities
- [[ForwardRequest]] - degree 71, connects to 9 communities
- [[test_main_simple.py]] - degree 23, connects to 3 communities
- [[test_security.py]] - degree 25, connects to 2 communities
- [[limit_request_body()]] - degree 8, connects to 2 communities