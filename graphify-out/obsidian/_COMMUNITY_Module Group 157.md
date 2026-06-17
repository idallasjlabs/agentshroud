---
type: community
cohesion: 0.09
members: 31
---

# Module Group 157

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

## Members
- [[.__init__()_83]] - code - gateway/security/output_schema.py
- [[._register_default_schema()]] - code - gateway/security/output_schema.py
- [[.register_schema()]] - code - gateway/security/output_schema.py
- [[.test_custom_schema_enforced()]] - code - gateway/tests/test_output_schema.py
- [[.test_default_schema_used_when_unknown()]] - code - gateway/tests/test_output_schema.py
- [[.test_large_base64_stripped()]] - code - gateway/tests/test_output_schema.py
- [[.test_output_exceeding_max_length_trimmed()]] - code - gateway/tests/test_output_schema.py
- [[.test_raw_file_path_stripped()]] - code - gateway/tests/test_output_schema.py
- [[.test_raw_tool_payload_stripped()]] - code - gateway/tests/test_output_schema.py
- [[.test_valid_output_passes()]] - code - gateway/tests/test_output_schema.py
- [[.validate()_1]] - code - gateway/security/output_schema.py
- [[A custom schema with a stricter max_length is applied correctly.]] - rationale - gateway/tests/test_output_schema.py
- [[Absolute file paths should be flagged and redacted.]] - rationale - gateway/tests/test_output_schema.py
- [[Base64 blobs  1 KB encoded (≈ 1370 chars) should be redacted.]] - rationale - gateway/tests/test_output_schema.py
- [[Definition for a named output schema.]] - rationale - gateway/security/output_schema.py
- [[JSON tool call payloads should be flagged and redacted.]] - rationale - gateway/tests/test_output_schema.py
- [[Normal short text should pass without violations.]] - rationale - gateway/tests/test_output_schema.py
- [[Output longer than 100 000 chars should be trimmed.]] - rationale - gateway/tests/test_output_schema.py
- [[OutputSchemaEnforcer]] - code - gateway/security/output_schema.py
- [[Register or replace a named schema.]] - rationale - gateway/security/output_schema.py
- [[Register the built-in default schema.]] - rationale - gateway/security/output_schema.py
- [[Result of validating output against a schema.]] - rationale - gateway/security/output_schema.py
- [[SchemaRule]] - code - gateway/security/output_schema.py
- [[SchemaValidationResult]] - code - gateway/security/output_schema.py
- [[TestOutputSchemaEnforcer]] - code - gateway/tests/test_output_schema.py
- [[Unknown schema names fall back to 'default'.]] - rationale - gateway/tests/test_output_schema.py
- [[Validate output against the named schema.          Args             output The]] - rationale - gateway/security/output_schema.py
- [[Validates outbound responses against structural schemas.      Usage          e]] - rationale - gateway/security/output_schema.py
- [[enforcer()]] - code - gateway/tests/test_output_schema.py
- [[output_schema.py]] - code - gateway/security/output_schema.py
- [[test_output_schema.py]] - code - gateway/tests/test_output_schema.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_157
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]

## Top bridge nodes
- [[OutputSchemaEnforcer]] - degree 11, connects to 1 community