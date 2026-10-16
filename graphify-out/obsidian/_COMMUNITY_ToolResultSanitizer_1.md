---
type: community
cohesion: 0.03
members: 73
---

# ToolResultSanitizer

**Cohesion:** 0.03 - loosely connected
**Members:** 73 nodes

## Members
- [[dot-__init__()_179]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_domain_matches_pattern()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_extract_code_blocks()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_is_domain_allowed()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_is_internal_link()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_restore_code_blocks()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-_url_has_blocked_patterns()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-sanitize()_4]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-sanitize_images()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-sanitize_links()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[dot-setup_method()_36]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_blocked_pattern_detection()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_code_blocks_preserved()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_convenience_function()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_custom_config()_3]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_default_config()_8]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_domain_matching_patterns()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_edge_cases()_4]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_empty_alt_text_handling()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_empty_or_none_input()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_external_domain_stripping()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_internal_link_detection()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_internal_links_preserved()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_is_domain_allowed()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_legitimate_links_preserved()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_logging()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_malicious_image_stripping()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_malicious_link_stripping()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_mixed_content_sanitization()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_performance_with_large_content()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_realistic_web_scraping_result()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_warn_mode()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Check if URL contains any blocked patterns.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if a URL's domain is in the allowlist.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if domain matches pattern (supports wildcards).]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Check if this is an internal link (relative, anchor, etc.).]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Convenience function to sanitize tool result content.      Args         content]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Enhanced markdown sanitizer with configurable domain allowlist.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Extract code blocks to preserve them during sanitization.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Integration tests for the sanitizer.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Remove or warn about markdown images pointing to non-allowlisted domains.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Restore code blocks after sanitization.]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Sanitize tool result content by filtering markdown links and images.          Ar]] - rationale - gateway/security/tool_result_sanitizer_enhanced.py
- [[Set up test fixtures._4]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test ToolResultSanitizerConfig.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test custom configuration.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test default configuration values._5]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test detection of blocked patterns in URLs.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test detection of internalrelative links.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test domain allowlist checking.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test domain pattern matching including wildcards.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test edge cases and malformed inputs.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test handling of empty or None input.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test handling of images with empty alt text.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test performance with large content.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test sanitization of mixed legitimate and malicious content.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test sanitizing a realistic web scraping result.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test stripping of links to non-allowlisted domains.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test stripping of malicious markdown images.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test stripping of malicious markdown links.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that appropriate logging occurs.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that code blocks with URLs are preserved.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that internalrelative links are preserved.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that legitimate links are preserved.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test the convenience sanitize_tool_result function.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test warn mode that marks but preserves external content.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[TestIntegration]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[TestToolResultSanitizer_1]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[TestToolResultSanitizerConfig]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[ToolResultSanitizer_1]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[sanitize_tool_result()]] - code - gateway/security/tool_result_sanitizer_enhanced.py
- [[test_tool_result_sanitizer_enhanced.py]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[tool_result_sanitizer_enhanced.py]] - code - gateway/security/tool_result_sanitizer_enhanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolResultSanitizer
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[ToolResultSanitizer_1]] - degree 34, connects to 1 community
- [[TestToolResultSanitizer_1]] - degree 22, connects to 1 community
- [[sanitize_tool_result()]] - degree 7, connects to 1 community
- [[test_tool_result_sanitizer_enhanced.py]] - degree 6, connects to 1 community
- [[TestIntegration]] - degree 6, connects to 1 community
