---
type: community
cohesion: 0.06
members: 31
---

# ToolResultSanitizer

**Cohesion:** 0.06 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-test_blocked_pattern_detection()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_code_blocks_preserved()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_domain_matching_patterns()]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[dot-test_edge_cases()_3]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py
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
- [[Test detection of blocked patterns in URLs.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test detection of internalrelative links.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test domain allowlist checking.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test domain pattern matching including wildcards.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test edge cases and malformed inputs.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test handling of empty or None input.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test handling of images with empty alt text.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test sanitization of mixed legitimate and malicious content.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test stripping of links to non-allowlisted domains.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test stripping of malicious markdown images.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test stripping of malicious markdown links.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that appropriate logging occurs.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that code blocks with URLs are preserved.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that internalrelative links are preserved.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[Test that legitimate links are preserved.]] - rationale - gateway/tests/test_tool_result_sanitizer_enhanced.py
- [[TestToolResultSanitizer]] - code - gateway/tests/test_tool_result_sanitizer_enhanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolResultSanitizer
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ToolResultSanitizer_2]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer_4]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer_6]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer_3]]

## Top bridge nodes
- [[TestToolResultSanitizer]] - degree 22, connects to 4 communities
