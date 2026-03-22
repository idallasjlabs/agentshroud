# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for OutputSchemaEnforcer (C25)."""
from __future__ import annotations

import re
import pytest

from gateway.security.output_schema import OutputSchemaEnforcer, SchemaRule, SchemaValidationResult


@pytest.fixture
def enforcer():
    return OutputSchemaEnforcer()


class TestOutputSchemaEnforcer:
    def test_valid_output_passes(self, enforcer):
        """Normal short text should pass without violations."""
        result = enforcer.validate("Hello! How can I help you today?")
        assert result.valid
        assert result.violations == []
        assert result.sanitized_output == "Hello! How can I help you today?"

    def test_output_exceeding_max_length_trimmed(self, enforcer):
        """Output longer than 100 000 chars should be trimmed."""
        # Use punctuation-heavy content to avoid triggering the base64 pattern
        long_output = "Hello, world! " * 8_000  # ~112 000 chars, no base64 match
        result = enforcer.validate(long_output)
        assert not result.valid
        assert any("output_too_long" in v for v in result.violations)
        assert len(result.sanitized_output) <= 100_000

    def test_raw_tool_payload_stripped(self, enforcer):
        """JSON tool call payloads should be flagged and redacted."""
        payload = 'Here is the answer. {"tool_name": "read_file", "params": {}}'
        result = enforcer.validate(payload)
        assert not result.valid
        assert any("forbidden_pattern" in v for v in result.violations)
        assert "SCHEMA_REDACTED" in result.sanitized_output

    def test_large_base64_stripped(self, enforcer):
        """Base64 blobs > 1 KB encoded (≈ 1370 chars) should be redacted."""
        big_b64 = "A" * 1500  # well above threshold
        output = f"Result: {big_b64} end"
        result = enforcer.validate(output)
        assert not result.valid
        assert "SCHEMA_REDACTED" in result.sanitized_output

    def test_raw_file_path_stripped(self, enforcer):
        """Absolute file paths should be flagged and redacted."""
        output = "I read the file /Users/ijefferson/secret.txt successfully."
        result = enforcer.validate(output)
        assert not result.valid
        assert "SCHEMA_REDACTED" in result.sanitized_output

    def test_custom_schema_enforced(self, enforcer):
        """A custom schema with a stricter max_length is applied correctly."""
        custom_rule = SchemaRule(
            name="strict",
            max_length=50,
            forbidden_patterns=[re.compile(r"badword", re.IGNORECASE)],
            content_type="text",
        )
        enforcer.register_schema("strict", custom_rule)

        # Length violation
        long_output = "x" * 60
        result = enforcer.validate(long_output, schema_name="strict")
        assert not result.valid
        assert len(result.sanitized_output) == 50

        # Pattern violation
        result2 = enforcer.validate("This is a badword example.", schema_name="strict")
        assert not result2.valid
        assert "SCHEMA_REDACTED" in result2.sanitized_output

    def test_default_schema_used_when_unknown(self, enforcer):
        """Unknown schema names fall back to 'default'."""
        result = enforcer.validate("Hello world", schema_name="nonexistent")
        assert result.valid
