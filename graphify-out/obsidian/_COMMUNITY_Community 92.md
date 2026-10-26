---
type: community
members: 56
---

# Community 92

**Members:** 56 nodes

## Members
- [[.content_not_empty()]] - code - gateway/ingest_api/models.py
- [[.test_empty_content_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_source_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.validate_source()]] - code - gateway/ingest_api/models.py
- [[An empty share-sheet payload is rejected before it reaches the pipeline.]] - rationale - gateway/tests/test_security.py
- [[Every content_type an iOS Shortcut can emit is accepted with source=shortcut.]] - rationale - gateway/tests/test_security.py
- [[ForwardRequest]] - code - gateway/ingest_api/models.py
- [[Request to forward content through the gateway      Received from iOS Shortcuts,]] - rationale - gateway/ingest_api/models.py
- [[Test ForwardRequest rejects empty content]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects invalid source]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test PII detection with special characters nearby]] - rationale - gateway/tests/test_security.py
- [[Test all valid sources are accepted]] - rationale - gateway/tests/test_security.py
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
- [[The iOSmacOS Shortcuts source value ('shortcut') is on the allowlist.]] - rationale - gateway/tests/test_security.py
- [[Verify authentication doesn't leak timing information]] - rationale - gateway/tests/test_security.py
- [[Verify token comparison is constant-time]] - rationale - gateway/tests/test_security.py
- [[content_type is a closed Literal set; a shortcut cannot invent new types.]] - rationale - gateway/tests/test_security.py
- [[gatewayingest_apiauth.py (RateLimiter, verify_token)]] - code - gateway/ingest_api/auth.py
- [[test_constant_time_comparison()]] - code - gateway/tests/test_security.py
- [[test_empty_content_rejection()]] - code - gateway/tests/test_security.py
- [[test_extremely_long_content()]] - code - gateway/tests/test_security.py
- [[test_false_positive_patterns()]] - code - gateway/tests/test_security.py
- [[test_forward_request_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_empty_content()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_invalid_source()]] - code - gateway/tests/test_main_simple.py
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
- [[test_very_large_content()]] - code - gateway/tests/test_security.py
- [[test_xss_attempt()]] - code - gateway/tests/test_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_92
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 36]]
- 5 edges to [[_COMMUNITY_Community 47]]
- 5 edges to [[_COMMUNITY_Community 368]]
- 4 edges to [[_COMMUNITY_Community 861]]
- 4 edges to [[_COMMUNITY_Community 7]]
- 4 edges to [[_COMMUNITY_Community 78]]
- 4 edges to [[_COMMUNITY_Community 325]]
- 4 edges to [[_COMMUNITY_Community 143]]
- 4 edges to [[_COMMUNITY_Community 34]]
- 3 edges to [[_COMMUNITY_Community 707]]
- 2 edges to [[_COMMUNITY_Community 138]]
- 2 edges to [[_COMMUNITY_Community 2154]]
- 1 edge to [[_COMMUNITY_Community 20]]
- 1 edge to [[_COMMUNITY_Community 254]]
- 1 edge to [[_COMMUNITY_Community 104]]

## Top bridge nodes
- [[ForwardRequest]] - degree 57, connects to 13 communities
- [[test_security.py]] - degree 25, connects to 2 communities
- [[test_forward_request_validation_empty_content()]] - degree 3, connects to 1 community
- [[test_forward_request_validation_invalid_source()]] - degree 3, connects to 1 community
- [[test_forward_request_valid()]] - degree 3, connects to 1 community