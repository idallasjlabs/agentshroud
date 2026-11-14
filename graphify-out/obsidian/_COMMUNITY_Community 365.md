---
type: community
members: 82
---

# Community 365

**Members:** 82 nodes

## Members
- [[.__init__()_112]] - code - gateway/security/metadata_guard.py
- [[.check_for_exif()]] - code - gateway/security/metadata_guard.py
- [[.check_oversized_headers()]] - code - gateway/security/metadata_guard.py
- [[.get_document_tag()]] - code - gateway/security/metadata_guard.py
- [[.guard()_1]] - code - gateway/tests/test_metadata_guard.py
- [[.sanitize_filename()]] - code - gateway/security/metadata_guard.py
- [[.sanitize_headers()]] - code - gateway/security/metadata_guard.py
- [[.sanitize_image_metadata()]] - code - gateway/security/metadata_guard.py
- [[.setup_method()_12]] - code - gateway/tests/test_metadata_guard.py
- [[.tag_document()]] - code - gateway/security/metadata_guard.py
- [[.test_all_unicode_control_chars_stripped()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_browser_security_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_check_for_exif_detects_magic_bytes()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_oversized_headers_flags_large_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_oversized_headers_passes_normal_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_dns_entropy_calculator()]] - code - gateway/tests/test_security_audit.py
- [[.test_dns_filter_config()]] - code - gateway/tests/test_security_audit.py
- [[.test_dns_low_entropy_legit()]] - code - gateway/tests/test_security_audit.py
- [[.test_document_tag_creation()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_lookup_by_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_untrusted_source()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_egress_monitor_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_guard_scrubs_output()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_get_document_tag_unknown_hash_returns_none()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_internal_ip_patterns_comprehensive()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_log_sanitizer_covers_stack_traces()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_metadata_guard_strips_internal_headers()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_metadata_oversized_headers()]] - code - gateway/tests/test_security_audit.py
- [[.test_metadata_path_traversal_stripped()]] - code - gateway/tests/test_security_audit.py
- [[.test_metadata_sanitize_filename()]] - code - gateway/tests/test_security_audit.py
- [[.test_network_validator_importable()]] - code - gateway/tests/test_security_audit.py
- [[.test_oauth_redirect_mismatch()]] - code - gateway/tests/test_security_audit.py
- [[.test_sanitize_filename_normalizes_unicode()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_filename_strips_control_chars()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_redacts_internal_ips()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_strips_sensitive()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_truncates_on_size_limit()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_image_metadata_preserves_non_exif()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_image_metadata_removes_exif()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_tag_document_different_content_different_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_token_error_no_secret_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[Check if binary data contains EXIF metadata.]] - rationale - gateway/security/metadata_guard.py
- [[Check if headers exceed size limits.]] - rationale - gateway/security/metadata_guard.py
- [[Create and store a provenance tag for a document.]] - rationale - gateway/security/metadata_guard.py
- [[Decryption errors shouldn't expose the encryption key.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[DocumentTag]] - code - gateway/security/metadata_guard.py
- [[Environment guard should scrub sensitive output.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Git guard errors shouldn't expose full file paths.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Guards against metadata channel attacks and information disclosure.]] - rationale - gateway/security/metadata_guard.py
- [[High-entropy domains (potential tunneling).]] - rationale - gateway/tests/test_security_audit.py
- [[Internal infrastructure headers should be stripped.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Legit domains have lower entropy.]] - rationale - gateway/tests/test_security_audit.py
- [[Look up a document tag by its SHA-256 content hash.]] - rationale - gateway/security/metadata_guard.py
- [[MetadataGuard]] - code - gateway/security/metadata_guard.py
- [[Numbered security control catalog (C8, C9, C18, C47, ...)]] - concept - gateway/tests/test_prompt_guard.py
- [[Provenance record for a document ingested into the agent context.]] - rationale - gateway/security/metadata_guard.py
- [[Remove EXIF metadata from image data if present.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize HTTP headers by removing sensitive information.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize filename by removing unicode control characters and normalizing.]] - rationale - gateway/security/metadata_guard.py
- [[Stack traces containing secrets should be sanitized.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test DNS filtering, SSRF prevention, and egress control.]] - rationale - gateway/tests/test_security_audit.py
- [[Test comprehensive internal IP pattern matching.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that EXIF metadata is removed from image data.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that all specified unicode control characters are stripped.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that errors don't leak sensitive information.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test that header sanitization stops at size limit.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that internal IPs are redacted from headers.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that non-EXIF data is preserved.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that normal-sized headers pass.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that oversized headers are flagged.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that sensitive headers are stripped.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that unicode control characters are stripped.]] - rationale - gateway/tests/test_metadata_guard.py
- [[Test that unicode is normalized with NFKC.]] - rationale - gateway/tests/test_metadata_guard.py
- [[TestDocumentTagging]] - code - gateway/tests/test_metadata_guard.py
- [[TestInfoLeakage]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestMetadataGuard]] - code - gateway/tests/test_metadata_guard.py
- [[TestNetworkSecurity]] - code - gateway/tests/test_security_audit.py
- [[Token validation errors shouldn't expose signing keys.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[metadata_guard.py]] - code - gateway/security/metadata_guard.py
- [[test_metadata_guard.py]] - code - gateway/tests/test_metadata_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_365
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 0]]
- 14 edges to [[_COMMUNITY_Community 72]]
- 8 edges to [[_COMMUNITY_Community 41]]
- 6 edges to [[_COMMUNITY_Community 7]]
- 6 edges to [[_COMMUNITY_Community 162]]
- 4 edges to [[_COMMUNITY_Community 477]]
- 4 edges to [[_COMMUNITY_Community 235]]
- 3 edges to [[_COMMUNITY_Community 93]]
- 3 edges to [[_COMMUNITY_Community 108]]
- 3 edges to [[_COMMUNITY_Community 121]]
- 3 edges to [[_COMMUNITY_Community 5]]
- 3 edges to [[_COMMUNITY_Community 146]]
- 2 edges to [[_COMMUNITY_Community 557]]
- 2 edges to [[_COMMUNITY_Community 166]]
- 2 edges to [[_COMMUNITY_Community 32]]
- 2 edges to [[_COMMUNITY_Community 684]]
- 2 edges to [[_COMMUNITY_Community 809]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 148]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 128]]
- 1 edge to [[_COMMUNITY_Community 479]]
- 1 edge to [[_COMMUNITY_Community 71]]
- 1 edge to [[_COMMUNITY_Community 917]]
- 1 edge to [[_COMMUNITY_Community 76]]

## Top bridge nodes
- [[TestNetworkSecurity]] - degree 46, connects to 18 communities
- [[TestInfoLeakage]] - degree 30, connects to 14 communities
- [[MetadataGuard]] - degree 54, connects to 13 communities
- [[Numbered security control catalog (C8, C9, C18, C47, ...)]] - degree 3, connects to 2 communities
- [[.test_encrypted_store_error_no_key_leak()]] - degree 3, connects to 1 community