---
type: community
cohesion: 0.04
members: 46
---

# Module Group 89

**Cohesion:** 0.04 - loosely connected
**Members:** 46 nodes

## Members
- [[Closed function_calls block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Closed function_results block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Closed invoke block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Closed parameter block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Closed system-reminder block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Closed thinking block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Empty string input returns empty string, not filtered.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Large XML block spanning many lines is fully removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Multiple XML blocks in one response are all removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Nested invoke inside function_calls is fully removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Normal text without XML blocks is returned unchanged.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Regular HTML-like tags that are NOT in the block list are not removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Result is stripped of leadingtrailing whitespace.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Return type is always (str, bool).]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Text before and after XML blocks is preserved.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Three or more consecutive newlines are collapsed to two.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Unclosed function_calls block (truncated output) is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Unclosed function_results block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Unclosed system-reminder block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[Unclosed thinking block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[sanitizer()_3]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_collapses_excessive_newlines()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_does_not_filter_normal_text()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_does_not_filter_regular_html_tags()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_empty_string_returns_unchanged()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filter_xml_blocks.py]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_blocks_preserves_surrounding_text()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_function_calls_block()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_function_results_block()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_invoke_block()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_large_block()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_multiple_blocks()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_nested_invoke_inside_function_calls()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_parameter_block()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_system_reminder_block()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_thinking_block()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_unclosed_function_calls()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_unclosed_function_results()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_unclosed_system_reminder()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_filters_unclosed_thinking()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_returns_tuple_of_str_and_bool()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_strips_leading_trailing_whitespace()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_was_filtered_false_when_no_blocks()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[test_was_filtered_true_when_block_present()]] - code - gateway/tests/test_filter_xml_blocks.py
- [[was_filtered is False when no XML blocks are present.]] - rationale - gateway/tests/test_filter_xml_blocks.py
- [[was_filtered is True when an XML block is removed.]] - rationale - gateway/tests/test_filter_xml_blocks.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_89
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Tool Result Sanitizer]]

## Top bridge nodes
- [[test_filter_xml_blocks.py]] - degree 25, connects to 1 community
- [[sanitizer()_3]] - degree 3, connects to 1 community