---
type: community
members: 72
---

# MetadataGuard

**Members:** 72 nodes

## Members
- [[dot-__init__()_94]] - code - gateway/security/metadata_guard.py
- [[dot-check_for_exif()]] - code - gateway/security/metadata_guard.py
- [[dot-check_oversized_headers()]] - code - gateway/security/metadata_guard.py
- [[dot-get_document_tag()]] - code - gateway/security/metadata_guard.py
- [[dot-guard()_5]] - code - gateway/tests/test_metadata_guard.py
- [[dot-sanitize_filename()]] - code - gateway/security/metadata_guard.py
- [[dot-sanitize_headers()]] - code - gateway/security/metadata_guard.py
- [[dot-sanitize_image_metadata()]] - code - gateway/security/metadata_guard.py
- [[dot-setup_method()_13]] - code - gateway/tests/test_metadata_guard.py
- [[dot-tag_document()]] - code - gateway/security/metadata_guard.py
- [[dot-test_all_unicode_control_chars_stripped()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_browser_security_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_check_for_exif_detects_magic_bytes()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_check_oversized_headers_flags_large_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_check_oversized_headers_passes_normal_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_dns_entropy_calculator()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_dns_filter_config()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_dns_low_entropy_legit()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_document_tag_creation()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_document_tag_lookup_by_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_document_tag_untrusted_source()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_egress_filter_loaded()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_egress_monitor_loaded()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_get_document_tag_unknown_hash_returns_none()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_internal_ip_patterns_comprehensive()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_metadata_oversized_headers()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_metadata_path_traversal_stripped()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_metadata_sanitize_filename()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_network_validator_importable()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_oauth_redirect_mismatch()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_sanitize_filename_normalizes_unicode()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_sanitize_filename_strips_control_chars()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_sanitize_headers_redacts_internal_ips()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_sanitize_headers_strips_sensitive()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_sanitize_headers_truncates_on_size_limit()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_sanitize_image_metadata_preserves_non_exif()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_sanitize_image_metadata_removes_exif()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_tag_document_different_content_different_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[Check if binary data contains EXIF metadata.]] - rationale - gateway/security/metadata_guard.py
- [[Check if headers exceed size limits.]] - rationale - gateway/security/metadata_guard.py
- [[Create and store a provenance tag for a document.]] - rationale - gateway/security/metadata_guard.py
- [[DocumentTag]] - code - gateway/security/metadata_guard.py
- [[Guards against metadata channel attacks and information disclosure.]] - rationale - gateway/security/metadata_guard.py
- [[High-entropy domains (potential tunneling).]] - rationale - gateway/tests/test_security_audit.py
- [[Legit domains have lower entropy.]] - rationale - gateway/tests/test_security_audit.py
- [[Look up a document tag by its SHA-256 content hash.]] - rationale - gateway/security/metadata_guard.py
- [[Metadata Channel Guard - Security Hardening Module Sanitize HTTP headers, image…]] - rationale - gateway/security/metadata_guard.py
- [[MetadataGuard]] - code - gateway/security/metadata_guard.py
- [[Provenance record for a document ingested into the agent context.]] - rationale - gateway/security/metadata_guard.py
- [[Remove EXIF metadata from image data if present.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize HTTP headers by removing sensitive information.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize filename by removing unicode control characters and normalizing.]] - rationale - gateway/security/metadata_guard.py
- [[Test DNS filtering, SSRF prevention, and egress control.]] - rationale - gateway/tests/test_security_audit.py
- [[Test comprehensive internal IP pattern matching.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that EXIF metadata is removed from image data.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that all specified unicode control characters are stripped.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that header sanitization stops at size limit.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that internal IPs are redacted from headers.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that non-EXIF data is preserved.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that normal-sized headers pass.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that oversized headers are flagged.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that sensitive headers are stripped.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that unicode control characters are stripped.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that unicode is normalized with NFKC.]] - rationale - gateway/tests/test_metadata_guard.py
- [[TestDocumentTagging]] - code - gateway/tests/test_metadata_guard.py
- [[TestMetadataGuard]] - code - gateway/tests/test_metadata_guard.py
- [[TestNetworkSecurity]] - code - gateway/tests/test_security_audit.py
- [[Tests for Metadata Channel Guard]] - rationale - gateway/tests/test_metadata_guard.py
- [[fixture_61]] - code
- [[metadata_guard.py]] - code - gateway/security/metadata_guard.py
- [[t_metadata()]] - code - gateway/ingest_api/main.py
- [[test_metadata_guard.py]] - code - gateway/tests/test_metadata_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MetadataGuard
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_DNSFilterConfig]]
- 3 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_LogSanitizer]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 1 edge to [[_COMMUNITY_web_proxy.py]]
- 1 edge to [[_COMMUNITY_BrowserSecurityGuard]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_NetworkValidator]]

## Top bridge nodes
- [[MetadataGuard]] - degree 28, connects to 6 communities
- [[TestNetworkSecurity]] - degree 21, connects to 6 communities
- [[metadata_guard.py]] - degree 5, connects to 1 community
- [[dot-test_dns_entropy_calculator()]] - degree 3, connects to 1 community
- [[dot-test_dns_low_entropy_legit()]] - degree 3, connects to 1 community
