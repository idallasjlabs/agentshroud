# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Tests for XMLLeakFilter.
"""

from __future__ import annotations

import pytest

from gateway.security.xml_leak_filter import FilterResult, XMLLeakFilter


class TestXMLLeakFilter:
    """Test cases for XMLLeakFilter."""

    def setup_method(self):
        """Set up test fixtures."""
        self.filter = XMLLeakFilter()

    def test_clean_response_passes_through(self):
        """Test that clean responses pass through unchanged."""
        clean_response = """
        I can help you with that task. Here's what I found:

        The weather today is sunny with a high of 75°F.
        You might want to consider going for a walk.
        """

        result = self.filter.filter_response(clean_response)

        assert result.filtered_content == clean_response
        assert len(result.removed_items) == 0
        assert result.filter_applied is False

    def test_function_calls_xml_removal(self):
        """Test removal of function call XML blocks."""
        response_with_xml = """Let me check that for you.

<function_calls>
<invoke name="web_search">
<parameter name="query">weather today</parameter>
</invoke>
</function_calls>

The weather today is sunny."""

        result = self.filter.filter_response(response_with_xml)

        assert "[FUNCTION_CALL_FILTERED]" in result.filtered_content
        assert "<function_calls>" not in result.filtered_content
        assert "<invoke" not in result.filtered_content
        assert "weather today is sunny" in result.filtered_content
        assert len(result.removed_items) > 0
        assert result.filter_applied is True

    def test_file_path_removal(self):
        """Test removal of file paths from responses."""
        response_with_paths = """I found the file at /Users/john/Documents/secret.txt
Also checked /home/user/config/database.conf
The app data is in /app/data/sensitive/info.json"""

        result = self.filter.filter_response(response_with_paths)

        assert "[PATH_FILTERED]" in result.filtered_content
        assert "/Users/john" not in result.filtered_content
        assert "/home/user" not in result.filtered_content
        assert "/app/data" not in result.filtered_content

        # Check that paths were logged
        path_items = [item for item in result.removed_items if item.startswith("file_path:")]
        assert len(path_items) >= 3
        assert result.filter_applied is True

    def test_quick_function_calls_filter(self):
        """Test the performance-optimized function calls only filter."""
        response_with_mixed = """Here's the result:

<function_calls>
<invoke name="test_tool">
<parameter name="value">test</parameter>
</invoke>
</function_calls>

File path: /home/user/secret.txt"""

        # The quick filter should only remove function calls
        filtered = self.filter.filter_function_calls_only(response_with_mixed)

        assert "[FUNCTION_CALL_FILTERED]" in filtered
        assert "<function_calls>" not in filtered
        # But paths should remain (this is the quick filter)
        assert "/home/user/secret.txt" in filtered


# ── C32: Command Injection Scan tests ────────────────────────────────────────


class TestCommandInjectionScan:
    @pytest.fixture
    def xml_filter(self):
        return XMLLeakFilter()

    def test_clean_text_passes(self, xml_filter):
        result = xml_filter.scan_command_injection("The answer is 42.")
        assert isinstance(result, FilterResult)
        assert not result.filter_applied
        assert result.removed_items == []

    def test_shell_injection_detected(self, xml_filter):
        result = xml_filter.scan_command_injection("Result: ; rm -rf /tmp/test")
        assert result.filter_applied
        assert any("command_injection" in item for item in result.removed_items)

    def test_sql_injection_detected(self, xml_filter):
        result = xml_filter.scan_command_injection("Input: ' OR '1'='1")
        assert result.filter_applied
        assert any("command_injection" in item for item in result.removed_items)

    def test_python_eval_detected(self, xml_filter):
        result = xml_filter.scan_command_injection("eval(compile('import os'))")
        assert result.filter_applied

    def test_empty_text_returns_clean(self, xml_filter):
        result = xml_filter.scan_command_injection("")
        assert not result.filter_applied
        assert result.removed_items == []
