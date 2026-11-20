---
type: community
members: 15
---

# Community 791

**Members:** 15 nodes

## Members
- [[.test_custom_schema_enforced()]] - code - gateway/tests/test_output_schema.py
- [[.test_default_schema_used_when_unknown()]] - code - gateway/tests/test_output_schema.py
- [[.test_large_base64_stripped()]] - code - gateway/tests/test_output_schema.py
- [[.test_output_exceeding_max_length_trimmed()]] - code - gateway/tests/test_output_schema.py
- [[.test_raw_file_path_stripped()]] - code - gateway/tests/test_output_schema.py
- [[.test_raw_tool_payload_stripped()]] - code - gateway/tests/test_output_schema.py
- [[.test_valid_output_passes()]] - code - gateway/tests/test_output_schema.py
- [[A custom schema with a stricter max_length is applied correctly.]] - rationale - gateway/tests/test_output_schema.py
- [[Absolute file paths should be flagged and redacted.]] - rationale - gateway/tests/test_output_schema.py
- [[Base64 blobs  1 KB encoded (≈ 1370 chars) should be redacted.]] - rationale - gateway/tests/test_output_schema.py
- [[JSON tool call payloads should be flagged and redacted.]] - rationale - gateway/tests/test_output_schema.py
- [[Normal short text should pass without violations.]] - rationale - gateway/tests/test_output_schema.py
- [[Output longer than 100 000 chars should be trimmed.]] - rationale - gateway/tests/test_output_schema.py
- [[TestOutputSchemaEnforcer]] - code - gateway/tests/test_output_schema.py
- [[Unknown schema names fall back to 'default'.]] - rationale - gateway/tests/test_output_schema.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_791
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 262]]

## Top bridge nodes
- [[TestOutputSchemaEnforcer]] - degree 10, connects to 1 community
- [[.test_custom_schema_enforced()]] - degree 3, connects to 1 community