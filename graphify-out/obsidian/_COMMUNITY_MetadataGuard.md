---
type: community
members: 42
---

# MetadataGuard

**Members:** 42 nodes

## Members
- [[dot-__init__()_89]] - code - gateway/security/metadata_guard.py
- [[dot-check_for_exif()]] - code - gateway/security/metadata_guard.py
- [[dot-check_oversized_headers()]] - code - gateway/security/metadata_guard.py
- [[dot-get_document_tag()]] - code - gateway/security/metadata_guard.py
- [[dot-guard()_1]] - code - gateway/tests/test_metadata_guard.py
- [[dot-sanitize_filename()]] - code - gateway/security/metadata_guard.py
- [[dot-sanitize_headers()]] - code - gateway/security/metadata_guard.py
- [[dot-sanitize_image_metadata()]] - code - gateway/security/metadata_guard.py
- [[dot-tag_document()]] - code - gateway/security/metadata_guard.py
- [[dot-test_browser_security_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_document_tag_creation()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_document_tag_lookup_by_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_document_tag_untrusted_source()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_egress_monitor_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_get_document_tag_unknown_hash_returns_none()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_metadata_oversized_headers()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_metadata_path_traversal_stripped()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_metadata_sanitize_filename()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_network_validator_importable()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_oauth_redirect_mismatch()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_tag_document_different_content_different_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[Check if binary data contains EXIF metadata.]] - rationale - gateway/security/metadata_guard.py
- [[Check if headers exceed size limits.]] - rationale - gateway/security/metadata_guard.py
- [[Create and store a provenance tag for a document.]] - rationale - gateway/security/metadata_guard.py
- [[DocumentTag]] - code - gateway/security/metadata_guard.py
- [[Guards against metadata channel attacks and information disclosure.]] - rationale - gateway/security/metadata_guard.py
- [[Look up a document tag by its SHA-256 content hash.]] - rationale - gateway/security/metadata_guard.py
- [[Metadata Channel Guard - Security Hardening Module Sanitize HTTP headers, image…]] - rationale - gateway/security/metadata_guard.py
- [[MetadataGuard]] - code - gateway/security/metadata_guard.py
- [[Provenance record for a document ingested into the agent context.]] - rationale - gateway/security/metadata_guard.py
- [[Remove EXIF metadata from image data if present.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize HTTP headers by removing sensitive information.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize filename by removing unicode control characters and normalizing.]] - rationale - gateway/security/metadata_guard.py
- [[Test DNS filtering, SSRF prevention, and egress control.]] - rationale - gateway/tests/test_security_audit.py
- [[TestDocumentTagging]] - code - gateway/tests/test_metadata_guard.py
- [[TestNetworkSecurity]] - code - gateway/tests/test_security_audit.py
- [[Tests for Metadata Channel Guard]] - rationale - gateway/tests/test_metadata_guard.py
- [[fixture_53]] - code
- [[metadata_guard.py]] - code - gateway/security/metadata_guard.py
- [[t_metadata()]] - code - gateway/ingest_api/main.py
- [[test_metadata_guard.py]] - code - gateway/tests/test_metadata_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MetadataGuard
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_TestMetadataGuard]]
- 3 edges to [[_COMMUNITY_TestExfiltrationDetection]]
- 2 edges to [[_COMMUNITY_TestInfoLeakage]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_EgressEvent]]
- 1 edge to [[_COMMUNITY_BrowserSecurityGuard]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_NetworkValidator]]
- 1 edge to [[_COMMUNITY_OAuthSecurityValidator]]

## Top bridge nodes
- [[TestNetworkSecurity]] - degree 21, connects to 8 communities
- [[MetadataGuard]] - degree 28, connects to 7 communities
- [[test_metadata_guard.py]] - degree 6, connects to 1 community
- [[metadata_guard.py]] - degree 5, connects to 1 community
- [[t_metadata()]] - degree 2, connects to 1 community
