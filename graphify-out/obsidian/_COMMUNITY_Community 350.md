---
type: community
cohesion: 0.08
members: 25
---

# Community 350

**Cohesion:** 0.08 - loosely connected
**Members:** 25 nodes

## Members
- [[.setup_method()_12]] - code - gateway/tests/test_metadata_guard.py
- [[.test_all_unicode_control_chars_stripped()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_for_exif_detects_magic_bytes()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_oversized_headers_flags_large_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_check_oversized_headers_passes_normal_headers()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_internal_ip_patterns_comprehensive()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_filename_normalizes_unicode()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_filename_strips_control_chars()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_redacts_internal_ips()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_strips_sensitive()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_headers_truncates_on_size_limit()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_image_metadata_preserves_non_exif()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_sanitize_image_metadata_removes_exif()]] - code - gateway/tests/test_metadata_guard.py
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
- [[TestMetadataGuard]] - code - gateway/tests/test_metadata_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_350
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 581]]
- 2 edges to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[TestMetadataGuard]] - degree 16, connects to 2 communities
- [[.setup_method()_12]] - degree 2, connects to 1 community