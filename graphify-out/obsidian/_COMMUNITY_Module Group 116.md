---
type: community
cohesion: 0.05
members: 40
---

# Module Group 116

**Cohesion:** 0.05 - loosely connected
**Members:** 40 nodes

## Members
- [[.get_document_tag()]] - code - gateway/security/metadata_guard.py
- [[.guard()_1]] - code - gateway/tests/test_metadata_guard.py
- [[.setup_method()_11]] - code - gateway/tests/test_metadata_guard.py
- [[.tag_document()]] - code - gateway/security/metadata_guard.py
- [[.test_all_unicode_control_chars_stripped()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_for_exif_detects_magic_bytes()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_oversized_headers_flags_large_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_oversized_headers_passes_normal_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_creation()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_lookup_by_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_untrusted_source()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_get_document_tag_unknown_hash_returns_none()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_internal_ip_patterns_comprehensive()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_filename_normalizes_unicode()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_filename_strips_control_chars()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_redacts_internal_ips()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_strips_sensitive()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_truncates_on_size_limit()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_image_metadata_preserves_non_exif()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_image_metadata_removes_exif()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_tag_document_different_content_different_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[Create and store a provenance tag for a document.]] - rationale - gateway/security/metadata_guard.py
- [[DocumentTag]] - code - gateway/security/metadata_guard.py
- [[Look up a document tag by its SHA-256 content hash.]] - rationale - gateway/security/metadata_guard.py
- [[Provenance record for a document ingested into the agent context.]] - rationale - gateway/security/metadata_guard.py
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
- [[metadata_guard.py]] - code - gateway/security/metadata_guard.py
- [[test_metadata_guard.py]] - code - gateway/tests/test_metadata_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_116
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Module Group 110]]

## Top bridge nodes
- [[TestMetadataGuard]] - degree 16, connects to 1 community
- [[TestDocumentTagging]] - degree 9, connects to 1 community
- [[test_metadata_guard.py]] - degree 4, connects to 1 community
- [[.get_document_tag()]] - degree 3, connects to 1 community
- [[.tag_document()]] - degree 3, connects to 1 community