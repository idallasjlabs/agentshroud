---
type: community
members: 51
---

# AgentTarget (2)

**Members:** 51 nodes

## Members
- [[dot-content_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-test_empty_content_rejected()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_invalid_source_rejected()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_valid_forward_request()]] - code - gateway/tests/test_config_validation.py
- [[dot-validate_source()]] - code - gateway/ingest_api/models.py
- [[An empty share-sheet payload is rejected before it reaches the pipeline.]] - rationale - gateway/tests/test_security.py
- [[Every content_type an iOS Shortcut can emit is accepted with source=shortcut.]] - rationale - gateway/tests/test_security.py
- [[ForwardRequest]] - code - gateway/ingest_api/models.py
- [[Request to forward content through the gateway      Received from iOS Shortcuts,]] - rationale - gateway/ingest_api/models.py
- [[Test PII detection with special characters nearby]] - rationale - gateway/tests/test_security.py
- [[Test all valid sources are accepted]] - rationale - gateway/tests/test_security.py
- [[Test content with Unicode characters]] - rationale - gateway/tests/test_security.py
- [[Test content with multiple instances of same PII type]] - rationale - gateway/tests/test_security.py
- [[Test handling of extremely long content (10MB)]] - rationale - gateway/tests/test_security.py
- [[Test handling of malformed metadata]] - rationale - gateway/tests/test_security.py
- [[Test handling of null bytes (potential injection attack)]] - rationale - gateway/tests/test_security.py
- [[Test handling of very large content (1MB+)]] - rationale - gateway/tests/test_security.py
- [[Test overlapping or nested PII patterns]] - rationale - gateway/tests/test_security.py
- [[Test routing to default target]] - rationale - gateway/tests/test_router.py
- [[Test routing with explicit route_to]] - rationale - gateway/tests/test_router.py
- [[Test routing with invalid explicit target falls back to default]] - rationale - gateway/tests/test_router.py
- [[Test that SQL injection is prevented]] - rationale - gateway/tests/test_security.py
- [[Test that XSS payloads are safely stored]] - rationale - gateway/tests/test_security.py
- [[Test that common false positives are handled]] - rationale - gateway/tests/test_security.py
- [[Test that empty content is rejected]] - rationale - gateway/tests/test_security.py
- [[Test that invalid source is rejected]] - rationale - gateway/tests/test_security.py
- [[The iOSmacOS Shortcuts source value ('shortcut') is on the allowlist.]] - rationale - gateway/tests/test_security.py
- [[content_type is a closed Literal set; a shortcut cannot invent new types.]] - rationale - gateway/tests/test_security.py
- [[gatewayingest_apiauth.py (RateLimiter, verify_token)]] - code - gateway/ingest_api/auth.py
- [[test_empty_content_rejection()]] - code - gateway/tests/test_security.py
- [[test_extremely_long_content()]] - code - gateway/tests/test_security.py
- [[test_false_positive_patterns()]] - code - gateway/tests/test_security.py
- [[test_invalid_source_rejection()]] - code - gateway/tests/test_security.py
- [[test_malformed_json_metadata()]] - code - gateway/tests/test_security.py
- [[test_multiple_same_type_pii()]] - code - gateway/tests/test_security.py
- [[test_nested_pii_patterns()]] - code - gateway/tests/test_security.py
- [[test_null_bytes_in_content()]] - code - gateway/tests/test_security.py
- [[test_resolve_target_default()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_explicit()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_invalid_explicit()]] - code - gateway/tests/test_router.py
- [[test_security.py]] - code - gateway/tests/test_security.py
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
TABLE source_file, type FROM #community/AgentTarget_2
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_AgentTarget (2)_1]]
- 10 edges to [[_COMMUNITY_AgentTarget]]
- 7 edges to [[_COMMUNITY_AgentTarget (3)]]
- 5 edges to [[_COMMUNITY_test_forward_stream.py]]
- 5 edges to [[_COMMUNITY_create_auth_dependency]]
- 4 edges to [[_COMMUNITY_Request]]
- 2 edges to [[_COMMUNITY_create_auth_dependency (2)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[ForwardRequest]] - degree 57, connects to 9 communities
- [[test_security.py]] - degree 25, connects to 1 community
- [[test_resolve_target_default()]] - degree 3, connects to 1 community
- [[test_resolve_target_explicit()]] - degree 3, connects to 1 community
- [[test_resolve_target_invalid_explicit()]] - degree 3, connects to 1 community
